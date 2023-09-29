max_calories = 0
file_name = "input"

with open(file_name, "r") as file:
    last_line = False
    elv_calories = 0
    while not last_line:
        calories = file.readline()

        if len(calories):
            if calories == "\n":
                max_calories = max_calories if max_calories >= elv_calories else elv_calories
                elv_calories = 0
            else:
                elv_calories += int(calories)
        else:
            last_line = True

print(max_calories)

