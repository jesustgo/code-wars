# Este no lo pude hacer entonces es mas como de revision por si llego a necesitar la logica

def longest_consec(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            print(strarr[index])
            
    return result

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 3))