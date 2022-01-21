import random
from typing import Union


class Food:
    """A food with specific ingredients and a link to its recipe.

    ==Attributes==
    name: The name of the food.
    ingredients: A list of ingredients used to make the food.
    recipe: A link to the recipe of the food.

    ==Representation Invariants==
    -No ingredient in ingredients is repeated more than once.

    ==Sample Usage==
    Creating a food:
    >>> salad = Food('Salad', 'https://www.loveandlemons.com/salad-recipes/')
    >>> salad.ingredients
    []

    Adding ingredients:
    >>> salad.add_ingredients(['lettuce', 'cucumber', 'tomato', 'carrot'])
    >>> salad.ingredients
    ['lettuce', 'cucumber', 'tomato', 'carrot']
    """
    name: str
    ingredients: list[str]
    recipe: str

    def __init__(self, name: str, link: str) -> None:
        """Initialise this food.
        >>> pizza = Food('Pizza',
        ... 'https://www.simplyrecipes.com/recipes/homemade_pizza/')
        >>> pizza.name
        'Pizza'
        >>> pizza.recipe
        'https://www.simplyrecipes.com/recipes/homemade_pizza/'
        >>> pizza.ingredients
        []
        """
        self.name = name
        self.recipe = link
        self.ingredients = []

    def __repr__(self) -> str:
        """Returns the official string representation of a food.
        >>> salad = Food('Salad',
        ... 'https://www.loveandlemons.com/salad-recipes/')
        >>> salad.add_ingredients(['lettuce', 'cucumber', 'tomato', 'carrot'])
        >>> salad
        Salad
        <BLANKLINE>
        Ingredients:
        -lettuce
        -cucumber
        -tomato
        -carrot
        <BLANKLINE>
        Link to recipe: https://www.loveandlemons.com/salad-recipes/
        """
        acc = f'{self.name}\n\nIngredients:\n'
        for ingredient in self.ingredients:
            acc += '-' + ingredient + '\n'
        acc += f'\nLink to recipe: {self.recipe}'
        return acc

    def add_ingredients(self, ingredients: list[str]) -> None:
        """Adds the list of <ingredients> to the food.

        Each ingredient is only added if it is not already already present in
        the ingredients of the food.

        >>> pasta = Food('Pasta',
        ... 'https://www.loveandlemons.com/homemade-pasta-recipe/')
        >>> pasta.add_ingredients(['flour', 'eggs', 'salt'])
        >>> pasta.ingredients
        ['flour', 'eggs', 'salt']
        """
        for ingredient in ingredients:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)


class RecipeBox:
    """A recipe box of different foods.

    ==Attributes==
    recipes: A list of Foods

    ==Sample Usage==
    >>> fridge = RecipeBox()
    >>> fridge.recipes
    []
    >>> pizza = Food('Pizza',
    ... 'https://www.simplyrecipes.com/recipes/homemade_pizza/')
    >>> fridge.add(pizza)
    >>> fridge.recipes
    [Pizza
    <BLANKLINE>
    Ingredients:
    <BLANKLINE>
    Link to recipe: https://www.simplyrecipes.com/recipes/homemade_pizza/]
    """
    recipes: list[Food]

    def __init__(self):
        self.recipes = []

    def add(self, recipe: Food) -> None:
        """Adds recipe to list of recipes.
        """
        self.recipes.append(recipe)

    def get_random(self) -> str:
        """Returns random recipe from list of recipes as a string.
        """
        return str(random.choice(self.recipes))

    def has_ingredients(self, ingredients: list[str]) -> Union[str, list[Food]]:
        """Returns list of all recipes that contain at least one ingredient
        from the input <ingredients>.

        If no recipe contains the input ingredients, "No matches found."
        is returned.
        """
        result = []
        for i in ingredients:
            for recipe in self.recipes:
                if (i.strip().lower() in recipe.ingredients) \
                        and (recipe not in result):
                    result.append(recipe)

        if not result:
            return 'No matches found.'
        return result

    def has_all_ingredients(self, ingredients: list[str]) -> \
            Union[str, list[Food]]:
        """Returns list of all recipes that can be made with only the input
        ingredients.

        If no recipe contains the input ingredients, "No matches found."
        is returned.
        """
        result = []
        for recipe in self.recipes:
            temp = []
            for i in ingredients:
                if i.strip().lower() in recipe.ingredients:
                    temp.append(i.strip().lower().capitalize())
            if len(temp) == len(recipe.ingredients):
                result.append(recipe)

        if not result:
            return 'No matches found.'
        return result
