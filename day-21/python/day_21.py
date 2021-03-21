import copy

all_ingrs = []
recipe_list = []
original_recipe_list = []
allergen_dict = {}
safe_ingrs = []

def read_files(input_filename):
    f = open(input_filename, 'r')

    for line in f.readlines():
        line = line.strip()
        if line != "":
            ingredients, allergens = line.split(" (contains ")
            ingredients = ingredients.split(" ")
            allergens = allergens[:-1].split(", ")
            recipe_list.append([ingredients, allergens])
            new_ingrs = [ingr for ingr in ingredients if ingr not in all_ingrs]
            all_ingrs.extend(new_ingrs)

def find_allergens():
    del_idx = []
    allergen_found = False

    for idx, val in enumerate(recipe_list):
        ingredients = val[0]
        allergens = val[1]
        if len(allergens) == 1 and len(ingredients) > 0:
            allergen_found = True
            if len(ingredients) == 1:
                allergen_dict[allergens[0]] = ingredients[0]
                del_idx.append(idx)
                continue
            test_allergen = allergens[0]
            for entry2 in recipe_list:
                ingredients2 = entry2[0]
                allergens2 = entry2[1]
                if ingredients2 != ingredients and test_allergen in allergens2:
                    recipe_list[idx][0] = [ingr for ingr in ingredients if ingr in ingredients2]
                    if len(recipe_list[idx][0]) == 1:
                        allergen_dict[test_allergen] = recipe_list[idx][0][0]
                        if idx not in del_idx: del_idx.append(idx)

    if not allergen_found:
        print(len(recipe_list))
        print(allergen_dict)
        print("No more allergies found")
        exit(3)

    # print('START DELETING')
    for index in sorted(del_idx, reverse=True):
        # print(recipe_list[index])
        del recipe_list[index]
    # print('DONE DELETING')

def ingredients_remaining():
    ingr_count = 0
    for recipe in recipe_list:
        ingr_count += len(recipe[0])
    return ingr_count

def remove_known_allergens():
    del_idx = []
    for rem_allergen in allergen_dict:
        rem_ingr = allergen_dict[rem_allergen]
        for idx, val in enumerate(recipe_list):
            ingredients = val[0]
            allergens = val[1]
            if rem_allergen in allergens or rem_ingr in ingredients:
                recipe_list[idx][0] = [ingr for ingr in ingredients if ingr != allergen_dict[rem_allergen]]
                recipe_list[idx][1] = [aller for aller in allergens if aller != rem_allergen]
                if len(recipe_list[idx][1]) == 0 and idx not in del_idx: del_idx.append(idx)

    for index in sorted(del_idx, reverse=True):
        del recipe_list[index]
    

if __name__=="__main__":
    read_files("../real-input.txt")
    # read_files("../test_input.txt")
    original_recipe_list = copy.deepcopy(recipe_list)
    
    max_runs = 100000
    while len(recipe_list) != 0 and max_runs > 0:
        if max_runs % 1000 == 0: print(f'{len(recipe_list)} recipes left and {ingredients_remaining()} ingredients.')
        # print('-------------')
        start_ingr_count = ingredients_remaining()
        find_allergens()
        remove_known_allergens()
        if start_ingr_count == ingredients_remaining():
            print(recipe_list)
            print(allergen_dict)
            print(f'No more ingredients being solved, {start_ingr_count} remaining in {len(recipe_list)} recipes.')
            exit(3)
        # print(recipe_list)
        # print(allergen_dict)
        max_runs -= 1

    safe_ingrs = [ingr for ingr in all_ingrs if ingr not in allergen_dict.values()]

    # print(allergen_dict)
    # print(safe_ingrs)
    # print(len(recipe_list))

    # print(original_recipe_list)
    safe_counter = []
    for recipe in original_recipe_list:
        for ingr in safe_ingrs:
            safe_counter.append(recipe[0].count(ingr))

    print(f'Safe ingredients occurred {sum(safe_counter)} times.')
    
