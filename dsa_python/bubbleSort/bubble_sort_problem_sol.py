def bubble_sort(data, sort_key):
    n = len(data)
    # Traverse through all array elements
    for i in range(n):
        # Compare array elements
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if data[j][sort_key] > data[j+1][sort_key]:
                data[j], data[j+1] = data[j+1], data[j]
    
    return data


if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    print(f'Given unsorted array:', *elements, sep='\n')
    
    bubble_sort(data=elements, sort_key='transaction_amount')

    print(f'Array after Sorting Based On Key:', *elements, sep='\n')