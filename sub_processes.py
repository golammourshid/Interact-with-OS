import subprocess

# A system command that sends ICMP packets can be executed within a script by using subprocess.run
# result = subprocess.run(["date"])
# print(result.returncode)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)
print(result.stdout.decode().split())
