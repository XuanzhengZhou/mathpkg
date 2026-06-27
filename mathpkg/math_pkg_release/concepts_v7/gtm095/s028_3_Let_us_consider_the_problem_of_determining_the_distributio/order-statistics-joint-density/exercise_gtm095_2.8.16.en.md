---
role: exercise
locale: en
chapter: "2"
section: "8. Random Variables: II"
exercise_number: 16
---

# Exercise 16

Let $X_1, \ldots, X_n$ be independent identically distributed random variables with distribution function $F = F(x)$ and density $f = f(x)$. Denote by

$$
X^{(1)} = \min(X_1, \ldots, X_n)
$$

the smallest of $X_1, \ldots, X_n$, by $X^{(2)}$ the second smallest, and so on, and by

$$
X^{(n)} = \max(X_1, \ldots, X_n)
$$

the largest of $X_1, \ldots, X_n$. (The variables $X^{(1)}, \ldots, X^{(n)}$ so defined are called **order statistics** of $X_1, \ldots, X_n$.)

Show that:

**(a)** The density function of $X^{(k)}$ has the form

$$
n f(x) \binom{n-1}{k-1} [F(x)]^{k-1} [1 - F(x)]^{n-k}.
$$

**(b)** The joint density $f(x^1, \ldots, x^n)$ of $X^{(1)}, \ldots, X^{(n)}$ is given by

$$
f(x^1, \ldots, x^n) = \begin{cases}
n! \, f(x^1) \cdots f(x^n), & \text{if } x^1 < x^2 < \cdots < x^n, \\
0, & \text{otherwise}.
\end{cases}
$$
