---
role: proof
locale: en
of_concept: morse-multiple-critical-points-one-value
source_book: gtm033
source_chapter: "6"
source_section: "6.3"
---

# Proof of Morse Cell Decomposition for a Single Critical Value

Let $z_1, \ldots, z_m$ be the critical points of $f$, with indices $k(1), \ldots, k(m)$. Since $f$ has only one critical value $c$, we have $f(z_i) = c$ for all $i$.

We first perturb $f$ slightly to separate the critical points. Choose small disjoint neighborhoods $U_i \subset M - \partial M$ of the critical points $z_i$ and define a function $g: M \to \mathbb{R}$ as follows. Outside the union of the $U_i$, set $g = f$. In $U_i$, set

$$g(x) = f(x) + \varepsilon_i \lambda_i(x)$$

where the $C^\infty$ map $\lambda_i: M \to [0,1]$ has support in $U_i$ and equals $1$ on a neighborhood of $z_i$, while $\varepsilon_i > 0$ are chosen so that the numbers $c + \varepsilon_i$ are all distinct. As $\max \varepsilon_i$ tends to $0$, $g$ tends to $f$ in $C^2(M, \mathbb{R})$. Thus for sufficiently small $\varepsilon_i$, $g$ is a Morse function having the same critical points as $f$, and these have the same indices. Moreover, $g$ now separates the critical points: $g(z_i) \neq g(z_j)$ for $i \neq j$.

By choosing $a', b'$ with $a < a' < \min g(z_i) < \max g(z_i) < b' < b$ and applying the regular interval theorem (Theorem 2.2), it suffices to prove the theorem for $g$ restricted to $g^{-1}[a', b']$.

Now order the critical points so that $g(z_1) < g(z_2) < \cdots < g(z_m)$. Choose regular values $c_0, c_1, \ldots, c_m$ with

$$a' = c_0 < g(z_1) < c_1 < g(z_2) < \cdots < c_{m-1} < g(z_m) < c_m = b'.$$

For each $j = 1, \ldots, m$, the restriction of $g$ to $g^{-1}[c_{j-1}, c_j]$ has a unique critical point $z_j$ of index $k(j)$. Applying Theorem 3.1, there exists a $k(j)$-cell $e_j \subset g^{-1}[c_{j-1}, c_j] - g^{-1}(c_j)$ with $e_j \cap g^{-1}(c_{j-1}) = \partial e_j$, and a deformation retraction of $g^{-1}[c_{j-1}, c_j]$ onto $g^{-1}(c_{j-1}) \cup e_j$.

By induction on $j$, $g^{-1}[a', c_j]$ deformation retracts onto

$$g^{-1}(a') \cup \bigcup_{i=1}^{j} e_i.$$

For $j = m$, we obtain a deformation retraction of $g^{-1}[a', b']$ onto

$$g^{-1}(a') \cup \bigcup_{i=1}^{m} e_i.$$

Grouping the cells by their dimension, for each $k = 0, \ldots, n$ there are exactly $v_k$ cells of dimension $k$, which we denote by $e_1^k, \ldots, e_{v_k}^k$. Each $e_i^k$ satisfies $e_i^k \cap g^{-1}(a') = \partial e_i^k$. Since $g$ can be chosen arbitrarily close to $f$, the same conclusion holds for $f$ (or more precisely, the original $M$ deformation retracts onto $f^{-1}(a)$ with the cells attached, by taking the limit as $\varepsilon_i \to 0$ or by noting that $f$ and $g$ have the same sublevel set homotopy types up to a small shift of regular values).
