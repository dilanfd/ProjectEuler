import numpy as np


def mult_of_3_or_5_upto_N(N):
    """
    Finds the sum of the multiples of 3 or 5 upto N
    Excluding N.

    Procedure:
    ---------
    Examples. The multiples of 3 or 5 upto 10 excluding
    10 are 3, 5, 6, 9. The sum of these values is 23.

    Input:
    -----
    N: Natural number (excluding zero)

    Output:
    -----
    The sum of the multiples of 3 or 5 upto but excluding
    N
    """
    list_of_numbers_to_N = np.arange(1, N, 1)
    mult_of_3_or_5 = [n for n in list_of_numbers_to_N if
                      (n % 3 == 0 or n % 5 == 0)]
    return sum(mult_of_3_or_5)


def main():
    return mult_of_3_or_5_upto_N(1000)


if __name__ == '__main__':
    print(main())
