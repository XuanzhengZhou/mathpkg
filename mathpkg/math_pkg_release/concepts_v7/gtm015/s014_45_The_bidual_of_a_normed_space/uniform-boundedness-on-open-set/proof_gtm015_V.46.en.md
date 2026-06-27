---
role: proof
locale: en
of_concept: uniform-boundedness-on-open-set
source_book: gtm015
source_chapter: "V"
source_section: "46"
---

# Proof of Uniform Boundedness on an Open Set in Baire Spaces

By assumption, for each $x \in X$ there exists a constant $M_x$ such that $|f_\iota(x)| \leq M_x$ for all $\iota \in I$; we seek a nonempty open set $U$ and a constant $M$ such that $|f_\iota(x)| \leq M$ for all $x \in U$ and $\iota \in I$.

For each $\iota \in I$ and each positive integer $n$, the set
$$A_{\iota n} = \{x \in X : |f_\iota(x)| \leq n\}$$
is closed, by the continuity of $f_\iota$; therefore, the set $A_n$, defined for each $n$ by
$$A_n = \bigcap_{\iota \in I} A_{\iota n} = \{x : |f_\iota(x)| \leq n \text{ for all } \iota \in I\},$$
is also closed. The pointwise boundedness assumption means that $X = \bigcup_{n=1}^{\infty} A_n$; since $X$ is a Baire space, $\operatorname{int}(A_m) \neq \varnothing$ for some index $m$, by the characterization of Baire spaces (the complement of every meager set is dense, equivalently, a countable union of closed sets with empty interior cannot have interior). Then $U = \operatorname{int}(A_m)$ and $M = m$ meet the requirements: for all $x \in U$ and $\iota \in I$, we have $|f_\iota(x)| \leq m = M$. $\square$
