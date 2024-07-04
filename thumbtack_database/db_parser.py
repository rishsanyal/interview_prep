
# Include type checking too

COMMAND_INFO = {
    "SET": {
        "alias": "INSERT",
        "num_args": 2,
        "value_type": int
    },
    "GET": {
        "num_args": 1,
        "result": True
    },
    "UNSET": {
        "num_args": 1,
    },
    "EXISTS": {
        "num_args": 1,
    },
    "NUMEQUALTO": {
        "num_args": 1,
        "key_type": int,
        "result": True
    },
    "BEGIN": {
        "num_args": 0
    },
    "ROLLBACK": {
        "num_args": 0
    },
    "COMMIT": {
        "num_args": 0
    }
}

def parse_command(command):
    """Parse command string to get command information. Raise error if invalid command

    Args:
        command (Str): Command string given by user

    Returns:
        Dict: Command information with key and value of command
    """
    cmd_list = command.split(" ")

    if cmd_list[0].upper() not in COMMAND_INFO:
        raise ValueError("Command not recognized.")
    else:
        cmd_info = COMMAND_INFO[cmd_list[0].upper()]
        if len(cmd_list) - 1 != cmd_info["num_args"]:
            raise ValueError(f"Command {cmd_list[0]} requires {cmd_info['num_args']} arguments.")

        if len(cmd_list) == 1:
            key = None
            value = None
        else:
            value_type = cmd_info.get("value_type", str)
            key_type = cmd_info.get("key_type", str)

            key = key_type(cmd_list[1])
            value = value_type(cmd_list[2]) if len(cmd_list) == 3 else None

        return {
            "command": cmd_info.get("alias", cmd_list[0]).lower(),
            "key": key,
            "value": value,
            "get_result": cmd_info.get("result", False)
        }

if __name__ == "__main__":
    # print(parse_command("SET a 10"))
    # print(parse_command("GET a"))
    # print(parse_command("DEL a"))
    # print(parse_command("EXISTS a"))
    # print(parse_command("NUMEQUALTO 10"))
    print(parse_command("COMMIT"))
    # print(parse_command("SET a"))
    # print(parse_command("EXISTS"))