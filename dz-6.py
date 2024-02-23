# example_list = [12, 3, 4, 10]
# example_list = [1]
# example_list = []
example_list = [12, 3, 4, 10, 8]


if len(example_list) > 1:
    last_element = example_list.pop()
    example_list.insert(0, last_element)
print(example_list)
