from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Player:
    id: int
    name: str
    number: int
    position: str = ""        # optional for now
    is_libero: bool = False
    is_captain: bool = False

@dataclass
class RotationState:
    # store player IDs, not Player objects
    court: List[int]            # 6 player IDs on court
    bench: List[int]            # bench player IDs
    sequence_number: int = 0

@dataclass
class Event:
    sequence_number: int
    event_type: str             # "start", "rotation", "substitution"
    details: Dict               # event-specific info


class RotationManager:
    def __init__(self, players: List[Player], starting_court_ids: List[int]):
        if len(starting_court_ids) != 6:
            raise ValueError("There must be exactly 6 starting court players.")

        # id -> Player map
        self.players: Dict[int, Player] = {p.id: p for p in players}

        # compute bench IDs
        bench_ids = [p.id for p in players if p.id not in starting_court_ids]

        self.sequence_number = 0
        self.current_state = RotationState(
            court=starting_court_ids[:],
            bench=bench_ids[:],
            sequence_number=self.sequence_number
        )
        self.events: List[Event] = []
        self._log_event(
            "start",
            {
                "court": self.current_state.court[:],
                "bench": self.current_state.bench[:],
            },
        )

    def _next_sequence(self) -> int:
        self.sequence_number += 1
        return self.sequence_number

    def _log_event(self, event_type: str, details: Dict):
        seq = self._next_sequence()
        self.current_state.sequence_number = seq
        self.events.append(Event(seq, event_type, details))

    def rotate_clockwise(self):
        # [1,2,3,4,5,6] -> [6,1,2,3,4,5]
        self.current_state.court = (
            [self.current_state.court[-1]] + self.current_state.court[:-1]
        )
        self._log_event("rotation", {"court": self.current_state.court[:]})

    def substitute(self, position_index: int, bench_player_id: int):
        if bench_player_id not in self.current_state.bench:
            raise ValueError("Bench player not available for substitution.")

        if not (0 <= position_index < 6):
            raise ValueError("Position index must be between 0 and 5.")

        leaving_player_id = self.current_state.court[position_index]

        # swap
        self.current_state.court[position_index] = bench_player_id
        self.current_state.bench.remove(bench_player_id)
        self.current_state.bench.append(leaving_player_id)

        self._log_event(
            "substitution",
            {
                "position": position_index + 1,
                "in": bench_player_id,
                "out": leaving_player_id,
                "new_court": self.current_state.court[:],
            },
        )

    def get_state(self) -> RotationState:
        return self.current_state

    def get_events(self) -> List[Event]:
        return self.events
