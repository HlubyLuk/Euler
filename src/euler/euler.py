# coding: UTF-8

'''
Created on Nov 3, 2018

@author: HlubyLuk
'''
from abc import ABCMeta
from abc import abstractmethod
from functools import reduce
from math import pow
from math import sqrt


class Problem(object):
    __metaclass__ = ABCMeta

    class CoinsChangeSolver(object):
        '''
        Help solve how many combinations should change target value.
        :see
        https://hackernoon.com/the-coin-change-problem-explained-ddd035a8f22f
        '''

        def __init__(self, values, target):
            '''
            Constructor.
            :values `list` of coins.
            :target price.
            '''
            self.v = values
            self.c = target

        def solve(self):
            '''
            Solve count of combinations.
            :return count of combinations target value.
            '''
            table = [[0 for _ in range(0, len(self.v))]
                     for _ in range(0, self.c + 1)]

            for i in range(0, len(self.v)):
                table[0][i] = 1

            for i in range(1, self.c + 1):
                for j in range(len(self.v)):
                    x = table[i - self.v[j]][j] if i - self.v[j] >= 0 else 0
                    y = table[i][j - 1]if j >= 1 else 0

                    table[i][j] = x + y

            return table[-1][-1]

    class Permutation(object):

        def __init__(self):
            pass

        def _reverse(self, value, start, end):
            while start < end:
                self._swap(value, start, end)

                start += 1
                end -= 1

        def _swap(self, value, k, l):
            tmp = value[k]
            value[k] = value[l]
            value[l] = tmp

        def next_lexigonal_permutation(self, current):
            pivot_k = len(current) - 2
            while pivot_k >= 0 and current[pivot_k] >= current[pivot_k + 1]:
                pivot_k -= 1

            if pivot_k == -1:
                return False

            pivot_l = len(current) - 1
            while current[pivot_k] >= current[pivot_l]:
                pivot_l -= 1

            self._swap(current, pivot_k, pivot_l)
            self._reverse(current, pivot_k + 1, len(current) - 1)

            return True

    @abstractmethod
    def solve(self):
        '''
        Problem solve method.
        '''
        raise NotImplementedError('subclasses must override solve() method!')

    def lcm(self, r=[]):
        '''
        Least common multiple.
        :r `range` for analyze.
        :return `int` of least common multiple.
        '''
        cache = dict()

        for item in r:
            for k, v in self.prime_factors(item).items():
                tmp = cache.get(k, 0)
                if tmp < v:
                    cache.update({k: tmp + v - tmp})

        return reduce(lambda a, b: a * b,
                      map(lambda x: pow(x[0], x[1]), cache.items()))

    def prime_factors(self, x):
        '''
        Prime factors of number.
        :return `dict` where key is number, value is how many times.
        '''
        cache = dict()
        number = x
        factor = 2

        while number > 1:
            while number % factor == 0:
                number /= factor
                tmp = cache.get(factor, 0)
                cache.update({factor: tmp + 1})

            factor += 1

        return cache

    def is_palindromic(self, number):
        '''
        Is number same from start to end and end to start.
        :return `True` is same, otherwise `False`
        '''
        return str(number) == str(number)[::-1]

    def is_prime(self, i=1):
        '''
        Analyze is number prime.
        :i `int` to analyze.
        :return `True` is prime, otherwise `False`.
        '''
        # return len([x for x in range(2, int(math.sqrt(i) + 1)) if i % x ==
        # 0]) == 0

        x = 2

        while x * x <= i:
            if (i % x == 0):
                return False

            x += 1

        return True

    def eratosthenes_sief(self, number):
        '''
        In mathematics, the sieve of Eratosthenes is a simple, ancient
        algorithm for finding all prime numbers up to any given limit.
        It does so by iteratively marking as composite the multiples of
        each prime.
        :number top limit
        :return `dict` of booleans, where `True` is not prime, `False` is
        prime.
        '''
        sieve = [False] * (number + 1)
        sieve[0], sieve[1] = True, True

        for item in range(2, int(sqrt(number)) + 1):
            if sieve[item]:
                continue

            step = item * 2
            while step <= number:
                sieve[step] = True
                step += item

        return sieve

    def factorial(self, number=1):
        """
        Return factorial value.
        :number input value.
        :return factorial value of input.
        """
        return 1 if number == 1 else number * self.factorial(number - 1)

    def combination_number(self, n, k):
        '''
        Selection of items from a collection, such that (unlike permutations)
        the order of selection does not matter.
        :see https://en.wikipedia.org/wiki/Combination
        :n things.
        :k at a time without repetition.
        :return count of combinations.
        '''
        return int(
            self.factorial(n) / (self.factorial(k) * self.factorial(n - k)))

    def divisors(self, x):
        '''
        Create collection of divisors.
        :x number which divisors you want known.
        :return collection of divisors.
        '''
        return [y for y in range(1, int(x / 2) + 1) if x % y == 0]

    def is_amicable_number(self, x):
        '''
        Amicable numbers are two different numbers so related that the
        sum of the proper divisors of each is equal to the other number
        :x
        :return `True` is amicable, otherwise `False`
        '''
        a = sum(self.divisors(x))
        b = sum(self.divisors(a))
        return x == b and a != b

    def is_abundant(self, x):
        '''
        Proper divisors is bigger than number.
        :x number to solve.
        :return `True` is abundant, otherwise `False`.
        '''
        return x < sum(self.divisors(x))

    def next_fibonacci(self, second_last, last):
        '''
        Next item in fibonacci sequence.
        :second_last last last element of sequence.
        :last last element of sequence.
        :return `pair` new second last and last item in sequence.
        '''
        return last, second_last + last

    def gcd(self, a, b):
        '''
        What is greater common divider.
        :a first input.
        :b second input.
        :return greater common divider.
        '''
        return a if b == 0 else self.gcd(b, a % b)

    def factorial_lambda(self, x):
        '''
        Compute factorial without used recursion.
        :number input value.
        :return factorial value of x
        '''
        return reduce(lambda y, z: y * z, range(x, 1, -1)) if x > 1 else 1

    def is_pandigital(self, what):
        '''
        Input contain all digits from 1 to 9.
        :what input number
        :return `True` contains all digits, otherwise `False`.
        '''
        tmp = reduce(lambda x, y:"{}{}".format(x, y), sorted(str(what)))
        return "123456789" == tmp


class Problem1(Problem):
    '''
    Multiples of 3 and 5
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    '''

    def solve(self):
        return sum([x for x in range(1, 1000, 1) if x % 3 == 0 or x % 5 == 0])


class Problem2(Problem):
    '''
    Even Fibonacci numbers
    Problem 2
    Each new term in the Fibonacci sequence is generated by adding the previous
    two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
    '''

    def solve(self):
        fibonacci = [1, 2]

        while True:
            index = len(fibonacci)
            x = fibonacci[index - 2] + fibonacci[index - 1]
            fibonacci.append(x)

            if x >= 4000000:
                break

        return sum(filter(lambda x: x % 2 == 0, fibonacci))


class Problem3(Problem):
    '''
    Largest prime factor
    Problem 3
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    '''

    def solve(self):
        return sorted(self.prime_factors(600851475143).keys())[-1]


class Problem4(Problem):
    '''
    Largest palindrome product
    Problem 4
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    '''

    def solve(self):
        r = range(999, 99, -1)

        return max([x * y for x in r for y in r if self.is_palindromic(x * y)])


class Problem5(Problem):
    '''
    Smallest multiple
    Problem 5
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
    '''

    def solve(self):
        return self.lcm([x for x in range(1, 21, 1)])


class Problem6(Problem):
    '''
    Sum square difference
    Problem 6
    The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
    '''

    def solve(self):
        seq = [x for x in range(1, 101, 1)]

        return pow(sum(seq), 2) - sum(map(lambda x: pow(x, 2), seq))


class Problem7(Problem):
    '''
    10001st prime
    Problem 7
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?
    '''

    def solve(self):
        counter = 0
        number = 2

        while True:
            if self.is_prime(number):
                counter += 1

            if counter == 10001:
                break

            number += 1

        return number


class Problem8(Problem):
    '''
    Largest product in a series
    Problem 8
    The four adjacent digits in the 1000-digit number that have the greatest
    product are 9 × 9 × 8 × 9 = 5832.

    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450

    Find the thirteen adjacent digits in the 1000-digit number that have the
    greatest product. What is the value of this product?
    '''

    def __init__(self):
        self.number_txt = "".join([
            "73167176531330624919225119674426574742355349194934",
            "96983520312774506326239578318016984801869478851843",
            "85861560789112949495459501737958331952853208805511",
            "12540698747158523863050715693290963295227443043557",
            "66896648950445244523161731856403098711121722383113",
            "62229893423380308135336276614282806444486645238749",
            "30358907296290491560440772390713810515859307960866",
            "70172427121883998797908792274921901699720888093776",
            "65727333001053367881220235421809751254540594752243",
            "52584907711670556013604839586446706324415722155397",
            "53697817977846174064955149290862569321978468622482",
            "83972241375657056057490261407972968652414535100474",
            "82166370484403199890008895243450658541227588666881",
            "16427171479924442928230863465674813919123162824586",
            "17866458359124566529476545682848912883142607690042",
            "24219022671055626321111109370544217506941658960408",
            "07198403850962455444362981230987879927244284909188",
            "84580156166097919133875499200524063689912560717606",
            "05886116467109405077541002256983155200055935729725",
            "71636269561882670428252483600823257530420752963450"])

    def solve(self):
        m = (lambda x: int(x))
        r = (lambda y, z: y * z)

        return max([reduce(r, map(m, self.number_txt[x:x + 13:1]))
                    for x in range(0, len(self.number_txt) - 13 + 1, 1)])


class Problem9(Problem):
    '''
    Special Pythagorean triplet
    Problem 9
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for
    which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    '''

    def __init__(self):
        self.x = 1000

    def solve(self):
        c = (lambda a, b: self.x - a - b)

        resuts = [{a, b, c(a, b)}
                  for a in range(1, int(self.x / 2))
                  for b in range(1, int(self.x / 3))
                  if a ** 2 + b ** 2 == (c(a, b)) ** 2]

        return list(map(lambda x: reduce(lambda y, z: y * z, x), resuts))[0]


class Problem10(Problem):
    '''
    Summation of primes
    Problem 10
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    '''

    def solve(self):
        # return sum([x for x in range(2, 2000000) if self.is_prime(x)])

        limit = 2000000
        f = (lambda x: x[1] is False)
        m = (lambda x: x[0])

        sieve = self.eratosthenes_sief(limit)
        indexs = [x for x in range(0, limit + 1)]

        return sum(map(m, filter(f, zip(indexs, sieve))))


class Problem11(Problem):
    '''
    Largest product in a grid
    Problem 11
    In the 20×20 grid below, four numbers along a diagonal line
    have been marked in red.

    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the same
    direction (up, down, left, right, or diagonally) in the 20×20 grid?
    '''

    def __init__(self):
        self.matrix = list(map(lambda x: int(x), " ".join([
            "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08",
            "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00",
            "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65",
            "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91",
            "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80",
            "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50",
            "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70",
            "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21",
            "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72",
            "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95",
            "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92",
            "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57",
            "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58",
            "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40",
            "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66",
            "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69",
            "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36",
            "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16",
            "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54",
            "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48",
        ]).split(" ")))

    def solve(self):
        rows = [self.matrix[x * 20 + y:x * 20 + y + 4]
                for x in range(0, 20)
                for y in range(0, 16)]

        columns = [self.matrix[x:x + 4 * 20:20]
                   for x in range(0, len(self.matrix) - 4 * 20)]

        main_diagonal = [self.matrix[x + 20 * y:x + 4 * 21 + y * 20:21]
                         for x in range(0, 17)
                         for y in range(0, 17)]

        other_diagonal = [self.matrix[x * 20 + y:x * 20 + y + 4 * 19:19]
                          for x in range(0, 17)
                          for y in range(3, 20)]

        product = (lambda a, b: a * b)
        mapper = (lambda x: reduce(product, x))

        return max(
            map(mapper, rows + columns + main_diagonal + other_diagonal))


class Problem12(Problem):
    '''
    Highly divisible triangular number
    Problem 12
    The sequence of triangle numbers is generated by adding
    the natural numbers. So the 7th triangle number would
    be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over
    five divisors.

    What is the value of the first triangle number to have over
    five hundred divisors?
    '''

    def solve(self):
        counter, triangle = 1, self.triangle_number(1)
        divisors = []

        while True:
            divisors = [x for x in range(1, int(sqrt(triangle)) + 1)
                        if triangle % x == 0]

            count = len(divisors) * 2

            if count > 500:
                break
            else:
                counter += 1
                triangle = self.triangle_number(counter)

        return triangle

    def triangle_number(self, i):
        '''
        Compute triangle number.
        :i input number.
        :return triangle number from input.
        '''
        return int((i * (i + 1)) / 2)


class Problem13(Problem):
    '''
    Large sum
    Problem 13
    Work out the first ten digits of the sum of the following
    one-hundred 50-digit numbers.

    37107287533902102798797998220837590246510135740250
    46376937677490009712648124896970078050417018260538
    74324986199524741059474233309513058123726617309629
    91942213363574161572522430563301811072406154908250
    23067588207539346171171980310421047513778063246676
    89261670696623633820136378418383684178734361726757
    28112879812849979408065481931592621691275889832738
    44274228917432520321923589422876796487670272189318
    47451445736001306439091167216856844588711603153276
    70386486105843025439939619828917593665686757934951
    62176457141856560629502157223196586755079324193331
    64906352462741904929101432445813822663347944758178
    92575867718337217661963751590579239728245598838407
    58203565325359399008402633568948830189458628227828
    80181199384826282014278194139940567587151170094390
    35398664372827112653829987240784473053190104293586
    86515506006295864861532075273371959191420517255829
    71693888707715466499115593487603532921714970056938
    54370070576826684624621495650076471787294438377604
    53282654108756828443191190634694037855217779295145
    36123272525000296071075082563815656710885258350721
    45876576172410976447339110607218265236877223636045
    17423706905851860660448207621209813287860733969412
    81142660418086830619328460811191061556940512689692
    51934325451728388641918047049293215058642563049483
    62467221648435076201727918039944693004732956340691
    15732444386908125794514089057706229429197107928209
    55037687525678773091862540744969844508330393682126
    18336384825330154686196124348767681297534375946515
    80386287592878490201521685554828717201219257766954
    78182833757993103614740356856449095527097864797581
    16726320100436897842553539920931837441497806860984
    48403098129077791799088218795327364475675590848030
    87086987551392711854517078544161852424320693150332
    59959406895756536782107074926966537676326235447210
    69793950679652694742597709739166693763042633987085
    41052684708299085211399427365734116182760315001271
    65378607361501080857009149939512557028198746004375
    35829035317434717326932123578154982629742552737307
    94953759765105305946966067683156574377167401875275
    88902802571733229619176668713819931811048770190271
    25267680276078003013678680992525463401061632866526
    36270218540497705585629946580636237993140746255962
    24074486908231174977792365466257246923322810917141
    91430288197103288597806669760892938638285025333403
    34413065578016127815921815005561868836468420090470
    23053081172816430487623791969842487255036638784583
    11487696932154902810424020138335124462181441773470
    63783299490636259666498587618221225225512486764533
    67720186971698544312419572409913959008952310058822
    95548255300263520781532296796249481641953868218774
    76085327132285723110424803456124867697064507995236
    37774242535411291684276865538926205024910326572967
    23701913275725675285653248258265463092207058596522
    29798860272258331913126375147341994889534765745501
    18495701454879288984856827726077713721403798879715
    38298203783031473527721580348144513491373226651381
    34829543829199918180278916522431027392251122869539
    40957953066405232632538044100059654939159879593635
    29746152185502371307642255121183693803580388584903
    41698116222072977186158236678424689157993532961922
    62467957194401269043877107275048102390895523597457
    23189706772547915061505504953922979530901129967519
    86188088225875314529584099251203829009407770775672
    11306739708304724483816533873502340845647058077308
    82959174767140363198008187129011875491310547126581
    97623331044818386269515456334926366572897563400500
    42846280183517070527831839425882145521227251250327
    55121603546981200581762165212827652751691296897789
    32238195734329339946437501907836945765883352399886
    75506164965184775180738168837861091527357929701337
    62177842752192623401942399639168044983993173312731
    32924185707147349566916674687634660915035914677504
    99518671430235219628894890102423325116913619626622
    73267460800591547471830798392868535206946944540724
    76841822524674417161514036427982273348055556214818
    97142617910342598647204516893989422179826088076852
    87783646182799346313767754307809363333018982642090
    10848802521674670883215120185883543223812876952786
    71329612474782464538636993009049310363619763878039
    62184073572399794223406235393808339651327408011116
    66627891981488087797941876876144230030984490851411
    60661826293682836764744779239180335110989069790714
    85786944089552990653640447425576083659976645795096
    66024396409905389607120198219976047599490197230297
    64913982680032973156037120041377903785566085089252
    16730939319872750275468906903707539413042652315011
    94809377245048795150954100921645863754710598436791
    78639167021187492431995700641917969777599028300699
    15368713711936614952811305876380278410754449733078
    40789923115535562561142322423255033685442488917353
    44889911501440648020369068063960672322193204149535
    41503128880339536053299340368006977710650566631954
    81234880673210146739058568557934581403627822703280
    82616570773948327592232845941706525094512325230608
    22918802058777319719839450180888072429661980811197
    77158542502016545090413245809786882778948721859617
    72107838435069186155435662884062257473692284509516
    20849603980134001723930671666823555245252804609722
    53503534226472524250874054075591789781264330331690
    '''

    def __init__(self):
        self.arr = [
            37107287533902102798797998220837590246510135740250,
            46376937677490009712648124896970078050417018260538,
            74324986199524741059474233309513058123726617309629,
            91942213363574161572522430563301811072406154908250,
            23067588207539346171171980310421047513778063246676,
            89261670696623633820136378418383684178734361726757,
            28112879812849979408065481931592621691275889832738,
            44274228917432520321923589422876796487670272189318,
            47451445736001306439091167216856844588711603153276,
            70386486105843025439939619828917593665686757934951,
            62176457141856560629502157223196586755079324193331,
            64906352462741904929101432445813822663347944758178,
            92575867718337217661963751590579239728245598838407,
            58203565325359399008402633568948830189458628227828,
            80181199384826282014278194139940567587151170094390,
            35398664372827112653829987240784473053190104293586,
            86515506006295864861532075273371959191420517255829,
            71693888707715466499115593487603532921714970056938,
            54370070576826684624621495650076471787294438377604,
            53282654108756828443191190634694037855217779295145,
            36123272525000296071075082563815656710885258350721,
            45876576172410976447339110607218265236877223636045,
            17423706905851860660448207621209813287860733969412,
            81142660418086830619328460811191061556940512689692,
            51934325451728388641918047049293215058642563049483,
            62467221648435076201727918039944693004732956340691,
            15732444386908125794514089057706229429197107928209,
            55037687525678773091862540744969844508330393682126,
            18336384825330154686196124348767681297534375946515,
            80386287592878490201521685554828717201219257766954,
            78182833757993103614740356856449095527097864797581,
            16726320100436897842553539920931837441497806860984,
            48403098129077791799088218795327364475675590848030,
            87086987551392711854517078544161852424320693150332,
            59959406895756536782107074926966537676326235447210,
            69793950679652694742597709739166693763042633987085,
            41052684708299085211399427365734116182760315001271,
            65378607361501080857009149939512557028198746004375,
            35829035317434717326932123578154982629742552737307,
            94953759765105305946966067683156574377167401875275,
            88902802571733229619176668713819931811048770190271,
            25267680276078003013678680992525463401061632866526,
            36270218540497705585629946580636237993140746255962,
            24074486908231174977792365466257246923322810917141,
            91430288197103288597806669760892938638285025333403,
            34413065578016127815921815005561868836468420090470,
            23053081172816430487623791969842487255036638784583,
            11487696932154902810424020138335124462181441773470,
            63783299490636259666498587618221225225512486764533,
            67720186971698544312419572409913959008952310058822,
            95548255300263520781532296796249481641953868218774,
            76085327132285723110424803456124867697064507995236,
            37774242535411291684276865538926205024910326572967,
            23701913275725675285653248258265463092207058596522,
            29798860272258331913126375147341994889534765745501,
            18495701454879288984856827726077713721403798879715,
            38298203783031473527721580348144513491373226651381,
            34829543829199918180278916522431027392251122869539,
            40957953066405232632538044100059654939159879593635,
            29746152185502371307642255121183693803580388584903,
            41698116222072977186158236678424689157993532961922,
            62467957194401269043877107275048102390895523597457,
            23189706772547915061505504953922979530901129967519,
            86188088225875314529584099251203829009407770775672,
            11306739708304724483816533873502340845647058077308,
            82959174767140363198008187129011875491310547126581,
            97623331044818386269515456334926366572897563400500,
            42846280183517070527831839425882145521227251250327,
            55121603546981200581762165212827652751691296897789,
            32238195734329339946437501907836945765883352399886,
            75506164965184775180738168837861091527357929701337,
            62177842752192623401942399639168044983993173312731,
            32924185707147349566916674687634660915035914677504,
            99518671430235219628894890102423325116913619626622,
            73267460800591547471830798392868535206946944540724,
            76841822524674417161514036427982273348055556214818,
            97142617910342598647204516893989422179826088076852,
            87783646182799346313767754307809363333018982642090,
            10848802521674670883215120185883543223812876952786,
            71329612474782464538636993009049310363619763878039,
            62184073572399794223406235393808339651327408011116,
            66627891981488087797941876876144230030984490851411,
            60661826293682836764744779239180335110989069790714,
            85786944089552990653640447425576083659976645795096,
            66024396409905389607120198219976047599490197230297,
            64913982680032973156037120041377903785566085089252,
            16730939319872750275468906903707539413042652315011,
            94809377245048795150954100921645863754710598436791,
            78639167021187492431995700641917969777599028300699,
            15368713711936614952811305876380278410754449733078,
            40789923115535562561142322423255033685442488917353,
            44889911501440648020369068063960672322193204149535,
            41503128880339536053299340368006977710650566631954,
            81234880673210146739058568557934581403627822703280,
            82616570773948327592232845941706525094512325230608,
            22918802058777319719839450180888072429661980811197,
            77158542502016545090413245809786882778948721859617,
            72107838435069186155435662884062257473692284509516,
            20849603980134001723930671666823555245252804609722,
            53503534226472524250874054075591789781264330331690, ]

    def solve(self):
        return int(str(sum(self.arr))[0:10:1])


class Problem14(Problem):
    '''
    Longest Collatz sequence
    Problem 14
    The following iterative sequence is defined for the set of
    positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the
    following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet
    (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    '''

    def solve(self):
        even = (lambda x: x / 2)
        odd = (lambda x: 3 * x + 1)
        collatz = (lambda x: even(x) if x % 2 == 0 else odd(x))

        cache = dict()

        for item in range(1, 1000000):
            tmp = item
            count = 1

            while True:
                count += 1
                tmp = collatz(tmp)

                cached = cache.get(tmp, None)
                if cached is not None:
                    cache.update({item: cached + count})
                    break
                elif tmp == 1:
                    cache.update({item: count})
                    break

        return sorted(cache.items(), key=lambda x: x[1], reverse=True)[0][0]


class Problem15(Problem):
    '''
    Lattice paths
    Problem 15
    Starting in the top left corner of a 2×2 grid, and only being able to
    move to the right and down, there are exactly 6 routes to the bottom
    right corner.

    How many such routes are there through a 20×20 grid?
    '''

    def __init__(self):
        self.edge = 20

    def solve(self):
        return self.combination_number(self.edge + self.edge, self.edge)


class Problem16(Problem):
    '''
    Power digit sum
    Problem 16
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    '''

    def solve(self):
        powerd = int(pow(2, 1000))

        cache = []
        while powerd != 0:
            cache.append(powerd % 10)
            powerd //= 10

        return sum(cache)


class Problem18(Problem):
    '''
    Maximum path sum I
    Problem 18
    By starting at the top of the triangle below and moving to
    adjacent numbers on the row below, the maximum total from
    top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23.

    Find the maximum total from top to bottom of the triangle below:

                                75
                              95  64
                            17  47  82
                          18  35  87  10
                        20  04  82  47  65
                      19  01  23  75  03  34
                    88  02  77  73  07  63  67
                  99  65  04  28  06  16  70  92
                41  41  26  56  83  40  80  70  33
              41  48  72  33  47  32  37  16  94  29
            53  71  44  65  25  43  91  52  97  51  14
          70  11  33  28  77  73  17  78  39  68  17  57
        91  71  52  38  17  14  91  43  58  50  27  29  48
      63  66  04  68  89  53  67  30  73  16  69  87  40  31
    04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

    NOTE: As there are only 16384 routes, it is possible to solve this
    problem by trying every route. However, Problem 67, is the same
    challenge with a triangle containing one-hundred rows; it cannot
    be solved by brute force, and requires a clever method! ;o)
    '''

    def __init__(self):
        self.rows = list(
            map(lambda x: list(map(lambda y: int(y), x.split(' '))),
                [
                "75",
                "95 64",
                "17 47 82",
                "18 35 87 10",
                "20 04 82 47 65",
                "19 01 23 75 03 34",
                "88 02 77 73 07 63 67",
                "99 65 04 28 06 16 70 92",
                "41 41 26 56 83 40 80 70 33",
                "41 48 72 33 47 32 37 16 94 29",
                "53 71 44 65 25 43 91 52 97 51 14",
                "70 11 33 28 77 73 17 78 39 68 17 57",
                "91 71 52 38 17 14 91 43 58 50 27 29 48",
                "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
                "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
            ]))

    def solve(self):
        e = self.rows[::-1]

        for i in range(1, len(e)):
            for j in range(0, len(e[i])):
                e[i][j] += max([e[i - 1][j], e[i - 1][j + 1]])

        return self.rows[0][0]


class Problem19(Problem):
    '''
    Counting Sundays
    Problem 19
    You are given the following information, but you may prefer to do
    some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on
    a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the
    twentieth century (1 Jan 1901 to 31 Dec 2000)?
    '''

    def solve(self):
        from datetime import date
        from datetime import timedelta

        count = 0
        start = date(1901, 1, 1)
        end = date(2000, 12, 31)
        delta = timedelta(days=1)

        while True:
            if start.isoweekday() == 7 and start.day == 1:
                count += 1

            start = start + delta

            if end < start:
                break

        return count


class Problem20(Problem):
    '''
    Factorial digit sum
    Problem 20
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number
    10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    '''

    def solve(self):
        return sum(map(lambda x: int(x), str(self.factorial(100))))


class Problem21(Problem):
    '''
    Amicable numbers
    Problem 21
    Let d(n) be defined as the sum of proper divisors of n
    (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are
    an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are
    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    therefore d(220) = 284. The proper divisors of 284 are
    1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    '''

    def solve(self):
        return sum([x for x in range(1, 10000) if self.is_amicable_number(x)])


class Problem22(Problem):
    '''
    Names scores
    Problem 22
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
    containing over five-thousand first names, begin by sorting it into
    alphabetical order. Then working out the alphabetical value for each name,
    multiply this value by its alphabetical position in the list to obtain a
    name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
    COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    '''

    def solve(self):
        import os

        char_int = (lambda x: ord(x) - ord('A') + 1)
        mapper = (lambda x: map(char_int, list(x)))
        word_sum = (lambda x: sum(mapper(x)))

        dir_name = os.path.dirname(__file__)
        path = os.path.join(dir_name, "names.txt")
        o = open(path)
        names = o.read()
        o.close()
        names_arr = sorted(names.replace('"', "").split(","))

        return sum([(x[0] + 1) * word_sum(x[1]) for x in enumerate(names_arr)])


class Problem23(Problem):
    '''
    Non-abundant sums
    Problem 23
    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper
    divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
    is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
    smallest number that can be written as the sum of two abundant numbers
    is 24. By mathematical analysis, it can be shown that all integers greater
    than 28123 can be written as the sum of two abundant numbers. However,
    this upper limit cannot be reduced any further by analysis even though it
    is known that the greatest number that cannot be expressed as the sum of
    two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
    '''

    def solve(self):
        limit = 28123
        cache = set()

        abundants = [x for x in range(1, limit) if self.is_abundant(x)]
        for i in abundants:
            for j in abundants:
                tmp = i + j
                if tmp <= limit:
                    cache.add(tmp)
                else:
                    break

        return sum(set(range(1, limit)) - cache)
        # return sum([x for x in range(1, limit) if x not in cache])


class Problem24(Problem):
    '''
    Lexicographic permutations
    Problem 24
    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    '''

    def solve(self):
        seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        perm = self.Permutation()

        i = 1
        while i < 1000000:
            perm.next_lexigonal_permutation(seq)
            i += 1

        return int(reduce(lambda x, y: "{}{}".format(x, y), seq))


class Problem25(Problem):
    '''
    1000-digit Fibonacci number
    Problem 25
    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to
    contain 1000 digits?
    '''

    def solve(self):
        fib_1, fib_2, idx = 1, 1, 2
        while True:
            fib_1, fib_2 = self.next_fibonacci(fib_1, fib_2)

            if len(str(fib_1)) == 1000:
                break
            else:
                idx += 1

        return idx


class Problem26(Problem):
    '''
    Reciprocal cycles
    Problem 26
    A unit fraction contains 1 in the numerator. The decimal representation
    of the unit fractions with denominators 2 to 10 are given:

    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10    =     0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring
    cycle in its decimal fraction part.
    '''

    def solve(self):
        longes_recurring = (0, 0)

        for item in range(2, 1000):
            cache_rests = []

            x = 1

            while True:
                if (x < item):
                    x *= 10
                else:
                    x %= item

                    if x in cache_rests:
                        count = len(cache_rests) - cache_rests.index(x)
                        maximum = max(longes_recurring, (count, item))
                        longes_recurring = maximum
                        break

                    if x == 0:
                        break

                    cache_rests.append(x)

        return longes_recurring[1]


class Problem27(Problem):
    '''
    Quadratic primes
    Problem 27
    Euler discovered the remarkable quadratic formula:

    n^2+n+41
    It turns out that the formula will produce 40 primes for the consecutive
    integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is
    divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible
    by 41.

    The incredible formula n^2−79n+1601 was discovered, which produces 80
    primes for the consecutive values 0≤n≤79. The product of the
    coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

    n^2+an+b, where |a|<1000 and |b|≤1000

    where |n| is the modulus/absolute value of n
    e.g. |11|=11 and |−4|=4
    Find the product of the coefficients, a and b, for the quadratic
    expression that produces the maximum number of primes for consecutive
    values of n, starting with n=0.
    '''

    def solve(self):
        minimum, maximum = -1000, 1000
        n, a, b = 0, 0, 0

        for i_a in range(minimum + 1, maximum, 1):
            for i_b in range(minimum, maximum + 1, 1):
                i_n = 0
                while True:
                    tmp = pow(i_n, 2) + i_n * i_a + i_b
                    if tmp < 0 or not self.is_prime(tmp):
                        break
                    i_n += 1

                if n < i_n:
                    n, a, b = i_n, i_a, i_b

        return a * b


class Problem28(Problem):
    '''
    Number spiral diagonals
    Problem 28
    Starting with the number 1 and moving to the right in a clockwise
    direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001
    spiral formed in the same way?
    '''

    def solve(self):
        result = 1

        for edge in range(3, 1001 + 1, 2):
            square = pow(edge, 2)
            for i in range(0, 4, 1):
                result += (square - ((edge - 1) * i))

        return int(result)


class Problem29(Problem):
    '''
    Distinct powers
    Problem 29
    Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    2^2=4,  2^3=8,   2^4=16,  2^5=32
    3^2=9,  3^3=27,  3^4=81,  3^5=243
    4^2=16, 4^3=64,  4^4=256, 4^5=1024
    5^2=25, 5^3=125, 5^4=625, 5^5=3125
    If they are then placed in numerical order, with any repeats removed,
    we get the following sequence of 15 distinct terms:

    4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

    How many distinct terms are in the sequence generated by a^b for
    2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
    '''

    def solve(self):
        terms = set()

        for a in range(2, 101, 1):
            for b in range(2, 101, 1):
                terms.add(pow(a, b))

        return len(terms)


class Problem30(Problem):
    '''
    Digit fifth powers
    Problem 30
    Surprisingly there are only three numbers that can be written as the
    sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4
    As 1 = 1^4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of
    fifth powers of their digits.
    '''

    def solve(self):

        def powers(i):
            return map(lambda x: pow(int(x), 5), str(i))

        cache = 0

        for item in range(2, 1000000):
            if item == sum(powers(item)):
                cache += item

        return cache


class Problem31(Problem):
    '''
    Coin sums
    Problem 31
    In England the currency is made up of pound, £, and pence, p, and there
    are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
    '''

    def solve(self):
        values = [1, 2, 5, 10, 20, 50, 100, 200]

        return self.CoinsChangeSolver(values, 200).solve()


class Problem32(Problem):
    '''
    Pandigital products
    Problem 32
    We shall say that an n-digit number is pandigital if it makes use of
    all the digits 1 to n exactly once; for example, the 5-digit number,
    15234, is 1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254,
    containing multiplicand, multiplier, and product is 1 through 9
    pandigital.

    Find the sum of all products whose multiplicand/multiplier/product
    identity can be written as a 1 through 9 pandigital.

    HINT: Some products can be obtained in more than one way so be
    sure to only include it once in your sum.
    '''

    def solve(self):
        cache = set()

        for a in range(1, 1000):
            for b in range(1, 10000):
                c = str("{}{}{}".format(a, b, a * b))

                if len(c) == 9 and "".join(sorted(c)) == "123456789":
                    cache.add(a * b)

        return sum(cache)


class Problem33(Problem):
    '''
    Digit cancelling fractions
    Problem 33
    The fraction 49/98 is a curious fraction, as an inexperienced
    mathematician in attempting to simplify it may incorrectly believe
    that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction,
    less than one in value, and containing two digits in the numerator
    and denominator.

    If the product of these four fractions is given in its lowest common
    terms, find the value of the denominator.
    '''

    def solve(self):
        a, b = 1, 1
        for n in range(1, 10):
            for d in range(n + 1, 10):
                for c in range(1, 10):
                    if ((n * 10 + c) * d == (c * 10 + d) * n):
                        a, b = a * n, b * d

        return b / self.gcd(a, b)


class Problem34(Problem):
    '''
    Digit factorials
    Problem 34
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the
    factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    '''

    def solve(self):

        def digit_list(x):
            return map(lambda y: int(y), str(x))

        def factorial_list(x):
            return map(lambda y: self.factorial_lambda(y), x)

        def curious(x):
            return sum(factorial_list(digit_list(x))) == x

        return sum([x for x in range(3, self.factorial_lambda(9)) if curious(x)])


class Problem35(Problem):
    '''
    Circular primes
    Problem 35
    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?
    '''

    def solve(self):

        def rotation(what):
            return what[-1] + what[:-1]

        def all_rotation(what):
            tmp = str(what)
            for _ in range(len(tmp)):
                # if not self.is_prime(int(tmp)):
                if sieve[int(tmp)]:
                    return False

                tmp = rotation(tmp)

            return True

        sieve = self.eratosthenes_sief(1000000)
        return len([x for x in range(2, 1000000) if all_rotation(x)])


class Problem36(Problem):
    '''
    Double-base palindromes
    Problem 36
    The decimal number, 585 = 1001001001 (binary),
    is palindromic in both bases.

    Find the sum of all numbers, less than one million,
    which are palindromic in base 10 and base 2.

    (Please note that the palindromic number,
    in either base, may not include leading zeros.)
    '''

    def solve(self):
        return sum([x for x in range(0, 1000000)
                    if self.is_palindromic(x)
                    and self.is_palindromic("{0:b}".format(x))])


class Problem37(Problem):
    '''
    Truncatable primes
    Problem 37
    The number 3797 has an interesting property.
    Being prime itself, it is possible to continuously
    remove digits from left to right, and remain prime
    at each stage: 3797, 797, 97, and 7.
    Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable
    from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    '''

    def solve(self):

        def r_t_l(what):
            tmp = str(what)
            if (len(tmp) > 1):
                return not sieve[int(tmp)] and r_t_l(tmp[1:])
            else:
                return not sieve[int(tmp)]

        def l_t_r(what):
            tmp = str(what)
            if (len(tmp) > 1):
                return not sieve[int(tmp)] and l_t_r(tmp[0:-1])
            else:
                return not sieve[int(tmp)]

        sieve = self.eratosthenes_sief(1000000)
        return sum([x for x in range(10, 1000000) if r_t_l(x) and l_t_r(x)])


class Problem38(Problem):
    '''
    Pandigital multiples
    Problem 38
    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9
    and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
    which is the concatenated product of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed
    as the concatenated product of an integer with (1,2, ... , n) where n > 1?
    '''

    def solve(self):

        def analyze(x):
            tmp = str(x)

            for y in range(2, 10):
                tmp = "{}{}".format(tmp, x * y)

                if (self.is_pandigital(tmp)):
                    return int(tmp)

                if len(tmp) > 9:
                    return 0

            return 0

        return max([analyze(x) for x in range(2, 10000)])


class Problem39(Problem):
    '''
    Integer right triangles

    Problem 39
    If p is the perimeter of a right angle triangle
    with integral length sides, {a,b,c},
    there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p ≤ 1000, is the number of solutions maximised?
    '''

    def solve(self):
        cache, ret = 0, 0

        for p in range(1, 1001):
            count = 0

            for a in range(1, p // 2):
                for b in range(1, p // 3):
                    c = sqrt(a * a + b * b)

                    if a + b + c == p:
                        count += 1

            if cache < count:
                cache = count
                ret = p

        return ret


class Problem40(Problem):
    '''
    Champernowne's constant

    Problem 40
    An irrational decimal fraction is created by
    concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part,
    find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    '''

    def solve(self):
        champernowne_constant = ""
        for item in range(1, int(pow(10, 7)) + 1):
            champernowne_constant += str(item)

        value = 1
        for to in range(7):
            value *= int(champernowne_constant[int(pow(10, to)) - 1])

        return value


class Problem41(Problem):
    '''
    Pandigital prime

    Problem 41
    We shall say that an n-digit number is pandigital
    if it makes use of all the digits 1 to n exactly once.
    For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    '''

    def solve(self):
        result = 0
        generator = self.Permutation()

        for item in range(1, 10):
            cache = [x for x in range(1, item + 1)]

            while True:
                r = reduce(lambda x, y: x * 10 + y, cache)

                if result < r and self.is_prime(r):
                    result = r

                if not generator.next_lexigonal_permutation(cache):
                    break

        return result


class Problem42(Problem):
    '''
    Coded triangle numbers

    Problem 42
    The nth term of the sequence of triangle numbers is given by,
    tn = ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding
    to its alphabetical position and adding these values we form a word value.
    For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
    If the word value is a triangle number then we shall call the word
    a triangle word.

    Using words.txt (right click and 'Save Link/Target As...'),
    a 16K text file containing nearly two-thousand common English words,
    how many are triangle words?
    '''

    def solve(self):
        from os import path
        ord_a = ord('A') - 1

        def word_to_value(word):
            return sum(map(lambda x: ord(x) - ord_a, str(word)))

        root_dir = path.dirname(__file__)
        path_words = path.join(root_dir, "words.txt")
        file_open = open(path_words)
        file_words = [x.split(",") for x in file_open.readlines()]
        file_flat_word = reduce(lambda x, y: x + y, file_words)
        words = [str(x).replace("\"", "") for x in file_flat_word]
        word_values = [word_to_value(x) for x in words]
        word_max_value = max(word_values)

        x = 1

        triangle_cache = list()
        while True:
            triangle = x * (x + 1) / 2

            if triangle > word_max_value:
                break

            triangle_cache.append(triangle)
            x += 1

        return len(filter(lambda x: x in triangle_cache, word_values))


class Problem43(Problem):
    '''
    Sub-string divisibility

    Problem 43
    The number, 1406357289, is a 0 to 9 pandigital number because
    it is made up of each of the digits 0 to 9 in some order,
    but it also has a rather interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit,
    and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17
    Find the sum of all 0 to 9 pandigital numbers with this property.
    '''

    def solve(self):
        ret = 0
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        divisibles = [2, 3, 5, 7, 11, 13, 17]

        def seq_int(seq):
            return reduce(lambda x, y: x * 10 + y, seq)

        perm = Problem.Permutation()
        while True:
            for i, d in enumerate(divisibles):
                if seq_int(arr[i + 1:i + 4]) % d != 0:
                    break
                elif d == divisibles[-1]:
                    ret += seq_int(arr)

            if not perm.next_lexigonal_permutation(arr):
                break

        return ret


class Problem44(Problem):
    '''
    Pentagon numbers

    Problem 44
    Pentagonal numbers are generated by the formula,
    Pn=n(3n−1)/2. The first ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

    It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However,
    their difference, 70 − 22 = 48, is not pentagonal.

    Find the pair of pentagonal numbers, Pj and Pk,
    for which their sum and difference are pentagonal
    and D = |Pk − Pj| is minimised; what is the value of D?
    '''

    def solve(self):

        def pentagonal_number(x):
            return x * (3 * x - 1) / 2

        def verify_pentagonal(x):
            a = 24 * x + 1
            b = sqrt(a)
            return b * b == a and b % 6 == 5

        k = 0
        while True:
            k += 1

            pentagonal_k = pentagonal_number(k)

            for j in range(1, k + 1):
                pentagonal_j = pentagonal_number(j)

                diff = abs(pentagonal_k - pentagonal_j)
                add = pentagonal_k + pentagonal_j

                pen_dif = verify_pentagonal(diff)
                pen_add = verify_pentagonal(add)

                if (pen_add and pen_dif):
                    return diff

        return 0


class Problem45(Problem):
    '''
    Triangular, pentagonal, and hexagonal

    Problem 45
    Triangle, pentagonal, and hexagonal numbers are generated
    by the following formulae:

    Triangle         Tn=n(n+1)/2        1, 3, 6, 10, 15, ...
    Pentagonal       Pn=n(3n−1)/2       1, 5, 12, 22, 35, ...
    Hexagonal        Hn=n(2n−1)         1, 6, 15, 28, 45, ...
    It can be verified that T285 = P165 = H143 = 40755.

    Find the next triangle number that is also pentagonal and hexagonal.
    '''

    def solve(self):

        def triangle_number(x):
            return x * (x + 1) / 2

        def is_triangle(x):
            return (sqrt(8 * x + 1) - 1) / 2 % 1 == 0

        def is_pentagona(x):
            return sqrt(24 * x + 1) % 6 == 5
        
        def is_hexagonal(x):
            return (sqrt(8 * x + 1) + 1) / 4 % 1 == 0

        x = 285 + 1
        while True:
            triangle = triangle_number(x)
            if is_pentagona(triangle) and is_hexagonal(triangle):
                return triangle
            else:
                x += 1

        return 0


class Problem46(Problem):
    '''
    Goldbach's other conjecture

    Problem 46
    It was proposed by Christian Goldbach that every odd composite number
    can be written as the sum of a prime and twice a square.

    9 = 7 + 2×1^2
    15 = 7 + 2×2^2
    21 = 3 + 2×3^2
    25 = 7 + 2×3^2
    27 = 19 + 2×2^2
    33 = 31 + 2×1^2

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written
    as the sum of a prime and twice a square?
    '''

    def solve(self):

        def analyze(x):
            primes = self.eratosthenes_sief(x)
            if x % 2 == 0 or not primes[-1]:
                return False
            y = 1
            while y * y <= x:
                tmp = x - y * y * 2
                if tmp < 0:
                    break
                if not primes[tmp]:
                    return  False
                y += 1
            return True

        x = 2
        while x < 5777 + 1:
            if analyze(x):
                return x
            x += 1

        return 0


class Problem47(Problem):
    '''
    Distinct primes factors

    Problem 47
    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers
    to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers
    to have four distinct prime factors each.
    What is the first of these numbers?
    '''

    def solve(self):
        consecutive_len = 4

        def consecutive(x):
            for y in range(x, x + consecutive_len):
                if len(self.prime_factors(y)) != consecutive_len:
                    return False
            return True

        x = 1
        while x <= 134043:
            if consecutive(x):
                return x
            else:
                x += 1
        return 0


class Problem48(Problem):
    '''
    Self powers

    Problem 48
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
    '''

    def solve(self):
        tmp = 0
        for x in range(1, 1000 + 1):
            tmp += reduce(lambda x, y: x * y, [x] * x)

        return int(str(tmp)[-10::])


class Problem49(Problem):
    '''
    Prime permutations

    Problem 49
    The arithmetic sequence, 1487, 4817, 8147,
    in which each of the terms increases by 3330,
    is unusual in two ways: (i) each of the three terms are prime,
    and, (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of
    three 1-, 2-, or 3-digit primes, exhibiting this property,
    but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating
    the three terms in this sequence?
    '''

    def solve(self):

        def same_digit(a, b, c):
            a_str = sorted(str(a))
            b_str = sorted(str(b))
            c_str = sorted(str(c))
            return a_str == b_str and b_str == c_str

        stop = 10000
        start = stop / 10

        primes = self.eratosthenes_sief(stop)
        for x in range(start, stop)[::-1]:
            if not primes[x]:
                for y in range(start, stop):
                    a, b = x + y, x + 2 * y

                    if same_digit(a, b, x) and not primes[a] and not primes[b]:
                        return reduce(lambda x, y: x * 10000 + y, [x, a, b])

        return 0


class Problem50(Problem):
    '''
    Consecutive prime sum

    Problem 50
    The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds
    to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds
    to a prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of
    the most consecutive primes?
    '''

    def solve(self):
        limit = 1000000

        prime_sieve = self.eratosthenes_sief(limit)
        primes = map(lambda x: x[0],
                     filter(lambda x: not x[1], enumerate(prime_sieve)))

        tmp = (0, 0)
        primes_len = len(primes)
        for i in range(primes_len):
            s = 0

            for idx, j in enumerate(range(i + 1, primes_len)):
                s += primes[j]

                if limit < s:
                    break
                elif not prime_sieve[s] and tmp[0] < idx:
                    tmp = (idx, s)

        return tmp[1]


if __name__ == '__main__':
    # import time
    # start = time.time()
    # Problem1().solve()
    # Problem2().solve()
    # Problem3().solve()
    # Problem4().solve()
    # Problem5().solve()
    # Problem6().solve()
    # Problem7().solve()
    # Problem8().solve()
    # Problem9().solve()
    # Problem10().solve()
    # Problem11().solve()
    # Problem12().solve()
    # Problem13().solve()
    # Problem14().solve()
    # Problem15().solve()
    # Problem16().solve()
    # # Problem17().solve()
    # Problem18().solve()
    # Problem19().solve()
    # Problem20().solve()
    # Problem21().solve()
    # Problem22().solve()
    # Problem23().solve()
    # Problem24().solve()
    # Problem25().solve()
    # Problem26().solve()
    # Problem27().solve()
    # Problem28().solve()
    # Problem29().solve()
    # Problem30().solve()
    # Problem31().solve()
    # Problem32().solve()
    # Problem33().solve()
    # Problem34().solve()
    # Problem35().solve()
    # Problem36().solve()
    # Problem37().solve()
    # Problem38().solve()
    # Problem39().solve()
    # Problem40().solve()
    # Problem41().solve()
    # Problem42().solve()
    # Problem43().solve()
    # Problem44().solve()
    # Problem45().solve()
    # Problem46().solve()
    # Problem47().solve()
    # Problem48().solve()
    # Problem49().solve()
    # Problem50().solve()
    # print(time.time() - start)
    pass

__all__ = ["Problem", "Problem1", "Problem2", "Problem3", "Problem4", \
           "Problem5", "Problem6", "Problem7", "Problem8", "Problem9", \
           "Problem10", "Problem11", "Problem12", "Problem13", "Problem14", \
           "Problem15", "Problem16", "Problem18", "Problem19", "Problem20", \
           "Problem21", "Problem22", "Problem23", "Problem24", "Problem25", \
           "Problem26", "Problem27", "Problem28", "Problem29", "Problem30", \
           "Problem31", "Problem32", "Problem33", "Problem34", "Problem35", \
           "Problem36", "Problem37", "Problem38", "Problem39", "Problem40", \
           "Problem41", "Problem42", "Problem43", "Problem44", "Problem45", \
           "Problem46", "Problem47", "Problem48", "Problem49", "Problem50"]
