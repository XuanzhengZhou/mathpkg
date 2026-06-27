---
role: proof
locale: en
of_concept: ordinal-space-normality
source_book: gtm027
source_chapter: "4"
source_section: "E. Problems (Ordinal Space Properties)"
---

# Proof of Normality of Ordinal Spaces

**Statement (c)**: Both $\Omega_0 = [0, \Omega)$ and $\Omega' = [0, \Omega]$ are normal spaces (with the order topology).

**Proof sketch** (following Kelley's hint):

Let $A$ and $B$ be disjoint closed subsets of $\Omega_0$. By the result of part (b), $\Omega$ is not an accumulation point of both $A$ and $B$.

**Case 1**: $\Omega$ is not an accumulation point of $A$. Then there exists $\alpha_0 < \Omega$ such that $A \subset [0, \alpha_0]$. The closed interval $[0, \alpha_0]$ (a successor ordinal segment) is compact in the order topology (countable ordinals up to a countable limit form a compact set). Compact Hausdorff spaces are normal, so we can separate $A$ and $B \cap [0, \alpha_0]$ within $[0, \alpha_0]$. The complement $(\alpha_0, \Omega)$ is open and contains the remainder of $B$. Thus $A$ and $B$ can be separated by disjoint open sets.

**Case 2** (general construction per Kelley's hint): If the first point of $A \cup B$ belongs to $A$, we construct a finite alternating sequence as follows.

Let $a_0 = \min(A \cup B) \in A$ (the first element of the union; such a minimum exists in a well-ordered set, or we work locally). Then define $b_0$ as the smallest point of $B$ greater than $a_0$ (if any). Then define $a_1$ as the smallest point of $A$ greater than $b_0$, and so on. By the disjointness and the fact that $\Omega$ is not an accumulation point of both, this process must terminate after finitely many steps, yielding a finite chain
$$a_0 < b_0 < a_1 < b_1 < \cdots < a_n \quad (\text{or } b_n)$$
such that no point of $A$ lies between $a_i$ and $b_i$, and no point of $B$ lies between $b_i$ and $a_{i+1}$.

Then the intervals $(a_i, b_i]$ are simultaneously open and closed (clopen) in the order topology, because for ordinals, the half-open interval $(a_i, b_i] = \{x : a_i < x \leq b_i\}$ is open (it equals $(a_i, b_i+1)$ if $b_i$ is a successor) and closed (its complement is $[0, a_i] \cup (b_i, \Omega)$, which is open).

These clopen intervals can be used to construct disjoint open neighborhoods separating $A$ and $B$:
$$U = \bigcup_i (a_i, b_i], \qquad V = \Omega_0 \setminus \overline{U}.$$

The same argument applies to $\Omega' = [0, \Omega]$ with the minor adjustment that $\Omega$ itself (the maximum element) has basic neighborhoods of the form $(\alpha, \Omega]$.

Thus both $\Omega_0$ and $\Omega'$ are normal.
