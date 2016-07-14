# ZeroDivision error 'swallowed' by pass statement
result = None
try:
    result = 10 / 0
except:
    ZeroDivisionError:
        print "Type error: division by 0."
		result = 0