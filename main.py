# write your code here
person={
    'name': 'Hessa',
    'age' : 15,
    'hobbies': ['reading','writing','coding'] 
}

print(person['name'])
print(person['age'])
person['age']=16

print(person['age'])
person['country']='kuwait'
print(person)
print(len(person))

person['hobbies'].append('sleeping')
def check_hobbies(person):
    if len(person['hobbies'] )> 3 :
        print('wow your amazing')
    else:
        print('add more hobbies :)')
check_hobbies(person)




