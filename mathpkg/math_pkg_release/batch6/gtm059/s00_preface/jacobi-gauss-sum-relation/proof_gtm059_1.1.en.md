---
role: proof
locale: en
of_concept: jacobi-gauss-sum-relation
source_book: gtm059
source_chapter: "1"
source_section: "1"
---

**Proof.** We compute the product $S(\chi)S(\psi)$:

$$S(\chi)S(\psi) = \sum_{x \in F^*} \chi(x)\lambda(x) \sum_{y \in F^*} \psi(y)\lambda(y) = \sum_{x,y \in F^*} \chi(x)\psi(y)\lambda(x+y).$$

Substitute $y = xz$ where $z \in F^*$, so as $y$ runs over $F^*$, $z$ also runs over $F^*$ (for fixed $x$):

$$S(\chi)S(\psi) = \sum_{x \in F^*} \sum_{z \in F^*} \chi(x)\psi(xz)\lambda(x + xz) = \sum_{x,z \in F^*} \chi\psi(x) \psi(z) \lambda(x(1+z)).$$

Now separate the terms where $z = -1$ from those where $z \neq -1$. For $z \neq -1$, change variable $x$: since $1+z \neq 0$, the map $x \mapsto x(1+z)$ permutes $F^*$, and we obtain contributions involving $\chi\psi(1+z)^{-1}$ times the Gauss sum $S(\chi\psi)$. Summing over $z$ and using the definition of the Jacobi sum yields the formula

$$S(\chi)S(\psi) = J(\chi, \psi) S(\chi\psi)$$

when $\chi\psi \neq 1$. For the case $\chi\psi = 1$, the sum over $x$ for $z \neq -1$ becomes $\sum_x \lambda(x(1+z)) = -1$ (since $1+z \neq 0$), and the term with $z = -1$ contributes $\chi(-1)(q-1)$, leading to $J(\chi, \chi^{-1}) = -\chi(-1)$.

Rearranging gives $J(\chi, \psi) = S(\chi)S(\psi)/S(\chi\psi)$ as desired. This completes the proof.
