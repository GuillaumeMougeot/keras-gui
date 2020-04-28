def init():
    #----------------------------------------------------------------------------
    # Data augmentation settings

    global samplewise_center
    # Boolean. Set each sample mean to 0.
    samplewise_center = False

    global samplewise_std_normalization
    # Boolean. Divide each input by its std.
    samplewise_std_normalization = False

    global rotation_range
    # Int. Degree range for random rotations.
    rotation_range = 0

    global width_shift_range
    # Float, 1-D array-like or int
    #     float: fraction of total width, if < 1, or pixels if >= 1.
    #     1-D array-like: random elements from the array.
    #     int: integer number of pixels from interval (-width_shift_range, +width_shift_range)
    #     With width_shift_range=2 possible values are integers [-1, 0, +1], same as with width_shift_range=[-1, 0, +1], while with width_shift_range=1.0 possible values are floats in the interval [-1.0, +1.0).
    width_shift_range = 0. 
    
    global height_shift_range
    # height_shift_range: Float, 1-D array-like or int
    #     float: fraction of total height, if < 1, or pixels if >= 1.
    #     1-D array-like: random elements from the array.
    #     int: integer number of pixels from interval (-height_shift_range, +height_shift_range)
    #     With height_shift_range=2 possible values are integers [-1, 0, +1], same as with height_shift_range=[-1, 0, +1], while with height_shift_range=1.0 possible values are floats in the interval [-1.0, +1.0).
    height_shift_range = 0.

    global zoom_range
    # Float or [lower, upper]. Range for random zoom. If a float, [lower, upper] = [1-zoom_range, 1+zoom_range].
    zoom_range = 0.

    global channel_shift_range
    # Float. Range for random channel shifts.
    channel_shift_range = 0.

    global fill_mode
    # One of {"constant", "nearest", "reflect" or "wrap"}. Default is 'nearest'. Points outside the boundaries of the input are filled according to the given mode:
    #     'constant': kkkkkkkk|abcd|kkkkkkkk (cval=k)
    #     'nearest': aaaaaaaa|abcd|dddddddd
    #     'reflect': abcddcba|abcd|dcbaabcd
    #     'wrap': abcdabcd|abcd|abcdabcd
    fill_mode = 'nearest'

    global horizontal_flip 
    # Boolean. Randomly flip inputs horizontally.
    horizontal_flip = False

    global vertical_flip
    # Boolean. Randomly flip inputs vertically.
    vertical_flip = False

    global validation_split
    # Float. Fraction of images reserved for validation (strictly between 0 and 1).
    validation_split = 0.

