from elevator_system import ElevatorSystem

requests = [[1, 10], [3, 11], [2, 6], [9, 4], [8, 9], [11, 5], [7, 4], [6, 3], [10, 11], [12, 8], [5, 2], [1, 7], [4, 12], [6, 8], [3, 5]]
elevator_system = ElevatorSystem(12, [12, 4])
elevator_system.run(requests)
elevator_system.get_history()
