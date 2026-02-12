def factorial(n: int) -> int:
    """
    Számolja ki egy nem negatív egész szám faktoriálisát rekurzívan.

    A faktoriális egy szám (*n!*) a következőképpen van definiálva:
        n! = n * (n-1) * ... * 2 * 1
    és 0! = 1.

    Paraméterek:
    ----------
    n : int
        A faktoriális kiszámításához szükséges nem negatív egész szám.

    Visszatérési érték:
    ----------
    int
        A megadott szám faktoriálisa.

    Hibák:
    ----------
    TypeError
        Ha a `n` nem egész szám.
    ValueError
        Ha a `n` negatív szám.

    Példák:
    ----------
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if type(n) != int:
        raise TypeError("A factorial függvény argumentuma csak egész szám lehet!")
    if n < 0:
        raise ValueError("A factorial függvény argumentuma csak nem negatív egész szám lehet!")
    if n < 2:
        return 1
    return n * factorial(n-1)

def fib(n:int) -> int:
    """
    Compute the nth Fibonacci number (1-indexed) using recursion with memoization.

    Parameters
    ----------
    n : int
        Position in the Fibonacci sequence to compute. Must be a positive integer (n >= 1).

    Returns
    -------
    int
        The nth Fibonacci number, where fib(1) == fib(2) == 1.

    Raises
    ------
    TypeError
        If n is not of built-in int type.
    ValueError
        If n is less than or equal to 0.

    Examples
    --------
    >>> fib(1)
    1
    >>> fib(7)
    13
    """
    if type(n) != int:
        raise TypeError
    if n <= 0:
        raise ValueError
    def f(n, memo={}):
        if n in memo.keys():
            return memo[n]
        if n == 1 or n == 2:
            return 1
        memo[n] = f(n-1, memo) + f(n-2, memo)
        return memo[n]
    return f(n)
    