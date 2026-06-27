---
role: proof
locale: en
of_concept: nowhere-dense-characterization
source_book: gtm055
source_chapter: "4"
source_section: "6"
---

If $N$ is not nowhere dense, then $N^-$ contains some nonempty open set $U$. Every nonempty open subset $V$ of $U$ must intersect $N$, for otherwise $V$ would be an open set disjoint from $N$ yet contained in $U \subset N^-$, contradicting that $N^-$ is the closure of $N$. Hence the condition is necessary.

Conversely, suppose the condition holds. If $N$ were not nowhere dense, then $N^-$ would contain some nonempty open set $U$. But then every nonempty open $V \subset U$ would intersect $N$ (since $U \subset N^-$), contradicting the hypothesis. Thus $N$ is nowhere dense.

For the stronger version, given a nowhere dense set $N$ and a nonempty open $U$, pick any $x \in U$ and a small radius $r > 0$ such that $D_{2r}(x) \subset U$. Since $N$ is nowhere dense, there exists a nonempty open $V$ with $V \subset D_r(x)$ and $V \cap N = \emptyset$. Choosing a ball $D \subset V$ with radius at most the prescribed bound and with $D^- \subset V$ (by shrinking radius further), we obtain $D^- \subset D_{2r}(x) \subset U$ and $D^- \cap N = \emptyset$.
