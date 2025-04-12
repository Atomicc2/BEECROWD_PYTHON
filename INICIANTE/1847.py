def temp(day1, day2, day3):
    if day1 > day2:
        if day2 <= day3:
            return ':)'
        elif (day1 - day2) > (day2 - day3):
            return ':)'
        elif (day1 - day2) <= (day2 - day3):
            return ':('
    if day1 < day2:
        if day2 >= day3:
            return ':('
        elif (day2 - day1) > (day3 - day2):
            return ':('
        elif (day2 - day1) <= (day3 - day2):
            return ':)'
    if day1 == day2:
        if day3 > day2:
            return ':)'
        if day3 <= day2:
            return ':('

day1, day2, day3 = map(int, input().split())
print(temp(day1, day2, day3))

