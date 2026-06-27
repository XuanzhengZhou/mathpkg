---
role: proof
locale: en
of_concept: pseudo-metric-to-metric-quotient
source_book: gtm002
source_chapter: "10"
source_section: "10"
---

Define the relation $x \sim y$ whenever $\varrho(x, y) = 0$. This is an equivalence relation: reflexivity $\varrho(x,x) = 0$ and symmetry $\varrho(x,y) = \varrho(y,x)$ are immediate from the axioms of a pseudo-metric. For transitivity, if $\varrho(x,y) = 0$ and $\varrho(y,z) = 0$, then by the triangle inequality $\varrho(x,z) \leq \varrho(x,y) + \varrho(y,z) = 0$, so $\varrho(x,z) = 0$.

Let $\tilde{X} = X/{\sim}$ be the set of equivalence classes. For $[x], [y] \in \tilde{X}$, define $\varrho([x], [y]) = \varrho(x, y)$. To verify well-definedness, suppose $x \sim x'$ and $y \sim y'$. Then

$$\varrho(x', y') \leq \varrho(x', x) + \varrho(x, y) + \varrho(y, y') = 0 + \varrho(x, y) + 0 = \varrho(x, y),$$

and similarly $\varrho(x, y) \leq \varrho(x', y')$, so $\varrho(x', y') = \varrho(x, y)$. Thus the distance depends only on equivalence classes.

Now $(\tilde{X}, \varrho)$ satisfies all four metric axioms. The first three are inherited from the pseudo-metric. For the fourth axiom, if $\varrho([x], [y]) = 0$, then $\varrho(x, y) = 0$, so $x \sim y$ and $[x] = [y]$. Therefore $(\tilde{X}, \varrho)$ is a metric space.
