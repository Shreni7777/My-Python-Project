# My-Python-Project
Project based on Movie Picker Program
Step 1: Includes importing all the required libraries like requests, Beautifulsoup, Pandas. 
Step 2: With the help of requests library we get the details of the url link by using get() and store the response of the website content in soup object of beautifulsoup library. 
Step 3: Then we search for the movie links that are enclosed in anchor tag <a> and store it in "movie_links". 
Step 4: Then we iterate through all the movie links using for loop.
Step 5: Then we create a dictionary with keys as Title and Genres and create an empty link for storing the values in the keys. 
Step 6: After that we create a function to split the links, remove tags and extract the text values for title and genres. This is done using split function. This function block also has the exceptions added to throw the processing error message. 
Step 7: In the next step, we create the dataframe for the fetched data and remove the blank spaces if any with dropna(). 
Step 8: After that we create the csv file named "movie_info" to store the complete data. 
Step 9 :Then we create another function for movie suggesstion based on genre. This function takes the input from user for genre information, it reads the CSV file and suggests the movie to the user. This funstion filters out the movies associate with their genre based on the input value given by user. It throws the filenotfound or an exception error in case of any issues. 

