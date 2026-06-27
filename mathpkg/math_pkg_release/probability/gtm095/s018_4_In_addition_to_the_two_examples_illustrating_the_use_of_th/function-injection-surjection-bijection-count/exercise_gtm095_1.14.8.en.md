---
role: exercise
locale: en
chapter: "1"
section: "14"
exercise_number: 8
---

# Exercise 8

Let $A = A(n)$ and $B = B(m)$ be two sets consisting of $n$ and $m$ elements respectively.

A mapping $\mathbb{F} : A \to B$ is said to be a *function* if to each $a \in A$ it makes correspond some $b \in B$.

A mapping $\mathbb{I} : A \to B$ is said to be an *injection* if to different elements of $A$ it makes correspond different elements of $B$. (In this case $n \leq m$.)

A mapping $\mathbb{S} : A \to B$ is said to be a *surjection* (or onto function) if for any $b \in B$ there is an $a \in A$ such that $\mathbb{S}(a) = b$. (In this case $n \geq m$.)

A mapping $\mathbb{B} : A \to B$ is said to be a *bijection* if it is both injection and surjection. (In this case $n = m$.)

Using the inclusion–exclusion principle, show that $N(\mathbb{F})$, $N(\mathbb{I})$, $N(\mathbb{S})$, and $N(\mathbb{B})$ (i.e., the number of functions, injections, surjections, and bijections) are given by the following formulas:

$$N(\mathbb{F}) = m^n,$$

$$N(\mathbb{I}) = (m)_n \quad (= m(m-1) \cdots (m-n+1)),$$

$$N(\mathbb{S}) = \sum_{i=0}^{m} (-1)^i \binom{m}{i} (m-i)^n,$$

$$N(\mathbb{B}) = n! \quad \left(= \sum_{i=0}^{n} (-1)^i \binom{n}{i} (n-i)^n\right).$$
