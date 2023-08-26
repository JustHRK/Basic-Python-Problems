#WAP to mine a log file and find out whether it contains "python"

with open("log.txt") as f:
    x=f.read().lower()

if "python" in x:
    print("python:found")
else:
    print("python:not found")