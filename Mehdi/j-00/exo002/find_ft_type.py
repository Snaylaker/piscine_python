def all_thing_is_obj(object: any) -> int:
    object_class = object.__class__
    if object_class.__name__ == "str":
        print(object, "is in the kitchen")
    elif object_class.__name__ == "int":
        print("Type not found")
    else:
        print(object_class.__name__.capitalize(), " :", type(object))
    return 42
