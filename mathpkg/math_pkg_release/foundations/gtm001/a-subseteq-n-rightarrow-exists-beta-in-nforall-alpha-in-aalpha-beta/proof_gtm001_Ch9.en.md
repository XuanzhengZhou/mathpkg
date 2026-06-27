---
role: proof
locale: en
of_concept: a-subseteq-n-rightarrow-exists-beta-in-nforall-alpha-in-aalpha-beta
source_book: gtm001
source_chapter: "9"
source_section: ""
---

If $\alpha \in a$, then $\alpha \subseteq \cup(a)$ and hence $\alpha = \overline{\alpha} \leq \overline{\cup(a)}$. But by Cantor's theorem

$$\overline{\cup(a)} < \overline{\mathcal{P}(\cup(a))}.$$

Remark. Cantor's theorem led him to the paradox of the largest cardinal. We formulate that paradox in the following form: Consider $N$ the "set" of all cardinal numbers. By *Proposition 10.17*, there exists a cardinal larger than any cardinal in $N$. But this contradicts the fact that $N$ contains all cardinals.

In ZF we can use this contradiction to conclude that $N$ is not a set.
