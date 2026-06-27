---
role: proof
locale: en
of_concept: adjunction-of-unity
source_book: gtm015
source_chapter: "VI"
source_section: "49"
---

# Proof of Adjunction of Unity to a Normed Algebra

Let $A$ be a normed algebra (with or without unity element), let $A_1 = A \times \mathbb{C}$ be the algebra unitification of $A$ (as constructed in 49.4), and define for $x \in A$, $\lambda \in \mathbb{C}$:
$$\|x + \lambda u\| = \|x\| + |\lambda|,$$
where $u = (0, 1)$ is the adjoined unity element.

**$\|\cdot\|$ is a norm:** Clearly $\|x + \lambda u\| \geq 0$, with equality iff $\|x\| = 0$ and $|\lambda| = 0$, i.e., $x = 0$ and $\lambda = 0$. The triangle inequality follows from those for $\|\cdot\|$ on $A$ and $|\cdot|$ on $\mathbb{C}$:
$$\|(x + \lambda u) + (y + \mu u)\| = \|(x+y) + (\lambda+\mu)u\| = \|x+y\| + |\lambda+\mu| \leq \|x\| + \|y\| + |\lambda| + |\mu| = \|x+\lambda u\| + \|y+\mu u\|.$$
Absolute homogeneity is clear.

**Submultiplicativity:** For $(x + \lambda u), (y + \mu u) \in A_1$,
$$(x + \lambda u)(y + \mu u) = xy + \mu x + \lambda y + \lambda\mu u.$$

Therefore
$$\|(x + \lambda u)(y + \mu u)\| = \|xy + \mu x + \lambda y\| + |\lambda\mu|$$
$$\leq \|x\|\|y\| + |\mu|\|x\| + |\lambda|\|y\| + |\lambda||\mu|$$
$$= (\|x\| + |\lambda|)(\|y\| + |\mu|) = \|x + \lambda u\|\|y + \mu u\|.$$

**Unity norm:** $\|u\| = \|0 + 1 \cdot u\| = \|0\| + |1| = 1$.

Thus $A_1$ is a normed algebra with the stated properties. The embedding $x \mapsto x + 0u$ of $A$ into $A_1$ is isometric: $\|x + 0u\| = \|x\| + 0 = \|x\|$. $\square$
