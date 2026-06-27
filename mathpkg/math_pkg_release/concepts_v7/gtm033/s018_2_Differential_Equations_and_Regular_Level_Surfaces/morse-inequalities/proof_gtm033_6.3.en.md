---
role: proof
locale: en
of_concept: morse-inequalities
source_book: gtm033
source_chapter: "6"
source_section: "6.3"
---

# Proof of Morse Inequalities

It is convenient to assume that $f$ separates the critical points, that is, $f(z_i) \neq f(z_j)$ if $z_i, z_j$ are distinct critical points. This can be arranged by perturbing $f$ slightly in disjoint neighborhoods $U_i \subset M - \partial M$ of the critical points $z_i$ to get a function $g: M \to \mathbb{R}$ of the following type. Outside the union of the $U_i$, $g = f$. In $U_i$ we have

$$g(x) = f(x) + \varepsilon_i \lambda_i(x)$$

where the $C^\infty$ map $\lambda_i: M \to [0,1]$ has support in $U_i$ and equals $1$ on a neighborhood of $z_i$, while $\varepsilon_i > 0$. As $\max \varepsilon_i$ tends to $0$, $g$ tends to $f$ in $C^2(M, \mathbb{R})$. Thus for small $\varepsilon_i$, $g$ will be a Morse function having the same critical points as $f$, and these will have the same indices. We can choose the $\varepsilon_i$ so that $g$ separates the critical points.

By the regular interval theorem (Theorem 2.2), the relative homology $H_*(M, f^{-1}(a); F)$ is isomorphic to $H_*(M, g^{-1}(a); F)$ (up to a small shift of regular values). Thus we may assume that $f$ already separates its critical points.

Order the critical points $z_1, \ldots, z_m$ so that $f(z_1) < f(z_2) < \cdots < f(z_m)$. Let $k(j)$ denote the index of $z_j$. Choose regular values $c_0, c_1, \ldots, c_m$ with

$$a = c_0 < f(z_1) < c_1 < f(z_2) < \cdots < c_{m-1} < f(z_m) < c_m = b.$$

Set $A = f^{-1}(a)$ and $X_j = f^{-1}(-\infty, c_j]$ for $j = 0, \ldots, m$. Note that $X_0 = A$ and $X_m = M$. By Theorem 3.1, $X_j$ is obtained from $X_{j-1}$ by attaching a $k(j)$-cell. Hence the pair $(X_j, X_{j-1})$ has homology concentrated in degree $k(j)$:

$$H_i(X_j, X_{j-1}; F) \cong \begin{cases} F & \text{if } i = k(j) \\ 0 & \text{otherwise}. \end{cases}$$

Define

$$\beta(i, j) = \dim_F H_i(X_j, A; F),$$
$$\alpha(i, j) = \dim_F H_i(X_j, X_{j-1}; F).$$

Since $X_j$ is obtained from $A$ by adding cells of dimensions $\leqslant n$, we have $\beta(i, j) = 0$ for $i > n$.

**Proof of part (b).** Consider the exact homology sequence of the triple $(X_j, X_{j-1}, A)$:

$$0 \to H_n(X_{j-1}, A) \to H_n(X_j, A) \to H_n(X_j, X_{j-1}) \to H_{n-1}(X_{j-1}, A) \to \cdots \to H_0(X_j, X_{j-1}) \to 0.$$

Exactness implies the vanishing of the corresponding alternating sum of dimensions of the vector spaces in the sequence. Grouping three terms at a time in this alternating sum gives:

$$0 = \sum_{i=0}^{n} (-1)^i \bigl[\beta(i, j-1) - \beta(i, j) + \alpha(i, j)\bigr].$$

Summing over $j$ from $1$ to $m$ yields:

$$\sum_{i=0}^{n} (-1)^i \left[ \sum_{j=1}^{m} \alpha(i, j) \right] = \sum_{i=0}^{n} (-1)^i \bigl[\beta(i, m) - \beta(i, 0)\bigr] = \sum_{i=0}^{n} (-1)^i \beta_i$$

because $\beta(i, m) = \dim_F H_i(M, A; F) = \beta_i$ and $\beta(i, 0) = \dim_F H_i(A, A; F) = 0$. Now

$$\sum_{j=1}^{m} \alpha(i, j)$$

is precisely the number of $j \in \{1, \ldots, m\}$ such that $k(j) = i$, which is $v_i$. Therefore

$$\sum_{i=0}^{n} (-1)^i v_i = \sum_{i=0}^{n} (-1)^i \beta_i = \chi'(M, f^{-1}(a)).$$

This proves part (b).

**Proof of part (a).** For each $j = 1, \ldots, m$ and each $m = 0, \ldots, n$, consider the segment of the exact sequence of the triple $(X_j, X_{j-1}, A)$:

$$0 \to K_{m,j} \to H_m(X_{j-1}, A) \to H_m(X_j, A) \to H_m(X_j, X_{j-1}) \to \cdots$$

where $K_{m,j}$ is the kernel of the map $H_m(X_{j-1}, A) \to H_m(X_j, A)$. From exactness we obtain the inequality

$$\beta(m, j-1) - \beta(m, j) + \alpha(m, j) \geqslant 0$$

for each $m$ and $j$. More generally, one can prove that the alternating sums

$$S_m = \sum_{i=0}^{m} (-1)^{m-i} \beta(i, j)$$

satisfy $S_m(j) \leqslant S_m(j-1) + \alpha(m, j)$, where the difference accounts for the $m$-cell attached at step $j$. Summing these inequalities over all $j$ yields

$$\sum_{k=0}^{m} (-1)^{k+m} v_k \geqslant \sum_{k=0}^{m} (-1)^{k+m} \beta_k$$

for $0 \leqslant m \leqslant n$, which is precisely part (a) of Theorem 3.4.
