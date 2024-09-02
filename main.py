#----------------------------Importing libraries--------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd

#----------------------------Getting the response from the website------------------------------------------
list_url = 'https://www.yidio.com/movies'
response = requests.get(list_url)
soup = BeautifulSoup(response.content, 'html')

#--------------------------Finding all the Movie links enclosed in anchor tag---------------------------------
movie_links = soup.find_all('a', class_='card movie')
urls = [link['href'] for link in movie_links]

print(urls)

#--------------------------Creating an empty list to store Movies and Genre values -------------------------------------------------------
movies_info = {
    'Title': [],
    'Genres': [],
}

#--------------A function to extract texts for title and genre and appending them into empty list-----------------------------
def get_movie_info(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content,'html')
            movie_title = soup.find('h1').text.strip().split(' ', 1)[1]
            genre_section = soup.find('div', class_='name', string='Genres').parent
            genres = genre_section.find_all('a', title=True)
            genre_list = [genre['title'].strip() for genre in genres]
            print('Processing movie ' + movie_title + '...' + str(genre_list))
            movies_info['Title'].append(movie_title)
            movies_info['Genres'].append(", ".join(genre_list))
    except Exception as e:
        print(f"Error processing {url}: {e}")
        pass

#---------------A function to organized the data and save into the csv file----------------------------
def main():
    for url in urls:
        get_movie_info(url)
    movies_df = pd.DataFrame(movies_info)
    movies_df = movies_df.dropna()
    
    movies_df.to_csv('movies_info.csv', index_label='id')
    print('==========================================================')
    print('\nMovie information saved to movies_info.csv successfully.')

#---------------A movie picker code to get the user input and make the movie suggesstions---------------
def suggest_movie_by_genre():
    try:
        movies_df = pd.read_csv('movies_info.csv')
        user_genre = input('Enter a genre: ').strip().title()
        genre_filtered = movies_df[movies_df['Genres'].str.contains(user_genre, case=False, na=False)]
        
        if not genre_filtered.empty:
            suggestions = genre_filtered.sample(n=min(2, len(genre_filtered)))['Title'].tolist()
            print(f"Suggested movies for the genre '{user_genre}': {', '.join(suggestions)}")
        else:
            print(f"No movies found for the genre '{user_genre}'.")
 #--------------------------------Rxception Handling----------------------------------------------------           
    except FileNotFoundError:
        print("The file 'movies_info.csv' was not found. Please run the main program first.")
    except Exception as e:
        print(f"An error occurred: {e}")

#-----------------------------Calling the function-------------------------------------------------------
if __name__ == '__main__':
    main()
    suggest_movie_by_genre()
