class Recipe:
    def __init__(self, r_dict):
        self.id = r_dict['idMeal']
        self.name = r_dict['strMeal']
        self.category = r_dict['strTags']
        self.genre = r_dict['strArea']

        self.instructions = r_dict['strInstructions']

        self.thumbnail = r_dict['strMealThumb']
        self.youtube = r_dict['strYoutube']

        self.ingredients = {}

        for i in range(1, 21):
            if r_dict[f"strIngredient{i}"] is None or r_dict[f"strIngredient{i}"] == "":
                break
            else:
                self.ingredients[r_dict[f"strIngredient{i}"]] = r_dict[f"strMeasure{i}"]
