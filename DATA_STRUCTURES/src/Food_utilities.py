'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = '2024-01-11'
'''

from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """

    # Your code here
    name = input("Name: ")
    print("Origin")
    print(Food.origins())

    origin = -1
    while origin < 0 or origin >= len(Food.ORIGIN):
        origin = int(input(": "))

    is_vegetarian = None
    while is_vegetarian not in (True, False):
        vegetarian = input("Vegetarian (Y/N): ")
        if vegetarian.lower() == "y":
            is_vegetarian = True
        elif vegetarian.lower() == "n":
            is_vegetarian = False

    calories = None
    while calories is None or calories < 0:
        try:
            calories = int(input("Calories: "))
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

    food = Food(name, origin, is_vegetarian, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
          name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """

    # Your code here
    name, origin, is_vegetarian, calories = line.split("|")
    origin = int(origin)
    is_vegetarian = is_vegetarian == "True"
    calories = int(calories)
    food = Food(name, origin, is_vegetarian, calories)

    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """

    # Your code here
    foods = []
    for line in file_variable:
        food = read_food(line)
        foods.append(food)

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    for food in foods:
        food_string = f"{food.name}|{food.origin}|{food.is_vegetarian}|{food.calories}\n"
        file_variable.write(food_string)

    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """

    # Your code here
    veggies = []
    for food in foods:
        if food.is_vegetarian:
            veggies.append(food)

    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    # Your code here
    origins = []
    for i in foods:
        if(i.origin == origin):
            origins.append(i)

    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """

    # Your code here
    total = 0
    for food in foods:
        total += food.calories
    avg = total / len(foods)

    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))

    # Your code here
    total = 0
    count = 0
    for food in foods:
        if food.origin == origin:
            total += food.calories
            count += 1
    avg = total / count

    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here
    foods.sort()

    print("Food                               Origin   Vegetarian Calories")
    print("---------------------------------- -------- ---------- --------")

    for food in foods:
        vegetarian = "True" if food.is_vegetarian else "False"
        print(
            f"{food.name:<35}{food.ORIGIN[food.origin]:<13}{vegetarian:<11}{food.calories:<8}")

    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))

    # Your code here
    result = []
    for food in foods:
        if(origin == -1 or food.origin == origin) and (max_cals == 0 or food.calories <= max_cals) and (not is_veg or food.is_vegetarian):
            result.append(food)

    return result

