---
role: proof
locale: en
of_concept: lubin-tate-construction-lemma
source_book: gtm059
source_chapter: "8"
source_section: "1. Lubin-Tate Groups"
---

We construct $F$ by induction on the degree. Write $F^{(r)}$ for the truncation of $F$ up to degree $r$. The base case $r = 1$ is given by $F^{(1)}(X) = L(X)$.

Assume we have constructed $F^{(r)}(X)$ satisfying
$$
F^{(r)}(X) \equiv L(X) \pmod{\deg 2}, \qquad f(F^{(r)}(X)) \equiv F^{(r)}(g(X)) \pmod{\deg r+1}.
$$
We seek a homogeneous polynomial $H_{r+1}(X)$ of degree $r+1$ such that $F^{(r+1)} = F^{(r)} + H_{r+1}$ satisfies the congruence modulo $\deg r+2$.

Compute:
$$
f(F^{(r+1)}(X)) = f(F^{(r)}(X) + H_{r+1}(X)).
$$
Since $f(X) \equiv \pi X \pmod{\deg 2}$, we have
$$
f(F^{(r)}(X) + H_{r+1}(X)) \equiv f(F^{(r)}(X)) + \pi H_{r+1}(X) \pmod{\deg r+2}.
$$
On the other hand,
$$
F^{(r+1)}(g(X)) = F^{(r)}(g(X)) + H_{r+1}(g(X)).
$$
Since $g(X) \equiv \pi X \pmod{\deg 2}$, we have $H_{r+1}(g(X)) \equiv \pi^{r+1} H_{r+1}(X) \pmod{\deg r+2}$ (modulo higher terms from the nonlinear part of $g$).

The condition to be satisfied modulo $\deg r+2$ is therefore:
$$
f(F^{(r)}(X)) + \pi H_{r+1}(X) \equiv F^{(r)}(g(X)) + H_{r+1}(g(X)) \pmod{\deg r+2}.
$$
By the induction hypothesis, the difference
$$
C(X) = f(F^{(r)}(X)) - F^{(r)}(g(X))
$$
has vanishing terms up to degree $r$, and we denote its degree $r+1$ part by $C_{r+1}(X)$ (a homogeneous polynomial). The required equation for the degree $r+1$ part becomes:
$$
\pi H_{r+1}(X) - \pi^{r+1} H_{r+1}(X) = -C_{r+1}(X),
$$
i.e.,
$$
(\pi - \pi^{r+1}) H_{r+1}(X) = -C_{r+1}(X).
$$
Since $\pi$ is not a zero divisor (multiplication by $\pi$ is injective), and $\pi(1 - \pi^r)$ is a non-zero-divisor, the coefficient $\pi - \pi^{r+1}$ is cancellable in each coefficient, yielding a unique homogeneous polynomial $H_{r+1}(X)$. Taking the limit as $r \to \infty$ yields the required power series $F$.

The addendum regarding completeness: The induction step determines each homogeneous component uniquely from the previous ones without requiring any completeness or convergence condition. Thus the result holds in any extension ring of $\mathfrak{o}$.
