def multi_level_sort(data, sorting_order):
    """
    Sorts the given list of dictionaries based on a given sorting order.
    """
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            for k in sorting_order:
                if data[j][k] < data[min_idx][k]:
                    min_idx = j
                    break
                elif data[j][k] > data[min_idx][k]:
                    break
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
    return data


if __name__ == '__main__':
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    print(f'Given unsorted array:', *elements, sep='\n')
    multi_level_sort(
        elements, 
        ['First Name', 'Last Name']
    )
    print(f'Array after Multi-Level Sorting:', *elements, sep='\n')
