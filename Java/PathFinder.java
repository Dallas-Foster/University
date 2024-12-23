package Assignment3;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

/**
 * Represents a PathFinder class that navigates through a pyramid-shaped map to find a path.
 */
public class PathFinder {
    private Map pyramidMap;

    /**
     * Constructs a PathFinder object and initializes the pyramidMap using the provided file.
     *
     * @param fileName The name of the file containing the pyramid map data.
     */
    public PathFinder(String fileName) {
        try {
            pyramidMap = new Map(fileName);
        } catch (InvalidMapCharacterException e) {
            System.out.println("Error: Invalid map character - " + e.getMessage());
            // If you want to provide more specific information about the character,
            // you can modify the message accordingly.
        } catch (FileNotFoundException e) {
            System.out.println("Error: File not found - " + e.getMessage());
            // Handle the case where the specified file is not found.
        } catch (IOException e) {
            System.out.println("Error: I/O error - " + e.getMessage());
            // Handle any other I/O-related exceptions that might occur.
        }
    }

    /**
     * Finds the path through the pyramid map starting from the entrance chamber.
     *
     * @return A DLStack containing the chambers forming the path. Empty if no path is found.
     */
    public DLStack path() {
        DLStack pathStack = new DLStack();
        Chamber entranceChamber = pyramidMap.getEntrance();
        if (entranceChamber == null) {
            return pathStack;
        }

        exploreChamber(entranceChamber, pathStack);
        return pathStack;
    }

    /**
     * Recursively explores the chambers starting from the current chamber to find the path.
     *
     * @param currentChamber The current chamber being explored.
     * @param pathStack The stack to keep track of the path.
     */
    private void exploreChamber(Chamber currentChamber, DLStack pathStack) {
        currentChamber.markExit();
        pathStack.push(currentChamber);

        Chamber nextChamber = bestChamber(currentChamber);
        while (nextChamber != null) {
            exploreChamber(nextChamber, pathStack);
            nextChamber = bestChamber(currentChamber);
        }
    }

    /**
     * Retrieves the pyramid map associated with this PathFinder.
     *
     * @return The Map object representing the pyramid map.
     */
    public Map getMap() {
        return pyramidMap;
    }
    
    /**
     * Checks if the current chamber has a neighbor of a specific type.
     *
     * @param currentChamber The chamber to check for neighbors.
     * @param type           The type of neighbor to look for ("lit" or "treasure").
     * @return true if the chamber has a neighbor of the specified type, false otherwise.
     */
    private boolean hasNeighborType(Chamber currentChamber, String type) {
    	for (int i = 0; i <= 5; i ++) {
    		try {
    			Chamber neighbour = currentChamber.getNeighbour(i);
    			switch (type) {
    			case "lit":
            		if (neighbour.isLighted()) {
            			return true;
            		}
            		break;
				case "treasure":
	        		if (neighbour.isTreasure()) {
	        			return true;
	        		}
	        		break;
    			}
    		}
    		catch (InvalidNeighbourIndexException e) {}
    	}
    	return false;
    }

    /**
     * Checks if the current chamber is dim, i.e., not sealed, not lighted, but has a lit neighbor.
     *
     * @param currentChamber The chamber to check.
     * @return true if the chamber is dim, false otherwise.
     */
    public boolean isDim(Chamber currentChamber) {
        return currentChamber != null && !currentChamber.isSealed() && !currentChamber.isLighted() && hasNeighborType(currentChamber, "lit");
    }
    
    /**
     * Finds the best chamber to explore from the current chamber based on specific criteria.
     *
     * @param currentChamber The current chamber to find the best neighbor.
     * @return The best neighbor chamber to explore, or null if none is found.
     */
    public Chamber bestChamber(Chamber currentChamber) {
    	for (int i = 0; i <= 5;) { // Loop through all 6 possible neighbors of the current chamber.
    		try {
    			Chamber neighbour = currentChamber.getNeighbour(i); // Get the neighbor at the specified index.
    			if (neighbour.isTreasure() && !neighbour.isMarked()) { // Check if the neighbor is a treasure and has not been marked.
    				return neighbour; // Return the neighbor if it meets the criteria.
    			}
    		}
    		catch (InvalidNeighbourIndexException e) {}  // Ignore invalid neighbor index exceptions.
    	}
    	
    	for (int i = 0; i <= 5;) {  // If no treasure neighbor is found, search for a lighted and unmarked neighbor.
    		try {
    			Chamber neighbour = currentChamber.getNeighbour(i);
  			
    			if (neighbour.isLighted() && !neighbour.isMarked()) { // Check if the neighbor is lighted and has not been marked.
    				return neighbour; // Return the neighbor if it meets the criteria.
    			}
    		}
    		catch (InvalidNeighbourIndexException e) {}
    	}
    	
    	for (int i = 0; i <= 5;) {  // If no lighted neighbor is found, search for a dim (not sealed, not lighted, but with a lit neighbor) neighbor.
    		try {
    			Chamber neighbour = currentChamber.getNeighbour(i);
    			
    			if (isDim(neighbour) && !neighbour.isMarked()) {
    				return neighbour;
    			}
    		}
    		catch (InvalidNeighbourIndexException e) {}
    	}
    	return null; // If no suitable neighbor is found, return null indicating no best chamber is available.
    }
}

/*
 * For me personally this was the hardest assignment out of the 3. I started by completing the pathfinder class, as I thought it would take less time
 * than the DLStack class. Problems started to arise while I was completing the DLStack class. It was difficult for me to set up the 
 * stacks to move in the order to pass the tests. I initially had the stacks inverted so I would be prepending to the top instead of the bottom. 
 * I solved this issue by using printline statements in the test file to see where it was going wrong. From there I realized that I had to swithc the 
 * order of some of my code in the class.
 */
