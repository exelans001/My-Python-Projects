#Mini-RPG Character Creator

import random

from colorama import Fore,init

#For Colorama
init(autoreset=True)

#Dicts
stats={"STR":0,
       "AGI":0,
       "INT":0
       }

#Name
name=input(Fore.CYAN + "Name: ")

#Class
class_choose=input(Fore.YELLOW + "Choose a class [Warrior,Archer,Magician]: ").strip().lower()



#Warrior
if class_choose=="Warrior":
    show=input("For see your stats write [stats]: ")
    if show.lower()=="stats":
     w_str=stats["STR"]=random.randint(5, 20)
     w_agi=stats["AGI"]=random.randint(1, 10)
     w_int=stats["INT"]=random.randint(1, 10)
     print(Fore.RED + f"Your stats: {stats}")

#Archer
elif class_choose=="Archer":
    show=input("For see your stats write [stats]: ")
    if show.lower()=="stats":
     a_str=stats["STR"]=random.randint(1, 10)
     a_agi=stats["AGI"]=random.randint(5,20)
     a_int=stats["INT"]=random.randint(5,15)
     print(Fore.RED + f"Your stats: {stats}")

#Magician
elif class_choose=="Magician":
    show=input("For see your stats write [stats]: ")
    if show.lower()=="stats":
        m_str=stats["STR"]=random.randint(1, 5)
        m_agi=stats["AGI"]=random.randint(1, 5)
        m_int=stats["INT"]=random.randint(10, 20)
        print(Fore.RED + f"Your stats: {stats}")
else:
    print("Wrong choose")    
