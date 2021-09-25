import os
os.system ("clear")
import random
import getpass
import time
import sys
def slowtype(t):
   for D in t + "\n":
   	sys.stdout.write(D)
   	sys.stdout.flush()
   	time.sleep(10/100)


#colors 
GG = "\033[32;1m" # Green light
RR = "\033[31;1m" # Red light


print("")
print("")
print("")
print(RR+"        [ Welcome The Tool killi Cood ] ")
print(GG+"""
                uu$$$$$$$$$$$uu
             uu$$$$$$$$$$$$$$$$$uu
            u$$$$$$$$$$$$$$$$$$$$$u
           u$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$$$$$$$$$$$$$$$$$$$$u
          u$$$$$$“   “$$$“   “$$$$$$u
          “$$$$“      u$u       $$$$“
           $$$u       u$u       u$$$
           $$$u      u$$$u      u$$$
            “$$$$uu$$$   $$$uu$$$$“
             “$$$$$$$“   “$$$$$$$“
               u$$$$$$$u$$$$$$$u
                u$“$“$“$“$“$“$u
     uuu        $$u$ $ $ $ $u$$       uuu
    u$$$$        $$$$$u$u$u$$$       u$$$$
     $$$$$uu      “$$$$$$$$$“     uu$$$$$$
   u$$$$$$$$$$$uu    “““““    uuuu$$$$$$$$$$
   $$$$“““$$$$$$$$$$uuu   uu$$$$$$$$$“““$$$“
    “““      ““$$$$$$$$$$$uu ““$“““
              uuuu ““$$$$$$$$$$uuu
     u$$$uuu$$$$$$$$$uu ““$$$$$$$$$$$uuu$$$
     $$$$$$$$$$““““           ““$$$$$$$$$$$“
      “$$$$$“                      ““$$$$““
        $$$“                         $$$$“""")

print("")
print("")
nmpr = input(RR+"Enter the Number Target : ")
print(GG+"")
def GetPassword(data):
	Max = 6
	password=""
	while len(password) != Max:
		value = random.choice(data)
		password += value
	return password

data ='1234567890'
for i in range(15):
	print(GetPassword(data))


print(RR+"")
print("×======================×")
slowtype("     by_HEKSOS")
print("×======================×")
slowtype(" YouTube : MR.HEKSOS")
print("×======================×")
print("")
