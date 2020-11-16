# Imports, Random Number Generator, Delay in Terminal, Commands
import random
import time

# Starting Health and Coins
health = 100;
coins = 50;

#Begin
print("Welcome new player!")
time.sleep(1)
name = input("What would you liked to be called, warrior? ")
print(f"Alright! {name} it is. We are being attacked by Spiders. Let's go!")
time.sleep(2)
print(f"Pick a weapon: \n")
time.sleep(1)
print("Old Bow (5-10dmg)\n")
time.sleep(1)
print("Lost Blade (5-10dmg)\n")
time.sleep(1)
print("Ancient Sword (5-10dmg)\n")
time.sleep(1)
weapon = input("To choose, type: bow/blade/sword ").lower()

if weapon == 'bow': 
	print("An Old Bow, great choice!")
	print(f"You deal {random.randint(5, 10)} damage and kill the spiders!")
elif weapon == 'blade':
	print("You picked the Lost Blade, nice one!")
	print(f"You deal {random.randint(5, 10)} damage and kill the spiders!")
elif weapon == 'sword':
	print("Ah, the Ancient Sword. Fantastic!")
	print(f"You deal {random.randint(5, 10)} damage and kill the spiders!")
else:
	print("Pick a weapon quickly! (bow/blade/sword)")
	
	

time.sleep(1)
print("Alright, let me explain. Our realm is being attacked by all kinds of monsters right now.")
time.sleep(2)
print("You are a Knight and we have no time to finish your training. We must fight!")
time.sleep(2)
print(f"You are to go on quests and fight these monsters. Your current health is: {health}. If you lose too much health... you die.")
time.sleep(2)
print(f"Get coins by fighting monsters or completing quests. You start with {coins} coins. Use them to buy better gear and get stronger")
time.sleep(2)
print(f"To check your current health or balance, just type: health or coins")
time.sleep(2)
print(f"During the game you get to make choices. The choices you can make are written in (). Good luck!")

