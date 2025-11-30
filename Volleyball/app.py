from flask import Flask, render_template, jsonify, request
from rotation import Player, RotationManager

app = Flask(__name__)

# Sample players (change names/numbers later if you want)
demo_players = [
    Player(id=1, name="Alice",   number=1, position="OH"),
    Player(id=2, name="Bella",   number=2, position="MB"),
    Player(id=3, name="Chloe",   number=3, position="S"),
    Player(id=4, name="Diana",   number=4, position="OPP"),
    Player(id=5, name="Ella",    number=5, position="L"),
    Player(id=6, name="Fiona",   number=6, position="OH"),
    Player(id=7, name="Grace",   number=7, position="DS"),
    Player(id=8, name="Hannah",  number=8, position="DS"),
]

rotation_manager: RotationManager | None = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/players", methods=["GET"])
def get_players():
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "number": p.number,
            "position": p.position,
            "is_libero": p.is_libero,
            "is_captain": p.is_captain,
        }
        for p in demo_players
    ])


@app.route("/api/start-set", methods=["POST"])
def start_set():
    global rotation_manager

    data = request.get_json() or {}
    starting_court_ids = data.get("starting_court_ids", [])

    if not starting_court_ids or len(starting_court_ids) != 6:
        return jsonify({"error": "starting_court_ids must be a list of 6 player IDs"}), 400

    rotation_manager = RotationManager(demo_players, starting_court_ids)
    state = rotation_manager.get_state()

    return jsonify({
        "message": "Set started",
        "court": state.court,
        "bench": state.bench,
        "sequence": state.sequence_number,
    })


@app.route("/api/state", methods=["GET"])
def get_state():
    global rotation_manager
    if rotation_manager is None:
        return jsonify({"error": "Set not started"}), 400

    state = rotation_manager.get_state()
    return jsonify({
        "court": state.court,
        "bench": state.bench,
        "sequence": state.sequence_number,
    })


@app.route("/api/rotate", methods=["POST"])
def rotate():
    global rotation_manager
    if rotation_manager is None:
        return jsonify({"error": "Set not started"}), 400

    rotation_manager.rotate_clockwise()
    state = rotation_manager.get_state()
    return jsonify({
        "court": state.court,
        "bench": state.bench,
        "sequence": state.sequence_number,
    })


@app.route("/api/substitute", methods=["POST"])
def substitute():
    """
    Expected JSON:
    {
      "position": 1-6,
      "bench_player_id": <id>
    }
    """
    global rotation_manager
    if rotation_manager is None:
        return jsonify({"error": "Set not started"}), 400

    data = request.get_json() or {}
    position = data.get("position")          # human 1–6
    bench_player_id = data.get("bench_player_id")

    if position is None or bench_player_id is None:
        return jsonify({"error": "position and bench_player_id required"}), 400

    try:
        rotation_manager.substitute(position, bench_player_id)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    state = rotation_manager.get_state()
    return jsonify({
        "court": state.court,
        "bench": state.bench,
        "sequence": state.sequence_number,
    })


@app.route("/api/events", methods=["GET"])
def get_events():
    global rotation_manager
    if rotation_manager is None:
        return jsonify({"error": "Set not started"}), 400

    events = rotation_manager.get_events()
    return jsonify([
        {
            "sequence": e.sequence_number,
            "type": e.event_type,
            "details": e.details,
        }
        for e in events
    ])


if __name__ == "__main__":
    app.run(debug=True)
