#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pocket_calculator' function below.
#
class OperatorNotRecognizedError(Exception):
    pass


class NegativeInputError(Exception):
    pass


class NegativeOutputError(Exception):
    pass


class NonIntegerInputError(Exception):
    pass


class OutputTooLargeError(Exception):
    pass


def pocket_calculator(x, operator, y):
    # Write your code here
    result = ''
    try:
        float(x)
        float(y)
        try:
            int(x)
            int(y)
        except ValueError:
            return 'NonIntegerInput'
        # if(x =='0.0' or y =='0.0'):
        #    raise NonIntegerInputError
        # if(float(x)!=float(int(float(x))) or float(y)!=float(int(float(y)))):
        #    raise NonIntegerInputError
        if (int(x) < 0 or int(y) < 0):
            raise NegativeInputError

        if operator == '+':
            result = int(x) + int(y)
        elif operator == '-':
            result = int(x) - int(y)
        elif operator == 'x':
            result = int(x) * int(y)
        elif operator == '/':
            if (int(y) == 0):
                result = 0
            else:
                result = int(x) / int(y)
        else:
            raise OperatorNotRecognizedError
        if result < 0:
            raise NegativeOutputError
        if result > 9999999:
            raise OutputTooLargeError
        result = str(int(result))
    except ValueError:
        return 'InputNotANumber'
    except OperatorNotRecognizedError:
        return 'OperatorNotRecognized'
    except NegativeInputError:
        return 'NegativeInput'
    except NegativeOutputError:
        return 'NegativeOutput'
    except NonIntegerInputError:
        return 'NonIntegerInput'
    except OutputTooLargeError:
        return 'OutputTooLarge'
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = input()

    operator = input()

    y = input()

    result = pocket_calculator(x, operator, y)

    fptr.write(result + '\n')

    fptr.close()
