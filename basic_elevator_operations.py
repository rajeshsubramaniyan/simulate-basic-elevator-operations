from random import randint


class ElevatorOperations(object):

    def __init__(self):
        """
        This method is used to initialize required variables and constants.
        It is assumed that the building has 10 floors excluding ground floor.
        """
        self.TOTAL_FLOORS = 10
        self.starting_floor = randint(0, 10)
        self.current_floor = self.starting_floor
        print("The Elevator is in level {}".format(self.current_floor))

    def receive_user_inputs(self, elevator_level):
        """
        This method is used to receive and validate user inputs.
        We are using set data structure to store user's destination floor numbers in order to avoid duplicate
        selections.
        :param elevator_level:
        :return unique_sorted_floors:
        """
        destination_floor = set()
        destination_floor.add(elevator_level)
        number_of_people = int(input("Enter number of people using the Elevator : "))

        for i in range(number_of_people):
            is_user_input_valid = False
            user_floor_input = int(input("User {}, Which floor you would like to go (0-10): ".format(i + 1)))
            while not is_user_input_valid:
                if user_floor_input > self.TOTAL_FLOORS or user_floor_input < 0:
                    user_floor_input = int(
                        input("Invalid destination floor. Please enter correct destination floor between 0 and 10: "))
                elif user_floor_input == elevator_level:
                    user_floor_input = int(input(
                        "You're already in {} floor. Please enter correct destination floor between 0 and 10: ".format(
                            elevator_level)))
                else:
                    is_user_input_valid = True
            destination_floor.add(user_floor_input)

        unique_sorted_floors = list(destination_floor)
        unique_sorted_floors.sort()
        print(unique_sorted_floors)
        return unique_sorted_floors

    def elevator_process(self, floors_to_operate):
        """
        This method is used to move the elevator Up and Down based on the current position of the lift.
        1. From the current floor move up in ascending order if any of the higher level floors are selected
        2. From the current floor move down in descending order if any of the lower level floors are selected

        Example: Let's assume the Elevator is at Floor 7, four users are entering and choosing 9, 10, 1 and 0 floors.
        Then the elevator will move in this order - Floor 9, 10, 1 and 0.
        :param floors_to_operate:
        :return:
        """
        index_of_start_floor = floors_to_operate.index(self.starting_floor)
        # This section is to handle upper floor requests
        for j in range(index_of_start_floor + 1, len(floors_to_operate)):
            current_floor = self.move_elevator(self.current_floor, floors_to_operate[j], "UP")
            self.current_floor = current_floor
            print("|<<<<<<<<<<<<<<<<<<<<<< OPEN_DOOR >>>>>>>>>>>>>>>>>>>>>>>>>>>|")
            print("|You've arrived at floor-{} . Please alight from the elevator.|".format(self.current_floor))
            print("|>>>>>>>>>>>>>>>>>>>>>> CLOSE_DOOR <<<<<<<<<<<<<<<<<<<<<<<<<<|")

        # This section is to handle lower floor requests
        for k in range(index_of_start_floor - 1, -1, -1):
            current_floor = self.move_elevator(self.current_floor, floors_to_operate[k], "DOWN")
            self.current_floor = current_floor
            print("|<<<<<<<<<<<<<<<<<<<<<< OPEN_DOOR >>>>>>>>>>>>>>>>>>>>>>>>>>>|")
            print("|You've arrived at floor-{} . Please alight from the elevator.|".format(self.current_floor))
            print("|>>>>>>>>>>>>>>>>>>>>>> CLOSE_DOOR <<<<<<<<<<<<<<<<<<<<<<<<<<|")

    def move_elevator(self, current_floor, destination, direction):
        """
        This method is used to either increase or decrease the elevator level based on the direction.
        :param current_floor:
        :param destination:
        :param direction:
        :return current_floor:
        """
        if direction == "UP":
            while current_floor != destination:
                current_floor += 1
                print("UP_1, Floor - {}".format(current_floor))
        elif direction == "DOWN":
            while current_floor != destination:
                current_floor -= 1
                print("DOWN_1, Floor - {}".format(current_floor))
        return current_floor


def main():
    """
    This is the main method to invoke sequence of operations.
    :return:
    """
    elevator = ElevatorOperations()
    floors_to_move = elevator.receive_user_inputs(elevator.current_floor)
    elevator.elevator_process(floors_to_move)


if __name__ == "__main__":
    main()
