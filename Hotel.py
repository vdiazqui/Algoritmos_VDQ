
from Room import Room
from Employee import Employee
class Hotel:
    """
    Python class to implement a comprehensive hotel management system.

    This class encompasses functionalities for managing hotel rooms, employees, and guest reservations, 
    providing a foundational system for hotel operations.

    Syntax
    ------
    obj = Hotel(name)

    Parameters
    ----------
    [in] name : str
        The name of the hotel.

    Returns
    -------
    obj : Hotel
        An instance of the Hotel class, representing a single hotel with its management capabilities.

    Attributes
    ----------
    name : str
        The name of the hotel.
    rooms : list
        A list of Room instances representing the rooms available in the hotel.
    employees : list
        A list of Employee instances representing the employees working at the hotel.
    reservations : dict
        A dictionary mapping room numbers to guest names, representing current reservations.
    """
    def __init__(self, name):
        """
        Constructor method to initialize a Hotel instance.

        Parameters:
        name (str): The name of the hotel.
        """
        self.name = name
        self.rooms = []
        self.employees = []
        self.reservations = {}

    def add_room(self, room):
        """
        Method to add a room to the hotel.

        Parameters:
        room (Room): The Room instance to be added.
        """
        self.rooms.append(room)

    def remove_room(self, room_number):
        """
        Method to remove a room from the hotel.

        Parameters:
        room_number (int): The room number of the room to be removed.
        """
        for room in self.rooms:
            if room.get_room_number() == room_number:
                self.rooms.remove(room)
                break

    def add_employee(self, employee):
        """
        Method to add an employee to the hotel.

        Parameters:
        employee (Employee): The Employee instance to be added.
        """
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        """
        Method to remove an employee from the hotel.

        Parameters:
        emp_id (int): The ID of the employee to be removed.
        """
        for employee in self.employees:
            if employee.get_emp_id() == emp_id:
                self.employees.remove(employee)
                break

    def check_in(self, room_number, guest_name):
        """
        Method to perform check-in for a guest.

        Parameters:
        room_number (int): The room number where the guest will check-in.
        guest_name (str): The name of the guest.

        Returns:
        str: A message indicating the success of the check-in process.
        """
        for room in self.rooms:
            if room.get_room_number() == room_number:
                if room.is_occupied():
                    return "Room not available or already occupied."
                else:
                    room.check_in()
                    self.reservations[room_number] = guest_name
                    return f"Check-in successful for {guest_name} in room {room_number}."
        return "Room not found."

    def check_out(self, room_number):
        """
        Method to perform check-out for a guest.

        Parameters:
        room_number (int): The room number from which the guest will check-out.

        Returns:
        str: A message indicating the success of the check-out process.
        """
        for room in self.rooms:
            if room.get_room_number() == room_number:
                if room.is_occupied():
                    guest_name = self.reservations.pop(room_number, None)
                    room.check_out()
                    return f"Check-out successful for {guest_name} from room {room_number}."
                else:
                    return "Room already unoccupied."
        return "Room not found."

    def find_room(self, room_number):
        """
        Method to find a room by its number.

        Parameters:
        room_number (int): The room number to search for.

        Returns:
        Room: The Room instance if found, None otherwise.
        """
        for room in self.rooms:
            if room.get_room_number() == room_number:
                return room
        return None
    


    


def main():
# TESTING
    print("=================================================================")
    print("Test Case 1: Create a Hotel.")
    print("=================================================================")
    hotel = Hotel("Grand Hotel")
    if hotel.name == "Grand Hotel":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================")
    print("Test Case 2: Add a Room to the Hotel.")
    print("=================================================================")

    room1 = Room("Doble", 101, "Desocupada", 150)
    hotel.add_room(room1)

    if hotel.rooms[0] == room1:
        print("Test PASS. Room has been successfully added to the hotel.")
    else:
        print("Test FAIL. Check the method add_room().")

    print("=================================================================")
    print("Test Case 3: Remove a Room from the Hotel.")
    print("=================================================================")

    hotel.remove_room(101)
    if len(hotel.rooms) == 0:
        print("Test PASS. Room has been successfully removed from the hotel.")
    else:
        print("Test FAIL. Check the method remove_room().")

    print("=================================================================")
    print("Test Case 4: Add an Employee to the Hotel.")
    print("=================================================================")

    emp1 = Employee(1, "John Doe", "Receptionist", 30000)
    hotel.add_employee(emp1)

    if hotel.employees[0] == emp1:
        print("Test PASS. Employee has been successfully added to the hotel.")
    else:
        print("Test FAIL. Check the method add_employee().")

    print("=================================================================")
    print("Test Case 5: Remove an Employee from the Hotel.")
    print("=================================================================")

    hotel.remove_employee(1)
    if len(hotel.employees) == 0:
        print("Test PASS. Employee has been successfully removed from the hotel.")
    else:
        print("Test FAIL. Check the method remove_employee().")

    print("=================================================================")
    print("Test Case 6: Check-in a Guest.")
    print("=================================================================")

    room2 = Room("Suite", 102, "Desocupada", 300)
    hotel.add_room(room2)
    check_in_result = hotel.check_in(102, "Alice")

    if check_in_result == "Check-in successful for Alice in room 102." and room2.room_state == "Ocupada":
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")

    print("=================================================================")
    print("Test Case 7: Check-out a Guest.")
    print("=================================================================")

    check_out_result = hotel.check_out(102)

    if check_out_result == "Check-out successful for Alice from room 102." and room2.room_state == "Desocupada":
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out().")

    print("=================================================================")
    print("Test Case 8: Attempt Check-in on an Occupied Room.")
    print("=================================================================")

    check_in_result = hotel.check_in(102, "Bob")
    if check_in_result == "Room not available or already occupied.":
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")

if __name__ == "__main__":
    main()