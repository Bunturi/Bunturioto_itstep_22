import json

# Open the JSON file for reading
with open("movies.json", "r", encoding="utf-8") as read_json:
    python_data = json.load(read_json)

# Initialize a list to store updated movie data
new_movies = []

# Iterate over each data entry in the loaded JSON
for data in python_data:
    for movie in data['results']:
        # Check if release year is greater than 2000 and genre is Crime
        if movie['release_date'][:4] > '2000' and 'Crime' in movie['genres']:
            # Update genre to 'New_Crime' if it was 'Crime', otherwise keep the genre unchanged
            movie['genres'] = ['New_Crime' if genre == 'Crime' else genre for genre in movie['genres']]
            new_movies.append(movie)

        # Check if release year is less than 2000 and genre is Drama
        elif movie['release_date'][:4] < '2000' and 'Drama' in movie['genres']:
            # Update genre to 'Old_Drama' if it was 'Drama', otherwise keep the genre unchanged
            movie['genres'] = ['Old_Drama' if genre == 'Drama' else genre for genre in movie['genres']]
            new_movies.append(movie)

        # Check if release year is 2000
        elif movie['release_date'][:4] == '2000':
            movie['genres'] = ['New_Century']  # Set genre to 'New_Century'
            new_movies.append(movie)
        else:
            new_movies.append(movie)  # If none of the conditions are met, add the movie unchanged

# Write the updated movie data back to the JSON file
with open('movies.json', 'w', encoding='utf-8') as file:
    json.dump(python_data, file, indent=4, ensure_ascii=False)
