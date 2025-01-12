def ft_filter(fn_filter, input_arr):
    ''' Return an iterator yielding those items of iterable for which function(item)\nis true. If function is None, return the items that are true.'''

    if fn_filter is None:
        return [input for input in input_arr if input]

    return [input for input in input_arr if fn_filter(input)]
