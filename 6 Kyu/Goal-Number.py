def two_sum(numbers, target):
    for index_i, i in enumerate(numbers):
        for index_a, a in enumerate(numbers):
            if i + a == target and index_i != index_a:
                result = (index_i, index_a)
                return result
            
print(two_sum([2,2,3], 4))