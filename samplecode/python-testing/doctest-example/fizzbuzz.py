def fizzbuzz(number: int) -> str:
    """FizzBuzzゲームを解く関数

    ref: https://pycamp.pycon.jp/textbook/2_intro.html#fizzbuzz

    >>> fizzbuzz(1)
    '1'
    >>> fizzbuzz(3)
    'Fizz'
    >>> fizzbuzz(5)
    'Buzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
