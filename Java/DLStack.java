package Assignment3;



/**
 * A generic implementation of a Double Linked Stack.
 *
 * @param <T> the type of elements held in this stack
 */
public class DLStack<T> implements DLStackADT<T> {
    private DoubleLinkedNode<T> top;
    private int numItems;

    /**
     * Constructs an empty stack.
     */
    public DLStack() {
        top = null;
        numItems = 0;
    }

    /**
     * Pushes a new element onto the top of the stack.
     *
     * @param dataItem the data item to be added to the stack
     */
    public void push(T dataItem) {
        DoubleLinkedNode<T> newNode = new DoubleLinkedNode<>(dataItem);
        if (top == null) {
            top = newNode; // If the stack is empty, the new node becomes the top
        } else {
            newNode.setPrevious(top);
            top.setNext(newNode);
            top = newNode; // New node becomes the top
        }
        numItems++;
    }

    /**
     * Removes and returns the element at the top of the stack.
     *
     * @return the element at the top of the stack
     * @throws EmptyStackException if the stack is empty
     */
    public T pop() throws EmptyStackException {
        if (isEmpty()) {
            throw new EmptyStackException("The stack is empty.");
        }

        return pop(1);
    }

    /**
     * Removes and returns the kth element from the top of the stack.
     *
     * @param k the index of the element to be removed (1-based index)
     * @return the element at the kth position from the top of the stack
     * @throws InvalidItemException if k is less than or equal to 0 or greater than the number of items in the stack
     */
    public T pop(int k) throws InvalidItemException {
        if (k <= 0 || k > numItems)  {// Check if the value of k is within valid range
            throw new InvalidItemException("There is an invalid item.");
        }

        int count = 1; // Initialize a counter to keep track of the node position
        DoubleLinkedNode<T> current = top; // Start from the top node of the double-linked list
        while (count < k) { // Traverse the list to find the k-th node
            current = current.getPrevious(); // Move to the previous node in the list
            count++;
        }

        T data = current.getElement(); // Store the data from the k-th node (the one to be removed)
        DoubleLinkedNode<T> prev = current.getPrevious(); // Get references to the previous and next nodes of the k-th node
        DoubleLinkedNode<T> next = current.getNext();
        
        if (k == 1) { // If the top element is removed, update the top to the next element
        	top = current.getPrevious();
        }
        
        if (prev != null) { // Link the previous node to the next node
            prev.setNext(next); 
        }
        
        if (next != null) { // Link the next node to the previous node
            next.setPrevious(prev);
        }
        numItems--;

        return data;
    }

    /**
     * Returns the element at the top of the stack without removing it.
     *
     * @return the element at the top of the stack
     * @throws EmptyStackException if the stack is empty
     */
    public T peek() throws EmptyStackException {
        if (isEmpty()) {
            throw new EmptyStackException("The stack is empty.");
        }

        return top.getElement();
    }

    /**
     * Checks if the stack is empty.
     *
     * @return true if the stack is empty, false otherwise
     */
    public boolean isEmpty() {
        return numItems == 0;
    }

    /**
     * Returns the number of elements in the stack.
     *
     * @return the number of elements in the stack
     */
    public int size() {
        return numItems;
    }

    /**
     * Returns the top node of the stack.
     *
     * @return the top node of the stack
     */
    public DoubleLinkedNode<T> getTop() {
        return top;
    }

    /**
     * Returns a string representation of the stack.
     *
     * @return a string representation of the stack
     */
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        DoubleLinkedNode<T> current = top;  // Start from the top node of the stack.
        while (current != null) {// Traverse through the stack nodes until the end
            sb.append(current.getElement()); // Append the element of the current node to the StringBuilder.
            if (current.getNext() != null) { // If there is a next node, add a space to separate elements.
                sb.append(" ");
            }
            current = current.getNext(); // Move to the next node in the stack.
        }
        sb.append("]");
        return sb.toString();
    }
}
