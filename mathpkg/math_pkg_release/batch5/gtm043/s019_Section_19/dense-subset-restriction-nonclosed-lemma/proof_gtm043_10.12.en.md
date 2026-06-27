---
role: proof
locale: en
of_concept: dense-subset-restriction-nonclosed-lemma
source_book: gtm043
source_chapter: "10"
source_section: "10.12"
---

Choose $p \in T - S$, and let $q = \varphi p$. The point $p$ has an open neighborhood whose closure $V$ (in $T$) does not meet the compact set $\varphi^{\leftarrow}(q) \cap S$. Then $q \notin \varphi[V \cap S]$. But $\operatorname{cl}_T(V \cap S) = V$, and $q \in \varphi[V]$. Hence

$$q \in \varphi[\operatorname{cl}_T(V \cap S)] \subset \operatorname{cl}_Y \varphi[V \cap S].$$

Therefore $\varphi|S$ takes the closed set $V \cap S$ in $S$ to a set that is not closed in $Y$.
