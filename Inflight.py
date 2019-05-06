# Given an int, flight_length, and a list, movie_lengths, as inputs, check() returns True if
# there are exactly two numbers in the list that add up to flight_length; otherwise, returns False
# Note: same number cannot be used twice to add up to the target sum
def check(flight_length, movie_lengths):
	
	dictionary = {}
	dictionary[movie_lengths[0]] = 0

	for i in range(1, len(movie_lengths)):
		second_movie_length = flight_length - movie_lengths[i]
		if second_movie_length in dictionary:
			return True
		else:
			dictionary[movie_lengths[i]] = i 

	return False

# test code
flight_length = 100
movie_lengths = [20, 40, 70, 60, 90]
result = check(flight_length, movie_lengths)
print result
# result = True

movie_lengths = [100, 20, 50, 100]
result = check(flight_length, movie_lengths)
print result
# result = False

movie_lengths = [80, 60, 35, 50, 25, 70]
result = check(flight_length, movie_lengths)
print result
# result = False

movie_lengths = [80, 60, 35, 50, 25, 70, 50]
result = check(flight_length, movie_lengths)
print result
# result = True
