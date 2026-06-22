def bg_lum(tuple_hex_set):
    rgb = tuple_hex_set[0]  # get tuple of RGB values
    luminance = (rgb[0] + rgb[1] + rgb[2])/(3*255) # calculate luminance, normalize to 0-1
    if luminance < 0.47:    # threshold for dark bgs
        return True
    return False