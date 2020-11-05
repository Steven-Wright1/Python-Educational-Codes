import statistics as s #Allows us to write statistics as s 

exList= [3,5,7,3,1,5,7,9,5,5,4,3,3,6,43,2,5,6,4,7,4]
print(s.mean(exList))

#if you only want to import one function from the library
from statistics import mean
#can also use shorthand here as well
from statistics import variance as v

print(mean(exList))
print(v(exList))

#allows you to import multiple
from statistics import stdev as st, mean as m
print(m(exList))
print(st(exList))
