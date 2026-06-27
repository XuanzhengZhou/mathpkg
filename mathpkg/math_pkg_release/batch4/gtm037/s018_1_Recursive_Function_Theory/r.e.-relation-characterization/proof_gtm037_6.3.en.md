---
role: proof
locale: en
of_concept: r.e.-relation-characterization
source_book: gtm037
source_chapter: "6"
source_section: "6.3"
---

The equivalences are established by a series of implications. The main direction, showing that any r.e. relation is enumerable by elementary functions, proceeds as follows.

We may assume that $R \neq \emptyset$; say $(a_0, \ldots, a_{m-1}) \in R$. Now for $i < m$ and any $x \in \omega$ let

$$f_i x = (x)_i \quad \text{if } (e, (x)_0, \ldots, (x)_m) \in T_m,$$
$$f_i x = a_i \quad \text{otherwise}.$$

Clearly each $f_i$ is elementary and $R = \{(f_0 x, \ldots, f_{m-1} x) : x \in \omega\}$.

The remaining implications show that each condition implies the next in a cycle establishing the equivalence of all ten formulations. In particular, (ix) characterizes r.e. relations as domains of partial recursive functions, and (x) characterizes them as projections of recursive relations (the $\Sigma_1$-definition), which is fundamental to the arithmetical hierarchy.
