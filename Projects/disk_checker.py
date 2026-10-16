import shutil

path = "/"

total, used, free = shutil.disk_usage(path)

used_percent = (used / total) * 100

print("--- Disk Health Report ---")
print(f"Total space: {total / (1024**3):.1f} GiB")
print(f"Used space: {used / (1024**3):.1f} GiB")
print(f"Free space: {free / (1024**3):.1f} GiB")
print(f"Disk usage: {used_percent:.1f}%")

if used_percent >= 90:
    print("Status: CRITICAL")
    print("Action: Investigate disk usage immediately.")
elif used_percent >= 80:
    print("Status: WARNING")
    print("Action: Check disk usage and plan cleanup.")
else:
    print("Status: HEALTHY")
    print("Action: No immediate disk-space action needed.")