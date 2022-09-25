import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater that 0.")
        else:
            print("Please enter a number!")

    return amount



def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet for (1-" + str(MAX_LINES) + "): ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines between 1 and " + str(MAX_LINES))
        else:
            print("Please enter a number!")

    return lines



def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between " + str(MIN_BET) + " and " + str(MAX_BET))
        else:
            print("Please enter a number!")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough balance to bet " + str(total_bet) + "$. Your current balance is " + str(
                balance) + "$")
        else:
            break

    print("\nYou are betting " + str(bet) + "$ on " + str(lines) + ". Total bet is equal to " + str(bet * lines) + "$")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print("You won " + str(winnings) + "$")
    print("You won on lines: ", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()

    while True:
        print("Current balance is ", str(balance), "$")
        answer = input("\nPress enter to play / q to quit")
        if answer == "q":
            break
        balance += spin(balance)

    print("You left with", str(balance), "$")
main()