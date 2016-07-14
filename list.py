# Overwriting built-in 'list' by assigning values to a variable called 'list'
car_list = [1, 2, 3]
# Defining a list 'cars', will now raise an error
cars = car_list()
# Error: TypeError: 'list' object is not callable