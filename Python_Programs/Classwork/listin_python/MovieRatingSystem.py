# Movie Rating System

ratings = list(map(int, input("Enter ratings (1-5) separated by space: ").split()))

# Remove invalid ratings
valid_ratings = [r for r in ratings if 1 <= r <= 5]

if valid_ratings:
    average = sum(valid_ratings) / len(valid_ratings)
    five_star = valid_ratings.count(5)
    valid_ratings.sort()

    print("Valid Ratings:", valid_ratings)
    print("Average Rating:", round(average, 2))
    print("Number of 5-Star Ratings:", five_star)
else:
    print("No valid ratings.")
    
    #output
    """ Enter ratings (1-5) separated by space: 4
Valid Ratings: [4]
Average Rating: 4.0
Number of 5-Star Ratings: 0"""