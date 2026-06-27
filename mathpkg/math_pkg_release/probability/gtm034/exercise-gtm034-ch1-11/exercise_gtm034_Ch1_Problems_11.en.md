---
role: exercise
locale: en
chapter: "1"
section: "Problems"
exercise_number: 11
---

11. Let $X_1, X_2, \ldots$ be independent identically distributed random variables, $S_0 = 0, S_n = X_1 + \cdots + X_n$, and $M_n = \max [S_0, S_1, \ldots, S_n]$, as in D19.1. Now we define two other sequences $Z_n$ and $W_n$ of random variables, with $n \geq 0$. The first of these is

$$Z_0 = 0, \quad Z_1 = (X_1)^+, \ldots, Z_{n+1} = (Z_n + X_{n+1})^+,$$

where $x^+ = x$ if $x > 0$, and 0 otherwise. The second sequence is defined by

$$W_0 = 0, \quad W_n = \sum_{k=1}^{n} X_k \theta(S_k),$$

where $\theta(x) = 1$ if $x > 0$, and 0 otherwise.

Prove that

$$P[M_n = x] = P[Z_n = x] = P[W_n = x]$$

for all non-negative integers $n$ and $x$. The sequence $Z_n$ has applications in queueing theory [17].
