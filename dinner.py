#Developed by: Dallas Foster
#Date: January 27th, 2023
#Desc: Restaurant order program
#Inputs: Number of invitees, dietary restrictions, food ordered
#Outputs: Total cost before tax, total cost after tax, total cost after tip

#This is to determine how many invitees there are
numInvitees = int(input("Please enter the number of invitees:"))

#This keeps a count on all of the meals that were ordered
cntPizza = 0
cntPasta = 0
cntFalafel = 0
cntSteak = 0
cntBeverage = 0

#Determine the orders for each invitee
for invitee in range(numInvitees):
    print("Please enter the order details for invitee Number {0}/{1}".format(str(invitee + 1), str(numInvitees)))

    #This is for a keto selection
    keto = input("Do you want a keto friendly meal?")
    #This is for a vegan selection
    vegan = input("Do you want a vegan meal?")
    #This is for a gluten-free selection
    glutenFree = input("Do you want a Gluten-free meal?")

    #This determines the meal the specified invitee recieves based on inputs given
    if keto == "y" and vegan == "y" and glutenFree != "y" :
        cntPizza += 1 
    else :
        if keto != "y" and vegan == "y" and glutenFree != "y" :
            cntPasta += 1
        else :
            if keto == "y" and vegan == "y" and glutenFree == "y" :
                cntFalafel += 1
            else :
                if keto == "y" and vegan != "y" and glutenFree == "y" :
                    cntSteak += 1 
                else :
                    cntBeverage += 1


#This determines how much the user would like to tip
tipPercent = int(input("How much do you want to tip your server (% percent)?"))

#Equations to calculate the total costs of the meal
costPizza = 44.50 * cntPizza
costPasta = 48.99 * cntPasta
costFalafel = 52.99 * cntFalafel
costSteak = 49.60 * cntSteak
costBeverage = 5.99 * cntBeverage
totExclTax = costPizza + costPasta + costFalafel + costSteak + costBeverage
totInclTax = totExclTax * 1.13
totInclTaxTip = totInclTax * (100 + tipPercent) / 100

#These are the printed outputs based on the users order
print("You have {0} invitees with the following orders: ".format(str(numInvitees)))
print("{0} invitees ordered Pizza. The cost is: ${1:.2f}".format(str(cntPizza), round(costPizza, 2)))
print("{0} invitees ordered Pasta. The cost is: ${1:.2f}".format(str(cntPasta), round(costPasta, 2)))
print("{0} invitees ordered Falafel. The cost is: ${1:.2f}".format(str(cntFalafel), round(costFalafel, 2)))
print("{0} invitees ordered Steak. The cost is: ${1:.2f}".format(str(cntSteak), round(costSteak, 2)))
print("{0} invitees ordered only Beverage. The cost is: ${1:.2f}".format(str(cntBeverage), round(costBeverage, 2)))

#These are the printed outputs for the total costs of the order
print("The total cost before tax is ${0:.2f}".format(round(totExclTax, 2)))
print("The total cost after tax is ${0:.2f}".format(round(totInclTax, 2)))
print("The total cost after {0}% tip is ${1:.2f}".format(str(tipPercent), round(totInclTaxTip, 2)))