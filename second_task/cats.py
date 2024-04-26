from pathlib import Path

def get_cats_info(path: Path) -> list:
    try:
        with open(path, 'r', encoding='utf8') as file:
            cats_list = []
            for line in file.readlines():
                cat_list = line.strip().split(',')
                cat_dict = {}
                cat_dict['id'] = cat_list[0]
                cat_dict['name'] = cat_list[1]
                cat_dict['age'] = cat_list[2]
                cats_list.append(cat_dict)         
        return cats_list
    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    print(get_cats_info('second_task/cats.txt'))