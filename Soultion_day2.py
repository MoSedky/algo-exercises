

def get_array(input_array):
    splitter_arr = input_array.split(' ')
    reversed_list = []
    get_rev_bk_list = []

    for word in splitter_arr:
        print(word[::-1])
        reversed_list.append(word[::-1])
        reversed_list = sorted(reversed_list, key=lambda x: x[0])

    for rev_word in reversed_list:
        get_rev_bk_list.append(rev_word[::-1])

    print(get_rev_bk_list)
    return


get_array("massage yes massage yes massage")
