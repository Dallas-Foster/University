package Assignment2;



/**
 * The Word class represents a word composed of a linked list of Letter objects.
 */
public class Word {
    private LinearNode<Letter> firstLetter;
    
    /**
     * Constructs a Word object with the given array of Letter objects.
     * The letters are linked together to form a linked list.
     * 
     * @param letters the array of Letter objects
     */
    public Word(Letter[] letters) {
    	
        if (letters.length > 0) {
            firstLetter = new LinearNode<>(letters[0]);
            LinearNode<Letter> currentNode = firstLetter;

            for (int i = 1; i < letters.length; i++) {
                LinearNode<Letter> newNode = new LinearNode<>(letters[i]);
                currentNode.setNext(newNode);
                currentNode = newNode;
            }
        }
    }
    /**
     * Returns a string representation of the Word object.
     * The string consists of the word label followed by the string representations of each letter in the word.
     * 
     * @return the string representation of the object
     */
    public String toString() {
        StringBuilder sb = new StringBuilder("Word: ");
        LinearNode<Letter> currentNode = firstLetter;

        while (currentNode != null) {
            sb.append(currentNode.getElement().toString()).append(" ");
            currentNode = currentNode.getNext();
        }

        return sb.toString();
    }

    /**
     * Labels the letters in this word based on a comparison with the letters in another word.
     * The labels are set to Unused, Used, or Correct depending on their positions and equality with the other word's letters.
     * 
     * @param mystery the other Word object for comparison
     * @return true if the labeled word matches the other word, false otherwise
     */
    public boolean labelWord(Word mystery) {
        LinearNode<Letter> currentGuessNode = firstLetter; //Set firstLetter 
        LinearNode<Letter> currentMysteryNode = mystery.firstLetter; // Set mystery.firstLetter
        //Construct strings to represent the guessed and mystery words
        String strGuess = "";
        while (currentGuessNode != null) {
    		Letter guessLetter = currentGuessNode.getElement();
    		strGuess += guessLetter.toString().trim();
    		currentGuessNode = currentGuessNode.getNext();
        }

        String strMystery = "";
        while (currentMysteryNode != null) {
    		Letter mysteryLetter = currentMysteryNode.getElement();
    		strMystery += mysteryLetter.toString().trim();
    		currentMysteryNode = currentMysteryNode.getNext();
        }
        // If both words are empty, return false
        currentGuessNode = firstLetter;
        currentMysteryNode = mystery.firstLetter;
        if (currentGuessNode == null && currentMysteryNode == null) return false;
    
        int guessPosition = 0;
        // Iterate through each letter in the guessed word
        while (currentGuessNode != null) {
    		Letter guessLetter = currentGuessNode.getElement();
    		guessLetter.setUnused();
    		
        	currentMysteryNode = mystery.firstLetter;
        	
        	int mysteryPosition = 0;
        	boolean correct = false;
        	// Compare the current guessed letter with each letter in the mystery word
        	while (currentMysteryNode != null) {
        		Letter mysteryLetter = currentMysteryNode.getElement();
        		// If the letters match
        		if (guessLetter.equals(mysteryLetter)) {
                    if (mysteryPosition == guessPosition) {
                    	// If the positions match, set the label to Correct
                    	guessLetter.setCorrect();
                    	correct = true;
                    	break;
                    } else {
                    	// If the positions don't match and no correct match has been found yet, set the label to Used
                    	if (!correct) {
	                    	guessLetter.setUsed();
	                    }
                    }
                }
        		currentMysteryNode = currentMysteryNode.getNext();
        		mysteryPosition++;
        	}
        	currentGuessNode = currentGuessNode.getNext();
        	guessPosition++;
        }
        // Check if the labeled word matches the other word
        return strMystery.equals(strGuess);
    }
}
