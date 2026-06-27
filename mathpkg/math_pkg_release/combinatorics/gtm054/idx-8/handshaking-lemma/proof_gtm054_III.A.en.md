---
role: proof
locale: en
of_concept: handshaking-lemma
source_book: gtm054
source_chapter: "III"
source_section: "A"
---

Let $M$ be an incidence matrix for $\Gamma = (V, f, E)$. Counting the 1's in $M$ by rows gives $\sum_{x \in V} \rho(x)$, since each row corresponding to vertex $x$ contains exactly $\rho(x)$ entries equal to 1. Since there are precisely two 1's in each column of $M$ (each edge is incident with exactly two vertices, counting multiplicities), the total number of 1's is also $2\nu_1(\Gamma)$. Equating the two counts yields

$$\sum_{x \in V} \rho(x) = 2\nu_1(\Gamma),$$

hence $\nu_1(\Gamma) = \frac{1}{2} \sum_{x \in V} \rho(x)$.
