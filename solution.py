def solution(n):
    max_current_number = 0
    list_n = list(str(n))
    array_size = len(list_n)

    for i in range(array_size):

        if list_n[i] == "5":
            delete_list = list_n.copy()
            delete_list.pop(i)
            after_delete = int("".join(delete_list))
            if max_current_number < after_delete:
                max_current_number = after_delete
            elif after_delete < 0 and after_delete < max_current_number:
                max_current_number = after_delete

    print(max_current_number)


solution(-5859)
