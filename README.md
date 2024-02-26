# Propositional Argument Validity

Due to taking a logic class, I have come across propositional logic. I learned how propositional arguments work using the book [Intermediate Logic by Canon Logic Series](https://www.amazon.com/Intermediate-Logic-Student-Canon/dp/1591281660). 

The main module used is called **[Sympy](https://www.sympy.org/en/index.html)**. It can be installed onto your computer using the command:
```
pip install sympy
```


## About

There are fives types of symbols in propositional logic that are important to know in this program.

```
& -- and
| -- or
>> -- conditional (p implies q ; if p then q)
=== -- biconditional (logical equivalence)
~ -- negation
```

>The ***and*** operator is only **True** when both variables are True (Ex. P & P - if P is true, the statement is true).

>The ***or*** operator is only **False** when both variables are False (Ex. P | P - if P is false, the statement is false).

>The ***>>*** (conditional) is only **False** when the antecedent variable is True and the consequent variable is False (Ex. P >> Q -- P = true and Q = false, then the statement is false).

> The ***===*** (biconditional) is only **True** when both sides of the statement match (Ex. P === Q - P = true, Q = true, then the statement is true).

> The ***~*** (negation) switches the value of the statement or variable (Ex. ~p - p = true, then the statement is false).
