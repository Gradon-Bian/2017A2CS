# Gradon Bian S3C5 Opt 1

## Chapter 29 End of Chapter Questions

### Question 1: a i 

```prolog
cityIn(london, uk).
```



### Question 1: a ii

```prolog
iVisited(strasbourg).
```



### Quesion 1: b

chile, argentuna.



### Question 1: c 

```prolog
countriesIVisited(Country) IF cityIn(City, Country) AND iVisited(City).
```



### Question 2: a i

Emma has license.



### Question 2: a ii

(From clause 15)

```prolog
allowedToDrive(X, V)
	IF hasLicense(X) AND minimumAge(V, L)
		AND age(X, A)
		AND A >= L.
```



### Question 2: b i

Who = jack



### Question 2: b ii

false

### Question2: b iii##

false



### Question2: c i##

```prolog
qualifiedCarDrivers(T) IF qualifiedDriver(T, car).
```



### Question2: c ii (referenced the answer)##
```prolog
partQualified(X)IF passedTheoryTest(X) AND NOT passedDrivingTest(X, _).
```



### Question2: d (referenced the answer because I didn't know how to solve it)

Clause 11 (true), clause 01 (instantiates L as 18), clause 05 (instantiates A
as 17), clause 15 ( A >= L is false) result is false.