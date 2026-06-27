---
role: proof
locale: en
of_concept: corollary-3-8
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. If $\alpha \in f(\mathbb{C})$, apply the preceding theorem to $f - \alpha$.

Exercises

1. Let $f$ be analytic in a region $G$ and suppose that $f$ is not identically zero. Let $G_0 = G - \{z: f(z) = 0\}$ and define $h: G_0 \to \mathbb{R}$ by $h(z) = \log |f(z)|$. Show that $\frac{\partial h}{\partial x} - i \frac{\partial h}{\partial y} = \frac{f'}{f}$ on $G_0$.

2. Refer to Exercise 2.7 and show that if $\lambda_1 \neq \lambda_2$ then $\lambda = \max(\lambda_1, \lambda_2)$.

3. (a) Let $f$ and $g$ be entire functions of finite order $\lambda$ and suppose that $f(a_n) = g(a_n)$ for a sequence $\{a_n\}$ such that $\sum |a_n|^{-(\lambda + 1)} = \infty$. Show that $f = g$.

(b) Use Exercise 2.8 to show that if $f, g$ and $\{a_n\}$ are as in part (a) with $\sum |a_n|^{-(\lambda + \epsilon)} = \infty$ for some $\epsilon > 0$ then $f = g$.

(c) Find all entire functions $f$ of finite order such that $f(\log n) = n$.

(d) Give an example of an entire function with zeros $\{\log 2, \log 3, \ldots\}$ and no other zeros.

Chapter XII

The Range of an Analytic Function

In this chapter the range of an analytic function is investigated. A generic problem of this type is the following: Let $F$ be a family of analytic functions on a region $G$ which satisfy some property $P$. What can be said about $f(G)$ for each $f$ in $F$? Are the sets $f(G)$ uniformly big in some sense? Does there exist a ball $B(a; r)$ such that $f(G) \supset B(a; r)$ for each $f$ in $F$? Needless to say, the answers to such questions depend on the property $P$ that is used to define $F$.

In fact there are a few theorems of this type that have already been encountered. For example, the Casorati-Weierstrass Theorem says that if $G = \{z: 0 < |z-a| < r\}$ and $F$ is the set of analytic functions on $G$ with an essential singularity at $z = a$, then for each $\delta, 0 < \delta < r$, and each $f$ in $F$ $f(\text{ann} (a; 0; \delta))$ is dense in $\mathbb{C}$ (V. 1.21). Recall (Exercise V. 1.13) that if $f$ is entire and $f(1/z)$ has a pole at $z = 0$, then $f$ is a polynomial. So if $f$ is not a polynomial then $f(1/z)$ has an essential singularity at $z = 0$. So as a corollary to the Casorati-Weierstrass Theorem, $f(\mathbb{C})$ is dense in $\mathbb{C}$ for each entire function (if $f$ is a polynomial then $f(\mathbb{C}) = \mathbb{C}$).

This chapter will culminate in the Great Picard Theorem that substantially improves the Casorati-Weierstrass Theorem. Indeed, it states that if $f$ has an essential singularity at $z = a$ then $f(\text{ann} (a; 0; \delta))$ is equal to the entire plane with possibly one point deleted. Moreover, $f$ assumes each
