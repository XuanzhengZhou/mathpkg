---
role: proof
locale: en
of_concept: compact-hausdorff-image-cantor
source_book: gtm027
source_chapter: "N"
source_section: "Examples on Closed Maps and Local Compactness"
---

# Proof of Every Compact Hausdorff Space is a Continuous Image of a Closed Subset of a Cantor Space

Let $X$ be a compact Hausdorff space. Let $F$ be the family of all functions $f$ on $2 = \{0,1\}$ such that $f(0)$ and $f(1)$ are closed subsets of $X$ and $f(0) \cup f(1) = X$.

Consider the Cantor space $2^F$ (all functions from $F$ to $\{0,1\}$ with the product topology). Define a map $\phi$ on a subset of $2^F$ as follows. For each $x \in 2^F$, consider the family $\{f(x_f) : f \in F\}$ of closed subsets of $X$. The intersection

$$
\bigcap \{f(x_f) : f \in F\}
$$

is either void or consists of a single point. In the latter case, define $\phi(x)$ to be that unique point.

One can prove that the domain of $\phi$ (the set of $x \in 2^F$ for which the intersection is non-empty) is a closed subset of $2^F$, and that $\phi$ is continuous. Moreover, $\phi$ is surjective onto $X$: for any $p \in X$, define $x \in 2^F$ by choosing $x_f$ such that $p \in f(x_f)$ for each $f \in F$; then $\bigcap \{f(x_f) : f \in F\} = \{p\}$.

If $U \subset X$, the inverse image is described by

$$
\phi^{-1}[U] = \left\{ x \in \operatorname{dom}(\phi) : \bigcap \{f(x_f) : f \in F\} \subset U \right\}.
$$

Thus $\phi$ maps a closed subset of the Cantor space $2^F$ continuously onto $X$, establishing the result.
