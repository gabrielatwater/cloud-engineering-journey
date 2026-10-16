import shutil

# Check disk space
total, used, free = shutil.disk_usage("/")
used_percent = (used / total) * 100 

# Count log messages
error_count = 0
warning_count = 0

try:
    with open("Labs/server.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1


except FileNotFoundError:
    print("Warning: Log file not found.")


# Print report
print("\n--- System Health Report ---")
print(f"Disk usage: {used_percent:.1f}%")
print(f"Errors found: {error_count}")
print(f"Warnings found: {warning_count}")

if used_percent >= 90 or error_count > 0:
    print("Overall status: INVESTIGATION NEEDED")
elif used_percent >= 80 or warning_count > 0:
    print("Overall status: WARNING")
else:
    print("Overall status: HEALTHY")