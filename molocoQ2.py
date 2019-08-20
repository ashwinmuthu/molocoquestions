import csv
import json
import collections

with open('q2data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    user_dict = collections.defaultdict(set)
    quantity_dict = collections.defaultdict(int)

    line_count = 0
    for row in csv_reader:
        parsed_row = json.loads(row[0])

        user_dict[parsed_row["product_id"]].add(parsed_row["user_id"])

        quantity_dict[parsed_row["product_id"]] += parsed_row["quantity"]

        line_count += 1


    # first we figure out (deterministically) what the max num of unique users are
    max_unique_users = 0
    popular_product = []
    for product in user_dict:
        num_users = len(user_dict[product])
        if num_users > max_unique_users:
            max_unique_users = num_users
    # then we see which products have a user_count matching that max
    for product in user_dict:
        num_users = len(user_dict[product])
        if num_users == max_unique_users:
            popular_product.append(product)

    # next we use a similar process for quantities of products
    max_quantity = 0
    popular_product_quantity = []
    for product in quantity_dict:
        if quantity_dict[product] > max_quantity:
            max_quantity = quantity_dict[product]
    for product in quantity_dict:
        if quantity_dict[product] == max_quantity:
            popular_product_quantity.append(product)


    print('Most popular product(s) based on the number of purchasers: ' + str(popular_product))
    print('Most popular product(s) based on the quantity of goods sold: ' + str(popular_product_quantity))