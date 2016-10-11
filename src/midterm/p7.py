def dict_interdiff(d1, d2):
    inter = {}
    for key,val in d1.items():
        if key in d2:            
            inter[key] = f(val, d2[key])

    diff = {}
    for key,val in d1.items():
        if key not in d2:            
            diff[key] = val

    for key,val in d2.items():
        if key not in d1:            
            diff[key] = val          

    return (inter, diff)