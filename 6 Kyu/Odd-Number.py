def find_it(seq):
    for i in range(min(seq),max(seq)+1):
        if seq.count(i) % 2 != 0:
            odd_num = i 
    return odd_num

print(find_it([0,1,0,1,0]))