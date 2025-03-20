import random

states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", 
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", 
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", 
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", 
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", 
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", 
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", 
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

capitals = [
    "Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", 
    "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", 
    "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", 
    "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", 
    "Boston", "Lansing", "Saint Paul", "Jackson", "Jefferson City", 
    "Helena", "Lincoln", "Carson City", "Concord", "Trenton", 
    "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", 
    "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", 
    "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", 
    "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"
]

geo_dict = dict(zip(states, capitals))
choice = 0


def main():
    """Accepting a capital and checking is this capital in the list"""
    random_state = random.choice(list(geo_dict.keys()))
    print(f'The state is {random_state}!')

    answer_capital = input('The capital is: ')
     
    if answer_capital == geo_dict[random_state]:
        print()
        print(
            f'You are absolutely right! \n'
            f'{answer_capital} is the capital of {random_state}!'
            )
    else:
        print('No, the answer is incorrect')


main()

def get_scores():
    pass
