# Gladiatorspelet

import random

spe_hal = 10

mot_hal = 10

print("\nVälkommen till Gladiatorspelet!")

Blod = input("Vill du ha blodiga beskrivningar?(ja eller nej?) ")

while spe_hal > 0 and mot_hal > 0: 

    Val = input("Vill du attackera med din järnhårda näve eller med din kvicka spark? ")

    MotVal = ["slag", "spark"]

    MotVall = (random.choice(MotVal))

    if Val == "spark":
        tärning = random.randrange(0, 10)
        if tärning <= 3:
            print("Du träffade")
            mot_hal = mot_hal - 4
            if Blod == "ja":
                print("Sparken får honom att spotta ut blod!")
        if tärning > 3:
            print("Du missade")
        


    if Val == "slag":
        tärning = random.randrange(0, 10)
        if tärning <= 7:
            print("Du träffade")
            mot_hal = mot_hal - 2
            if Blod == "ja":
                print("Slaget får honom att spotta ut blod!")
        if tärning > 7:
            print("Du missade")
    
    if MotVall == "spark":
        tärning = random.randrange(0, 10)
        if tärning <= 3:
            print("Motståndaren träffade med en spark")
            spe_hal = spe_hal - 4
            if Blod == "ja":
                print("Sparken får dig att spotta ut blod!")
        if tärning > 3:
            print("Motståndaren missade sin spark")

    if MotVall == "slag":
        tärning = random.randrange(0, 10)
        if tärning < 7:
            print("Motståndaren träffade med ett slag")
            spe_hal = spe_hal - 2
            if Blod == "ja":
                print("Slaget får dig att spotta ut blod!")
        if tärning >= 7:
            print("Motståndaren missade sitt slag")


    print("Motståndaren har ", mot_hal, " hälsopoäng.")
    print("Du har ", spe_hal, " hälsopoäng.")


