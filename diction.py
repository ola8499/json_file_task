import json
from collections import Counter


def open_file(file):
    try:
        with open(file) as data:
            output = json.load(data)
    except IOError:
        print("Failed to open the file: \"laureate.json\"")
    else:
        return output


# task 1
def create_list(output):
    g = 0
    array = output["laureates"]
    a = [d["id"] for d in array]
    for i in range(len(a)):
        g += 1

    return g


# task 2
def economics_laureates(output):
    ecolaur = []
    array = output["laureates"]
    for i in range(len(array)):
        key = array[i]
        dic = key["prizes"]
        b = [d["category"] for d in dic]
        if b == ["economics"]:
            zmienna = key["surname"]
            ecolaur.append(zmienna)
    ecolaur.sort()
    print("\nAll Laureates in Economics:")
    for i in range(len(ecolaur)):
        print(ecolaur[i])

    return ecolaur


# task 3
def many_awards(output):
    name = []
    value_list = []
    array = output["laureates"]
    for i in range(len(array)):
        key = array[i]
        firstname = key["firstname"]
        try:
            surname = key["surname"]
            name.append(firstname + surname)
        except KeyError:
            name.append(firstname)
    print("\nMore than one prize awarded: ")
    oneprize = dict(Counter(name))
    for person, amount in oneprize.items():
        if amount == 1:
            value_list.append(person)
    for i in value_list:
        del oneprize[i]
    prize = dict(sorted(oneprize.items(), key=lambda item: item[1], reverse=True))
    print(prize)


if __name__ == '__main__':
    new_file = open_file("laureate.json")
    g = create_list(new_file)
    print("\nThe Nobel Prize was awarded", g, "laureates.")
    ecolaur = economics_laureates(new_file)
    many_awards(new_file)
