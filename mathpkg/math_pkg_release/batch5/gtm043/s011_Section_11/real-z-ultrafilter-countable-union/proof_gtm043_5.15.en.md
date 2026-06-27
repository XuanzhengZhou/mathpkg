---
role: proof
locale: en
of_concept: real-z-ultrafilter-countable-union
source_book: gtm043
source_chapter: "5"
source_section: "5.15"
---

The proof is an exact analogue of the set-theoretic proof given in 2.13 that any $z$-ultrafilter is prime. Suppose $\bigcup_{n \in \mathbb{N}} Z_n \in \mathcal{A}$ where each $Z_n$ is a zero-set and $\mathcal{A}$ is a real $z$-ultrafilter. Assume, for contradiction, that $Z_n \notin \mathcal{A}$ for every $n$. Then, since $\mathcal{A}$ is a $z$-ultrafilter (hence maximal among $z$-filters), each $Z_n$ is disjoint from some member $A_n \in \mathcal{A}$. Thus $\bigcap_n A_n$ is a countable intersection of members of $\mathcal{A}$ that is disjoint from $\bigcup_n Z_n$. By the countable intersection property of $\mathcal{A}$, $\bigcap_n A_n \in \mathcal{A}$. But $\bigcup_n Z_n \in \mathcal{A}$ and $(\bigcap_n A_n) \cap (\bigcup_n Z_n) = \varnothing$, contradicting the fact that $\mathcal{A}$ is a $z$-filter (members must intersect). Hence at least one $Z_n$ belongs to $\mathcal{A}$.
