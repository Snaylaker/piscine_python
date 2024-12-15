from time import time, strftime, gmtime

current_time = time()
print("type : ", type(current_time))
print("Seconds since January 1, 1970: ", "{:,}".format(current_time), " ", "{:.3e}".format(current_time), " in scientific notation")
print(strftime("%b %d %Y"))