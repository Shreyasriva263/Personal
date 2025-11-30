from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Player:
    id: int
    name: str
    number: int
    position: str
    is_libero: bool = False
    is_captain: bool = False
@dataclass
class RotationState:
    court_players: List[Player]
    bench_players: List[Player]
    sequence_number:int =0

@dataclass
class Event:
    squence_number: int
    event_type: str
    details: Dict #dictionary to hold event specific details, its like a struct in c

@dataclass
class RotationManager:
    def __init__(self, players: List[Player], starting_court_ids: List[int]):
        if len(starting_court_ids) != 6:
            raise ValueError("There must be exactly 6 starting court players.")
        self.players: Dict[int, Player] = {player.id: player for player in players}
        bench_ids = [p.id for p in players if p.id not in starting_court_ids]

        self.sequence_number = 0
        self.Current_state = RotationState(
            court_players=starting_court_ids[:],
            bench_players=bench_ids[:],
            sequence_number=self.sequence_number
        )
        self.events: List[Event] = []
        self._log_event("initial_setup", {"court_players": self.Current_state.court_players[:], "bench_players": self.Current_state.bench_players[:]})

    def _next_sequence(self):
        self.sequence_number += 1
        return self.sequence_number
    def _log_event(self, event_type: str, details: Dict):

        seq= self._next_sequence()
        self.Current_state.sequence_number=seq
        self.events.append(Event(seq, event_type, details))
    
    def rotate_clockwise(self):
        self.Current_state.court_players = [self.Current_state.court_players[-1]] + self.Current_state.court_players[:-1]
        self._log_event("rotation", {"court": self.Current_state.court_players[:]})
        ###court = [1, 2, 3, 4, 5, 6]
        ####rotate:
        ###self.current_state.court[-1] → last element → 6
        ###self.current_state.court[:-1] → everything except last → [1,2,3,4,5]
        # => [6,1,2,3,4,5]
    def substitute(self, position_index: int, bench_player_id: int):
        if bench_player_id not in self.Current_state.bench_players:
            raise ValueError("Bench player not available for substitution.")
        
        if not (0 <= position_index < 6):
            raise ValueError("Position index must be between 0 and 5.")
        
        leaving_player_id = self.Current_state.court_players[position_index]

        self.Current_state.court_players[position_index] = bench_player_id
        self.Current_state.bench_players.remove(bench_player_id) #remove benched player
        self.Current_state.bench_players.append(leaving_player_id) #add leaving player to bench

        self._log_event("substitution", {
        "position": position_index + 1,
        "in": bench_player_id,
        "out": leaving_player_id,
        "new_court": self.Current_state.court_players[:]
    })
    def get_current_state(self) -> RotationState:
        return self.Current_state
    def get_event_log(self) -> List[Event]:
        return self.events