'''Pseudocode/Thinking
Create a function that takes in a string as a parameter
and returns the number of vowels
(a, e, i, o, and u) contained in the string.

1. Get input from user to enter any message
2. create def function that takes in user's input as a parameter
3. create a list called vowels so the computer knows what the vowels are
4. compare each letter of user's input against vowels to see if the message has a vowel
5. print the number of vowels in the string
'''

vowels = ['a', 'e', 'i', 'o', 'u']

mess = input(f"Enter any message\n>").lower()

def vowel(mess):
    for char in mess:
        if char in vowels:
            print([char])
vowel(mess)