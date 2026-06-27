---
role: proof
locale: en
of_concept: integral-closure-contained-in-finite-module
source_book: gtm028
source_chapter: "V"
source_section: "§4. Finiteness theorems"
---

**First proof.** We first notice that if we denote by $A^*$ the set of non-zero elements of $A$ then we have $F = A'_{A^*}$; that is, given any element $x$ of $F$ there exists a non-zero element $s$ of $A$ such that $sx \in A'$: in fact, if $X^n + c_{n-1}X^{n-1} + \cdots + c_0$ is the minimal polynomial of $x$ over $K$ ($c_i \in K$), and if we take a common denominator $s \neq 0$ in $A$ such that $sc_i \in A$ for all $i$, then $sx$ satisfies the monic polynomial $X^n + sc_{n-1}X^{n-1} + \cdots + s^n c_0$ with coefficients in $A$, hence $sx \in A'$. Therefore we can find a basis $\{u_1, \cdots, u_n\}$ of $F$ over $K$ contained in $A'$. Let $d = d(u_1, \cdots, u_n)$ be the discriminant of this basis. By Theorem 4 of §3, we have $d \in A$. Since $F$ is separable over $K$, the discriminant $d$ is non-zero. For each $i$, write

$$u_i = \frac{v_i}{d}$$

with $v_i \in A'$, where the trace-based construction gives $db_i \in A$ (cf. II, §11, p. 92), and since $A$ is integrally closed, we have $db_i \in A$. Therefore, if we take $x_i = u_i/d$, then $A'$ is contained in the $A$-module $\sum_i A x_i$.

**Second proof (using trace form).** Let $\{u_1, \cdots, u_n\}$ be a basis of $F$ over $K$ contained in $A'$. The bilinear function $(x, y) \mapsto T(xy)$ is non-degenerate since $F$ is separable over $K$. Thus it defines an isomorphism of $F$, considered as a vector space over $K$, onto its dual. Let $\{v_1, \cdots, v_n\}$ be the elements of $F$ corresponding to those of the dual basis of $\{u_1, \cdots, u_n\}$, that is, the elements of $F$ satisfying $T(u_i v_j) = \delta_{ij}$ for all $i, j$. If an element $x = \sum_j x_j v_j$ ($x_j \in K$) is in $A'$, we have $x u_i \in A'$ for every $i$, whence $T(x u_i) \in A$ (§3, Theorem 4). Since

$$T(x u_i) = \sum_j x_j T(u_i v_j) = x_i,$$

we have $x_i \in A$ for all $i$, and therefore $A' \subset \sum_j A v_j$. This type of reasoning will again be used in §11 (see the proof of Theorem 30).
