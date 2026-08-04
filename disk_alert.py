import subprocess

result = subprocess.run(["df", "-h","/"], capture_output=True, text=True)

output = result.stdout.strip().strip('\n')

data_lines = output.split('\n')

data_columns = data_lines[1].split()

used_percentage = data_columns[4]

used_percentage_value = int(used_percentage.strip('%'))


if used_percentage_value > 20:
    print(f"[CRITICAL]: {used_percentage}")
else:
    print(f"[OK]: {used_percentage}")
