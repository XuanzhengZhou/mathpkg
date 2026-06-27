---
role: proof
locale: en
of_concept: normal-stress-energy-timelike-eigenvector
source_book: gtm048
source_chapter: "3"
source_section: "3.14"
---

**Proof of Proposition 3.14.1.** Let $S$ be the unit sphere on $M_x$ relative to an arbitrary positive definite inner product on $M_x$. Let $A$ be the set of nonspacelike one-dimensional subspaces of $M_x$. Then $A \cap S$ has two components, each diffeomorphic to the closed unit ball in $\mathbb{R}^3$ (by Exercise 1.1.9). Take one of these components and call it $\mathcal{C}$. By assumption, the endomorphism $\tilde{T} : M_x \rightarrow M_x$ carries $A$ into itself, and hence $\hat{T}$ induces a continuous map $f$ of $\mathcal{C}$ into itself. By Brouwer's fixed point theorem, $f : \mathcal{C} \rightarrow \mathcal{C}$ has a fixed point, say $X$. Since $\hat{T}$ is normal at $x$, the image of $f$ consists only of timelike vectors. Hence $X$ is timelike, and it follows from the definition of $f$ that $\tilde{T}X = aX$ for some $a \in \mathbb{R}$.

To show that $X$ is unique up to a nonzero multiple: suppose not, and let $Z$ be another timelike vector in $M_x$ such that $\tilde{T}Z = bZ$ and $\{X, Z\}$ are linearly independent. Let $T$ be the $(0, 2)$-tensor field physically equivalent to $\hat{T}$. Since $X$ and $Z$ are both timelike eigenvectors, their span is a 2-dimensional subspace of $M_x$. Every nonzero linear combination of two linearly independent timelike vectors contains a null (lightlike) vector. Since $T$ is normal at $x$, the image under $\tilde{T}$ of any causal vector must be timelike, but this would be contradicted by the existence of a null vector in $\operatorname{span}\{X, Z\}$. Therefore, no such linearly independent second eigenvector can exist, and $X$ is unique up to nonzero scalar multiples.
