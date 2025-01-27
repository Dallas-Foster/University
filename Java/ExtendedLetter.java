package Assignment2;



/**
 * The ExtendedLetter class represents an extended version of the Letter class.
 * It includes additional properties such as content, family, and related.
 */
public class ExtendedLetter extends Letter {
    private String content;
    private int family;
    private boolean related;
    
    private static final int SINGLETON = -1;
    
    /**
     * Constructs an ExtendedLetter object with the given content.
     * The family is set to SINGLETON and the related status is set to false.
     * 
     * @param s the content of the extended letter
     */
    public ExtendedLetter(String s) {
    	super(' ');
        content = s;
        related = false;
        family = SINGLETON;
    }
    
    /**
     * Constructs an ExtendedLetter object with the given content and family.
     * The related status is set to false.
     * 
     * @param s    the content of the extended letter
     * @param fam  the family code of the extended letter
     */
    public ExtendedLetter(String s, int fam) {
    	super(' ');
        content = s;
        related = false;
        family = fam;
    }
    
    /**
     * Checks if this ExtendedLetter object is equal to the specified object.
     * Two extended letters are considered equal if their families match and their content is the same.
     * If the families match, the related status of this letter is set to true.
     * 
     * @param other the object to compare with
     * @return true if the objects are equal, false otherwise
     */
    public boolean equals(Object other) {
        if (!(other instanceof ExtendedLetter)) {
            return false;
        }
        
        ExtendedLetter otherLetter = (ExtendedLetter) other;
        
        if (otherLetter.family == this.family) {
            this.related = true;
        }
        
        return otherLetter.content.equals(this.content);
    }
    
    /**
     * Returns a string representation of the ExtendedLetter object.
     * If the letter is unused and related, the string consists of a dot, the content, and another dot.
     * Otherwise, the string is generated by calling the decorator method of the superclass.
     * 
     * @return the string representation of the object
     */
    public String toString() {
        if (isUnused() && related) {
            return "." + content + ".";
        } else {
            return super.decorator() + content + super.decorator();
        }
    }
    
    /**
     * Converts arrays of content strings and family codes into an array of ExtendedLetter objects.
     * If the codes array is null, each content string is used to create an ExtendedLetter with the default family.
     * Otherwise, the corresponding family code is used to create each ExtendedLetter.
     * 
     * @param content the array of content strings
     * @param codes   the array of family codes (can be null)
     * @return an array of ExtendedLetter objects
     */
    public static Letter[] fromStrings(String[] content, int[] codes) {
        Letter[] letters = new Letter[content.length];
        
        for (int i = 0; i < content.length; i++) {
            if (codes == null) {
                letters[i] = new ExtendedLetter(content[i]);
            } else {
                letters[i] = new ExtendedLetter(content[i], codes[i]);
            }
        }
        
        return letters;
    }
}
