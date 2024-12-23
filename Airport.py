#Define a class called Airport that takes four parameters: code, city, country, continent
class Airport:
    #initialize the values
    def __init__(self, code, city, country, continent):
        """
        Initialize the instance variables _code, _city, _country, and _continent based on the corresponding parameters in the constructor

        Args:
            code (string): 3 letter airport code
            city (string): city of airport
            country (string): country of airport
            continent (string): contitent of airport
            
        Return: Nothing
        """
        #Check to ensure that the parameters are of type string, otherwise raise a TypeError
        #Checks if code is type string
        if isinstance(code, str) == False:
             raise TypeError("The code must be a string.")
        
        #Checks if city is type string
        if isinstance(city, str) == False:
             raise TypeError("The city must be a string.")
        
        #Checks if country is type string
        if isinstance(country, str) == False:
             raise TypeError("The country must be a string.")
        
        #Checks if continent is type string
        if isinstance(continent, str) == False:
             raise TypeError("The continent must be a string.")
        
        #Assign the self parameters
        self._code = code
        self._city = city
        self._country = country
        self._continent = continent
    

    #Representation of any given airport in the form of a string
    def __repr__(self):
        """
        Return the representation of this Airport
        
        Args: Nothing
        
        Return (string): {code} ({city}, {country})
            e.g., YYZ (Toronto, Canada)        
        """
        #Format of the representation of an airport as a string
        return f"{self._code} ({self._city}, {self._country})"
    

    #Getter function that returns the code of an airport
    def getCode(self):
        """
        Getter that returns the Airport code
        
        Args: None
        
        Return: (string) {code}
            e.g., YYZ
        """
        return self._code
    

    #Getter function that returns the city of an airport
    def getCity(self):
        """
        Getter that returns the Airport city
        
        Args: None
        
        Return: (string) {city}        
            e.g., Toronto    
        """
        return self._city
    

    #Getter function that returns the country of an airport    
    def getCountry(self):
        """
        Getter that returns the Airport country

        Args: None
        
        Return: (string) {country}
                e.g., Canada
        """
        return self._country
    

    #Getter function that returns the continent of an airport
    def getContinent(self):
        """
        Getter that returns the Airport continent
                
        Args: None
        
        Return: (string) {continent}    
            e.g., North America
        """
        return self._continent


    #Setter that sets the city parameter
    def setCity(self, city):
        """
        Setter that sets the Airport city
        Args:
            city (string): city of airport
            
        Return: Nothing
        """
        #Check whether city parameter is a string or not
        if isinstance(city, str) == False:
             #Raise error if city is not type string
             raise TypeError("The city must be a string.")
        
        #Sets city instance to city parameter
        self._city = city
    

    #Setter that sets the country parameter
    def setCountry(self, country):
        """
        Setter that sets the Airport country
        Args:
            country (string): country of airport
            
        Return: Nothing
        """
        #Check whether country parameter is a string or not
        if isinstance(country, str) == False:
             #Raise error if country is not type string
             raise TypeError("The country must be a string.")
        
        #Sets country instance to country parameter       
        self._country = country
    

    #Setter that sets the continent parameter
    def setContinent(self, continent):
        """
        Setter that sets the Airport continent
        Args:
            continent (string): contitent of airport
            
        Return: Nothing
        """
        #Check whether continent parameter is a string or not
        if isinstance(continent, str) == False:
            #Raise error if continent is not type string
            raise TypeError("The continent must be a string.")
        
        #Sets continent instance to continent parameter        
        self._continent = continent
    