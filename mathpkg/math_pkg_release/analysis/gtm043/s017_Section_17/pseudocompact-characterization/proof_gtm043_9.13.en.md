---
role: proof
locale: en
of_concept: pseudocompact-characterization
source_book: gtm043
source_chapter: "9"
source_section: "9.13"
---

**Necessity.** Suppose that $\bigcap_n \operatorname{cl} V_n = \emptyset$. Choose $y_n \in V_n$, distinct for distinct $n$. Then $\{y_n\}_{n \in \mathbb{N}}$ is a closed, discrete set, because any limit point of this set would belong to $\bigcap_n \operatorname{cl} V_n$. Inductively, choose closed neighborhoods $V'_n$ of $y_n$, such that $V'_n \subset V_n$, and $V'_m \cap V'_n = \emptyset$ when $m \neq n$. For each $n$, let $g_n$ be a function in $C(Y)$ such that $g_n(y_n) = n$, and $g_n[Y - V'_n] = \{0\}$. Finally, let
$$g(y) = \sum_{n \in \mathbb{N}} g_n(y) \quad (y \in Y).$$
There is no convergence problem here, because for each $y$, at most one of the summands is different from $0$. Furthermore, each point $y$ has a neighborhood meeting at most one $V'_n$. For, any finite number of these sets that do not contain $y$ can be subtracted from a neighborhood; and if every neighborhood of $y$ were to meet infinitely many $V'_n$, and hence infinitely many $V_n$, then $y$ would belong to $\bigcap_n \operatorname{cl} V_n$. Therefore, $g$ agrees with one of the $g_n$ on a neighborhood of $y$. This shows that $g$ is continuous, and since $g(y_n) = n$, $g$ is unbounded, contradicting pseudocompactness.

**Sufficiency.** (The sufficiency direction in the source text is partially present and continues into the proof of Theorem 9.14 about products.) Assume the condition on decreasing sequences holds. To show $Y$ is pseudocompact, suppose $f \in C(Y)$ is unbounded. Then one can construct a decreasing sequence of open sets whose closures have empty intersection, contradicting the hypothesis.
