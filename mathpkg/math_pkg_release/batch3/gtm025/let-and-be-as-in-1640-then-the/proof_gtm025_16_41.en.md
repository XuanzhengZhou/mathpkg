---
role: proof
locale: en
of_concept: "let-and-be-as-in-1640-then-the"
source_book: gtm025
source_chapter: "Integration on Locally Compact Spaces"
source_section: "16.41"
---

Equality (iv) was established in (16.40). Equalities (i)–(iii) follow from the uniqueness of the adjoint and the following computations:

$$\langle (T_1 + T_2)(x), y \rangle = \langle T_1(x), y \rangle + \langle T_2(x), y \rangle$$
$$= \langle x, T_1^*(y) \rangle + \langle x, T_2^*(y) \rangle$$
$$= \langle x, (T_1^* + T_2^*)(y) \rangle$$
$$\langle (\alpha T)(x), y \rangle = \alpha \langle T(x), y \rangle = \alpha \langle x, T^*(y) \rangle$$
$$= \langle x, \bar{\alpha} T^*(y) \rangle$$
$$\langle (T_1 T_2)(x), y \rangle = \langle T_1(T_2(x)), y \rangle = \langle T_2(x), T_1^*(y) \rangle = \langle x

(16.44) Exercise. Let $H$ and $A$ be as in (16.43) and let $z$ be any element of $H$. Prove that there is a unique element $y_0 \in A$ such that

$$\|y_0 - z\| = \inf\{\|y - z\| : y \in A\}.$$

[The right side of (i) is the distance from $\{z\}$ to $A$ as defined in (6.87).]

[Hints. Cf. (15.16.c), noting that $H$ is uniformly convex; or apply the parallelogram law directly. Choose a sequence $(y_n)$ of elements in $A$ such that $\lim_{n \to \infty} \|y_n - z\| = \inf\{\|y - z\| : y \in A\}$. Apply uniform convexity to $y_n - z$ and $y_m + z$ to infer that $(y_n)$ is a Cauchy sequence and so has a limit $y_0$ in $A$. Uniqueness is proved similarly.]

(16.45) Exercise. Let $H$ be an inner product space and let $\{x_n\}_{n=1}^{\infty}$ be a set of vectors in $H$. Let $S_n$ be the linear space spanned by $\{x_1, \ldots, x_n\}$. Suppose that $x_n$ is the element of $S_n$ nearest to $x_{n+1}$ for $n = 1, 2, 3, \ldots$.

[This element exists by (16.43.c) and (16.44).] The set $\{x_n\}_{n=1}^{\infty}$ is called a martingale in the wide sense. Write $y_1 = x_1$ and $y_n = x_n - x_{n-1}$ for $n > 1$. Prove the following.

(a) The vectors $y_n$ are pairwise orthogonal and $x_n = y_1 + \cdots + y_n$.

(b) The inequalities $\|x_1\| \leq \|x_2\| \leq \cdots

and $g \in \mathfrak{F}$ imply $gf \in \mathfrak{M}$ [i.e., $\mathfrak{M}$ is invariant under multiplication by functions in $\mathfrak{F}$]. Let $P$ be the projection of $\mathfrak{L}_2$ onto $\mathfrak{M}$ as defined in (16.47). Prove that $P(\varphi) = P(1) \cdot \varphi$ for all $\varphi \in \mathfrak{L}_2$ and that $P(1) = \xi_E$ for some set $E \in \mathfrak{A}$. Thus $\mathfrak{M}$ is exactly the set of all functions in $\mathfrak{L}_2$ that vanish on $E'$. Note that every such set is plainly a closed subspace of $\mathfrak{L}_2$ invariant under multiplication by functions in $\mathfrak{F}$. [Hints. Consider any $h \in \mathfrak{M}^\perp$, $f \in \mathfrak{M}$, and $g \in \mathfrak{F}$. We have

$$\int_X f \overline{gh} d\mu = \int_X (f\bar{g}) \bar{h} d\mu = 0$$

and so $\mathfrak{M}^\perp$ too is invariant under multiplication by functions in $\mathfrak{F}$. Since $1 - P(1) \in \mathfrak{M}^\perp$, it follows that $P\left(g(1 - P(1))\right) = 0$ and so $P(g) = P(gP(1)) = gP(1)$ for all $g \in \mathfrak{F}$. As $\mathfrak{F}$ is dense in $\mathfrak{L}_2$, we infer that $P(\varphi) = \varphi P(1)$ for all $\varphi \in \mathfrak{L}_2$. Since $P(1) = P(1)^2$, we have $P(1) = \xi_E$.

(b) Let $(X, \mathfrak{A}, \mu)$ be a $\sigma$-finite measure space

Let $\mathfrak{d}$ be the orthogonal dimension of the Hilbert space $\mathfrak{L}_2(X, \mathcal{A}, \mu)$. Prove the following assertions. If $\mathfrak{d}$ is finite, then $m = 2^b$. If $\mathfrak{d}$ is infinite, then $m = \mathfrak{d}$. [Hints. Consider first the case in which $\mu$ assumes only finitely many values, and use (10.56.a) and (12.60) to prove that $m = 2^b$. If $\mu$ assumes infinitely many values, then (10.56.c) shows that $\mathfrak{d}$ is infinite. In this case, the inequalities $m \leq \mathfrak{d}$ and $\mathfrak{d} \leq m$ are proved by simple arguments.]

(16.54) Exercise. Let $H$ be the real Hilbert space $l'_2(R)$. For each $t \in R$ let $u_t$ be that element of $H$ defined on $R$ by $u_t(s) = \delta_{t,s}$ [Kronecker's delta]. Define $X = \{f \in H : f = \alpha u_t$ for some $t \in R, 0 \leq \alpha \leq 1\}$. Then $X$, with the metric of $H$, is a metric space. Prove that there exists a one-to-one mapping $\varphi$ of $X$ onto the French railroad space $(D, \varrho)$ [see (6.13.e)] such that both $\varphi$ and $\varphi^{-1}$ are uniformly continuous.

(16.55) Exercise. Let $H$ be a Hilbert space and let $T \in \mathfrak{B}(H)$. Write $\alpha(T) = \sup\{| \langle Tx, x \rangle | : x \in H, \|x\| = 1\}$.

(a) Prove that $\alpha(T) = \|T\|$ if $T = T^*$. [Use the identity $4 \|Tx\|^3 = \langle T(\|Tx\| x + Tx), \|Tx

CHAPTER FIVE

Differentiation

This chapter contains first a brief but reasonably complete treatment of the theory of differentiation for complex-valued functions defined on intervals of the line. Section 17 is severely classical, containing examples and Lebesgue's famous theorem on differentiation of functions of finite variation. In § 18, we explore the conditions under which the classical equality

$$f(b) - f(a) = \int_{a}^{b} f'(t) dt$$

is valid. This exploration leads to interesting and perhaps unexpected measure-theoretic ideas, which have little to do with differentiation and which have applications in extraordinarily diverse fields. The main result in this direction is the Lebesgue-Radon-Nikodym theorem, which we examine thoroughly in § 19 and apply to the decomposition of measures on $R$. In § 20, we present several other applications of the Lebesgue-Radon-Nikodym theorem to problems in abstract analysis. Sections 17 and 18 are important, and should be studied by all readers. The same is true of § 19, up to and including (19.24). The remainder of § 19 may be omitted by readers pressed for time. Of § 20, (20.1)–(20.5) and (20.41)–(20.52) are topics important for every student. The remainder of § 20 is in our opinion interesting but less vital, and it too may be omitted by readers pressed for time.

§ 17. Differentiable and nondifferentiable functions

This section deals solely with functions defined on intervals of $R$. While reasonably elementary, it is an indispensable introduction to the more sophisticated matters considered in §§ 18 and 19. Throughout this section, "almost everywhere" means "λ-almost everywhere" and "measurable" means "𝔼𝔼-measurable". As usual, we begin with some definitions.
