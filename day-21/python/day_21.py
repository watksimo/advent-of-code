def read_files(input_filename):
    allergen_ingr_dict = {}
    non_unique_ingredients = []
    unique_ingredients = []
    f = open(input_filename, 'r')

    for line in f.readlines():
        line = line.strip()
        if line != "":
            ingredients, allergens = line.split(" (contains ")
            ingredient_list = ingredients.split(" ")
            allergen_list = allergens[:-1].split(", ")
            non_unique_ingredients.extend(ingredient_list)
            unique_ingredients.extend([ingr for ingr in ingredient_list if ingr not in unique_ingredients])
            for allergen in allergen_list:
                if allergen not in allergen_ingr_dict:
                    allergen_ingr_dict[allergen] = [set(ingredient_list)]
                else:
                    allergen_ingr_dict[allergen].append(set(ingredient_list))

    return allergen_ingr_dict, non_unique_ingredients, unique_ingredients
    
def perform_allergen_intersection(allergen_ingr_dict):
    allergen_mapping = {}
    for allergen in allergen_ingr_dict:
        ingr_set_list = allergen_ingr_dict[allergen]
        all_ingr = set.intersection(*ingr_set_list)
        allergen_mapping[allergen] = all_ingr

    return allergen_mapping

def remove_known_allergens(allergen_intersection):
    all_confirmed = True
    allergen_confirmed = {}
    for allergen in allergen_intersection:
        ingredients = allergen_intersection[allergen]
        if len(ingredients) == 1:
            allergen_confirmed[allergen] = list(ingredients)[0]
    
    for allergen in allergen_confirmed:
        ingredient = allergen_confirmed[allergen]
        for allergen2 in allergen_intersection:
            if allergen2 != allergen:
                ingredient_list = allergen_intersection[allergen2]
                allergen_intersection[allergen2] = [ingr for ingr in ingredient_list if ingr != ingredient]
            if len(allergen_intersection[allergen2]) > 1: all_confirmed = False

    return all_confirmed, allergen_confirmed, allergen_intersection


if __name__=="__main__":
    allergen_ingr_dict, non_unique_ingredients, unique_ingredients = read_files("../real-input.txt")
    # allergen_ingr_dict, non_unique_ingredients, unique_ingredients = read_files("../test_input.txt")
    # allergen_ingr_dict, non_unique_ingredients, unique_ingredients = read_files("../test_input2.txt")

    allergen_intersection = perform_allergen_intersection(allergen_ingr_dict)

    all_confirmed = False
    loop_counter = 0
    allergen_confirmed = None
    while not all_confirmed and loop_counter < 10:
        all_confirmed, allergen_confirmed, allergen_intersection = remove_known_allergens(allergen_intersection)
        loop_counter += 1

    safe_ingredients = [ingr for ingr in unique_ingredients if ingr not in list(allergen_confirmed.values())]
    safe_occurrences = sum([1 for ingr in non_unique_ingredients if ingr in safe_ingredients])

    print(f'Part 1 solution is: {safe_occurrences}')

    allergens = list(allergen_confirmed.values())
    allergens.sort()
    part2 = ','.join([elem[1] for elem in sorted(allergen_confirmed.items())])

    print(f'Part 2 solution is: {part2}')