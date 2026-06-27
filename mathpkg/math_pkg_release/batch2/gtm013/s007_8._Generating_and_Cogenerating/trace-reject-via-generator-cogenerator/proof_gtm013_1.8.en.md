---
role: proof
locale: en
of_concept: trace-reject-via-generator-cogenerator
source_book: gtm013
source_chapter: "1"
source_section: "8"
---

Since $G$ is a generator for $\mathrm{Gen}(\mathcal{U})$, we have $\{G\} \subseteq \mathrm{Gen}(\mathcal{U})$ and $\mathcal{U} \subseteq \mathrm{Gen}(G)$. By Lemma 8.19(1), this implies $\mathrm{Tr}_M(G) \leq \mathrm{Tr}_M(\mathcal{U})$ and $\mathrm{Tr}_M(\mathcal{U}) \leq \mathrm{Tr}_M(G)$. Hence $\mathrm{Tr}_M(\mathcal{U}) = \mathrm{Tr}_M(G)$.

The dual argument using Lemma 8.19(2) and the fact that $C$ is a cogenerator for $\mathrm{Cog}(\mathcal{U})$ yields $\mathrm{Rej}_M(\mathcal{U}) = \mathrm{Rej}_M(C)$.
