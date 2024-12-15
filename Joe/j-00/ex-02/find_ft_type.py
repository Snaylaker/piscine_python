def all_thing_is_obj(object: any) -> int:
    #print(object)
    current_type = type(object)
    if (current_type.__name__ == "str"):
        print(object, " is in the kitchen : ", end="")
    elif (current_type.__name__ == "int"):
        print("Type not found")
        return 42
    else:
        print(current_type.__name__.capitalize(), " : ", end="")
    print(current_type)
    return 42