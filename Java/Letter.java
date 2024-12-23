package Assignment2;



/**
 * The Letter class represents a letter with its associated label.
 */
public class Letter {
    private char letter;
    private int label;
    private static final int Unset = 0; // Integer representation of unset, unused, used, and correct letters
    private static final int Unused = 1;
    private static final int Used = 2;
    private static final int Correct = 3;
    
    /**
     * Constructs a Letter object with the given character and an unset label.
     * 
     * @param c the character representing the letter
     */
    public Letter(char c) {
        letter = c;
        label = Unset;
    }
    
    /**
     * Checks if this Letter object is equal to the specified object.
     * Two letters are considered equal if they have the same character.
     * 
     * @param otherObject the object to compare with
     * @return true if the objects are equal, false otherwise
     */
    public boolean equals(Object otherObject) {
        if (otherObject instanceof Letter) {
            Letter otherLetter = (Letter) otherObject;
            return letter == otherLetter.letter;
        }
        return false;
    }
    
    /**
     * Returns a decorator string based on the label value. Each case has a specific value
     * 
     * @return the decorator string
     */
    public String decorator() {
        switch (label) {
            case Unused:
                return "-";
            case Used:
                return "+";
            case Correct:
                return "!";
            default:
                return " ";
        }
    }
    
    /**
     * Returns a string representation of the Letter object.
     * The string consists of the decorator, the letter character, and the decorator.
     * 
     * @return the string representation of the object
     */
    public String toString() {
    	//System.out.println("Letter .........." +letter);
        return decorator() + letter + decorator();
    }
    
    /**
     * Sets the label of the Letter object to Unused.
     */
    public void setUnused() {
        label = Unused;
    }
    
    /**
     * Sets the label of the Letter object to Used.
     */
    public void setUsed() {
        label = Used;
    }
    
    /**
     * Sets the label of the Letter object to Correct.
     */
    public void setCorrect() {
        label = Correct;
    }
    
    /**
     * Checks if the Letter object has the Unused label.
     * 
     * @return true if the letter is unused, false otherwise
     */
    public boolean isUnused() {
        return label == Unused;
    }
    
    /**
     * Converts a string representation of letters into an array of Letter objects.
     * Each character in the string is converted into a Letter object.
     * 
     * @param s the input string
     * @return an array of Letter objects
     */
    public static Letter[] fromString(String s) {
        int length = s.length();
        Letter[] lettersArray = new Letter[length];

        for (int i = 0; i < length; i++) {
            char c = s.charAt(i);
            lettersArray[i] = new Letter(c);
        }

        return lettersArray;
    }
}
