####numeric
#1.int
var=10
print(type(var))

#2.float
var=10.6
print(type(var))

#3.complex..(real+imaginary)
var=50+8j
print(type(var))

####Text
#1.str(string)
var='firstbit solution.' 
var="firstbit solution."
print(type(var))

####2.sequentical
#1.list
var=[10,20,30,40]
print(type(var))
var=list[20,49,35]

#2.tuple
var=(10,20,30,40)
print(type(var))

#range
var=range(10,60000)
print(type(var))

####set type
#1.set
var={10,20,30,40}
print(type(var))

#2.forzenset
var=frozenset({10,20,30})
print(type(var))

####mapping
#1.dictionary

var={'id':101,'name':'mayur','sal':2000}
print(type(var))

####other
#1.boolean(true/false)
var=True
print(type(var))

#2.nonetype
var=None
print(type(var))

