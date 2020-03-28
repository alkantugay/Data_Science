# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:40:01 2020

@author: alkan
"""
from Rent_a_Vehicle import carRent, bikeRent, Customer

bike = bikeRent(100)
car = carRent(10)
customer = Customer()

main_menu = True

while True:
    
    if main_menu:
        print("""
              ***** Vehicle Rental Shop *****
              A.Bike Menu
              B.Car Menu
              Q.Exit              
              """)
        
        main_menu = False
        choice = input("Enter choice: ")
        
        if choice == "A" or choice == "a":
            
            print("""
                  *****  BIKE MENU  *****
                  1. Display available bikes
                  2. Request a bike onhourly basis $5
                  3. Request a bike ondaily basis $84
                  4. Return a bike
                  5. Main Menu
                  6. Exit
                  """)
            choice = input("Enter choice: ")
            
            try:
                choice = int(choice)
            
            except ValueError:
                print("It is not integer")
                continue
            
            
            if choice == 1:
                bike.displayStock()
                choice = "A"
            
            elif choice == 2:
                customer.rentalTime_b = bike.rentHourly(customer.requestVehicle("bike"))
                customer.rentalBasis_b = 1
                main_menu = True
                print("---------------------------")
                
            elif choice == 3:
                customer.rentalTime_b = bike.rentDaily(customer.requestVehicle("bike"))
                customer.rentalBasis_b = 2
                main_menu = True
                print("---------------------------")
            
            elif choice == 4:
                customer.bill = bike.returnVehicle(customer.returnVehicle("bike"),"bike")
                customer.rentalBasis_b, customer.rentalTime_b, customer.bikes = 0,0,0
                main_menu = True
            
            elif choice == 5:
                main_menu = True
            
            elif choice == 6:
                break
            
            else:
                print("Invalid Input")
                main_menu = True
            
                        
        elif choice == "B" or choice == "b":
            
            print("""
                  *****  CAR MENU  *****
                  1. Display available bikes
                  2. Request a bike onhourly basis $10
                  3. Request a bike on daily basis $ 192
                  4. Return a bike
                  5. Main Menu
                  6. Exit
                  """)
            choice = input("Enter choice: ")
            
            try:
                choice = int(choice)
            
            except ValueError:
                print("It is not integer")
                continue
            
            
            if choice == 1:
                car.displayStock()
                choice = "A"
            
            elif choice == 2:
                customer.rentalTime_c = car.rentHourly(customer.requestVehicle("car"))
                customer.rentalBasis_c = 1
                main_menu = True
                print("---------------------------")
                
            elif choice == 3:
                customer.rentalTime_c = car.rentDaily(customer.requestVehicle("car"))
                customer.rentalBasis_c = 2
                main_menu = True
                print("---------------------------")
            
            elif choice == 4:
                customer.bill = car.returnVehicle(customer.returnVehicle("car"),"car")
                customer.rentalBasis_c, customer.rentalTime_c, customer.cars = 0,0,0
                main_menu = True
            
            elif choice == 5:
                main_menu = True
            
            elif choice == 6:
                break
            
            else:
                print("Invalid Input")               
                main_menu = True
        
        elif choice == "Q" or choice == "q":
            break
    
        else:
            print("Invalid input")
            main_menu = True
        
        print("Thanks for using the vehicle rental shop")