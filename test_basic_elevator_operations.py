import unittest
from elevator_modules.main.basic_elevator_operations import ElevatorOperations


class TestElevatorOperations(unittest.TestCase):

    def test_when_user_enters_inputs(self):
        """
        Test case - To validate user input function returns unique sorted list.
        :return:
        """
        elevator_user_inputs = ElevatorOperations()
        """ In the user input panel, enter values as mentioned below.
            Enter number of people using the Elevator : 5
            User 1, Which floor you would like to go (0-10): 10
            User 2, Which floor you would like to go (0-10): 1
            User 3, Which floor you would like to go (0-10): 2
            User 4, Which floor you would like to go (0-10): 0
            User 5, Which floor you would like to go (0-10): 0
        """
        final_floors = elevator_user_inputs.receive_user_inputs(4)
        expected_floors = [0, 1, 2, 4, 10]
        self.assertEqual(final_floors, expected_floors)

    def test_elevator_movement(self):
        """
        Test case - To validate it reaches the destination floor.
        :return:
        """
        move_elevator_opt = ElevatorOperations()
        """ Test case to validate elevator moving up """
        current_floor = 4
        destination_floor = 10
        new_floor = move_elevator_opt.move_elevator(current_floor, destination_floor, "UP")
        self.assertEqual(new_floor, destination_floor)

        """ Test case to validate elevator moving down """
        current_floor = 5
        destination_floor = 0
        new_floor = move_elevator_opt.move_elevator(current_floor, destination_floor, "DOWN")
        self.assertEqual(new_floor, destination_floor)


if __name__ == "__main__":
    unittest.main()
