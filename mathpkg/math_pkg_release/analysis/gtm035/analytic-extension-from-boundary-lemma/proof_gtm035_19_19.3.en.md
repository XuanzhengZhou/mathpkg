---
role: proof
locale: en
of_concept: analytic-extension-from-boundary-lemma
source_book: gtm035
source_chapter: "Chapter 19"
source_section: "19.3"
---

# Proof of Analytic Extension from Boundary Lemma

**Proof.** By shrinking $\alpha$ we may assume that there is an integer $l$, $0 \leq l \leq M$, such that, for each $a \in \alpha$, $G(a, w)$ can be written as a quotient of two relatively prime polynomials in $w$ such that the denominator is always of degree exactly equal to $l$.

$\mathfrak{A}$ is an integral domain, and we form the field of quotients of $\mathfrak{A}$, denoted $\mathcal{F}$. The space $\mathcal{F}^{l+1}$ of $(l+1)$-tuples $(t_1, \ldots, t_{l+1})$ of elements of $\mathcal{F}$ is then an $(l+1)$-dimensional vector space over $\mathcal{F}$.

We denote by $\mathcal{W}$ the subspace of $\mathcal{F}^{l+1}$ spanned by the set of vectors

$$(g_{-i}, g_{-i-1}, \ldots, g_{-i-l}), \quad i = 1, 2, \ldots$$

We claim that $\dim \mathcal{W} < l + 1$. Suppose not. Then $\mathcal{W} = \mathcal{F}^{l+1}$ and, in particular, there exist indices $i_1, i_2, \ldots, i_{l+1}$ such that the corresponding $l+1$ vectors form a basis of $\mathcal{F}^{l+1}$. In the standard basis, let $D$ be the determinant of the $(l+1) \times (l+1)$ matrix whose rows are these vectors. Then $D \in \mathfrak{A}$ and $D \neq 0$.

Now fix $a \in \alpha$. Since $G(a, w)$ is rational, there exist polynomials $P(w)$ and $Q(w)$ such that $G(a, w) = P(w)/Q(w)$ with $\deg Q = l$. Write $Q(w) = q_l^0 w^l + \cdots + q_0^0$ with $q_l^0 \neq 0$. Then $G(a, w) Q(w) = P(w)$ is a polynomial, so expanding the Laurent series of $G(a, w)$ times $Q(w)$ yields no negative powers of $w$. Equating the coefficients of $w^{-1}, w^{-2}, \ldots, w^{-(l+1)}$ to zero gives the system of $l + 1$ equations:

$$g_{-i_\nu}(a) q_0^0 + g_{-i_\nu-1}(a) q_1^0 + \cdots + g_{-i_\nu-l}(a) q_l^0 = 0, \quad \nu = 1, 2, \ldots, l + 1.$$

The coefficient matrix of this system has a vanishing determinant, since $q_l^0 \neq 0$. Thus $D(a) = 0$.

This holds for each $a \in \alpha$. Since $D$ is analytic on $\Omega$ and continuous on $\Omega \cup \alpha$, it follows that $D = 0$ in $\mathfrak{A}$. This is a contradiction and so $\dim \mathcal{W} < l + 1$, as claimed.

Because of the claim, there exists $(C_0, C_1, \ldots, C_l) \in \mathcal{F}^{l+1}$ with not all $C_j = 0$, such that

$$g_{-i} C_0 + g_{-i-1} C_1 + \cdots + g_{-i-l} C_l = 0, \quad i = 1, 2, \ldots$$

Since each $C_j \in \mathcal{F}$, it follows by clearing the denominators that there exist $q_j \in \mathfrak{A}$, $j = 0, 1, \ldots, l$, not all zero, so that

$$g_{-i} q_0 + g_{-i-1} q_1 + \cdots + g_{-i-l} q_l = 0, \quad i = 1, 2, \ldots$$

But this is equivalent to

$$\left( \sum_{k=-\infty}^{N} g_k(z) w^k \right) \left( \sum_{j=0}^{l} q_j(z) w^j \right) = \sum_{j=0}^{k} p_j(z) w^j,$$

for some functions $p_0, p_1, \ldots, p_k \in \mathfrak{A}$. This yields Lemma 19.3. $\square$
