---
role: proof
locale: en
of_concept: flow-space-dimension
source_book: gtm054
source_chapter: "IV"
source_section: "B"
---

**Proof of (a).** From the fundamental result
$$\dim(\mathbb{Q}^W) = \dim(\ker \partial) + \dim(\partial[\mathbb{Q}^W])$$
it follows that
$$\dim(F) = |W| - \dim(\partial[\mathbb{Q}^W]) = |V|^2 - |V| - \dim(\partial[\mathbb{Q}^W]).$$

Let $L = \{g \in \mathbb{Q}^V : \sum_{x \in V} g(x) = 0\}$. Clearly $L$ is the kernel of the transformation $h \mapsto \sum_{x \in V} h(x)$ from $\mathbb{Q}^V$ onto $\mathbb{Q}$. Hence
$$\dim(L) = \dim(\mathbb{Q}^V) - \dim(\mathbb{Q}) = |V| - 1,$$
and to prove (a) it will suffice to prove that $L = \partial[\mathbb{Q}^W]$.

From B1 we have that for each $h \in \mathbb{Q}^W$,
$$\sum_{x \in V} \partial(h)(x) = 0,$$
so $\partial(h) \in L$, and hence $\partial[\mathbb{Q}^W] \subseteq L$. The reverse inclusion $L \subseteq \partial[\mathbb{Q}^W]$ is proved by considering the standard basis elements, showing that $\dim(\partial[\mathbb{Q}^W]) = |V| - 1$, which yields the desired formula.

**Proof of (b).** From the dimension formula for orthogonal complements,
$$\dim(F^\perp) = \dim(\mathbb{Q}^W) - \dim(F) = |V|^2 - |V| - (|V| - 1)^2 = |V| - 1.$$
