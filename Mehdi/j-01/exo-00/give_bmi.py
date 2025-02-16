import numpy as np
import array

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    ## check if parameters are properly typed
    assert len(height) > 0, "height array must contain at least one element"
    assert len(weight) > 0, "weight array must contain at least one element"

    ## add error templating for errors
    ## check if there is both arrays are same length
    assert len(height) == len(weight), "Arrays(height, weight) must be of the same length"

    ## check for no null values or empty values 0 check proper typs inside list
    assert all(height), "height array must not contain empty values"
    assert all(weight), "weight array must not contain empty values"

    # check if int and float
    assert all(isinstance(i, int) or isinstance(i,float)  for i in height),"contents must be ints or floats"
    assert all(isinstance(i, int) or isinstance(i,float)  for i in weight),"contents must be ints or floats" 


    ## do math weight/height ^2
    np_weight = np.array(weight)
    np_height = np.array(height)

    np_result = np_weight/(np_height ** 2 ) 
    
    return list(np_result) 



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ## this sounds weak need better checking
    assert type(limit) is int, "Limit must be an int"
    assert limit > 0, "Limit must be greater than 0"

    np_bmi = np.array(bmi)

    return  np_bmi > limit 
