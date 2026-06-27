---
role: proof
locale: en
of_concept: frobenius-endomorphism
source_book: gtm028
source_chapter: "II"
source_section: "4. The characteristic of a field"
---

Let $k$ be a field of characteristic $p \neq 0$, and define $F: k \to k$ by $F(x) = x^p$. Let $k^p = \{a^p \mid a \in k\}$ be the image of $F$.

**$k^p$ is closed under addition and subtraction:** For any $b^p, c^p \in k^p$ (with $b, c \in k$), the identity (6) gives
$$
b^p \pm c^p = (b \pm c)^p \in k^p.
$$

**$k^p$ is closed under multiplication and division:** For $b^p, c^p \in k^p$,
$$
b^p c^p = (bc)^p \in k^p,
$$
and if $c \neq 0$,
$$
b^p / c^p = (b/c)^p \in k^p.
$$

These closure properties show that $k^p$ is a subfield of $k$.

**$F$ is a field homomorphism:** For any $x, y \in k$,
$$
F(x + y) = (x + y)^p = x^p + y^p = F(x) + F(y) \quad \text{(by identity (6))},
$$
$$
F(xy) = (xy)^p = x^p y^p = F(x)F(y),
$$
$$
F(1) = 1^p = 1.
$$

Thus $F$ is a homomorphism of fields, called the Frobenius endomorphism. It is injective since every field homomorphism has trivial kernel.
