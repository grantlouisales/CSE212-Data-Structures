def intersection(names1, names2):
    """
    Purpose: Use intersection to make a new set.
    Return: New intersected set.
    """
    return names1 & names2

def union(names1, names2):
    """
    Purpose: union to make a new set.
    Return: New unioned set.
    """
    return names1 | names2

def add_names_to_sets(list_of_names1, list_of_names2):
    """
    Purpose: Add all of the names from 
    list 1 into the facebook set and then add
    all of the names from list 2 into the 
    instagram set.

    Return: return a tuple containing both update
    sets.
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
    """
    Purpose: Remove follower from list. 
    Return: The updated set.
    """
    union_set.remove(value)
    return union_set


facebook_followers = ["Grant Ales", "Jeremy Williams", "Breanna Ales", "Hudson Ales", "Hunter Stratton", "Dawson Stratton", "Jonathon Tanner", "Wyatt Ogden", "Amber Ales", "Lauren Ales", "Spencer Ales"]
instagram_followers = ["Grant Ales", "Hudson Ales", "Dakota Acker", "Joe Acker", "Theo Acker", "Cam Steele", "Nick Cade", "John Crespo", "Braeden Eberle", "Amber Ales", "Lauren Ales", "Spencer Ales"]

print("=================== Test 1 ===================")
print()
# Result: Since sets are unordered they will show a different result everytime. Make sure the corresponding sets contains the correct followers.
social_media_sets = add_names_to_sets(facebook_followers, instagram_followers) 

print(intersection(social_media_sets[0], social_media_sets[1])) # Result: Contain names 'Amber Ales', 'Spencer Ales', 'Lauren Ales', 'Grant Ales', 'Hudson Ales'
print()

total_followers = union(social_media_sets[0], social_media_sets[1])
print(total_followers)  # Result: 'Breanna Ales', 'Lauren Ales', 'Jonathon Tanner', 'Grant Ales', 'John Crespo', 'Wyatt Ogden', 'Hunter Stratton', 'Amber Ales', 'Spencer Ales',
                        # 'Cam Steele', 'Nick Cade', 'Dakota Acker', 'Joe Acker', 'Dawson Stratton', 'Braeden Eberle', 'Hudson Ales', 'Jeremy Williams', 'Theo Acker'


print("\n Grant Ales has been mean to other customers on our social media platforms. Please remove him from all platforms.")
name = input("Please enter the name of who you want to ban from the social media> ") 
print(remove_name_from_sets(name, total_followers)) # Result: Contain names: 'Breanna Ales', 'Lauren Ales', 'Jonathon Tanner', 'Grant Ales', 'John Crespo', 'Wyatt Ogden', 'Hunter Stratton',
                                                    # 'Amber Ales', 'Spencer Ales', 'Cam Steele', 'Nick Cade', 'Dakota Acker', 'Joe Acker', 'Dawson Stratton', 'Braeden Eberle', 'Hudson Ales', 
                                                    # 'Jeremy Williams', 'Theo Acker'
