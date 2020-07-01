"""You can raise your own exceptions: raise Exception(‘This is the error message.')
You can also use assertions: assert condition, ‘Error message'
Assertions are for detecting programmer errors that are not meant to be recovered from.
 User errors should raise exceptions."""
"""
#raise Exception('This is an error')
***********
*         *
*         *
***********
"""
def boxPrint(symbol, width, height):
    """How to build a box
    input: symbol used in the box, height and width of the box
    width&height>2
    output: print a box"""
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1')
    if width<=2 or height<=2:
        raise Exception('"width" and "height" must be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' '*(width-2))+symbol)
    print(symbol*width)
boxPrint('+', 10, 5)
#boxPrint('+*', 10, 5)


#How to save errors in a file
import traceback
import os
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written in error_log.txt in: '+ os.getcwd())


#Assertions
market_2nd = {'ns':'green', 'ew':'red'}
def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

print(switchLights(market_2nd))
print(market_2nd)
#This will cause error  But we can modify it by:

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red'
print(switchLights(market_2nd))
print(market_2nd)
