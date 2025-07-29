def find_outlier(integers):
    count_even, count_odd = 0, 0
    for i in integers:
        if i % 2 == 0:
            count_even += 1 
            even_number = i
        else:
            odd_number = i
            count_odd += 1
    return even_number if count_even == 1 else odd_number

print(find_outlier([-123456789,-18,6,-8,-10,6,12,-24,36]))