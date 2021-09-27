#David Chong
#SoftDev
#K05 Python Random List Amalgamation
#2021-09-25

#SUMMARY OF TRIO DISCUSSION
#Roshani and I shared our code and looked at each others, seeing what was good about the others.
#DISCOVERIES
#Roshani discovered the random.choice() function, which helped me condense my code.
#QUESTIONS
#the change of adding both lists into classes led me to wonder how to access the class1 and class2.
#COMMENTS
#changed pd1 and pd2 to include actual names. put both lists in classes
import random

KREWES = {
'class1': ["Alejandro Alonso", "Aryaman Goenka", "Christopher Liu", "Deven Maheshwari", "Emma Buller", "Ella Krechmer", "Gavin McGinley",
       "Haotian Gan", "Ivan Lam", "Ishraq Mahid", "Ivan Mijacika", "Julia Nelson", "Lucas Lee", "Lucas Tom wong",
       "Michelle Lo", "Oscar Wang", "Rayat Roy", "Reng geng Zheng", "Shriya Anand", "Shyne Choi", "Sadid Ethun",
       "Tomas Acuna", "Theodore Fahey", "Tina Nguyen", "Tami Takada", "William Chen", "Yusef Elsharawy", "Zhao yu Lin"],


'class2': ["Alif Abdullah", "Andrew Juang", "Andy Lin", "Austin Ngan", "Annabel Zhang", "Cameron Nelson", "David Chong",
        "Daniel Sooknanan", "Eric Guo", "Eliza Knapp", "Hebe Huang", "Han Zhang", "Yoonah Chang", "Joshua Kloepfer",
        "Josephine Lee", "Jonathan Wu", "Jesse Xie", "Justin Zou", "Kevin Cao", "Liesel Wong", "Michael Borczuk",
        "Noakai Aronesty", "Patrick Ging", "Qina Liu", "Roshani Shrestha", "Rachel Xiao", "Raymond Yeung", "Sophie Liu",
        "Shadman Rakib", "Thomas Yu", "Wen hao Dong", "Yaying Liang li", "Yuqing Wu"]
    }


def random_student():
    val = input("Which class? class1 or class2\n")
    if(val == "class1"):
        print(random.choice(KREWES["class1"]))
    elif(val == "class2"):
        print(random.choice(KREWES["class2"]))
    else:
        random_class = random.choice(KREWES["class1", class2])
        print(random.choice(random_class))
        
        

random_student()
