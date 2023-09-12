# set
from datetime import datetime

set_1 = set("hello")
# print(sorted(set_1))
# set_2 = {(1, 2), (1, 2)}
# print(len(set_2))
# for i in set_2:
#     print(i)
# dict_set = dict(set_2)
# tuple_1 = tuple(set_2)
# list_1 = list(set_2)
# print(dict_set)
# print(tuple_1)
# print(list_1)
# print((1, ))

# list1 = [1, 1, 2, 3, 4]
# start_time = datetime.now()
# new_list = []
# for i in list1:
#     if i not in new_list:
#         new_list.append(i)
# end_time = datetime.now() - start_time
# print(end_time)

# start_time = datetime.now()
# new_set = list(set(list1))
# end_time = datetime.now() - start_time
# print(end_time)
list1 = {1, 1, 2, 3, 4}
# list1.update({1, 1, 3, 6})
# list1.remove(9)
element = list1.pop()
element2 = list1.pop()
print(list1)
print(element)
print(element2)
list1.clear()
print(list1)