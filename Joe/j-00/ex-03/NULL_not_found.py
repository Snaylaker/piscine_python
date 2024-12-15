def NULL_not_found(object: any) -> int:

    def error_function() -> int:
        print("Type not Found")
        return 1

    def print_answer(str):
        print(str, " ", object, " ", object_type)

    object_type = type(object)
    match object_type.__name__:
        case "NoneType" :
            print_answer("Nothing:")
        case "float":
            if object != object:
                print_answer("Cheese:")
            else:
                return error_function()
        case "int":
            if object == 0:
                print_answer("Zero:")
            else:
                return error_function()
        case "str":
            if object == "":
                print_answer("Empty:")
            else:
                return error_function()
        case "bool":
            if object == False:
                print_answer("Fake:")
            else:
                return error_function()
        case _:
            return error_function()
    return 0