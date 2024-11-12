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
                    "standing": lambda x: x,
                    "moving_up": lambda x: x.move_up,
                    "moving_down": lambda x: x.move_down
                    },
                "open": {
                    "standing": lambda x: x.close_doors,
                    "moving_up": lambda x: x,
                    "moving_down": lambda x: x
                    },
                "moving_up": {
                    "standing": lambda x: x.stop_moving,
                    "moving_up": lambda x: x,
                    "moving_down": lambda x: x.stop_moving
                    },
                "moving_down": {
                    "standing": lambda x: x.stop_moving,
                    "moving_up": lambda x: x.stop_moving,
                    "moving_down": lambda x: x
                    }
            }
        self.transition_map[1] = {
            "standing": {
                "standing": lambda x: x,
                "moving_up": lambda x: x.move_up,
                "moving_down": lambda x: x.move_down
                },
            "open": {
                "standing": lambda x: x.close_doors,
                "moving_up": lambda x: x,
                },
            "moving_up": {
                "standing": lambda x: x.stop_moving,
                "moving_up": lambda x: x,
                },
            "moving_down": {
                "standing": lambda x: x.stop_moving,
                "moving_up": lambda x: x.stop_moving,
                }
            }
        self.transition_map[num_floors] = {
            "standing": {
                "standing": lambda x: x,
                "moving_down": lambda x: x.move_down
                },
            "open": {
                "standing": lambda x: x.close_doors,
                "moving_down": lambda x: x
                },
            "moving_up": {
                "standing": lambda x: x.stop_moving,
                "moving_down": lambda x: x.stop_moving
                },
            "moving_down": {
                "standing": lambda x: x.stop_moving,
                "moving_down": lambda x: x
                }
            }

    def process_floor_request(self, requested_floor):
        try:
            state_transition = self.transition_map[self.current_floor][self.state].get(self.get_transition_state(requested_floor))
            state_transition(self)(requested_floor)
        except:
            raise ValueError("Некорректный номер этажа")

    def get_transition_state(self, requested_floor):
        return "standing"*(self.current_floor==requested_floor) + "moving_up"*(self.current_floor<requested_floor) + "moving_down"*(self.current_floor>requested_floor)

    def open_doors(self):
            self.history.append(f"{self.id + 1} лифт открыл дври на {self.current_floor} этаже.")
            self.state = "open"

    def close_doors(self):
            self.history.append(f"{self.id + 1} лифт закрыл двери на {self.current_floor} этаже.")
            self.state = "standing"

    def move_up(self, requested_floor):
        self.state = "moving_up"

        while self.current_floor < requested_floor:
            self.current_floor += 1
            self.history.append(f"{self.id + 1} лифт поднялся на этаж. Текущий этаж: {self.current_floor}.")

        self.open_doors()

    def move_down(self, requested_floor):
        self.state = "moving_down"

        while self.current_floor > requested_floor:
            self.current_floor -= 1
            self.history.append(f"{self.id + 1} лифт спустился на этаж ниже. Текущий этаж: {self.current_floor}.")

        self.open_doors()

    def stop_moving(self, requested_floor):
        pass

    def reset(self):
        self.state = "standing"
