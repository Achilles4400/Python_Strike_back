__author__ = 'guillaume'


from Client import api_call_code

codeA = """
print 'start'

total = 0

for i in range(1, 50000000):
    total = total + (i / (i * i))

return_value = total
"""

codeB = """
return_value = 1+1
"""

resA = api_call_code(codeA)
resB = api_call_code(codeB)
print resA
print resB

true_resA = resA.get()
true_resB = resB.get()



print true_resA
print true_resB
print true_resA - true_resB