#Import Airport file
from Assignments.Airport import *

#Define a class called Flight that takes three parameters: flightNo, origAirport, destAirport
class Flight:

    #Initialize the values
    def __init__(self, flightNo, origAirport, destAirport):
        """
        First check that both origAirport and destAirport are Airport objects (hint: use the isinstance function).
        If either or both are not Airport objects, raise a TypeError exception that states:
        "The origin and destination arguments must be Airport objects"

        In the case that the flightNo is not a string of 6-character code containing 3 letters followed by 3
        digits, raise a TypeError exception that states:
        "The flight number format is incorrect"
        
        When the origAirport and destAirport are both Airport objects, proceed to initialize the instance
        variables _flightNo, _origin, and _destination based on the corresponding parameters in the
        constructor.

        Args:
            flightNo (string): unique code for the flight
            origAirport (Airport): airport object where the flight originates
            destAirport (Airport): airport object where the flight goes to
            
        Return: Nothing
        """
        #This checks whether the flight number is valid or not. It calls a helper function "isValidFlightCode" to do this. If the flight number is not valid, it raises an error
        if self.isValidFlightCode(flightNo) == False:
            raise TypeError("The flight number format is incorrect")
        
        #This checks whether both origAirport and destAirport are type Airport. If one or both of them is not a type of Airport, it raises an error 
        if isinstance(origAirport, Airport) == False or isinstance(destAirport, Airport) == False:
            raise TypeError("The origin and destination arguments must be Airport objects")
        
        #Assign the self parameters
        self._flightNo = flightNo
        self._origAirport = origAirport
        self._destAirport = destAirport
        
    
    #Representation of any given flight in the form of a string
    def __repr__(self):
        """
        Return the representation of this Flight containing the flightNo, origin city, and destination city, and an
        indication of whether the Flight is domestic or international (see the isDomesticFlight method description
        below).
                
        Args: None
        
        Return: (string) Flight({flightNo}): {originCity} -> {destinationCity} {[domestic]/[international]}
            e.g.,
            Flight(MCK533): Toronto -> Montreal [domestic]
            Flight(WCL282): Toronto -> Chicago [international]
        """
        #This determines whether or not the flight is international or domestic, to be added to the end of the string as per specifications
        flightType = 'domestic'
        #Calls the isDomesticFlight function and applies a boolean to determine if the flight is domestic. If false, the flight must be international
        if self.isDomesticFlight() == False:
            flightType = 'international'

        #Format of the representation of an airport as a string
        return f"Flight({self._flightNo}): {self._origAirport.getCity()} -> {self._destAirport.getCity()} [{flightType}]"
    
    
    def __eq__(self, other):
        """
        Method that returns True if self and other flights are considered the same flight. Two flights are considered
        the same if the origin and destination are the same for both Flights i.e., self and other. Make sure that if
        “other” variable is not a Flight object, this means False should be returned.
        Args:
            other (Flight): another flight object to compare to self
            
        Return: (boolean) Are the flights the same?
            e.g., True
        """
       
        #This checks if other is of type Flight, and returns False if not.
        if not isinstance(other, Flight):
            return False
        
        #This checks if the origin and destination airport codes are the same for both flights. If both the origin and destination airport codes are the same, return True, indicating that the two flights are the same.
        return self.getOrigin() == other.getOrigin() and self.getDestination() == other.getDestination()
    

    #Getter function that returns the flight number of a flight
    def getFlightNumber(self):
        """
        Getter that returns the Flight number string code
        Args: Nothing
        
        Return: (string) {flightNo}
            e.g., XYZ123
        """
        return self._flightNo
    

    #Getter function that returns the origin of a flight
    def getOrigin(self):
        """
        Getter that returns the object of the Flight origin
        Args: Nothing
        
        Return (Airport) {origAirport}
            e.g., YYZ
        """
        return self._origAirport
    

    #Getter function that returns the destination of a flight
    def getDestination(self):
        """
        Getter that returns the object of the Flight destination        
        Args: Nothing
        
        Return (Airport) {destAirport}
            e.g., YYZ
        """
        return self._destAirport
    

    #Function that determines whether or not a flight is domestic or international
    def isDomesticFlight(self):
        """
        This method returns True if the flight is domestic, i.e. within the same country (the origin and destination
        are in the same country); However, it returns False if the flight is international (the origin and destination
        are in different countries).        
        
        Args: Nothing
        
        Return (boolean) Are teh orig and dest airports in the same country
            e.g., True
        """
        #If the country of origin of the flight instance is the same country as the destination, return True indicating a domestic flight. If not, return False meaning that the flight is international
        return self._origAirport.getCountry() == self._destAirport.getCountry()
    

    #Setter that sets the origin parameter
    def setOrigin(self, origin):
        """
        Setter that sets (updates) the Flight origin

        Args:
            origin (Airport): the new origin airport object for the flight
            
        Return: Nothing
        """
        #Check whether the origin parameter is an object of Airport
        if isinstance(origin, Airport) == False:
             #Raise an error if the origin is not an object of Airport
             raise TypeError("The origin must be an Airport object.")
        
        #this sets origin instance to origin parameter
        self._origAirport = origin
    

    #Setter that sets the destination parameter
    def setDestination(self, destination):
        """
        Setter that sets (updates) the Flight destination
        
        Args:
            destination (Airport): the new destination airport object for the flight
            
        Return: Nothing
        """
        #Check whether the destination parameter is an object of Airport
        if isinstance(destination, Airport) == False:
             #Raise an error if the destination is not an object of Airport
             raise TypeError("The destination must be an Airport object.")
        
        #this sets destination instance to destination parameter
        self._destAirport = destination


    #Helper function to determine if a flights code is valid or not
    def isValidFlightCode(self, flightCode):
        """
        This helper function validates the flight code by ensuring the first 3 characters of the code are letters, and the last 3 are digits

        Args:
            flightCode (string): The code that will be validated (eg. XYZ123)

        Returns:
            Boolean: Returns whether the code is valid or not
        """
        #This ensures that the flights code is 6 characters long
        if len(flightCode) == 6:
            #This ensures that the first 3 characters of the code are letters
            if flightCode[0:2].isalpha():
                #This ensures the the last 3 characters of the code are numbers
                if flightCode[3:5].isnumeric():
                    #Return True if the code instance satisfies all of these
                    return True
                
        #Return False if any of these paramters are not met by the code instance        
        return False

