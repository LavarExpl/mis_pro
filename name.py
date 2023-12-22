dict1 = {'david':{'address':'726',
                 'phone':'718',
                 'email':"Icloud.com"},

         'jerry': {'address': '785',
                   'phone': '347',
                   'email': "gmail.com"}
         }


numbers = dict1['jerry']['email']
class Name:
    def __init__(self,name,college):
        self.name = name

        self.college = college



class Person(Name):
    def __init__(self,first_name,last_name,eye_color,age,):
        self.first_name =first_name
        self.last_name =last_name
        self.eye_color = eye_color
        self.age = age
        self.name = Name('larry','maine')

person = Person(first_name='lavar',last_name= 'Harewoood',eye_color='brown',age=65,)


print(person.first_name)

P2 =(person.name.name  +  '\n' + person.name.college)
P2 = person.first_name = 'pam'
print(P2)