"""Assignment #3 submitted by Ketaki Kekatpure. Course - CS21A

This program takes keys/values of three dictionaries as input. The function
combines all the dictionaries in a single dictionary. The output dictionary
contains the keys/values of all dictionaries and creates a list of values where
there are multiple values for common keys in different dictionaries."""

d1 = {1: 'a',  2: 'b', 3: 'c', 4: 'd'}

d2 = {10: 'i', 20: 'j', 3: 'k', 40: 'l'}

d3 = {100: 's', 200: 't', 3: 'u', 400: 'v'}


dall = [d1, d2, d3]

dkeys = set(list(d1.keys()) + list(d2.keys()) + list(d3.keys()))

d = {}

for key in dkeys:
    d.update({key: []})

for dic in dall:
    for (dk, dv) in dic.items():
        d.setdefault(dk, []).append(dv)

for key, value in d.items():
    if len(d[key]) == 1:
        d[key] = d[key][0]
print(d)

"""
First data set - INPUT
=====================================================================================================
d1 = {1: 'a',  2: 'b', 3: 'c', 4: 'd'}

d2 = {10: 'i', 20: 'j', 3: 'k', 40: 'l'}

d3 = {100: 's', 200: 't', 3: 'u', 400: 'v'}

=====================================================================================================
First data set - OUTPUT
======================================================================================================
{400: 'v', 1: 'a', 2: 'b', 3: ['c', 'k', 'u'], 4: 'd', 40: 'l', 100: 's', 10: 'i', 200: 't', 20: 'j'}
======================================================================================================

======================================================================================================
Second data set - INPUT
======================================================================================================
d1 = {
    'Andrew': 56,
    'Colin': 88,
    'Alan': 95,
    'Mary': 76,
    'Tricia': 99,
    'Tom' : 100
}
d2 = {
    'Andrew': 79,
    'Colin':62,
    'Alan': 88,
    'Mary': 88,
    'Tricia': 92,
    'John' : 100,
    'Tom' : 99
}
d3 = {
    'Andrew': 90,
    'Colin': 60,
    'Alan': 92,
    'Mary': 85,
    'Tricia': 95,
    'Bob' : 100
}

=====================================================================================================
Second data set - OUTPUT
======================================================================================================
{'Andrew': [56, 79, 90], 'Bob': 100, 'Mary': [76, 88, 85], 'Tricia': [99, 92, 95], 'Colin': [88, 62, 60], 'Tom': [100, 99], 'John': 100, 'Alan': [95, 88, 92]}

"""
