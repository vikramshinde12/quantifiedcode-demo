#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Outdated style string formatting
print "This is an old-style string formatting {0!s}".format("Test")

# Replacement fields not explicitly numbered
print "{} is {}".format("life", "hard")

# Mutable default argument used
def test(a, b=None):
    if b is None:
        b = []
    pass

# Duplicate dictionary keys
time = { "minute": 37, "second": 05, "hour": 12}

# Invalid NoneType comparisons
x = None
if x == None:
  print "Use is, not =="

# Outdated <> operator
i, k = 1, 2
if i <> k:
    print("Use !=")

# Using list instead of iterator
any(i*2 == 12 for i in range(10))
all(i*2 < 10 for i in range(10))

# No dict/set comprehensions used
times=[]
times.append({"hour": 8, "minute": 37, "second": 05})
times.append({"hour": 9, "minute": 37, "second": 05})
stuff_dict = {t["minute"]: t["hour"] for t in times}