---
role: proof
locale: en
of_concept: equivalence-preserves-completeness
source_book: gtm055
source_chapter: "12"
source_section: "Bounded linear transformations"
---

Suppose without loss of generality that $\mathcal{E}$ is complete, and that $T: \mathcal{E} \rightarrow \mathcal{F}$ is an equivalence. Let $\{y_n\}$ be a Cauchy sequence in $\mathcal{F}$, and let $x_n = T^{-1}y_n$, $n \in \mathbb{N}$. Then $\|x_m - x_n\| \leq \|T^{-1}\| \|y_m - y_n\|$ for all $m$ and $n$, so $\{x_n\}$ is a Cauchy sequence in $\mathcal{E}$. But then $\{x_n\}$ is convergent in $\mathcal{E}$, whence it follows that $\{y_n\} = \{Tx_n\}$ is convergent in $\mathcal{F}$.
