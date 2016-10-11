def closest_power(base, num):
    hi = 1
    lo = 0
    while True:
        result_hi = base**hi 
        result_lo = base**lo
        
        if result_hi >= num and result_lo <= num:
            diff_hi = abs(num - result_hi)
            diff_lo = abs(num - result_lo)
            if diff_hi >= diff_lo:
                return lo
            else:
                return hi

        hi += 1
        lo += 1