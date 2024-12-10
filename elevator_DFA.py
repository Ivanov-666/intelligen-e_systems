from elevator import Elevator
class Elevator_DFA:
    def __init__(self, num_floors, start_floor, id, history):
        self.num_floors = num_floors
        self.elevator = Elevator(id, start_floor, history)
        self.transition_map = {}
        for floor in range(2, num_floors):
            self.transition_map[floor] = {
                "standing": {
                    "standing": self.empty_command,
                    "moving_up": self.elevator.move_up,
                    "moving_down": self.elevator.move_down,
                    "open": self.elevator.open_doors,
                    },
                "open": {
                    "standing": self.elevator.close_doors,
                    "moving_up": self.elevator.close_doors,
                    "moving_down": self.elevator.close_doors,
                    },
                "moving_up": {
                    "standing": self.elevator.stop_moving,
                    "moving_up": self.elevator.move_up,
                    "moving_down": self.elevator.stop_moving,
                    "open": self.elevator.open_doors,
                    },
                "moving_down": {
                    "standing": self.elevator.stop_moving,
                    "moving_up": self.elevator.stop_moving,
                    "moving_down": self.elevator.move_down,
                    "open": self.elevator.open_doors,
                    }
            }
        self.transition_map[1] = {
            "standing": {
                "standing": self.empty_command,
                "moving_up": self.elevator.move_up,
                "open": self.elevator.open_doors,
                },
            "open": {
                "standing": self.elevator.close_doors,
                "moving_up": self.elevator.close_doors,
                },
            "moving_up": {
                "standing": self.elevator.stop_moving,
                "moving_up": self.elevator.move_up,
                "open": self.elevator.open_doors,
                },
            "moving_down": {
                "standing": self.elevator.stop_moving,
                "moving_up": self.elevator.stop_moving,
                "open": self.elevator.open_doors,
                }
            }
        self.transition_map[num_floors] = {
            "standing": {
                "standing": self.empty_command,
                "moving_down": self.elevator.move_down,
                "open": self.elevator.open_doors,
                },
            "open": {
                "standing": self.elevator.close_doors,
                "moving_down": self.elevator.close_doors,
                },
            "moving_up": {
                "standing": self.elevator.stop_moving,
                "moving_down": self.elevator.stop_moving,
                "open": self.elevator.open_doors,
                },
            "moving_down": {
                "standing": self.elevator.stop_moving,
                "moving_down": self.elevator.move_down,
                "open": self.elevator.open_doors,
                }
            }

    def process_request(self, requested_floor):
        while self.elevator.current_floor != requested_floor:
            try:
                state_transition = self.transition_map[self.elevator.current_floor][self.elevator.state].get(self.get_transition_state(requested_floor))
                state_transition()
                state_doors = self.transition_map[self.elevator.current_floor][self.elevator.state].get(self.get_door_state(requested_floor))
                state_doors()
            except: 
                raise ValueError("Некорректный номер этажа")

    def get_transition_state(self, requested_floor):
        return "standing"*(self.elevator.current_floor==requested_floor) + "moving_up"*(self.elevator.current_floor<requested_floor) + "moving_down"*(self.elevator.current_floor>requested_floor)
    
    def get_door_state(self, requested_floor):
        return "open"*(self.elevator.current_floor == requested_floor) + "standing"*(self.elevator.current_floor != requested_floor)
    
    def get_elevator_floor(self):
        return self.elevator.current_floor
    
    def empty_command(self,):
        pass

    def reset(self):
        self.state = "standing"
