"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    letters_list = ['A', 'B', 'C', 'D']
    letters_list_index = 0
    for index in range(number):
        yield letters_list[index % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For exampl: 3C, 3D, 4A, 4B

    """
    lettters = generate_seat_letters(number)# 生产座位字母
    
    for i in range(1, number+1):
        lettter = next(lettters) # 座位字母
        number = (i - 1) // 4 + 1 # 座位行号
        
        # 13行座位处理
        if number >= 13:
            row = number + 1
        else:
            row = number
        yield f"{row}{lettter}" # 返回值
        
        

def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    passengers_number = len(passengers)
    passengers_seat_info = generate_seats(passengers_number)

    passengers_info = dict(zip(passengers, passengers_seat_info))

    return passengers_info
    
        
        
def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers:
        ticket = f"{seat_number}{flight_id}"
        yield f"{ticket:0<12}"
