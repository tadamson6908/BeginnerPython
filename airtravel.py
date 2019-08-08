"""
A flight class. Model for aircraft flights
"""
import re

class Flight:
    """
    A flight with a particular pasenger aircraft
    """

    def __init__(self, number, aircraft):
        #Validate flight number
        # check = list(number)
        # if len(number) != 5:
        #     raise ValueError
        # if number[2:].isdigit() and number[:2].isalpha():
        #     self._number = number
        # else:
        #     raise ValueError("Does not match AA### format")
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]


        pattern = re.compile("[A-Z]{2}[0-9]{3}")
        if pattern.match(number):
            self._number = number
        else:
            raise ValueError

    def number(self):
        """
        Flight Number
        :return: flight number
        """
        return self._number[2:]

    def airline(self):
        """

        :return: The airline code
        """
        return self._number[:2]


    def alllocate_seat(self, seat, passenger):
        """
        Allocates a seat to a passenger
        :param seat: seat designator such as 12c or 13b
        :param passenger: The passenger name
        :return:
        """
        rows, seat_letter = self._aircraft.seating_plan()
        letter = seat[-1]
        row = seat[:-1]
        if letter not in seat_letter:
            raise ValueError("Invalid seat letter {}".format(letter))
        try:
            row = int(row)
        except ValueError:
            raise ValueError("Invalid seat row{}".format(row))
        if row not in rows:
            raise ValueError("Invalid row number{}".format(row))
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        self._seating[row][letter] = passenger

class Aircraft:
    """
    It flies
    """

    def __init__(self,registration, model, num_rows, num_seats_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_row = num_seats_row



    def getreg(self):
        return self._registration
    def getmodel(self):
        return self._model
    def seating_plan(self):
        return(range(1,self._num_rows+1)), "ABCEDFGHJK"[:self._num_seats_row]

def main():
    """

    :return:
    """



if __name__ == '__main__':
    main()
    exit(0)