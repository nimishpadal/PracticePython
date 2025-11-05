'''
Problem:
Given a list of integers or strings, identify and return all duplicate elements using Python sets.

'''

def duplicates(data):
    # Convert list to set to get unique elements
    unique_set = set(data)
    # Create a list of duplicates by checking counts
    duplicates_list = [item for item in unique_set if data.count(item) > 1]
    return duplicates_list

if __name__ == '__main__':
    nums = [4, 2, 7, 4, 9, 2, 3]
    data = ["apple", "banana", "apple"]
    print(f"The duplicated from {data} is / are {duplicates(data=data)}")