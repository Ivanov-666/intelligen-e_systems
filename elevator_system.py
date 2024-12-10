from elevator_DFA import Elevator_DFA


class ElevatorSystem:
    def __init__(self, num_floors, elevator_info):
        self.history = []
        self.elevator_DFAs = [Elevator_DFA(num_floors, start_floor, i, self.history) for i, start_floor in enumerate(elevator_info)]

    def run(self, curr_floor, call_floor):
        elevator_DFA = min(self.elevator_DFAs, key=lambda elevator_DFA: abs(curr_floor-elevator_DFA.get_elevator_floor()))
        elevator_DFA.process_request(curr_floor)
        elevator_DFA.process_request(call_floor)

    def get_history(self):
        for step in self.history:
            print(step)
