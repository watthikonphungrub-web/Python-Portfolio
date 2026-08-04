import subprocess 

result = subprocess.run([ "df", "-h"], capture_output=True, text=True)


print("Errors and Warnings:")
print(result.stdout)

