'''
Problem:
Given two sorted lists list1 and list2, merge them into a single sorted list without using 
Python’s built-in functions like sorted() or sort().

'''

def merge_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list

if __name__ == '__main__':
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8, 10, 12]

    print(f"The merged and sorted list of {list1} and {list2} is {merge_lists(list1,list2)}")