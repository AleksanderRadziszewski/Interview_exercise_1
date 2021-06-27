import decimal


# def solution_v_one(n):
#     max_current_number = 0
#     n = decimal.Decimal(n)
#     list_n = list(str(n))
#     array_size = len(list_n)
#
#     for i in range(array_size):
#
#         if list_n[i] == "5":
#             delete_list = list_n.copy()
#             delete_list.pop(i)
#             after_delete = int("".join(delete_list))
#             if max_current_number < after_delete:
#                 max_current_number = after_delete
#             elif after_delete < 0 and after_delete < max_current_number:
#                 max_current_number = after_delete
#
#     print(max_current_number)
#
#
# solution_v_one(15958)


def solution_v_two(n):
    max_value = []
    item = "5"
    n = decimal.Decimal(n)
    lst = list(str(n))
    indexes = [i for i, x in enumerate(lst) if x == item]

    for i in indexes:
        lst.pop(i)
        lst_value = int("".join(lst))
        max_value.append(lst_value)
        lst.insert(i, item)
    print(max(max_value))


solution_v_two(15958)
