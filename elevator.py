class Elevator:
    def __init__(self, id, current_floor, history):
        self.id = id
        self.current_floor = current_floor
        self.state = "standing"
        self.history = history

    def open_doors(self):
        self.history.append(f"{self.id + 1} лифт открыл двери на {self.current_floor} этаже.")
        self.state = "open"

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
