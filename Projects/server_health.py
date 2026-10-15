try:
    disk_usage = float(input("Enter disk usage percentage: "))

    if disk_usage < 0 or disk_usage > 100:
        print("Error: Enter a percentage between 0 and 100.")
    else:
        print("\n--- Server Health Report ---")

        if disk_usage > 80:
            print("Status: WARNING")
            print("Disk usage is too high!")
        else:
            print("Status: HEALTHY")
            print("Disk usage is within acceptable limits.")

        print("Disk usage:", disk_usage, "%")

except ValueError:
    print("Error: Please enter a valid number.")
