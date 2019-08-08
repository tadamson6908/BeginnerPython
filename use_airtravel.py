"""
use flight class
"""
from airtravel import Flight, Aircraft

def make_flight():
    a1 = Aircraft("blah", "airbus", 22, 6)
    flight = Flight("SN066", a1)
    print(flight, type(flight))
    print(flight.number())
    flight.alllocate_seat("1C", "John")
    flight.alllocate_seat("11C", "Cindy")
    return flight




def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
              "Flight: {1}" \
              " Seat: {2}"\
                " Aircraft {3}"\
               " |".format(passenger,flight_number,seat,aircraft)
    banner = "+" + "-" * (len(output)-2) + "+"
    border = "|" + " " * (len(output) -2) + "|"
    lines = [banner,border,output,border,banner]
    card = '\n'.join(lines)
    print(card)
    print()
def main():
    """

    :return:
    """
    flight = make_flight()
    print(flight._seating)
    print(flight.num_available_seats())
    flight.make_boarding_class(console_card_printer)



if __name__ == '__main__':
    main()
    exit(0)