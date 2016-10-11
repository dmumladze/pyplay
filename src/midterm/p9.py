def flatten(aList):    
    flat = []
    for itm in aList:    
        if type(itm) == list: 
            flat.extend(flatten(itm))
        else:                      
            flat.append(itm) 
    return flat