# second largest number
"""num = [45, 37, 20, 89, 36]
largest = 0
second_largest = 0
for i in num:
    if i > largest:
        second_largest = largest
        largest = i

print("Largest:", largest)
print("Second Largest:", second_largest)"""

#Count vowels.
word=input("enter the word : ")
vowels="aeiou"
count=0
for i in word:
    if i in vowels:
            count+=1
            
print(count)