---
role: proof
locale: en
of_concept: classification-of-two-sided-ideals
source_book: gtm031
source_chapter: "Chapter VIII: The Ring of Linear Transformations"
source_section: "9. Rank of a linear transformation. Two-sided ideals"
---
**Proof.** Let $\mathfrak{B}$ be any proper two-sided ideal in $\mathfrak{L}$. Let $e$ be the smallest infinite cardinal such that $e > \rho(B)$ for all $B \in \mathfrak{B}$. If $\mathfrak{B}$ contained a transformation of rank $b = \dim \mathfrak{R}$, then by the rank comparison lemma, $\mathfrak{B}$ would equal $\mathfrak{L}$, contradicting properness. Thus $b > \rho(B)$ for every $B \in \mathfrak{B}$, so $e \leq b$. By definition, $\mathfrak{B} \subseteq \mathfrak{L}_e$.

Conversely, if $C \in \mathfrak{L}_e$, then $\rho(C) < e$. If $\rho(C)$ is infinite, there exists $B \in \mathfrak{B}$ with $\rho(B) \geq \rho(C)$, hence $C \in \mathfrak{B}$ by the lemma. If $\rho(C)$ is finite, one shows every transformation of rank 1 is in $\mathfrak{B}$, and any finite rank transformation is a sum of rank-1 transformations, so $C \in \mathfrak{B}$. Thus $\mathfrak{B} = \mathfrak{L}_e$.

The strict inclusion for $e < e'$ follows because there exist transformations of any rank $\leq b$.
