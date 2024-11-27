from elevator import Elevator


class ElevatorSystem:
    def __init__(self, num_floors, elevator_info):
        self.history = []
        self.elevators = [Elevator(num_floors, start_floor, i, self.history) for i, start_floor in enumerate(elevator_info)]

    def run(self, curr_floor, call_floor):
        elevator = min(self.elevators, key=lambda elevator: abs(curr_floor-elevator.current_floor))
        elevator.process_request(curr_floor)
        elevator.process_request(call_floor)

    def get_history(self):
        for step in self.history:
            print(step)
