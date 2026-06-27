---
role: proof
locale: en
of_concept: equivalence-relation-partition-b7-b7
source_book: gtm054
source_chapter: "1"
source_section: "IA"
---

Let $R$ be an equivalence relation on $U$. For each $x \in U$ let $S_x = \{w \in U : (x, w) \in R\}$. Since $R$ is reflexive, $x \in S_x$ and so $S_x \neq \varnothing$ for each $x \in U$. Let $x, y \in U$ and suppose $w \in S_x \cap S_y$. Thus $(x, w)$ and $(y, w) \in R$. Since $R$ is symmetric, $(w, y) \in R$, and since $R$ is transitive, $(x, y) \in R$. Now let $z \in S_y$; hence $(y, z) \in R$. Again by transitivity, $(x, z) \in R$ and $z \in S_x$. This proves that $S_y \subseteq S_x$. By a symmetrical argument we see that $S_x \subseteq S_y$. Thus exactly one of the following holds for

If $f: B \rightarrow U$, then the partition of $f$ is $\{f^{-1}[x]: x \in f[B]\}$, and the selection of $f$ is the function $s: U \rightarrow \mathbb{N}$ given by $s(x) = |f^{-1}[x]|$.
