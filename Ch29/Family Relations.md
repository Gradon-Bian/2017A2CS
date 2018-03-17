brother(x, y):- male(x).
sister(x, y):- female(x).

son(x, y):- male(x),parent(y, x).
daughter(x, y):- female(x),parent(y, x).

married(x, y):- male(x),female(y);male(y),female(x).

