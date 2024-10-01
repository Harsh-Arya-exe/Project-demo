people = {'Arham':'Blue', 'Lisa': 'Yellow', 'Vinod':'Purple', 'Jenny':'Pink'}
print("1. The number of students in the list are: ",len(people))
people['Lisa'] = 'Black'
print("2. The List after changing color of Lisa: ",people)
people.pop('Jenny')
print("3. Dictionary after removing 'Jenny':",people)
students = list(people.keys())
students.sort()

new_people = dict()
for i in students:
    new_people[i] = people[i]
print("4.Dictionary after sorting the names alphabetically",new_people)