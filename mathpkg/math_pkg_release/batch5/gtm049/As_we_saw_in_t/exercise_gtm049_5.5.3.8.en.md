---
role: exercise
locale: en
chapter: "5"
section: "5.3"
exercise_number: 8
---

Let $(a_1, \ldots, a_n)$ be an ordered basis of $V$ and $q$ a quadratic form on $V$. We define the matrix of $q$ with respect to $(a_1, \ldots, a_n)$ to be $(q_{ij})$, where

$$q_{ii} = q(a_i),$$
$$q_{ij} = arphi(a_i, a_j) \quad 	ext{if} \quad i 
eq j,$$

where $arphi$ is the bilinear form associated with $q$. Prove that

$$q(x_1 a_1 + \cdots + x_n a_n) = \sum_{i \leq j} q_{ij} x_i x_j.$$

(Use induction on $n$. Observe that the result is valid irrespective of whether $F$ is of characteristic 2 or not.)
