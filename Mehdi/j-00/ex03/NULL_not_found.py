def NULL_not_found(object: any) -> int:
    object_class = object.__class__
    if not object:
        match object_class.__name__:
            case 'NoneType':
                print("Nothing:", object, type(object))
            case 'float':
                print("Cheese:", object, type(object))
            case 'int':
                print("Zero:", object, type(object))
            case 'str':
                print("Empty:", object, type(object))
            case 'bool':
                print("Fake:", object, type(object))
    else:
        print("Type not found")
        return 1

    return 0
