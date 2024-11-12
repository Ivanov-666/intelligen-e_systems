from elevator import Elevator


class ElevatorSystem:
    def __init__(self, num_floors, elevator_info):
        self.history = []
        self.elevators = [Elevator(num_floors, start_floor, i, self.history) for i, start_floor in enumerate(elevator_info)]

    def request(self, call_floor, target_floor):
        free_elevator = min(self.elevators, key=lambda elevator: abs(call_floor-elevator.current_floor))
        self.history.append(f"{free_elevator.id + 1} лифт обслуживает вызов '{call_floor} - {target_floor}'.")
        free_elevator.process_floor_request(call_floor)
        free_elevator.close_doors()
        free_elevator.process_floor_request(target_floor)
        free_elevator.close_doors()
        

    def run(self, requests):
        for elevator in self.elevators:
            elevator.reset()

        for request in requests:
            call_floor, target_floor = request
            self.request(call_floor, target_floor)

    def get_history(self):
        for step in self.history:
            print(step)
