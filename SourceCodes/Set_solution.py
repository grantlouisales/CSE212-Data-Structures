def intersection(names1, names2):
    pass

def union(names1, names2):
    pass


def add_names_to_sets(list_of_names1, list_of_names2):
    """
    Purpose: Create two empty sets and 

    """
    facebook_set = set()
    instagram_set = set()

    for i in range(len(list_of_names1)):
        follower = list_of_names1[i]
        facebook_set.add(follower)

    for i in range(len(list_of_names2)):
        follower = list_of_names2[i]
        instagram_set.add(follower)

    return (facebook_set, instagram_set)

def remove_name_from_sets(value, union_set):
    pass


facebook_followers = ["Grant Ales", "Jeremy Williams", "Breanna Ales", "Hudson Ales", "Hunter Stratton", "Dawson Stratton", "Jonathon Tanner", "Wyatt Ogden", "Amber Ales", "Lauren Ales", "Spencer Ales"]
instagram_followers = ["Grant Ales", "Hudson Ales", "Dakota Acker", "Joe Acker", "Theo Acker", "Cam Steele", "Nick Cade", "John Crespo", "Braeden Eberle", "Amber Ales", "Lauren Ales", "Spencer Ales"]

# Result: Since sets are unordered they will show a different result everytime. Make sure the corresponding sets contains the correct followers.
social_media_sets = add_names_to_sets(facebook_followers, instagram_followers) 

print(intersection(social_media_sets[0], social_media_sets[1])) # Result:

total_followers = union(social_media_sets[0], social_media_sets[1])
print(total_followers) # Result: 

print("Grant Ales has been mean to other customers on our social media platforms. Please remove him from all platforms.")
name = input("Please enter the name of who you want to ban from the social media> ") 
print(remove_name_from_sets(name, total_followers))
