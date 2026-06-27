---
role: exercise
locale: en
chapter: "IV. Derived Functors"
section: "1. Complexes"
exercise_number: 2
---

# Exercise 1.2

Given a chain map $\varphi: C \to D$, construct a chain complex as follows:

$$
E_n = C_{n-1} \oplus D_n,
$$
$$
\partial(a, b) = (-\partial a, \;\varphi a + \partial b), \qquad a \in C_{n-1},\; b \in D_n.
$$

Show that $E = \{E_n, \partial_n\}$ is indeed a chain complex and that the inclusion $D \hookrightarrow E$ is a chain map.

Write $E = E(\varphi)$, the **mapping cone** of $\varphi$.
