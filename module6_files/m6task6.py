"""
There is a file with recipes in following format:

60b90c1c13067a15887e1ae1,Herbed Baked Salmon,4 lemons,1 large red onion,2 tablespoons chopped fresh basil
60b90c2413067a15887e1ae2,Lemon Pancakes,2 tablespoons baking powder,1 cup vanilla-flavored almond milk,1 lemon
60b90c2e13067a15887e1ae3,Chicken and Cold Noodles,6 ounces dry Chinese noodles,1 tablespoon sesame oil,3 tablespoons soy sauce
60b90c3b13067a15887e1ae4,Watermelon Cucumber Salad,1 large seedless watermelon,12 leaves fresh mint,1 cup crumbled feta cheese
60b90c4613067a15887e1ae5,State Fair Lemonade,6 lemons,1 cups white sugar,5 cups cold water

Implement a function get_recipe(path, search_id) that will return dictionary for the recipe with specified MongoDB identifyer

path - path to the file
search_id MongoDB key for the seach of recipe


Recuirements:
- Use context manager with
- If the recipe with the key specified is absent function should return None

For example: get_recipe("./data/ingredients.csv", "60b90c3b13067a15887e1ae4")

should return: 

{
    "id": "60b90c3b13067a15887e1ae4",
    "name": "Watermelon Cucumber Salad",
    "ingredients": [
        "1 large seedless watermelon",
        "12 leaves fresh mint",
        "1 cup crumbled feta cheese",
    ],
}

"""

def get_recipe(path, search_id):
    res = None
    with open(path, 'r') as file:
        for record in file:
            rec_lst = record.split(',')
            if rec_lst[0]  == search_id:
                last_el = len(rec_lst) - 1
                rec_lst[last_el] = rec_lst[last_el].rstrip('\n')

                res = {"id" : rec_lst[0], "name" : rec_lst[1], "ingredients" : rec_lst[2 : last_el+1] }
    return res


print(get_recipe("./module6_files/task6txt/recipe.txt", "60b90c3b13067a15887e1ae4"))