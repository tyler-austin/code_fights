def sort_by_height(in_list: list):
    no_trees = list(filter(lambda x: x != -1, in_list))
    no_trees.sort(reverse=True)
    new_list = []
    for h in in_list:
        if h == -1:
            new_list.append(h)
        else:
            new_list.append(no_trees.pop())
    return new_list


if __name__ == '__main__':

    heights = [-1, 150, 190, 170, -1, -1, 160, 180]

    print(sort_by_height(heights))
