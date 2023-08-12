#Variables that will be changed in the code 
breakfast_amount = 0
dinner_amount = 0
discount = 0
discount_counter = 0
end_price = 0
payment_accept = 0
price = 0
service_price =0

#function for the order module
def order():
    global price
    global discount_counter
    global breakfast_amount
    global dinner_amount
    global service_price
    global payment_accept
    #This counter is for going back to the main menu
    order_counter = 0
    if payment_accept == 1:
        reorder = input("Would you like to order for a new session? /n Y - Yes /n N - No")
        if reorder == "Y":
            print ("Redirecting to Main Menu")
            payment_accept = 0
            breakfast_amount = 0
            dinner_amount = 0
            discount = 0
            discount_counter = 0
            end_price = 0
            payment_accept = 0
            price = 0
            service_price =0
        elif reorder == "N":
            print ("Redirecting to Main Menu")
        else:
            print ("Invalid entry , redirecting to main menu")
    else:
        while order_counter == 0:
            order_option = input("Choose what do you want to order \n F - Foods \n S - Services\n M - Return to Main Menu \n")
            if (order_option == "F"):
                #This counter is for entering the loop
                food_counter = 0
                while food_counter == 0:
                    #This counter is to stop the loop from happening again,resulting in returning to the main menu possible for some options
                    food_counter = 1
                    order_counter = 1
                    food_options = input ("Choose which menu would you like to order \n  B - Breakfast - 20 RM(Consists of the combination of either Cow Bacon,Rice,Noodle,Omelet Egg,and Chicken Nugget) \n  D - Dinner - 30 RM (Consist of combinations of either rice , chicken fillet , lamb chops , salad , and pudding)\n")
                    if (food_options == "B"):
                        breakfast_amount_add = int(input("How many servings would you want to order?\n"))
                        breakfast_amount = breakfast_amount + breakfast_amount_add
                        price += breakfast_amount_add*20
                        discount_counter += breakfast_amount_add*1
                        print ("You have ordered " , breakfast_amount_add , " Breakfast servings")
                        food_reorder = input ("Would you like to order another food? \n Y - Yes \n N - No\n")
                        if food_reorder == "Y":
                            print ("You will be redirected to the food order menu")
                            food_counter = 0
                            order_counter = 0
                        elif food_reorder == "N":
                            print ("You will be redirected to the main menu")
                        else:
                            print ("Invalid Entry,redirecting to main menu")                        
                    elif (food_options == "D"):
                        dinner_amount_add = int(input("How many servings would you want to order?\n"))
                        dinner_amount = dinner_amount + dinner_amount_add
                        price += dinner_amount_add *30
                        discount_counter += dinner_amount_add*1
                        print ("You have ordered ", dinner_amount_add ," Dinner servings  \n ")
                        food_reorder = input ("Would you like to order another food? \n Y - Yes \n N - No\n")
                        if food_reorder == "Y":
                            print ("You will be redirected to the food order menu")
                            food_counter = 0
                            order_counter = 0
                        elif food_reorder == "N":
                            print ("You will be redirected to the main menu")
                        else:
                            print ("Invalid Entry,redirecting to main menu")
                    else :
                        print ("Invalid Input,returning to main menu\n")                    
            elif (order_option == "S"):
                #This counter is for entering the loop
                service_counter = 0
                while service_counter == 0:
                    #This counter is to stop the loop from happening again,resulting in returning to the main menu possible for some options
                    service_counter = 1
                    order_counter = 1
                    service_options = input ("Choose which services would you like to order \n 1 - Baby Chair - 15 RM \n 2 - Baby Apron - 10 RM \n 3 - Tissues - 2 RM \n ")                
                    if (service_options == "1"):
                        price += 15
                        service_price += 15
                        service_reorder = input("You have chosen the baby chair services \n Would you like to order any another services? \n Y - Yes \n N - No \n")
                        if service_reorder == "Y" :
                            print ("You will be redirected to the services order menu")
                            service_counter = 0
                            order_counter = 0
                        elif service_reorder == "N" :
                            print ("You will be redirected to the main menu")
                        else:
                            print ("Invalid Entry , redirecting to main menu")                        
                    elif (service_options == "2"):
                        price += 10
                        service_price += 10
                        service_reorder = input("You have chosen the baby apron services \n Would you like to order any another services? \n Y - Yes \n N - No \n")
                        if service_reorder == "Y" :
                            print ("You will be redirected to the services order menu")
                            service_counter = 0
                            order_counter = 0
                        elif service_reorder == "N" :
                            print ("You will be redirected to the main menu")
                        else:
                            print ("Invalid Entry , redirecting to main menu")                        
                    elif (service_options == "3"):
                        service_reorder = input("You have chosen the tissues services \n Would you like to order any another services? \n Y - Yes \n N - No \n")
                        price += 2
                        service_price += 2
                        if service_reorder == "Y" :
                            print ("You will be redirected to the services order menu")
                            service_counter = 0
                            order_counter = 0
                        elif service_reorder == "N" :
                            print ("You will be redirected to the main menu")
                        else:
                            print ("Invalid Entry , redirecting to main menu")                        
                    else:
                        print ("Invalid Input,returning to main menu\n")                    
            elif (order_option =="M"):
                print ("You will be returned to the main menu\n")
                order_counter = 1
            else:
                print ("Invalid Entry , returning to main menu")
                order_counter = 1
                    
#function for calculate discount module
def calculate_discount():
    global end_price
    global discount
    if (discount_counter > 9 and discount_counter < 16):
        end_price = 0.95 * price
    elif (discount_counter >15 and discount_counter <51):
        end_price = 0.90 * price
    elif (discount_counter > 50 and discount_counter < 101):
        end_price = 0.85 * price
    elif (discount_counter > 100):
        end_price = 0.80 * price
    discount = price - end_price 
        
#function for the payment module
def payment():
    global payment_accept
    payment_counter = 0
    while payment_counter == 0:
        payment_options = input("Choose an option below \n D - Discount Lists \n P - Make Payment \n M - Main Menu \n")
        if (payment_options == "D"):
            print (" The list of discounts are \n 5% if you ordered 10-15 sets of foods \n 10% if you ordered 16-50 sets of food \n 15% if you ordered 51-100 sets of foods \n 20% if you ordered more than 100 sets of foods \n")
            price_check = input("Would you like to see your discounted amount now? \n Y - Yes \n N - No\n")
            if price_check == "Y":
                print ( "The amount of money you will have to pay is " , end_price , "RM")
            elif price_check == "N" :
                print ( "You can check the amount of money you need to pay in the summary or in the Make Payment options" )
            else:
                print ("Invalid entry")
            print ("Returning to the payment options \n")
        elif (payment_options == "P"):
            print ("The amount of money you wil be paying is " , end_price , "RM")
            pay = int(input("Please put in the amount you want to pay (We do not accept cents or coins)\n"))
            if (pay > end_price):
                change = pay - end_price
                print ("Your change is " , change , "RM. Thank you for doing business with us")
                payment_counter = 1
                payment_accept = 1
            elif (pay == end_price):
                print ("Thank you for doing business with us")
                payment_counter = 1
                payment_accept = 1
            elif (pay < end_price):
                print ("Unsufficient amount , returning to the payment options")
        elif (payment_options == "M"):
            print ("You will be redirected to the main menu now")
            payment_counter = 1
        else:
            print ("Invalid Entry,returning to main menu")
            payment_counter = 1

#function for report
def report():
    report_counter = 0
    while report_counter == 0 :
        report_options = input("Choose an option below \n I - Display Invoice \n S - Display Summary of orders and Payments \n M - Return to main menu \n")
        if (report_options == "I"):
            print ("Here is your invoice\nBreakfast               " ,breakfast_amount,"     ", breakfast_amount*20, "RM. \nDinner                  " , dinner_amount ,"     ",dinner_amount*30,"RM. \nServices                         ",service_price,"RM \nPrice                            ", price , "RM\nDiscount                         ", discount,"RM\nDiscounted Price                 ",end_price,"RM.  ")
            print ("Returning to report menu")
        elif (report_options == "S"):
            print ("Here's the summary of your order\n Breakfast ordered ",breakfast_amount,"\n Dinner ordered ",dinner_amount,"\n Services Total Amount" , service_price ,"\n Total Price After Discount",end_price)
            if (payment_accept == 1 ):
                print ("You have paid your order\n")
            else :
                print ("You have not paid your order\n")
            print ("Returning to main menu\n")
            report_counter = 1
        elif (report_options == "M"):
            print ("Returning to main menu\n")
            report_counter = 1

print ("Greetings and welcome to our catering service!")
while True:
    option=input("Please enter an option \n O - Ordering \n P - Payment \n R - Report \n E - Exit \n")
    if (option == "O" ):
        order()
        calculate_discount()
    elif (option == "P" ):
        payment()
    elif (option == "R" ):
        report()
    elif (option == "E" ):
        exit()
    else:
        print ("Invalid Entry, Make sure you typed the letter in capital")


      

        
