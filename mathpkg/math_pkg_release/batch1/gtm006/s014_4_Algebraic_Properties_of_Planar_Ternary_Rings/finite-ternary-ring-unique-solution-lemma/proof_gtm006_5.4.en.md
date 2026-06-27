---
role: proof
locale: en
of_concept: finite-ternary-ring-unique-solution-lemma
source_book: gtm006
source_chapter: "5"
source_section: "4"
---

**Proof of Lemma 5.6.** Let $(R, T)$ be a finite ternary ring satisfying condition (D). Suppose that equations of the form $T(x, a, b) = T(x, c, d)$ with $a \neq c$ have at most one solution for $x$.

Given $x, a, b, c \in R$ with $a \neq c$, define $xA$ by
$$
T(x, a, b) = T(x, c, xA).
$$
By condition (D), $xA$ is uniquely determined for each $x \in R$.

We claim the mapping $A: R \to R$ is one-to-one. If $x \neq y$ but $xA = yA$, then
$$
T(x, a, b) = T(x, c, xA), \qquad T(y, a, b) = T(y, c, xA).
$$
This implies that the equation $T(u, a, b) = T(u, c, xA)$ has the distinct solutions $u = x$ and $u = y$, contradicting the assumption that such equations have at most one solution. Hence $A$ is injective.

Since $R$ is finite, an injective map $A: R \to R$ is necessarily surjective. Therefore, for any $d \in R$, there exists a unique $x \in R$ such that $xA = d$, i.e.,
$$
T(x, a, b) = T(x, c, d).
$$
Thus the equation has exactly one solution for $x$. $\square$
