class Elevator:
    def __init__(self, num_floors, start_floor, id, history):
        self.num_floors = num_floors
        self.current_floor = start_floor
        self.id = id
        self.state = "standing"
        self.history = history
        self.transition_map = {}
        for floor in range(2, num_floors):
            self.transition_map[floor] = {
                "standing": {
                    "standing": lambda x: x.empty,
                    "moving_up": lambda x: x.move_up,
                    "moving_down": lambda x: x.move_down,
                    "open": lambda x: x.open_doors,
                    },
                "open": {
                    "standing": lambda x: x.close_doors,
                    "moving_up": lambda x: x.close_doors,
                    "moving_down": lambda x: x.close_doors,
                    },
                "moving_up": {
                    "standing": lambda x: x.stop_moving,
                    "moving_up": lambda x: x.move_up,
                    "moving_down": lambda x: x.stop_moving,
                    "open": lambda x: x.open_doors,
                    },
                "moving_down": {
                    "standing": lambda x: x.stop_moving,
                    "moving_up": lambda x: x.stop_moving,
                    "moving_down": lambda x: x.move_down,
                    "open": lambda x: x.open_doors,
                    }
            }
        self.transition_map[1] = {
            "standing": {
                "standing": lambda x: x.empty,
                "moving_up": lambda x: x.move_up,
                "open": lambda x: x.open_doors,
                },
            "open": {
                "standing": lambda x: x.close_doors,
                "moving_up": lambda x: x.close_doors,
                },
            "moving_up": {
                "standing": lambda x: x.stop_moving,
                "moving_up": lambda x: x.move_up,
                "open": lambda x: x.open_doors,
                },
            "moving_down": {
                "standing": lambda x: x.stop_moving,
                "moving_up": lambda x: x.stop_moving,
                "open": lambda x: x.open_doors,
                }
            }
        self.transition_map[num_floors] = {
            "standing": {
                "standing": lambda x: x.empty,
                "moving_down": lambda x: x.move_down,
                "open": lambda x: x.open_doors,
                },
            "open": {
                "standing": lambda x: x.close_doors,
                "moving_down": lambda x: x.close_doors,
                },
            "moving_up": {
                "standing": lambda x: x.stop_moving,
                "moving_down": lambda x: x.stop_moving,
                "open": lambda x: x.open_doors,
                },
            "moving_down": {
                "standing": lambda x: x.stop_moving,
                "moving_down": lambda x: x.move_down,
                "open": lambda x: x.open_doors,
                }
            }

    def process_request(self, requests):
        for request in requests:
            self.request = request
            while len(self.request) != 0:
                requested_floor = self.request[0]
                try:
                    state_transition = self.transition_map[self.current_floor][self.state].get(self.get_transition_state(requested_floor))
                    state_transition(self)()
                    state_doors = self.transition_map[self.current_floor][self.state].get(self.get_door_state(requested_floor))
                    state_doors(self)()
                except: 
                    raise ValueError("Некорректный номер этажа")

    def get_transition_state(self, requested_floor):
        return "standing"*(self.current_floor==requested_floor) + "moving_up"*(self.current_floor<requested_floor) + "moving_down"*(self.current_floor>requested_floor)
    
    def get_door_state(self, requested_floor):
        return "open"*(self.current_floor == requested_floor) + "standing"*(self.current_floor != requested_floor)

    def open_doors(self):
        self.history.append(f"{self.id + 1} лифт открыл двери на {self.current_floor} этаже.")
        self.state = "open"
        self.request.remove(self.current_floor)

    def close_doors(self):
        self.history.append(f"{self.id + 1} лифт закрыл двери на {self.current_floor} этаже.")
        self.state = "standing"

    def move_up(self):
        self.state = "moving_up"
        self.current_floor += 1
        self.history.append(f"{self.id + 1} лифт поднялся на этаж. Текущий этаж: {self.current_floor}.")

    def move_down(self):
        self.state = "moving_down"
        self.current_floor -= 1
        self.history.append(f"{self.id + 1} лифт спустился на этаж ниже. Текущий этаж: {self.current_floor}.")

    def stop_moving(self):
        pass

    def empty(self):
        pass

    def reset(self):
        self.state = "standing"
