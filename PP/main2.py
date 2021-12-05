def calculate_norm_avg(low=0, high=1, *list):
    print(f"Input List:{list}")
    print(f"Thresholds:{low, high}")
    norm_list = []
    for i in list:
        norm_value = (i - min(list)) / (max(list) - min(list))
        norm_list.append(norm_value)
    print(f"Normalized List:{norm_list}")
    filtered_list = []
    for index, value in enumerate(norm_list):
        if low <= value <= high:
            filtered_list.append(value)
    print(f"Result output:{filtered_list}")
    sum = 0
    for i in filtered_list:
        sum += i
    mean = round(sum / len(filtered_list), 2)
    print(f"Agv from normalized values:{mean}")


calculate_norm_avg(0.5, 1, 1, 2, 3, 4, 5)