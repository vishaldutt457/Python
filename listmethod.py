# currencies = ['Dollar', 'Euro', 'Pound']

# currencies.append('Yen')
# print(currencies)
# # Output: ['Dollar', 'Euro', 'Pound', 'Yen']


# vowel = ['a', 'e', 'i', 'u']
# vowel.insert(3, 'o')
# print('List:', vowel)
# # Output: List: ['a', 'e', 'i', 'o', 'u']


# prime_numbers = [2, 3, 5]
# numbers = [1, 4]
# numbers.extend(prime_numbers)
# print('List after extend():', numbers)


# prime_numbers = [2, 3, 5, 7]
# # remove the element at index 2
# removed_element = prime_numbers.pop(2)
# print('Removed Element:', removed_element)
# print('Updated List:', prime_numbers)
# # Output: 
# # Removed Element: 5
# # Updated List: [2, 3, 7]


# prime_numbers = [2, 3, 5, 7, 9, 11]
# prime_numbers.remove(9)
# print('Updated List: ', prime_numbers)
# # Output: Updated List:  [2, 3, 5, 7, 11]


# prime_numbers = [2, 3, 5, 7, 9, 11]
# print(prime_numbers.clear())
# # Output: List after clear(): []


# prime_numbers = [2, 3, 5, 7]
# prime_numbers.reverse()
# print('Reversed List:', prime_numbers)
# # Output: Reversed List: [7, 5, 3, 2]


# prime_numbers = [11, 3, 7, 5, 2]
# prime_numbers.sort()
# print(prime_numbers)
# # Output: [2, 3, 5, 7, 11]


# # create a list
# numbers = [2, 3, 5, 2, 11, 2, 7]
# count = numbers.count(2)
# print('Count of 2:', count)
# # Output: Count of 2: 3


# animals = ['cat', 'dog', 'rabbit', 'horse']
# index = animals.index('dog')
# print(index)
# # Output: 1

# prime_numbers = [2, 3, 5]
# numbers = prime_numbers.copy()
# print('Copied List:', numbers)
# # Output: Copied List: [2, 3, 5]


def occur(list):
    dict={}
    for item in list:
        if item in dict:
            dict[item]+=1;
        else:
            dict[item]=1
    return dict

print(occur([2, 3, 5, 2, 11, 2, 7]));