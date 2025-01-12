# If function is none remove falsy elements
def ft_filter(function, iterable):

    try:
        if function != None:
            return [item for item in iterable if function(item)]
        else:
            return [item for item in iterable if item]
        
    except Exception as err:
       # print(f"Unexpected {err=}, {type(err)=}")
        raise
    #     iter(iterable)
    # except:
    #     print(f"Value error: {type(iterable)} is not iterable")

# def is_odd(num):
#     if num % 2:
#         return False
#     return True

# nums = [0,1,2,3,4]

# test = ft_filter(is_odd, nums)
# test2 = filter(is_odd, nums)
# # #print(filter.__doc__)
# print(test)
# print(test2)
