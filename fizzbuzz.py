def fizzbuzz(intList):
    '''
    Your fizzbuzz function. The grader will run `fizzbuzz(intList)` to check if your
    function returns the correct output.

    intList: list containing integers

    Make sure you write the script so that your algorithm is part of the
    function; you do not need to call the function yourself.
    '''
    data = []
    for each in intList:
        if each % 3 == 0 and each % 5 == 0:
            data.append('FizzBuzz')
        elif each % 3 == 0 and not each % 5 == 0:
            data.append('Fizz')
        elif not each % 3 == 0 and each % 5 == 0:
            data.append('Buzz')
        else:
            data.append(each)
    return data
