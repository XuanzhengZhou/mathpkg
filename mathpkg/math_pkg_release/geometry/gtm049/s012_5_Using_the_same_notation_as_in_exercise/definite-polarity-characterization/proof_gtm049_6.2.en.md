---
role: proof
locale: en
of_concept: definite-polarity-characterization
source_book: gtm049
source_chapter: "6"
source_section: "6.2"
---

The "if" part is obvious: if $\sigma$ is either positive definite or negative definite, then $\sigma(v, v) \neq 0$ for all non-zero vectors $v$, so the quadric is empty and $\perp(\sigma)$ is definite.

Assume therefore that $\sigma(v, v) \neq 0$ for all non-zero vectors $v$, i.e., that $\perp(\sigma)$ is definite. We must show that $\sigma$ is either positive definite or negative definite.

Suppose for contradiction that there exist vectors $a$ and $b$ such that $\sigma(a, a) > 0$ and $\sigma(b, b) < 0$. Then

$$\sigma(a, b)^2 - \sigma(a, a)\sigma(b, b) > 0$$

and therefore the equation

$$\sigma(Xa - b, Xa - b) = 0,$$

i.e.,

$$\sigma(a, a)X^2 - 2\sigma(a, b)X + \sigma(b, b) = 0,$$

has real roots. If $x$ is a real root, then $xa - b$ is a non-zero vector (since $b \neq 0$ and if $xa = b$ then $\sigma(b, b) = x^2\sigma(a, a)$, contradicting the sign difference) with $\sigma(xa - b, xa - b) = 0$, contradicting the assumption that the quadric is empty.

Thus $\sigma(a, a)$ cannot take both positive and negative values on non-zero vectors. Hence $\sigma$ is either positive definite or negative definite.
