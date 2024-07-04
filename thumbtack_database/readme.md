## Database

Commands and Syntax:
- SET name value
- GET name
- UNSET name
- NUMEQUALTO value
- END

- Files:
  - database.py: Client to interact with the database and users
  - db_parser.py: Parser to parse the commands and return the output
    - `parse_command` function to parse the command and return the output
  - db.py: Database to store the data and execute commands on it

Questions:
1. We can't nest these commands yet, right? - Nope
2. Do we need to make NUMEQUALTO O(logn)?