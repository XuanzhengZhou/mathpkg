---
role: proof
locale: en
of_concept: pseudo-metric-to-metric-quotient
source_book: gtm002
source_chapter: "10"
source_section: "10"
---

Define a relation $\sim$ on the pseudo-metric space $X$ by $x \sim y$ if and only if $\varrho(x, y) = 0$. We verify that $\sim$ is an equivalence relation:

- **Reflexivity**: $\varrho(x, x) = 0$ by the first metric axiom, so $x \sim x$.
- **Symmetry**: If $x \sim y$, then $\varrho(x, y) = 0$. By the symmetry axiom, $\varrho(y, x) = \varrho(x, y) = 0$, so $y \sim x$.
- **Transitivity**: If $x \sim y$ and $y \sim z$, then $\varrho(x, y) = 0$ and $\varrho(y, z) = 0$. By the triangle inequality, $\varrho(x, z) \leq \varrho(x, y) + \varrho(y, z) = 0$. Since $\varrho(x, z) \geq 0$, we have $\varrho(x, z) = 0$, so $x \sim z$.

Now let $\tilde{X}$ be the set of equivalence classes $[x] = \{y \in X : \varrho(x, y) = 0\}$. Define $\tilde{\varrho}([x], [y]) = \varrho(x, y)$. We must show this is well-defined: if $x' \in [x]$ and $y' \in [y]$, then by the triangle inequality,
$$\varrho(x', y') \leq \varrho(x', x) + \varrho(x, y) + \varrho(y, y') = 0 + \varrho(x, y) + 0 = \varrho(x, y).$$
Similarly, $\varrho(x, y) \leq \varrho(x', y')$, so $\varrho(x', y') = \varrho(x, y)$. Thus $\tilde{\varrho}$ is well-defined.

The first three metric axioms for $\tilde{\varrho}$ follow immediately from those of $\varrho$. For the fourth axiom: if $\tilde{\varrho}([x], [y]) = 0$, then $\varrho(x, y) = 0$, so $x \sim y$, hence $[x] = [y]$. Therefore $(\tilde{X}, \tilde{\varrho})$ is a genuine metric space.
