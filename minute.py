import pprint
new_list = []
phrase = "Don't Panic"
plist = list(phrase)
print(phrase)
print(plist)
temps = [32.0,212.0,0.0,81.6,100.0,45.3]
words = ['hello','world']
car_details = ['Toyota','RAV4',2.2,6087]
comp = [new_list,temps,words,car_details]
vowels = ['a','e','i','o','u']
for x in words:
    if x in vowels:
        print("This word has a vowel")
    else:
        print("This word has no vowel")
print(len(temps))
temps.append(34.88)
print(len(temps))
if 23.9 not in temps:
    temps.append(23.9)
print(temps)
print(temps.pop())
print(temps)
temps.extend([43.7,89.5,23.2])
print(temps)
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))
print(plist)
new = ''.join(plist)
print(new)
#sets
new_vowels = {'a','e','i','o','u'}
print(new_vowels)
x= 'kaushik'
u = new_vowels.union(set(x))
print(u)
c = new_vowels.difference(set(x))
print(c)
i = new_vowels.intersection(set(x))
print(sorted(i))
#tuples
new_vowels1 = ('a','e','i','o','u')
print(new_vowels1)
#storing a table in a dictionary
people = {}
people['Ford']={'Name':"Ford Prefect",'Gender':'Male','Occupation':'Researcher'}
people['Arthur']={'Name':"Arthur Dent",'Gender':'Male','Occupation':'Sandwich_maker'}
people['Robot'] = {'Name':'Marvin','Gender':'Unknown','Occupation':'Paranoid Android'}
print(people)
pprint.pprint(people)
print(people['Arthur']['Occupation'])

