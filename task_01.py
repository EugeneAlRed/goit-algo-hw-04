def total_salary(path):
    """returns the total and average wages

    Args:
        path (str): path to the text file 

    Returns:
        int: total and average wages
    """
    try:
        with open(path, 'r') as fh:
            total = 0
            average = 0
            count = 0
            while True:
                line = fh.readline()

                if not line:
                    break
                salary_list = line.split(',')
                salar = salary_list[-1]
                count += 1
                total += int(salar)
            average = total // count
        return total, average
    except FileNotFoundError:
        print(f'No such file or directory: {path}')


total, average = total_salary("file.txt")
print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
