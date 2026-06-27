---
role: proof
locale: en
of_concept: isomorphism-of-free-closures
source_book: gtm006
source_chapter: "11"
source_section: "3. Generation"
---

If such a sequence exists, then clearly $\mathcal{F}(\mathcal{C}_i) = \mathcal{F}(\mathcal{C}_{i+1})$ for each $i$, since if $\mathcal{C}_{i+1}$ is a free extension of $\mathcal{C}_i$, then both generate the same free closure. By transitivity, $\mathcal{F}(\mathcal{C}_1) \cong \mathcal{F}(\mathcal{C}_n)$, so $\mathcal{F}(\mathcal{A}) \cong \mathcal{F}(\mathcal{B})$.

Conversely, suppose $\mathcal{F}(\mathcal{A}) \cong \mathcal{F}(\mathcal{B})$. By Lemma 11.7, since $\mathcal{A}$ and $\mathcal{B}$ are each contained in free extensions of each other (via the isomorphism between their free closures), there exists a configuration $\mathcal{C}$ that is a common free extension of both. Setting $\mathcal{C}_1 = \mathcal{A}$, $\mathcal{C}_2 = \mathcal{C}$, $\mathcal{C}_3 = \mathcal{B}$ gives the desired sequence: $\mathcal{C}_2$ is a free extension of $\mathcal{C}_1$ and also a free extension of $\mathcal{C}_3$ (so $\mathcal{C}_3$ is contained in a free extension of $\mathcal{C}_2$, hence by Lemma 11.6 there is a free extension relationship in the reverse direction as needed).
