#David Chong
#SoftDev
#K05 Python Random List Amalgamation
#2021-09-25

#summary - Roshani and I shared our code and looked at each others, seeing what was good about the others.
#discoveries - Roshani discovered the random.choice() function, which helped me condense my code.
#questions - none so far
#comments - changed pd1 and pd2 to include actual names.
import random

class1 = [
    "cliu20",
    "llee20",
    "ekrechmer20",
    "aalonso20",
    "owang20",
    "schoi20",
    "ttakada20",
    "dmaheshwari20",
    "wchen20",
    "tfahey20",
    "jnelson20",
    "mlo20",
    "tnguyen20",
    "agoenka20",
    "sanand20",
    "ebuller20",
    "rroy20",
    "yelsharawy20",
    "gmcginley20",
    "rzheng21",
    "sethun20",
    "imahid20",
    "zlin20",
    "imijacika20",
    "hgan20",
    "ilam21",
    "ltomwong20",
    "tacuna20"
]

class2 = [
    "alin21",
    "naronesty20",
    "dsooknanan20",
    "kcao20",
    "rxiao20",
    "aabdullah20",
    "ywu20",
    "ichang20",
    "wdong20",
    "jzou20",
    "pging20",
    "ryeung20",
    "jlee25",
    "eguo20",
    "azhang22",
    "qliu20",
    "rshrestha20",
    "angan20",
    "dchong20",
    "eknapp20",
    "mborczuk20",
    "hzhang20",
    "tyu20",
    "jwu20",
    "jxie20",
    "jkloepfer20",
    "srakib20",
    "lwong20",
    "sliu202",
    "yliangli20",
    "cnelson20",
    "ajuang20",
    "hhuang20"
]


def random_student():
    val = input("Which class? class1 or class2\n")
    if(val == "class1"):
        print(random.choice(class1))
    elif(val == "class2"):
        print(random.choice(class2))
    else:
        random_class = random.choice([class1, class2])
        print(random.choice(random_class))
        
        

random_student()