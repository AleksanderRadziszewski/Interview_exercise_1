def solution(N):
    max_current_number = 0
    list_N = list(str(N))
    array_size = len(str(N))

    for i in range(array_size):
        if list_N[i] == "5":
            delete_list = list_N.copy()
            delete_list.pop(i)
            after_delete = int("".join(delete_list))
            if max_current_number < after_delete:
                max_current_number = after_delete
            elif after_delete < 0 and after_delete < max_current_number:
                max_current_number = after_delete

    print(max_current_number)


solution(-5859)