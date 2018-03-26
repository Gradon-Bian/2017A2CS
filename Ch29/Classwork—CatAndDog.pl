/* According to Teacher's solutions. */
cat(jack).
cat(black).
dog(lucky).
dog(cake).

animal(X): -dog(X).
animal(X): -cat(X).
enimies(X,Y): -(cat(X), dog(Y)).
enimies(X,Y): -(cat(Y), dog(X)).

