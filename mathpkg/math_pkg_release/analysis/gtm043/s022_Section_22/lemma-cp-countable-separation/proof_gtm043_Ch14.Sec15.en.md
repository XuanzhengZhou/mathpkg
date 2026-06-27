---
role: proof
locale: en
of_concept: lemma-cp-countable-separation
source_book: gtm043
source_chapter: "14"
source_section: "15"
---

Lemma 13.7 yields (a) when $M^p$ is hyper-real ($p \notin \upsilon X$). The same lemma (with $B = \emptyset$) shows no countable set is cofinal in this case. The converse in (b) is obvious: if $p \in \upsilon X$, then $C/P$ has no infinitely large elements (7.16), so that the elements $P(n)$, for $n \in \mathbf{N}$, form a cofinal set.

For (a) when $p \in \upsilon X$: we may assume $X = \upsilon X$ so $p \in X$. We may assume $A$ has no greatest element and $B$ no least. By 13.6(a) and Lemma 13.5, there exist sequences $(f_n)$ and $(g_n)$ cofinal in $A$ and coinitial in $B$ respectively. If there exists a real number $r$ with $\sup_n f_n(p) < r < \inf_n g_n(p)$, then $r$ is the required element.

Otherwise, $\sup_n f_n(p) = \inf_n g_n(p)$. Define a function $s$ on $X$ converging uniformly to provide neighborhoods of $p$. Define auxiliary functions $\varphi_k \in C(\mathbf{R})$ forming a partition of unity. Then
$$h(x) = \sum_{k \in \mathbf{N}} \varphi_k(s(x)) g_k(x)$$
is continuous on $X$, satisfies $f_n \leq h \leq g_n$ modulo $P$, and provides the required element $c = P(h)$.
