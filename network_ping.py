import  subprocess

result = subprocess.run(["ping", "-c", "3", "8.8.8.8"], timeout=10, capture_output=True, text=True)



print("Ping Output:")
print(result.stdout)

