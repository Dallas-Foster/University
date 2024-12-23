#Developed by: Dallas Foster
#Date: February 18th, 2023
#Desc: PC builder based on inputs
#Inputs: Pre-built or Self-Built Options, PC Component Selection
#Outputs: Customized PC receipt, Total Costs

#2D Lists of components for custom builds -->  Id, Name, Price
SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
 
#2D List of options for prebuilt computers -->  Id, Name, Price
PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99],
             ['2', 'SkyTech Prism II Gaming PC', 2839.99], 
             ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]
 
#Dictionary of options for valid CPU/Motherboard combinations. CPU Id with a list of compatible MBs
VALID_MOTHERBOARDS = {'1': ['2'], '2': ['1']}


#This function will make sure the CPU matches the motherboard. It is a special case that has to check MB compatibility
def isValidEntryMotherboard(selectedMotherboardId, selectedCPUId ):
   if selectedCPUId in VALID_MOTHERBOARDS.keys():
        if selectedMotherboardId in VALID_MOTHERBOARDS.get(selectedCPUId):
            return True
   
   return False


#This function will print out all of the selections in the MB list. This is a special case because it has to check CPU compatibility
def printValidMotherboards(selectedCPUId):
    for motherboard in MOTHERBOARD:
        #Is this component's Id in the valid dictionary using Key
        if isValidEntryMotherboard(motherboard[0], selectedCPUId):
             #Is ths selected CPU in the value list for the compatible MBs
            print(f'{motherboard[0]}: {motherboard[1]}, ${motherboard[2]}')


#This function will print out all of the selections in the given list
def printAvailableSolutions(list):
    for item in list:
        print(f'{item[0]}: {item[1]}, ${item[2]}')


#printAvailableSolutions(PREBUILTS)
def isValidEntry(list, selectedId):
    for item in list:
        if item[0] == selectedId:
            return True
        
    return False


#This function will make sure the GC selection is in the list. It is a special case because the user can select 'x' to not choose a GC
def isValidEntryGC(selectedId):
    return isValidEntry(GRAPHICS_CARD, selectedId) or selectedId.lower() == 'x'


#This function will make sure the SSD selection is in the list. It is a special case because the user can select 'x' to not choose an SSD
def isValidEntrySSD(selectedId):
    return isValidEntry(SSD, selectedId) or selectedId.lower() == 'x'


#This function will make sure the HDD selection is in the list. It is a special case because the user can select 'x' to not choose an HDD as long as they had an SSD
def isValidEntryHDD(selectedHDDId, selectedSSDId):
    validHDD = isValidEntry(HDD, selectedHDDId)
    if selectedSSDId.lower != 'x':
        return validHDD
    else:
        return validHDD or selectedHDDId.lower() == 'x'


#This give the price of the selected component from the given list
def getCommonPrice(list, selectedId):
    for item in list:
        if item[0] == selectedId:
            return item[2]
        
    #This returns a price of 0. This handles the case in which the user inputs a valid "X" 
    return 0


#this walks the user through selecting a prebuilt machine
def selectPrebuilt():
    print('\nGreat! Let\'s pick a pre-built PC!\n\nWhich prebuilt would you like to order?')
    #print out the options
    printAvailableSolutions(PREBUILTS)
    
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    id = ''
    while isValidEntry(PREBUILTS, id) == False:
        id = input('Choose the number that corresponds to the part you want: ') 

    #get the price, print it out, and return the value
    price = getCommonPrice(PREBUILTS, id)
    print('\nYour total price for this prebuilt is ${:.2f}'.format(price))
    return price


#this walks the user through selecting a custom machine
def selectCustom():
    #this holds the total price as we build the PC
    price = 0

    print('\nGreat! Let\'s start building your PC!')
    print('\nFirst, let\'s pick a CPU.')
    #print out the options
    printAvailableSolutions(CPU)
    
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    cpuId = ''
    while isValidEntry(CPU, cpuId) == False:
        cpuId = input('Choose the number that corresponds to the part you want: ') 
    
    #get the component price and add it to the PC price
    price += getCommonPrice(CPU, cpuId)

    print('\nNext, let\'s pick a compatible motherboard.')
    #print out the options
    printValidMotherboards(cpuId)
    
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    motherboardId = ''
    while isValidEntryMotherboard(motherboardId, cpuId) == False:
        motherboardId = input('Choose the number that corresponds to the part you want: ') 

    #get the component price and add it to the PC price
    price += getCommonPrice(MOTHERBOARD, motherboardId)

    print('\nNext, let\'s pick your RAM.')
    #print out the options
    printAvailableSolutions(RAM)
    
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    ramId = ''
    while isValidEntry(RAM, ramId) == False:
        ramId = input('Choose the number that corresponds to the part you want: ') 
    
    #get the component price and add it to the PC price
    price += getCommonPrice(RAM, ramId)

    print('\nNext, let\'s pick your PSU.')
    #print out the options
    printAvailableSolutions(PSU)
    
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    psuId = ''
    while isValidEntry(PSU, psuId) == False:
        psuId = input('Choose the number that corresponds to the part you want: ') 
    
    #get the component price and add it to the PC price
    price += getCommonPrice(PSU, psuId)

    print('\nNext, let\'s pick your case.')
    #print out the options
    printAvailableSolutions(CASE)
    
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    caseId = ''
    while isValidEntry(CASE, caseId) == False:
        caseId = input('Choose the number that corresponds to the part you want: ') 
    
    #get the component price and add it to the PC price
    price += getCommonPrice(CASE, caseId)

    print('\nNext, let\'s pick an SSD (optional, but have at least one SSD or HDD).')
    #print out the options
    printAvailableSolutions(SSD)
    
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    ssdId = ''
    while isValidEntrySSD(ssdId) == False:
        ssdId = input('Choose the number that corresponds to the part you want (or X not to get an SSD): ') 
    
    #get the component price and add it to the PC price
    price += getCommonPrice(SSD, ssdId)

    print('\nNext, let\'s pick an HDD (optional, but have at least one SSD or HDD).')
    #print out the options
    printAvailableSolutions(HDD)
    
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    hddId = ''
    while isValidEntryHDD(hddId, ssdId) == False:
        hddId = input('Choose the number that corresponds to the part you want (or X not to get an HDD): ') 
    
    #get the component price and add it to the PC price
    price += getCommonPrice(HDD, hddId)

    print('\nFinally, let\'s pick your graphics card (or X to not get a graphics card).')
    #print out the options
    printAvailableSolutions(GRAPHICS_CARD)
    
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    gcId = ''
    while isValidEntryGC(gcId) == False:
        gcId = input('Choose the number that corresponds to the part you want: ') 
    
    #get the component price and add it to the PC price
    price += getCommonPrice(GRAPHICS_CARD, gcId)

    print('\nYou have selected all the required parts! Your total for this PC is ${:.2f}'.format(price))

    #This returns the combined price of all the selected components 
    return price


#This is the main function called by the project. It loops through allowing the user to select any number of prebuilt or custom PCs.  It returns a list of prices
def pickItems():
    prices = []
    #loop until a valid selection is made. Seed the selection with an invalid value so it enters the loop
    selection = ''
    while selection != '3':
        selection = input('\nWould you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ')
        if selection == '1':
            #Build a custom PC and add the price to the list
            prices.append(selectCustom())
        elif selection == '2':
            #Pick a prebuilt PC and add the price to the list
            prices.append(selectPrebuilt())

    #This returns the list of prices of both custom PC's and Pre-built PCs
    print(prices)
    return





#This is the program.  It calls picklistItems to allow the user to select PCs.  It gets back the list of prices and prints them
print('Welcome to my PC shop!')
pricelist = pickItems()
print(pricelist)
 