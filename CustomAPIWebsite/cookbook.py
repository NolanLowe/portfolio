from recipe import Recipe


class Cookbook:
    def __init__(self):
        self.recipes = []
        self.letter = None

    def add_recipe(self, contents):
        self.recipes.append(Recipe(contents))

    def get(self, recipe_id):
        for page in self.recipes:
            if page.id == recipe_id:
                return page

    def clear(self):
        self.recipes.clear()
