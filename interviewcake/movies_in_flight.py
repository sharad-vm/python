# Write a function that takes an integer flight_length (in minutes) and a list of integers 
# movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers 
# in movie_lengths whose sum equals flight_length.

def two_movies_in_flight(movie_lengths, flight_time):
    watched_movie_lengths = set()
    
    for first_movie in movie_lengths:
        second_movie = flight_time - first_movie
        if second_movie in watched_movie_lengths:
            return True
        
        watched_movie_lengths.add(first_movie)
    return False

# run your function through some test cases here
# remember: debugging is half the battle!

movie_lengths = [60, 89, 92, 120, 130, 54, 160]

print two_movies_in_flight(movie_lengths, 180)
print two_movies_in_flight(movie_lengths, 240)
print two_movies_in_flight(movie_lengths, 380)

# Bonus
# What if we wanted the movie lengths to sum to something close to
# the flight length (say, within 20 minutes)?

def two_movies_in_flight(movie_lengths, flight_time):
    watched_movie_lengths = set()
    flight_time = flight_time - 20
    
    for first_movie in movie_lengths:
        second_movie = flight_time - first_movie
        if second_movie in watched_movie_lengths:
            return True
        
        watched_movie_lengths.add(first_movie)
    return False

# run your function through some test cases here
# remember: debugging is half the battle!

movie_lengths = [60, 89, 92, 120, 130, 54, 160]

print two_movies_in_flight(movie_lengths, 180)
print two_movies_in_flight(movie_lengths, 240)
print two_movies_in_flight(movie_lengths, 380)
