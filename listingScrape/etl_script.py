import json
import pandas as pd
import sys


def get_average_price():
    total = 0.00
    number_obj = len(json_list)

    for obj in json_list:
        try:
            total += float(obj["price"][1::].replace(",", ""))
        except:
            # print(f"Non float price value: {obj}")
            number_obj -= 1

    average_price = format(total / number_obj, ".2f")
    print(f"Average price: ${average_price}")
    return average_price


def get_max_price():
    max_price = 0.00
    for obj in json_list:
        try:
            current_price = float(obj["price"][1::].replace(",", ""))
            max_price = current_price if current_price > max_price else max_price
        except:
            pass
            # print(f"Non integer price value: {obj}")

    print(f"Max price: ${format(max_price, '.2f')}")
    return max_price


def get_min_price():
    min_price = float(json_list[0]["price"][1::].replace(",", ""))
    for obj in json_list:
        try:
            current_price = float(obj["price"][1::].replace(",", ""))
            min_price = current_price if current_price < min_price else min_price
        except:
            pass
            # print(f"Non integer price value: {obj}")

    print(f"Min price: ${format(min_price, '.2f')}")
    return min_price


def get_count_by_type():
    type_dict = {}

    for obj in json_list:
        if obj["type"] not in type_dict:
            type_dict[obj["type"]] = 1
        else:
            type_dict[obj["type"]] += 1

    for entry in type_dict:
        print(f"{entry}: {type_dict[entry]}")

    return type_dict


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Incorrect usage")
    else:
        input_file = sys.argv[1]
        with open(input_file, "r") as json_file:
            json_data = json_file.read()

        json_list = json.loads(json_data)

        # get_max_price()
        # get_min_price()
        # get_average_price()
        get_count_by_type()
