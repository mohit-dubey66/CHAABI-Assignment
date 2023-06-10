"""
Q8. Some neat tricks up her sleeve:
Looking at the below code, write down the final values of A0, A1, ...An
    A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
    A1 = range(10)
    A2 = sorted([i for i in A1 if i in A0])
    A3 = sorted([A0[s] for s in A0])
    A4 = [i for i in A1 if i in A3]
    A5 = {i:i*i for i in A1}
    A6 = [[i,i*i] for i in A1]
    A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
    A8 = map(lambda x: x*2, [1,2,3,4])
    A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])

"""
#1
A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
"""
Answer: The above code creates a dictionary A0 where the keys
        are the elements in the tuple ('a', 'b', 'c', 'd', 'e')
        and the values are the elements in the tuple (1, 2, 3, 4, 5).
        The final value of A0 will be {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.
"""


#2
A1 = range(10)
"""
Answer: The above code creates a range object A1 that represents the numbers from 0 to 9.
        The final value of A1 will be range(0, 10).
"""


#3
A2 = sorted([i for i in A1 if i in A0])
"""
Answer: The above code creates a list comprehension that iterates over A1 and keeps only
        the elements that are present in A0. It then sorts the resulting list.
        The final value of A2 will be [1, 2, 3, 4, 5].
"""


#4
A3 = sorted([A0[s] for s in A0])
"""
Answer: The above code creates a list comprehension that iterates over the keys of
        A0 and retrieves the corresponding values from A0. It then sorts the resulting list.
        The final value of A3 will be [1, 2, 3, 4, 5].
"""


#5
A4 = [i for i in A1 if i in A3]
"""
Answer: The above code creates a list comprehension that iterates over A1 and keeps
        only the elements that are present in A3. The final value of A4 will be [1, 2, 3, 4, 5].
"""


#6
A5 = {i: i*i for i in A1}
"""
Answer: The above code creates a dictionary comprehension that squares each element in A1 and
        uses it as both the key and value in the resulting dictionary.
        The final value of A5 will be {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}.
"""


#7
A6 = [[i, i*i] for i in A1]
"""
Answer: The above code creates a list comprehension that creates a list of lists, where each inner
        list contains an element from A1 and its square. The final value of A6 will be
        [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]].
"""


#8 
from functools import reduce
A7 = reduce(lambda x, y: x+y, [10, 23, -45, 33])
"""
Answer: The above code uses the reduce function from the functools module to apply the lambda
        function (lambda x, y: x+y) to the list [10, 23, -45, 33] in a cumulative way.
        The lambda function simply sums two numbers.
        The final value of A7 will be 21 (the sum of the elements in the list).
"""


#9
A8 = map(lambda x: x*2, [1, 2, 3, 4])
"""
Answer: The above code uses the map function to apply the lambda function (lambda x: x*2) to
        each element in the list [1, 2, 3, 4]. The lambda function doubles each number.
        The final value of A8 will be a map object that contains the values [2, 4, 6, 8].
"""


#10
A9 = filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"])
"""
Answer: The above code uses the filter function to apply the lambda function (lambda x: len(x) > 3)
        to each element in the list ["I", "want", "to", "learn", "python"].
        The lambda function filters out the elements with a length less than or equal to 3.
        The final value of A9 will be a filter object that contains the values ["want", "learn", "python"].
"""


# Hence, final values of all lists are:
"""
Summary: A0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
         A1 = range(0, 10)
         A2 = [1, 2, 3, 4, 5]
         A3 = [1, 2, 3, 4, 5]
         A4 = [1, 2, 3, 4, 5]
         A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
         A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
         A7 = 21
         A8 = map object containing [2, 4, 6, 8]
         A9 = filter object containing ["want", "learn", "python"]

"""