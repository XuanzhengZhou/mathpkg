---
role: proof
locale: en
of_concept: equality-of-morphisms-on-dense-open
source_book: gtm052
source_chapter: "I"
source_section: "4"
---

We may assume that $Y \subseteq \mathbf{P}^n$ for some $n$. Then by composing with the inclusion morphism $Y \to \mathbf{P}^n$, we reduce to the case $Y = \mathbf{P}^n$. We consider the product $\mathbf{P}^n \times \mathbf{P}^n$, which has a structure of projective variety given by its Segre embedding (Ex. 3.16). The morphisms $\varphi$ and $\psi$ determine a map $\varphi \times \psi: X \to \mathbf{P}^n \times \mathbf{P}^n$, which in fact is a morphism (Ex. 3.16c). Let $\Delta = \{P \times P \mid P \in \mathbf{P}^n\}$ be the diagonal subset of $\mathbf{P}^n \times \mathbf{P}^n$. It is defined by the equations $\{x_i y_j = x_j y_i \mid i, j = 0, 1, \ldots, n\}$ and so is a closed subset of $\mathbf{P}^n \times \mathbf{P}^n$. By hypothesis $\varphi \times \psi(U) \subseteq \Delta$. But $U$ is dense in $X$, and $\Delta$ is closed, so $\varphi \times \psi(X) \subseteq \Delta$. This says that $\varphi = \psi$.
