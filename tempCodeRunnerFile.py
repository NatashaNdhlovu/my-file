
import random
number=random.randint (1,100)
guese=0
tries=0

while guese!=number:
       guese=int(input("guese the number"))
       if guese < number:
           print("low")
       elif guese > number:
           print("high")
       else:
           print ("correct")    