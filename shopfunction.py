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


def isValidEntryMotherboard(selectedMotherboardId, selectedCPUId ):
   if selectedCPUId in VALID_MOTHERBOARDS.keys():
        if selectedMotherboardId in VALID_MOTHERBOARDS.get(selectedCPUId):
            return True
   
   return False


def printValidMotherboards(selectedCPUId):
    for motherboard in MOTHERBOARD:
        if isValidEntryMotherboard(motherboard[0], selectedCPUId):
            print(f'{motherboard[0]}: {motherboard[1]}, ${motherboard[2]}')
            
    

def printAvailableSolutions(list):
    for item in list:
        print(f'{item[0]}: {item[1]}, ${item[2]}')

#printAvailableSolutions(PREBUILTS)

def isValidEntry(list, selectedId):
    for item in list:
        if item[0] == selectedId:
            return True
        
    return False

def isValidEntryGC(selectedId):
    return isValidEntry(GRAPHICS_CARD, selectedId) or selectedId.lower() == 'x'

def isValidEntrySSD(selectedId):
    return isValidEntry(SSD, selectedId) or selectedId.lower() == 'x'

def isValidEntryHDD(selectedHDDId, selectedSSDId):
    validHDD = isValidEntry(HDD, selectedHDDId)
    if selectedSSDId.lower == 'x':
        return validHDD
    else:
        return validHDD or selectedHDDId.lower() == 'x'


#print(isValidEntry(PREBUILTS, 'x'))

def getCommonPrice(list, selectedId):
    for item in list:
        if item[0] == selectedId:
            return item[2]
        
    return 0












def selectPrebuilt():
    print('\nGreat! Let\'s pick a pre-built PC!\n\nWhich prebuilt would you like to order?')
    printAvailableSolutions(PREBUILTS)
    
    id = ''
    while isValidEntry(PREBUILTS, id) == False:
        id = input('Choose the number that corresponds to the part you want:') 


    price = getCommonPrice(PREBUILTS, id)
    print('\nYour total price for this prebuilt is ${:.2f}'.format(price))
    return price

def selectCustom():
    price = 0

    print('\nGreat! Let\'s start building your PC!')
    print('\nFirst, let\'s pick a CPU.')
    printAvailableSolutions(CPU)
    
    cpuId = ''
    while isValidEntry(CPU, cpuId) == False:
        cpuId = input('Choose the number that corresponds to the part you want:') 
    
    price += getCommonPrice(CPU, cpuId)


    print('\nNext, let\'s pick a compatible motherboard.')
    printValidMotherboards(cpuId)
    
    motherboardId = ''
    while isValidEntryMotherboard(motherboardId, cpuId) == False:
        motherboardId = input('Choose the number that corresponds to the part you want:') 
    
    price += getCommonPrice(MOTHERBOARD, motherboardId)


    print('\nNext, let\'s pick your RAM.')
    printAvailableSolutions(RAM)
    
    ramId = ''
    while isValidEntry(RAM, ramId) == False:
        ramId = input('Choose the number that corresponds to the part you want:') 
    
    price += getCommonPrice(RAM, ramId)


    print('\nNext, let\'s pick your PSU.')
    printAvailableSolutions(PSU)
    
    psuId = ''
    while isValidEntry(PSU, psuId) == False:
        psuId = input('Choose the number that corresponds to the part you want:') 
    
    price += getCommonPrice(PSU, psuId)


    print('\nNext, let\'s pick your case.')
    printAvailableSolutions(CASE)
    
    caseId = ''
    while isValidEntry(CASE, caseId) == False:
        caseId = input('Choose the number that corresponds to the part you want:') 
    
    price += getCommonPrice(CASE, caseId)


    print('\nNext, let\'s pick an SSD (optional, but have at least one SSD or HDD).')
    printAvailableSolutions(SSD)
    
    ssdId = ''
    while isValidEntrySSD(ssdId) == False:
        ssdId = input('Choose the number that corresponds to the part you want (or X not to get an SSD):') 
    
    price += getCommonPrice(SSD, ssdId)


    print('\nNext, let\'s pick an HDD (optional, but have at least one SSD or HDD).')
    printAvailableSolutions(HDD)
    
    hddId = ''
    while isValidEntryHDD(hddId, ssdId) == False:
        hddId = input('Choose the number that corresponds to the part you want (or X not to get an HDD):') 
    
    price += getCommonPrice(HDD, hddId)


    print('\nFinally, let\'s pick your graphics card (or X to not get a graphics card).')
    printAvailableSolutions(GRAPHICS_CARD)
    
    gcId = ''
    while isValidEntryGC(gcId) == False:
        gcId = input('Choose the number that corresponds to the part you want:') 
    
    price += getCommonPrice(GRAPHICS_CARD, gcId)


    print('\nYou have selected all the required parts! Your total for this PC is $',price)


    


def pickItems():
    selection = ''
    prices = []
    while selection != '3':
        selection = input('\nWould you like to build a custom PC (1), Purchase a pre-built PC (2), or would you like to checkout (3)?')
        if selection == '2':
            prices.append(selectPrebuilt())

        elif selection == '1':
            prices.append(selectCustom())

    return prices


print('Welcome to my PC shop!')
pricelist = pickItems()
print(pricelist)





