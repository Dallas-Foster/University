from Assignments.Flight import *
from Assignments.Airport import *

class Aviation:
    def __init__(self):
        self._allAirports = {}
        self._allFlights = {}
        self._allCountries = {}
    
        
    def getAllAirports(self):
        """
        Getter that returns all airport objects
        Args: None
        
        Return (dict) key: airport code, value: Airport
            e.g., {YYZ: Airport, YHM: Airport}
        """
        return self._allAirports
    
    
    def getAllFlights(self):
        """
        Getter that returns all flight objects
        Args: None
        
        Return (dict) {flight} key: flightNo, value: Flight
            e.g., { XYZ123: Flight, ABC789: Flight}
        """        
        return self._allFlights
    
    
    def getAllCountries(self):
        """
        Getter that returns all country objects
        Args: None
        
        Return (dict) {country} key: country, value: continent
            e.g., {Canada: North America, United States: North America}
        """        
        return self._allCountries
    
    
    def setAllAirports(self, airports):
       """
       Retrieves a list of all airports from a data source and sets it as the global variable `all_airports`.

       Args: dict {Airports}

       Returns: Nothing
       """
       if isinstance(airports, dict) == False:
           raise TypeError("Airports must be a dictionary")
       
       for dictKey in airports: 
            if isinstance(dictKey, str) == False:
               raise TypeError("The key must be a string")
            
            dictValue = airports[dictKey]
            if isinstance(dictValue, Airport) == False:
                raise TypeError("The value must be an Airport")
           
       self._allAirports = airports
    
    
    def setAllFlights(self, flights):
        """
        A function that retrieves information about all flights from a database and creates a list of Flight objects.

        Args: dict {Flights}

        Returns: Nothing
        """
        
        #Checks to see if flights is a dictionary, if not, raise error
        if isinstance(flights, dict) == False:
           raise TypeError("Flights must be a dictionary")
       
        for dictKey in flights: 
            #Checks to see if the key is a string, if not, raise error
            if isinstance(dictKey, str) == False:
               raise TypeError("The key must be a string")
            
            dictValue = flights[dictKey]
            #Checks to see if the value is a list, if not, raise error
            if isinstance(dictValue, list) == False:
                raise TypeError("The value must be a list")
            
            #If the list has items, make sure they are all Flights, if not, raise an error
            for listValue in dictValue:
                if isinstance(listValue, Flight) == False:
                    raise TypeError("The value list be a Flight")

        self._allFlights = flights
    
    
    def setAllCountries(self, countries):
        """
        A function that retrieves information about all countries from a database and creates a list of Country objects.

        Args: dict {Countries}

        Returns: Nothing
        """
        if isinstance(countries, dict) == False:
           raise TypeError("Countries must be a dictionary")
       
        for dictKey in countries: 
            if isinstance(dictKey, str) == False:
               raise TypeError("The key must be a string")
            
            dictValue = countries[dictKey]
            if isinstance(dictValue, str) == False:
                raise TypeError("The value must be a string")
            
        self._allCountries = countries
    
    
    def loadAirportData(self, airportFile):
        """
        Helper function that loads the airport data from the airport file

        Args:
            airportFile: file containing the data of the airports being used

        Raises:
            ValueError: The file had the wrong number of columns in the lineContents

        Returns:
            Boolean: Returns False if an exception is hit, the file could not be opened properly
        """
        #Must put try here to handle multiple exceptions later on
        try:
            #This opens the fle for reading
            f = open(airportFile, "r", encoding="utf8")

            for line in f.readlines():
                #Strip leading/trailing whitespace, tabs, and newline characters from the line
                line = line.strip(" \t\n")
                #Split the line on commas
                lineContents = line.split(",")
                
                #Remove leading/trailing whitespace, tabs, and newline characters from each item in the line
                cleanContents = [lineItem.strip(" \t\n") for lineItem in lineContents]
                
                #Sets the varibles of the airport to the position in cleanContents
                airportCode = cleanContents[0]
                airportCountry = cleanContents[1]
                airportCity = cleanContents[2]

                #Get the contitent from the country dict
                airportContinent = self._allCountries[airportCountry]

                #Create an Aiport object
                airport = Airport(airportCode, airportCity, airportCountry, airportContinent)

                #Add the Airport to our dict
                self._allAirports[airportCode] = airport

            #close the file before leaving the function        
            f.close()

            return True
        
        except:
            return False
        
    
    def loadFlightData(self, flightFile):
        """
        Helper function that loads the data from the flightfile

        Args:
            flightFile: File that contains the data of the flights

        Returns:
            Boolean: returns True if the file could be opened properly
        """
        try:
            #This opens the fle for reading
            f = open(flightFile, "r", encoding="utf8")
            
            #This iterates over the lines, stripping tabs and newlines, and also splitting commas           
            for line in f.readlines():
                #Strip leading/trailing whitespace, tabs, and newline characters from the line
                line = line.strip(" \t\n")
                #Split the line on commas
                lineContents = line.split(",")
                #Remove leading/trailing whitespace, tabs, and newline characters from each item in the line
                cleanContents = [lineItem.strip(" \t\n") for lineItem in lineContents]
                
                #Sets the varibles of the flight to the position in cleanContents
                flightCode = cleanContents[0]
                originCode = cleanContents[1]
                destCode = cleanContents[2]

                #Get airports from codes in the file
                originAirport = self._allAirports[originCode]
                destAirport = self._allAirports[destCode]
                
                #Try to create a new flight
                flight = Flight(flightCode, originAirport, destAirport)
                
                #Check if the origin code is in our flights dictionary. If not, add it
                if originCode not in self._allFlights:
                    self._allFlights[originCode] = []
                    
                #Append the flight to the dictionary value
                self._allFlights[originCode].append(flight)

            #close the file before leaving the function     
            f.close()

            return True
        
        except:
            return False
    
        
    def loadCountriesData(self, countriesFile):
        """
        Loads data for only the countries file

        Args:
            countriesFile File: A file containing the Countries

        Returns:
            Boolean: returns true if the file could be opened properly
        """
        
        try:
            f = open(countriesFile, "r", encoding="utf8")
            for line in f:
                #Strip leading/trailing whitespace, tabs, and newline characters from the line
                line = line.strip(" \t\n")
                #Split the line on commas
                lineContents = line.split(",")
                #Remove leading/trailing whitespace, tabs, and newline characters from each item in the line
                cleanContents = [lineItem.strip(" \t\n") for lineItem in lineContents]
                
                #Add the country/continent to our dict.  No need to check if it exists first as this is a string/string dict.
                self._allCountries[cleanContents[0]] = cleanContents[1]
                    
            #close the file before leaving the function
            f.close()

            return True
        
        except:
            return False

        
    def loadData(self, airportFile, flightFile, countriesFile):
        """
        A function that loads data from three files into the application.
    
        Args:
        - airportFile: A string representing the name of the file containing airport data.
        - flightFile: A string representing the name of the file containing flight data.
        - countriesFile: A string representing the name of the file containing country data.
        
        Returns:
        None
        """
        
        #Loads the data from each file after being passed through the loadCountriesData helper function to screen for errors
        if self.loadCountriesData(countriesFile) == True:
            if self.loadAirportData(airportFile) == True:
                if self.loadFlightData(flightFile) == True:
                    return True
        return False
        

    def getAirportByCode(self, code):
        """
         A function that retrieves an Airport object from a list of Airport objects based on its code.
    
        Args:
        - code: A string representing the code of the airport to retrieve.
        
        Returns:
        An Airport object containing information about the airport with the specified code.
        
        """
        #Check if the code is in the dictionary of airports
        if code in self._allAirports:
            #The airport is found, return the corresponding Airport object
            return self._allAirports[code]
        
        #The airport is not found, return -1
        return -1
    
    
    def findAllCityFlights(self, city):
        """
        A function that finds all flights that depart from or arrive at a given city.
    
        Args:
        - city: A string representing the name of the city to search for.
        
        Returns:
        A list of Flight objects containing information about all flights that depart from or arrive at the given city.
        
        """
        
        #Initialize an empty list to store the matching flights
        matchingFlights = []
        #Get all Flights in _allFlights from our helper function.  
        allFlights = self.getAllFlightsFromDictionary()
        
        #Iterate over all flights
        for flight in allFlights:
            #Check if either the origin or destination city of the flight matches the given city
            if flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city:
                #The flight matches, add it to the list of matching flights
                matchingFlights.append(flight)
                
        return matchingFlights
                

    def findFlightByNo(self,flightNo):
        """
        A function that finds a flight with a given flight number.
    
        Args:
        - flightNo: A string representing the flight number to search for.
        
        Returns:
        A Flight object containing information about the flight with the given flight number.
        """
        #Get all Flights in _allFlights from our helper function.
        allFlights = self.getAllFlightsFromDictionary()
        
        #Iterate over all flights
        for flight in allFlights:
            #Check if the flight number matches
            if flight.getFlightNumber() == flightNo:
                #It matched, so return the Flight
                return flight
        return -1
 
        
    def findAllCountryFlights(self, country):
        """
         A function that finds all flights that depart from or arrive at airports in a given country.
    
        Args:
        - country: A string representing the name of the country to search for.
        
        Returns:
        A list of Flight objects containing information about all flights that depart from or arrive at airports in the given country.
        """
        #Initialize an empty list to store the matching flights
        matchingCountryFlights = []
        
        #Get all Flights in _allFlights from our helper function.  
        allFlights = self.getAllFlightsFromDictionary()
        
        #Iterate over all flights
        for flight in allFlights:
            #Check if either the origin or destination country of the flight matches the given country
            if flight.getOrigin().getCountry() == country or flight.getDestination().getCountry() == country:
                #The flight matches, add it to the list of matching flights
                matchingCountryFlights.append(flight)
        return matchingCountryFlights
    
    
    def findFlightBetween(self, origAirport, destAirport):
        """
        A function that finds all flights that depart from a given origin airport and arrive at a given destination airport.
    
        Args:
        - origAirport: An Airport object representing the origin airport.
        - destAirport: An Airport object representing the destination airport.
        
        Returns:
        A list of Flight objects containing information about all flights that depart from the given origin airport and arrive at the given destination airport.
        """
        
        #Get all Flights in _allFlights from our helper function.  
        allFlights = self.getAllFlightsFromDictionary()
        
        #Check for direct flights between the origin and destination airports
        #Iterate over all flights
        for flight in allFlights:
            #Do the origin and destination airports of the flight match
            if flight.getOrigin() == origAirport and flight.getDestination() == destAirport:
                #The origin and destination airports of the flight match, so return the flight
                return f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"
        
        #There are no direct flights, look for single-hop flights between the origin and destination airports
        #Initialize a set for single-hop flights    
        singleHopFlights = set()
        
        #Iterate over all flights
        for flight1 in allFlights:
            #Check the 1st flight's origin
            if flight1.getOrigin() == origAirport:
                #1st flight has the correct origin, so check for 2nd hop of the flight by looping though flights again
                for flight2 in allFlights:
                    #Is the destination of the 2nd flight the correct one, and the layover airport the destination of the 1st flight and origin of the 2nd
                    if flight2.getOrigin() == flight1.getDestination() and flight2.getDestination() == destAirport:
                        #Add the destination airport code to the set of single-hop flight destinations
                        singleHopFlights.add(flight1.getDestination().getCode())

        #If there are single-hop flights available, return the set of single-hop flight destinations
        if len(singleHopFlights) > 0:
            return singleHopFlights
        
        #There were no single hop flights, so return -1
        return -1
    
    
    def findReturnFlight(self, firstFlight):
        """
        A function that finds a return flight for a given flight.
    
        Args:
        - firstFlight: A Flight object representing the flight for which to find a return flight.
        
        Returns:
        A Flight object containing information about the return flight.
        """
        #Get all Flights in _allFlights from our helper function.  
        allFlights = self.getAllFlightsFromDictionary()
        
        #Iterate over all flights
        for flight in allFlights:
            #Check the origin of the current flight is the same as the destination of firstFlight and the destination of the current flight is the same as the origin of firstFlight.
            if flight.getOrigin() == firstFlight.getDestination() and flight.getDestination() == firstFlight.getOrigin():
                #Return the current flight.
                return flight
        return -1

            
    def findFlightsAcross(self, ocean):
        """
         A method that finds all flights that cross a given ocean.
    
        Args:
        - ocean: A string representing the name of the ocean to search for.
        
        Returns:
        A set of Flight codes for all flights that cross the given ocean.
        """
        #Define lists of continents in each "zone"
        redZone = ['Asia', 'Australia']
        blueZone = ['Europe', 'Africa']
        greenZone = ['North America', 'South America']
        
        #Initialize an empty set to hold the Flight codes of flights that cross the ocean    
        flightNumbersAcross = set()
        
        #Get all Flights in _allFlights from our helper function.  
        allFlights = self.getAllFlightsFromDictionary()
        
        #Iterate over all flights
        for flight in allFlights:
            #Check if the ocean being searched for is the Pacific
            if ocean == "Pacific":
                #Check if the flight's origin continent is in the redZone and destination continent is in the greenZone
                if flight.getOrigin().getContinent() in redZone and flight.getDestination().getContinent() in greenZone:
                    #Add the flight's code to the flightNumbersAcross set
                    flightNumbersAcross.add(flight.getFlightNumber())

                #Check if the flight's origin continent is in the greenZone and destination continent is in the redZone
                elif flight.getOrigin().getContinent() in greenZone and flight.getDestination().getContinent() in redZone:
                    #Add the flight's code to the flightNumbersAcross set
                    flightNumbersAcross.add(flight.getFlightNumber())

            if ocean == "Atlantic":
                #Check if the flight's origin continent is in the greenZone and destination continent is in the blueZone
                if flight.getOrigin().getContinent() in greenZone and flight.getDestination().getContinent() in blueZone:
                    #Add the flight's code to the flightNumbersAcross set
                    flightNumbersAcross.add(flight.getFlightNumber())

                #Check if the flight's origin continent is in the blueZone and destination continent is in the greenZone
                elif flight.getOrigin().getContinent() in blueZone and flight.getDestination().getContinent() in greenZone:
                    #Add the flight's code to the flightNumbersAcross set
                    flightNumbersAcross.add(flight.getFlightNumber())

        #If there are flights that cross the given ocean, return the set of Flight codes
        if len(flightNumbersAcross) > 0:
            return flightNumbersAcross
        
        #There are no flights that cross the given ocean, return -1
        return -1    

    def getAllFlightsFromDictionary(self):
        '''
        This helper function gets all the flights in the _allflights dictionary and adds them to a list

            Args:
                None

            Returns:
                List of flights in _allflights dictionary
        
        '''
        #Create an empty list called "allFlightsList"    
        allFlightsList = []
        #Loop through all the values of the _allflights dictionary
        for allFlights in self._allFlights.values():
            #Loop through each flight in the values of the allflights list
            for flight in allFlights:
                #Append each flight to the allFlightsList list
                allFlightsList.append(flight)
            
        #Return the list
        return allFlightsList

    