
from db_parser import parse_command
from db import Database

db = Database()

while True:
    curr_command = input("Enter command: ")
    if curr_command == "END" or curr_command == "end":
        print("Ending program...")
        break

    # print("Command entered: ", curr_command)

    parsed_cmd = parse_command(curr_command)
    # print("Parsed command: ", parsed_cmd)

    res = db.process(parsed_cmd)

    if res is not None:
        print("Result: ", res)

