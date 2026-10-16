log_file = "Labs/server.log"


error_count = 0
warning_count = 0

try:
    with open(log_file, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
                print("Found an error:", line.strip())

            elif "WARNING" in line:
                warning_count += 1
                print("Found a warning:", line.strip())

    print("\n--- Log Summary ---")
    print("Total errors:", error_count)
    print("Total warnings:", warning_count)

    if error_count > 0: 
        print("Overall status: INVESTIGATION NEEDED")
    else:
        print("Overall status: NO ERRORS FOUND")

except FileNotFoundError:
    print("Error: The log file was not found:", log_file)

except PermissionError:
    print("Error: You do not have permission to read:", log_file) 

