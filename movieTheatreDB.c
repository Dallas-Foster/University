/*
 * Movie Database: By Dallas Foster, 251287541
 *
 * This program serves as a movie database system. It stores up to 100 user inputted movies in the database
 * by continuously prompting users for five possible commands: 'i' to insert a new movie, requesting a unique
 * movie code, name, genre, and rating while validating inputs for uniqueness, acceptable length of name and
 * genre, and a valid rating range (0.0 to 10.0); 's' to search for a movie using its code, printing its
 * details if found or notifying the user if the code doesn't exist; 'u' to update an existing movie by code,
 * prompting users to modify all attributes (code, name, genre, rating) and alerting if the specified code
 * isn't found; 'p' to print a table listing all movies in the database with attributes like Movie Code, Name,
 * Genre, and Rating; 'q' to quit the program,
 */

#include <stdio.h>
#include <string.h>


// Define the movie structure
struct Movie {
    // Unique identifier for the movie
    int code;
    // Array to store the movie name (up to 100 characters)
    char name[100];
    // Array to store the movie genre (up to 25 characters)
    char genre[25];
    // Floating-point variable to store the movie rating
    float rating;
};

// The line creates an array named 'movieDatabase' of 100 elements,
// each element being a structure of type 'Movie', allowing you to store information about 100 movies.
struct Movie movieDatabase[100];
// Declare and initialize a variable 'numMovies' with the value 0.
// This variable will be used to keep track of the current number of movies in the 'movieDatabase'.
int numMovies = 0;

// Function to insert a new movie
void insertMovie() {
    // Declare variables to store information about the new movie
    int code;
    char name[100];
    char genre[25];
    float rating;

    // Prompt the user to enter the movie code
    printf("\tEnter movie code: ");
    // Read the entered movie code from the user and store it in the 'code' variable
    scanf(" %d", &code);

    int codeExists = 0;
// Initialize a variable 'codeExists' to 0. This variable will be used to check if the entered movie code already exists in the database.

    for (int i = 0; i < numMovies; i++) {
        // Loop through the existing movies in the database
        if (movieDatabase[i].code == code) {
            // If the entered movie code matches an existing movie code
            codeExists = 1;
            // Set 'codeExists' to 1 to indicate that the code already exists
            break;
            // Exit the loop since the code has been found, no need to continue checking
        }
    }

    if (code < 0 || codeExists || numMovies >= 100) {
        // Check if the entered movie code is negative, or if it already exists,
        // or if the database is already full (100 movies)
        printf("Error: Invalid movie code or database full.\n");
        // Print an error message indicating the issue
        return;
        // Exit the function since the code is invalid or the database is full
    }

    // Prompt the user to enter the name of the movie
    printf("\tEnter movie name: ");
    // Read up to 99 characters (excluding newline) and store them in the 'name' variable
    scanf(" %99[^\n]", name);

    // Prompt the user to enter the genre of the movie
    printf("\tEnter movie genre: ");
    // Read up to 24 characters (excluding newline) and store them in the 'genre' variable
    scanf(" %24[^\n]", genre);

    // Prompt the user to enter the rating of the movie
    printf("\tEnter movie rating: ");
    // Read a floating-point number from the user and store it in the 'rating' variable
    scanf(" %4f", &rating);
    //
    float ratingMultiplier = rating * 10;
    // Compare the multiplied rating to the float rating to determine if there was a valid rating inputted
    int ratingRound = (int)ratingMultiplier;
    // Final check to determine if inputted rating was between 0 and 10.0 with a valid decimal
    if (rating < 0 || rating > 10 || ratingMultiplier != ratingRound) {
        // If not, user is prompted to re-enter a rating
        printf("Please input a valid rating between 0-10.0");
        return;

    }


    // Add the movie to the database
    // Assign the entered movie code to the 'code' member of the new movie in the database
    movieDatabase[numMovies].code = code;
    // Copy the entered movie name to the 'name' member of the new movie in the database
    strcpy(movieDatabase[numMovies].name, name);
    // Copy the entered movie genre to the 'genre' member of the new movie in the database
    strcpy(movieDatabase[numMovies].genre, genre);
    // Assign the entered movie rating to the 'rating' member of the new movie in the database
    movieDatabase[numMovies].rating = rating;
    // Increment the 'numMovies' variable to reflect the addition of the new movie to the database
    numMovies++;
}

// When the index parameter is not equal to -1, it means that a specific movie is requested for printing.
// In this case, the minLoop and maxLoop variables are set to the value of the specified index. This ensures that the loop only iterates once, focusing on the specific movie.
// The loop then checks if the current iteration (i) is equal to the specified index (index). If it is, or if index is -1 (indicating a request to print all movies), the information for the movie is printed.
// If index is -1, the loop will iterate over all movies, printing information for each one.
void printMovies(int index) {
    // Initialize variables to store the maximum lengths of columns for formatting
    int maxCode = strlen("Movie Code");
    int maxName = strlen("Movie Name");
    int maxGenre = strlen("Movie Genre");
    int maxRating = strlen("Movie Rating");

    // Initialize loop boundaries for iterating through the movies in the database
    int minLoop = 0;
    int maxLoop = numMovies - 1;

    // Adjust loop boundaries if a specific 'index' is provided
    if (index != -1) {
        minLoop = index;
        maxLoop = index;
    }

    // Iterate through the movies in the specified range
    for (int i = minLoop; i <= maxLoop; i++) {
        // Check if printing all movies or only a specific movie (specified by 'index')
        if (i == index || index == -1) {
            // Calculate the length of the current movie's name
            int lengthName = strlen(movieDatabase[i].name);
            // Update the maximum name length if the current name is longer
            if (lengthName > maxName) {
                maxName = lengthName;
            }

            // Calculate the length of the current movie's genre
            int lengthGenre = strlen(movieDatabase[i].genre);
            // Update the maximum genre length if the current genre is longer
            if (lengthGenre > maxGenre) {
                maxGenre = lengthGenre;
            }
        }
    }

    // Print the header row with column names
    printf("%-*s\t%-*s\t%-*s\t%-*s\n", maxCode, "Movie Code", maxName, "Movie Name", maxGenre, "Movie Genre", maxRating, "Movie Rating");

    // Iterate through the movies in the specified range for printing
    for (int i = minLoop; i <= maxLoop; i++) {
        // Check if printing all movies or only a specific movie (specified by 'index')
        if (i == index || index == -1) {
            // Print the movie row with movie details
            printf("%-*d\t%-*s\t%-*s\t%-*.1f\n", maxCode, movieDatabase[i].code, maxName, movieDatabase[i].name, maxGenre, movieDatabase[i].genre, maxRating, movieDatabase[i].rating);
        }
    }
}

// Function to search for a movie by code
void searchMovie() {
    // Declare a variable to store the user-entered movie code
    int code;
    printf("\tEnter movie code: ");
    // Prompt the user to enter the movie code
    scanf("%d", &code);

    // Initialize a variable to check if the movie is found
    int found = 0;

    // Loop through the existing movies in the database
    for (int i = 0; i < numMovies; i++) {
        // Check if the movie code matches the entered code
        if (movieDatabase[i].code == code) {
            // Set 'found' to 1 to indicate that the movie is found
            found = 1;
            // Call the 'printMovies' function to print details of the found movie
            printMovies(i);
            // Exit the loop since the movie is found
            break;
        }
    }

    // Check if the movie was not found
    if (found == 0) {
        printf("\tMovie not found.");
    }
}

// Function to update a movie by code
void updateMovie() {
    // Declare a variable to store the user-entered movie code
    int code;
    printf("\tEnter movie code: ");
    // Prompt the user to enter the movie code
    scanf("%d", &code);

    // Initialize a variable to check if the movie is found
    int found = 0;

    // Loop through the existing movies in the database
    for (int i = 0; i < numMovies; i++) {
        // Check if the movie code matches the entered code
        if (movieDatabase[i].code == code) {
            // Prompt the user to enter the updated movie name
            printf("\tEnter movie name: ");
            // Read up to 99 characters (excluding newline) and store them in the 'name' member
            scanf(" %99[^\n]", movieDatabase[i].name);

            // Prompt the user to enter the updated movie genre
            printf("\tEnter movie genre: ");
            // Read up to 24 characters (excluding newline) and store them in the 'genre' member
            scanf(" %24[^\n]", movieDatabase[i].genre);

            // Prompt the user to enter the updated movie rating
            printf("\tEnter movie rating: ");
            // Read a floating-point number from the user and store it in the 'rating' member
            scanf(" %f", &movieDatabase[i].rating);

            // Set 'found' to 1 to indicate that the movie is found and updated
            found = 1;
            // Exit the loop since the movie is found and updated
            break;
        }
    }

    // Check if the movie was not found
    if (!found) {
        printf("\tMovie not found.");
    }
}

int main() {
    printf("*********************\n");
    printf("* 2211 Movie Cinema *\n");
    printf("*********************\n");

    while (1) {
        char command;
        printf("\nEnter operation code: ");
        scanf(" %c", &command);

        switch (command) {
            case 'i':
                insertMovie();
                break;
            case 's':
                searchMovie();
                break;
            case 'u':
                updateMovie();
                break;
            case 'p':
                printMovies(-1);
                break;
            case 'q':
                return 0;
            default:
                printf("Invalid command. Try again.\n");
        }
    }
}

