data = []

print("Enter name,age,height (empty line to stop):")
while True:
    line = input()
    if line == "":
        break
    name, age, height = line.split(",")
    data.append((name, int(age), int(height)))

data.sort(key=lambda x: (x[0], x[1], x[2]))
print(data)
