with open('input.txt', 'r') as infile:
    data = infile.readlines()

task = 2
if task == 1:
    # first task
    valid_reports = 0
    for line in data:
        numbers = line.split()
        previous = int(numbers[0])
        increasing = 0
        for number in numbers[1:]:
            number = int(number)
            if increasing == 0:
                if number > previous:
                    increasing = 1
                elif number < previous:
                    increasing = -1
                else:
                    break
            diff = number - previous
            if diff * increasing < 1 or diff * increasing > 3:
                break
            previous = number
        else:
            valid_reports += 1
    print(valid_reports)
else:
    # second task
    valid_reports = []
    for reverse in (False, True):
        for idx, line in enumerate(data):
            if idx in valid_reports:
                continue
            nbr_errors = 0
            numbers = line.split()
            if reverse:
                numbers.reverse()
            previous = int(numbers[0])
            increasing = 0
            for number in numbers[1:]:
                number = int(number)
                if increasing == 0:
                    if number > previous:
                        increasing = 1
                    elif number < previous:
                        increasing = -1
                    else:
                        if nbr_errors:
                            break
                        else:
                            nbr_errors += 1
                            continue
                diff = number - previous
                if diff * increasing < 1 or diff * increasing > 3:
                    if nbr_errors:
                        break
                    else:
                        nbr_errors += 1
                        continue
                previous = number
            else:
                valid_reports.append(idx)
    print(len(valid_reports))