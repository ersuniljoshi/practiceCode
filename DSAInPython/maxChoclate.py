def maxChoclate(r, w):
    total_choc = r
    wrapper_choc = r
    while wrapper_choc:
        if wrapper_choc % w == 0:
            total_choc += wrapper_choc // w
            wrapper_choc = wrapper_choc // w
        else:
            total_choc += wrapper_choc // w
            wrapper_choc = wrapper_choc // w + wrapper_choc % w
        if wrapper_choc < 3:
            return total_choc
    return total_choc

rs = 9
print maxChoclate(rs, w=3)
