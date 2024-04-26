from pathlib import Path

def total_salary(path: Path) -> tuple:
    try:
        with open(path, 'r', encoding='utf8') as file:
            count = 0
            sum = 0
            for line in file.readlines():
                emloyee = line.strip().split(',')
                count += 1
                sum += float(emloyee[1])
            average = sum / count
        return (sum, average)
    except Exception as e:
        print(e)
        return (None, None)

if __name__ == '__main__':
    print(total_salary('first_task/employees.txt'))


