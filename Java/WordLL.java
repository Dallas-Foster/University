package Assignment2;



/**
 * The WordLL class represents a linked list of Word objects used for word guessing.
 * It maintains a mystery word and keeps track of the guessing history.
 */
public class WordLL {
    private Word mysteryWord;
    private LinearNode<Word> history;

    /**
     * Constructs a WordLL object with the given mystery word.
     *
     * @param mystery the mystery word to be guessed
     */
    public WordLL(Word mystery) {
        mysteryWord = mystery;
        history = null;
    }

    /**
     * Tries a word guess by labeling it and adding it to the guessing history.
     * The word's labels are set based on its comparison with the mystery word.
     *
     * @param guess the word being guessed
     * @return true if the guessed word matches the mystery word, false otherwise
     */
    public boolean tryWord(Word guess) {
        guess.labelWord(mysteryWord);

        LinearNode<Word> newNode = new LinearNode<>(guess);
        newNode.setNext(history);
        history = newNode;

        return guess.toString().equals(mysteryWord.toString());
    }

    /**
     * Returns a string representation of the guessing history.
     * The string consists of each word in the history, separated by newline characters.
     *
     * @return the string representation of the guessing history
     */
    public String toString() {
        StringBuilder sb = new StringBuilder();

        LinearNode<Word> currentNode = history;
        while (currentNode != null) {
            sb.append(currentNode.getElement().toString()).append("\n");
            currentNode = currentNode.getNext();
        }

        return sb.toString();
    }
}

/**
 * Summary:
 * To start this assignment I completed the Letter class first, followed by the wordLL and ExtendedLetter then finally 
 * Word. I did word last due to the difficulty of figuring out the Labelword method. It took the most time because
 * I had a few issues with verifying the used and correct labels for each specific letter, making sure that 
 * they were in the correct position. I had to iterate over the list of the word used to do so. For other tests such as test 5
 * I needed to use pirntline statements to figure out where the program was going wrong with the labels.
 */