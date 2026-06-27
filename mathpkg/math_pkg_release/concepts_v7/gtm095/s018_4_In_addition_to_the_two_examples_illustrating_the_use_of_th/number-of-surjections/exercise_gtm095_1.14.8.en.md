---
role: exercise
locale: en
chapter: "1"
section: "14"
exercise_number: 8
---

# Exercise 8

Let $A = A(n)$ and $B = B(m)$ be two sets consisting of $n$ and $m$ elements respectively ($n \geq m$).

A mapping $\mathbb{S} : A \to B$ is said to be a *surjection* (or onto function) if for any $b \in B$ there is an $a \in A$ such that $\mathbb{S}(a) = b$.

Using the inclusion–exclusion principle, show that the number of surjections $N(\mathbb{S})$ is given by

$$N(\mathbb{S}) = \sum_{i=0}^{m} (-1)^i \binom{m}{i} (m-i)^n.$$

Interpret this formula combinatorially: the term $i = 0$ gives $m^n$ (total functions), the term $i = 1$ subtracts functions missing one element, $i = 2$ adds back functions missing two elements, and so on.
