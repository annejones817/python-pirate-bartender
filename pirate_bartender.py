import random 

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

preferences = {}
drink = []

def askQuestions(questions):
    """Ask each question and record the appropriate response in the preferences dictionary"""
    for taste in questions: 
        while True: 
            preference = input("{}\n".format(questions[taste]))
            if (preference.lower() == 'yes' or preference.lower() == 'y'):
                preferences[taste]=True
                break
            elif (preference.lower() == 'no' or preference.lower() == 'n'):
                preferences[taste]=False
                break
            else: 
                print("Please enter yes or no")

def makeDrink(preferences):
    for taste in preferences: 
       # print(preferences[taste])
        if (preferences[taste]) == True: 
            addedIngredient = random.choice(ingredients[taste])
            #print(addedIngredient)
            drink.append(addedIngredient)
            
if __name__ == '__main__':
    askQuestions(questions)            
                
    makeDrink(preferences)        
    
    drinkContents = ', '.join(drink)
    
    if (len(drink)>0):
        print("Your drink includes: {}".format(drinkContents))
    else: 
        print("Sorry, we don't have any ingredients you like.")
    