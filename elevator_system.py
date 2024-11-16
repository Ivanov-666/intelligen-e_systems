from elevator import Elevator


class ElevatorSystem:
    def __init__(self, num_floors, elevator_info):
        self.history = []
        self.elevators = [Elevator(num_floors, start_floor, i, self.history) for i, start_floor in enumerate(elevator_info)]

    def run(self, requests):
        for elevator in self.elevators:
            elevator.reset()

        up_requests = list(filter(lambda x: x[0] < x[1], requests))
        down_requests = list(filter(lambda x: x[0] > x[1], requests))
        elevator_up = min(self.elevators, key=lambda elevator: elevator.current_floor)
        elevator_down = max(self.elevators, key=lambda elevator: elevator.current_floor)
        elevator_up.process_request(up_requests)
        elevator_down.process_request(down_requests)

    def get_history(self):
        for step in self.history:
            print(step)
