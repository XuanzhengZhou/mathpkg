---
role: proof
locale: en
of_concept: negative-x-y-equals-negative-xy
source_book: gtm012
source_chapter: "1"
source_section: "2. Real and complex numbers"
---

# Proof of $(-x) \cdot y = -(xy)$

Using the field axioms, we compute:

$$(-x) \cdot y = ((-1) \cdot x) \cdot y \quad (\text{since } -x = (-1) \cdot x)$$
$$= (-1) \cdot (x \cdot y) \quad (\text{by associativity of multiplication, M1})$$
$$= -(xy) \quad (\text{since } (-1) \cdot z = -z \text{ for any } z).$$

The step $(-1) \cdot x = -x$ was established earlier from the axioms: $x + (-1) \cdot x = 1 \cdot x + (-1) \cdot x = (1 + (-1)) \cdot x = 0 \cdot x = 0$, so $(-1) \cdot x$ is the additive inverse of $x$, i.e., $-x$. Similarly, $(-1) \cdot (xy) = -(xy)$.

Thus $(-x) \cdot y = -(xy)$ for all $x, y \in \mathbb{R}$.
