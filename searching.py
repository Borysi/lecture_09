import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode= "r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]


def linear_search(numbers_sekvention, looking_number):
    slovnik = {"positions of number": [], "appears of number": 0}

    index = 0
    for number in numbers_sekvention:

        if number == looking_number:

            slovnik["positions of number"].append(index)
            slovnik["appears of number"] += 1

        index += 1

    return slovnik





def main():
    sequantial_data = read_data("sequential.json", "unordered_numbers")
    print(sequantial_data)
    analysa = linear_search(sequantial_data,9)
    print(analysa)
if __name__ == '__main__':
    main()