#
# Written By Kicki Lindstrand
# Date 2022
# Version 1.0
# Mail: kicki.lindstrand@gmail.com
#

import os
from sys import breakpointhook

#list of cars
pet1 = ['Lucy', 'Cat', 'Female', '3 years', 'Gray']
pet2 = ['Milo', 'Cat', 'Male', '5 years', 'White']
pet3 = ['Cosmo', 'Cat', 'Male', '2 years', 'Black']
pet4 = ['Diezel', 'Dog', 'Male' '3 years', 'Black and white']
pet5 = ['Marcy', 'Dog', 'Female' '1 year', 'Brown']
pet6 = ['Carrie', 'Dog', 'Female' '8 years', 'Black']
pet7 = ['Python', 'Snake', 'Male' '1 years', '4 feet']

petList = ["Lucy", "Milo", "Cosmo", "Diezel", "Marcy", "Carrie", "Python"]

#list of staff
ans11 = ("Karl Nilsson, tel 070-12345678, anställd 2020")
ans12 = ("Eva Johnsson, tel 070-12345678, anställd 2021")
ans13 = ("Lena Olsson, tel 070-12345678, anställd 2015")
ans14 = ("Frida Andersson, tel 070-12345678, anställd 2013")
ans15 = ("Gustav Pettersson, tel 070-12345678, anställd 2022")
staff = [ans11, ans12, ans13, ans14, ans15]


#function for calculating adoptioncost
animal = 0 
cost = 0


def AdoptCost(animal):
    Xcost = 250 + cost
    print("The adoptioncost for " + animal + " is " + str(Xcost) + " SEK.")  
    input("Press enter to return")  
        

#function for calculating price of repair
def RepairCost(hour, material):
    hCost = int(hour)*535
    repair = int(hCost) + int(material)
    print("Kostnaden för reparationen är " + str(repair) + "kr.")
    
#function for adding staff to list
def addStaff():
    newStaff = str(sname + ", tel " + tel + ", anställd " + year + " ")
    staff.append(newStaff)
    print(sname + " är nu tillagd i personallistan. ")

#Variable holding users choise
x = 0 

#backup error-catch
try: 
    #Loop back to menu
    while True:
        #Clear the screen
        os.system('cls')

        #Menu-options for the user
        print("Welcome to Pet Adoption ")
        print("How can we help you?: ")
        print("***************************")
        print("1.Facts about pets")
        print("2.Pets to adopt")
        print("3.Expences")
        print("4.More information\n")
        print("5.Avsluta programmet")

        #Collecting users choise and converting to integer
        x = int(input("Ange siffra för att välja: "))

        #Conditions to get the function of choise 
        if x == 1:
            #Clear screen and confirm users choise
            os.system('cls')
            print("*******************************************")
            print("Du vill registrera en köpare.")
            print("*******************************************")
            input("Tryck enter för att fortsätta")
            #Ask user to enter information about customer and save to variables
            os.system('cls')
            print ("Ange köparens fullständiga namn:")
            name = input()
            print ("Ange bilmärke och modell:")
            model = input()
            print ("Ange datum för köp:")
            date = input()
            print ("Ange eventuella övriga anteckningar:")
            other = input()
            #Save information in variable owner1: 
            owner1 = name + " köpte " + model + " den " + date + ". Övrig info: " + other + "."
            #Confirm saved information
            print ("Du har angett följande uppgifter: " + owner1)
            #Return to main menu
            input("Tryck enter för att återgå till huvudmenyn")
        
        elif x == 2:
            #Clear screen and confirm users choise
            os.system('cls')
            print("*******************************************")
            print("Du vill se innevarande bilar")
            print("*******************************************")
            input("Tryck enter för att fortsätta")
            print("*******************************************")
            print("De bilar som finns inne är:\n ")
            #Show list billista
            for i in billista:
                print(i)
            print("*******************************************")
            input("För att söka efter bilmärke - tryck enter")
            print("*******************************************")
            #Loop back to submenu
            while True:
                #Clear screen and offer options for user
                os.system('cls')
                print("*För att söka efter bil, ange aktuellt bilmärke (små bokstäver). ")
                print("*För att återgå till huvudmenyn, skriv AVS ")
                bil = input("Ange ditt val: ")
                #If car exist, print the value from the variable
                if bil == 'ford':
                    print (bil1)
                    #Return to submenu
                    input("Tryck enter för att återgå ")
                elif bil == 'nissan':
                    print (bil2)
                    #Return to submenu
                    input("Tryck enter för att återgå ")
                elif bil == 'scoda':
                    print (bil3)
                    #Return to submenu
                    input("Tryck enter för att återgå ")
                elif bil == 'volvo':
                    print (bil4)
                    #Return to submenu
                    input("Tryck enter för att återgå ")
                #To return to main menu
                elif bil == 'AVS':
                    break
                #Message if no car is availible
                else:
                    print ("Tyvärr har vi ingen sådan bil i lager.")
                    #Return to submenu
                    input("Tryck enter för att återgå ")
            #Return to main menu
            input ("Tryck enter för att återgå till huvudmenyn. ")
        
        elif x == 3:
            #Clear screen and confirm users choise
            os.system('cls')
            print("*******************************************")
            print("Du vill hantera service, reparation och garantiärenden")
            print("*******************************************")
            input("Tryck enter för att fortsätta")
            #Loop back to submenu
            while True:
                #Offer options for user
                print("*******************************************")
                print("För att räkna ut pris för adoption   - skriv ADOPT")
                print("För att räkna ut pris för reparation - skriv REP")
                print("För att återgå till huvudmeny        - skriv AVS")
                print("*******************************************")
                val=input()
                #call function ServiceCost
                if val == "ADOPT":
                    animal=input("What pet would you like info about? ")
                    if animal == "cat":
                           cost = 1500
                    elif animal == "dog":
                            cost = 1800
                    elif animal == "rabbit":
                            cost = 1000
                    elif animal == "snake":
                            cost = 1200
                    elif animal == "Exit":
                            break
                    else :
                            print("There is no info of this animal")
                    AdoptCost(animal)
                    #Go back to submenu
                    
                    input("Tryck enter för att återgå")
                #call function RepairCost and add values
                elif val == "REP":
                    x = input ("Ange antal timmar för arbetet ")
                    y = input ("Ange materialkostnad ")
                    RepairCost(x, y)
                    #Go back to submenu
                    input("Tryck enter för att återgå")
                #Stop loop
                elif val == "AVS":
                    os.system('cls')
                    break
                #Message if wrong option is entered, go back to submenu
                else:
                    input("Du gjorde ett felaktigt val. Tryck enter och försök igen.")
            #Return to main menu
            input("Tryck enter för att återgå till huvudmenyn")
        
        elif x == 4:
            #Clear screen and confirm users choise
            os.system('cls')
            print("*******************************************")
            print("Du vill hantera personal")
            print("*******************************************")
            input("Tryck enter för att fortsätta")
            #Loop back to submenu
            while True:
                os.system('cls')
                #Offer options for user
                print("*******************************************")
                print("För att lägga till anställd      - tryck 1")
                print("För att se personallista         - tryck 2")
                print("För att återgå till huvudmeny    - tryck 3")
                print("*******************************************")
                s = int(input("Ange ditt val: "))
                #To add new employee
                if s == 1:
                    os.system('cls')
                    #Add values
                    print ("Ange fullständigt namn:")
                    sname = input()
                    print ("Ange telefonnummer")
                    tel = input()
                    print ("Ange anställd sedan (år):")
                    year = input()
                    #Call funcion addStaff to add staff member
                    addStaff()
                    #Return to submenu
                    input("Tryck enter för att återgå")
                #To se list of staff
                elif s == 2:
                    os.system('cls')
                    #print list of staff
                    for i in staff:
                        print(i)
                    #Return to submenu
                    input("Tryck enter för att återgå")
                #To exit program
                elif s == 3:
                    os.system('cls')
                    break
                #Message if no staff member is availible
                else:
                    input("Du gjorde ett felaktigt val. Tryck enter och försök igen.")
            #Return to main menu            
            input ("Tryck enter för att återgå till huvudmenyn. ")
        
        #To exit the program
        elif x == 5:
            #Clear screen and confirm users choise
            os.system('cls')
            print("Du har valt att avsluta programmet")
            input("Tryck enter för att avsluta")
            break
        
        #If user press number outside of choise
        else:
            os.system('cls')
            print("Du har angett ett ogiltigt val.")
            #Return to main menu
            input ("Tryck på enter för att återgå till menyn")

    #Message when exit
    os.system('cls')
    print("*******************************************")
    print("Programmet har avslutats, välkommen åter!")
    print("*******************************************")

#Catch errors
except: 
    print("Nu blev det något fel")
    print("Starta om programmet.")
    input("Tryck enter för att avsluta.")