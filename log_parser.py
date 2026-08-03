with open("app.log", "r") as log_file:
    for line in log_file:
        if "ERROR" in line:
            print(f"Error found: {line.strip()}")
        elif "WARNING" in line:
            print(f"Warning found: {line.strip()}")
        else:
            print(f"Info: {line.strip()}")  