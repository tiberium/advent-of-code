top_calories = [0, 0, 0]
file_name = "input"

with open(file_name, "r") as file:
    last_line = False
    elv_calories = 0
    while not last_line:
        calories = file.readline()

        if len(calories):
            if calories == "\n":
                if elv_calories > min(top_calories):
                    top_calories[top_calories.index(min(top_calories))] = elv_calories

                elv_calories = 0
            else:
                elv_calories += int(calories)
        else:
            last_line = True

print(sum(top_calories))

