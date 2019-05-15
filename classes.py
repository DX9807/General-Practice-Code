# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:01:51 2019

@author: Subodh
"""
'''
class Myclass():
    string='Subodh Yadav'
    Integer=1995
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    

x=Myclass('Rahul yadav',25)
print(x.string,x.Integer)
x1=Myclass('Ankit Yadav',29)

print(x1.name,x1.age)
print(x.name,x.age)'''


class Dog():
    legs=4
    tongue=1
    eyes=2
    ears=2
    
    def __init__(self,color,breed):
        self.color=color
        self.breed=breed
      
    def bark(self):
        print(self.color,self.breed)
        print('Every Dog Barks..........')
    
   
    def run(self):
        print(self.color,self.breed)
        print('Runs very fast.......')
        


dog1=Dog('Red','Pamelian')
dog2=Dog('Black','Desi')
dog3=Dog('White','BullDog')



print(dog1.bark())
print(dog2.bark())
print(dog3.bark())
print(dog1.run())

class TimeStone:
    string='Dr Strange has timestone'
    def __init__(self,soulstone,powerstone,tesseract):
        self.soulstone=soulstone
        self.powerstone=powerstone
        self.tesseract=tesseract
        
    def show_soulstone(self):
        print('Soulstone is kept in {}'.format(self.soulstone))
    def show_powerstone(self):
        print('Powerstone is kept at {}'.format(self.powerstone))
        
    def show_tesseract(self):
        print('Tesseract is kept on {}'.format(self.tesseract))
        
        
        
ts=TimeStone('Earth','Earth','Xandar')     
#ts=TimeStone('Asgard','Xandar','Earth')
print(ts.string)
print(ts.show_powerstone(),ts.show_soulstone(),ts.show_tesseract())        
        





