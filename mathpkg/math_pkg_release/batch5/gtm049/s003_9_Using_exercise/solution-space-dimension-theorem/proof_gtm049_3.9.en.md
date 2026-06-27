---
role: proof
locale: en
of_concept: solution-space-dimension-theorem
source_book: gtm049
source_chapter: "3"
source_section: "9"
---

If $r = 0$ then the theorem is true since then every element of $F^n$ is a solution. We suppose therefore that one of the coefficients $a_{ij}$ is non-zero. By suitably renumbering the equations and variables, if necessary, we may assume that $a_{11} \neq 0$. Write $L_i$ for $\sum_{j=1}^{n} a_{ij} X_j$, $i = 1, \ldots, m$. Define

$$L_1' = L_1,$$

$$L_i' = L_i - \frac{a_{i1}}{a_{11}} L_1 \quad \text{for } i = 2, \ldots, m.$$

Then the system $L_i' = 0$ ($i = 1, \ldots, m$) has exactly the same set of solutions and the same coefficient space as the system $L_i = 0$ ($i = 1, \ldots, m$). This follows from the fact that every $L_i'$ is a linear combination of the $L_j$, and every $L_i$ is a linear combination of the $L_j'$.

We reduce the equations step by step in this way (with suitable renumberings, if necessary) until a "truncated triangle" of equations is obtained, say

$$b_{11} X_1 + \cdots + b_{1n} X_n = 0$$
$$\qquad b_{22} X_2 + \cdots + b_{2n} X_n = 0$$
$$\qquad\qquad \ddots$$
$$\qquad\qquad\qquad b_{rr} X_r + \cdots + b_{rn} X_n = 0,$$

where the diagonal coefficients $b_{11}, b_{22}, \ldots, b_{rr}$ are all non-zero. At this stage it is clear that $X_{r+1}, \ldots, X_n$ can be chosen arbitrarily and then $X_r, X_{r-1}, \ldots, X_1$ are determined uniquely in turn. Hence the solution space has dimension $n - r$, and the $r$ non-zero rows are linearly independent, so $r$ equals the rank of the original coefficient matrix.
