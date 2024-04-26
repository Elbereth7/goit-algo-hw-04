from first_task import total_salary
from second_task import get_cats_info
from third_task import directory_content, Path

# First task output
total, average = total_salary("first_task/employees.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

# Second task output
cats_info = get_cats_info("second_task/cats.txt")
print(cats_info)

# Third task output
parent_folder_path = Path('.')
directory_content(parent_folder_path)

