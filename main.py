def get_best_operator(number, operators):
    best_operator = None
    best_price = float('inf')
    best_prefix = None
    max_prefix_len = 0

    for operator in operators:
        prefix = number
        while len(prefix) > 0:
            price = operator.get(prefix)
            if price is not None:
                if len(prefix) > max_prefix_len or (len(prefix) == max_prefix_len and price < best_price):
                    best_price = price
                    best_operator = operator
                    best_prefix = prefix
                    max_prefix_len = len(prefix)
            prefix = prefix[:-1]

    return (best_operator, best_price, best_prefix)

operators = [
    {'1': 0.9, '268': 5.1, '46': 0.17, '4620': 0.0, '468': 0.15, '4631': 0.15, '4673': 0.9, '46732': 1.1},
    {'1': 0.92, '44': 0.5, '46': 0.2, '467': 1.0, '48': 1.2}
]

number = input("Enter the number : ")
best_operator, best_price, best_prefix = get_best_operator(number, operators)
if best_operator is not None:
    print(f"The cheapest operator for {number} with a price of {best_price} for prefix {best_prefix}")
else:
    print("No operator found for {}".format(number))
