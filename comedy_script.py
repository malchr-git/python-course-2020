# First time writing a script 
#

import time 

print("Hey there!")
time.sleep(2)
print("I'm a Comedy Robot!")
time.sleep(2)
print("Give me 2 sec..")
time.sleep(3)
print("Okaaayy, I am readyyy to...")

time.sleep(1)
for letter in "PARTYYY":    
    print(letter, sep=' ')    
    time.sleep(1)
    
print()
time.sleep(3)
print("Alright, maybe not party...")
time.sleep(2)

print("But let's crack some jokes anyways.. Welcome to my first comedy script!!")
time.sleep(2)

print("I'm Roberta The Comedy Robot and I am excited to get started!!")
time.sleep(2)

print()
print()
print("What is your name?")
time.sleep(1)

name = input("Please type your name here: ")
for i in range(1):    
    print(f"What a beautiful name... {name}!")    
    time.sleep(1)
    
print(f"I hope I can make you laugh, {name}!")
time.sleep(3)

print()
print()
print("Let's get to know each other a bit better first. I was born a few weeks ago, how old are you?")
time.sleep(2)

age = int(input("Please type your age here: "))
print()
print()

if age > 25:    
    print("Holy Moley, we got an oldie in the house!")    
    time.sleep(2)    
    print()    
    print("You have been alive for...")    
    
    for i in range(age):        
        if i % 2 != 0 and i < 15:            
            print(i)            
            i += 1            
            time.sleep(1)    
    print("Wait, I am not even gonna bother counting that much ;)")
else:    
    print("Oh must be nice, being that young..")

print()    
time.sleep(4)                      
print(f"Alright, enough chit chat Buddy. Let's get started, {name}.")
time.sleep(2)
print("The rules will be as follows.")
print()
time.sleep(3)
print("I am going to make 3 jokes and if I make you laugh at least 2 out of 3 times, I win and you owe me an Aperol Spritz.. mmhhh..")
print()
time.sleep(3)
print("Otherwise, I will buy you pizza! I hope you are ready!\n\n") 

wins = 0

loss = 0

time.sleep(4)

print("-" * 70)
print("-" * 30 + " Joke 1! " + "-" * 30)
print("-" * 70)
print()
print()
#### Let's get started with some jokes

time.sleep(2)
print("What do you call a cow in an earthquake??")
answer1 = input("Please type your answer here: ")

if answer1.lower() == 'a milkshake':    
    print("haha, that's correct. I guess you can be funny too!")
else:    
    print("No silly")    
    print("The answer is a milkshake! :)")
    
time.sleep(2)
record1 = input("Did you laugh??? Please answer yes or no: ")
time.sleep(1)

if record1.lower() == 'yes':    
    wins += 1
else:    
    loss += 1
    print("Cool, let's keep going!\n\n")

print()

time.sleep(3)
print("-" * 70)
print("-" * 30 + " Joke 2! " + "-" * 30)
print("-" * 70)
print()
print()

time.sleep(2)
print("Yesterday I saw a guy spill all his Scrabble letters on the road.")

time.sleep(2)
print("I asked him, \"What\'s the word on the street?\".")

record2 = input("Did you laugh??? Please answer yes or no: ")
time.sleep(1)
if record2.lower() == 'yes':    
    wins += 1
else:    
    loss += 1

print("Cool, let's keep going!\n\n")
time.sleep(4)

print("-" * 70)
print("-" * 30 + " Joke 3! " + "-" * 30)
print("-" * 70)
print()
print()
time.sleep(2)

print("What do you call an illegally parked frog?")
answer3 = input("Please type your answer here: ")

if answer3.lower() == 'toad':    
    print("haha, that's correct. I guess you can be funny too!")
else:    
    print("No silly")    
    print("Toad! :)")

record3 = input("Did you laugh??? Please answer yes or no: ")
time.sleep(2)

if record3.lower() == 'yes':    
    wins += 1
else:    
    loss += 1 
time.sleep(2)
print("Okay, let's tally things up!")
time.sleep(2)
print("-" * 70)

print("I won {} times, and you won {} times.\n".format(wins, loss))
if wins > loss:    
    print("Wohoooooo!!! I won, and now you have to buy me a BIG delicious Aperol Spritz ;)") 
    print()
    time.sleep(3)    
    print("This was a lot of fun, I hope you come visit me again soon. Take care!")
else:    
    print("Dang it, you're a tough crowd. Ohh well, I will definitely get you next time.") 
    print()
    time.sleep(3)    
    print(f"This was a lot of fun {name}, I hope you wanna stop by my joke factory again soon. Takecare!")

