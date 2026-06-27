---
role: proof
locale: en
of_concept: hilbert-basis-theorem
source_book: gtm044
source_chapter: "3"
source_section: "3.5"
---

# Proof of Hilbert Basis Theorem

**Theorem 3.5** (Hilbert Basis Theorem). If $R$ is Noetherian, so is $R[X]$.

**Proof.** By Lemma 3.3, a ring is Noetherian iff every ideal has a finite basis. We show that if every ideal of $R$ has a finite basis, then every ideal of $R[X]$ has a finite basis.

If $r_0 X^n + \cdots + r_n$ ($r_0 \neq 0$) is any nonzero polynomial of $R[X]$, we call $r_0$ the **leading coefficient** of the polynomial. Now let $\mathfrak{A}$ be any ideal of $R[X]$. Define $\mathfrak{a}_k$ ($k = 0, 1, 2, \ldots$) to be the set of all leading coefficients of polynomials in $\mathfrak{A}$ of degree $\leq k$, together with $0$. It is easy to verify that each $\mathfrak{a}_k$ is an ideal of $R$, and that

$$\mathfrak{a}_0 \subseteq \mathfrak{a}_1 \subseteq \mathfrak{a}_2 \subseteq \cdots$$

is an ascending chain. Since $R$ satisfies the a.c.c., there is an index $m^*$ such that

$$\mathfrak{a}_{m^*} = \mathfrak{a}_{m^*+1} = \mathfrak{a}_{m^*+2} = \cdots.$$

Since each $\mathfrak{a}_k$ has a finite basis, we may write

$$\mathfrak{a}_k = (a_{k1}, \ldots, a_{kn_k}), \qquad k = 0, 1, \ldots, m^*.$$

For each such basis element $a_{kj}$, choose a polynomial $p_{kj}(X) \in \mathfrak{A}$ of degree $\leq k$ having $a_{kj}$ as its leading coefficient. Let $p_1, \ldots, p_N$ be the polynomials among the $p_{m^*j}$ ($j = 1, \ldots, n_{m^*}$) — i.e., those corresponding to the stabilized ideal $\mathfrak{a}_{m^*}$. Let $q_1(X), \ldots, q_M(X)$ be the polynomials of $\mathfrak{A}$ whose leading coefficients are the basis elements $a_{kj}$ of the ideals $\mathfrak{a}_0, \mathfrak{a}_1, \ldots, \mathfrak{a}_{m^*-1}$.

We claim that

$$\mathfrak{A} = (p_1, \ldots, p_N, q_1, \ldots, q_M).$$

Denote $(p_1, \ldots, p_N, q_1, \ldots, q_M)$ by $\mathfrak{A}^\dagger$. Since all polynomials $p_i$ and $q_j$ were chosen from $\mathfrak{A}$, obviously $\mathfrak{A}^\dagger \subseteq \mathfrak{A}$. We show $\mathfrak{A} \subseteq \mathfrak{A}^\dagger$ by contradiction. Assume $\mathfrak{A}^\dagger \subsetneq \mathfrak{A}$, and let $p$ be any polynomial of lowest degree which is in $\mathfrak{A}$ but not in $\mathfrak{A}^\dagger$. Write $p$'s leading coefficient as $a$, and let $\deg p = d$.

**Case 1:** $d \geq m^*$. Since $a \in \mathfrak{a}_d = \mathfrak{a}_{m^*}$, we can write $a = \sum_{i=1}^{N} r_i a_i$, where $a_i$ are the leading coefficients of $p_1, \ldots, p_N$. Consider the linear combination

$$\sum_{i=1}^{N} r_i X^{d - \deg p_i} \cdot p_i.$$

Since $d \geq m^* \geq \deg p_i$ for each $i$, the exponents $d - \deg p_i$ are nonnegative. The leading term of each summand $r_i X^{d - \deg p_i} p_i$ is $r_i a_i X^d$, so the sum has leading term $(\sum_i r_i a_i) X^d = a X^d$, which is exactly the leading term of $p$. Therefore

$$p - \sum_{i=1}^{N} r_i X^{d - \deg p_i} p_i$$

is a polynomial in $\mathfrak{A}$ of degree strictly less than $d$, and it belongs to $\mathfrak{A}^\dagger$ (since the subtracted sum does). Moreover, $p$ itself differs from this element by an element of $\mathfrak{A}^\dagger$, so if the lower-degree polynomial is in $\mathfrak{A}^\dagger$, then $p$ must be as well. But $p$ was chosen to have minimal degree among elements of $\mathfrak{A} \setminus \mathfrak{A}^\dagger$. This contradiction shows that this case cannot occur.

**Case 2:** $d < m^*$. Then $a \in \mathfrak{a}_d$, so we can write $a = \sum_{j} s_j a_{dj}$, where $a_{dj}$ are the leading coefficients of the polynomials $q_j$ corresponding to $\mathfrak{a}_d$. By an analogous argument using $X^{d - \deg q_j} q_j$ in place of $X^{d - \deg p_i} p_i$, we reach the same contradiction.

Since both cases lead to contradictions, our assumption $\mathfrak{A}^\dagger \subsetneq \mathfrak{A}$ is false. Hence $\mathfrak{A} = \mathfrak{A}^\dagger = (p_1, \ldots, p_N, q_1, \ldots, q_M)$ has a finite basis.

Thus $R[X]$ satisfies the finite basis condition, so by Lemma 3.3, $R[X]$ is Noetherian. $\square$
