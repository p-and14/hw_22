# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля
from typing import List

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read() -> List:
    return [x.split(";") for x in csv.split('\n')]


def _sort(data: List) -> List:
    return sorted(data, key=lambda x: int(x[1]))


def _filter(data):
    return [x for x in data if int(x[1]) > 10]


def get_users_list():
    data = _read()
    data = _sort(data)
    return _filter(data)


if __name__ == '__main__':
    print(get_users_list())
