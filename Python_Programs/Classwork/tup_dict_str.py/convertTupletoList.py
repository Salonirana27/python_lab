#convert tuple to a list and modifie it
t = (10, 20, 30)
lst = list(t)
lst.append(40)
t = tuple(lst)
print("Modified Tuple:", t)

#output
"""Modified Tuple: (10, 20, 30, 40)"""