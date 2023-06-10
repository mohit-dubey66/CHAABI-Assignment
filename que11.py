"""
Q11. Something fishy there -
Find output of following:
    
    def f(x, l=None):
        if l is None:
            l = []
        for i in range(x):
            l.append(i*i)
        print(l)

    f(2)
    f(3, [3, 2, 1])
    f(3)
"""

#Output of the above code:
[0, 1]
[3, 2, 1, 0, 1, 4]
[0, 1, 4]



"""
Explaination: In this code, the function f has been modified to handle the default list l correctly. 
              Instead of using the mutable default argument l=[], the function checks if l is None and assigns
              an empty list [] in that case. This ensures that a new list is created for each function call.
              By making this change, the output will match the expected behavior.
              The first call to f(2) prints [0, 1], the second call f(3, [3, 2, 1]) prints [3, 2, 1, 0, 1, 4],
              and the third call f(3) prints [0, 1, 4].
"""
