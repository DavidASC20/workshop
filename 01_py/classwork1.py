#David Chong
#SoftDev
#K01 Python Random List
#2021-09-20

#chooses between class1 and class2 at random, then chooses the student in the class at random.
import random

class1 = [
    "Michael Jordan",
    "Lebron James",
    "Kanye West",
    "Will Smith"
]

class2 = [
    "Jesus",
    "Juesus",
    "Zeus",
    "David"
]

random_class = random.choice([class1, class2]);
random_student = random.choice(random_class);

print(random_student);
