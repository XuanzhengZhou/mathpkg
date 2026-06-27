---
role: proof
locale: en
of_concept: compact-metric-image-cantor
source_book: gtm027
source_chapter: "N"
source_section: "Examples on Closed Maps and Local Compactness"
---

# Proof of Every Compact Metric Space is a Continuous Image of the Cantor Space $2^\omega$

Let $X$ be a compact metric space. Since $X$ is a compact metric space, it is second countable. Let $\{U_0, U_1, \dots, U_n, \dots\}$ be a countable base for the topology of $X$.

For each $n \in \omega$, define a function $f_n : \{0,1\} \to \mathcal{C}(X)$ (where $\mathcal{C}(X)$ denotes the closed subsets of $X$) by

$$
f_n(0) = \overline{U_n}, \qquad f_n(1) = X \setminus U_n.
$$

Note that $f_n(0) \cup f_n(1) = X$ and both are closed in $X$. Then $F = \{f_n : n \in \omega\}$ is a countable family. By part (d) (compact-hausdorff-image-cantor), applied to the compact Hausdorff space $X$ with the family $F$, there exists a continuous surjection from a closed subset of $2^F$ onto $X$.

Since $F$ is countable, $2^F$ is homeomorphic to the Cantor space $2^\omega$ (the product of countably many copies of $\{0,1\}$). Moreover, every closed subset of $2^\omega$ is itself a continuous image of $2^\omega$ (indeed, $2^\omega$ retracts onto its closed subsets).

Composing the continuous surjection from a closed subset of $2^\omega$ onto $X$ with a continuous surjection from $2^\omega$ onto that closed subset yields a continuous surjection from $2^\omega$ onto $X$.

Thus $X$ is the continuous image of the Cantor space $2^\omega$.
