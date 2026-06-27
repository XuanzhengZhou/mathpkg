---
role: proof
locale: en
of_concept: bounded-transformations-form-subspace
source_book: gtm023
source_chapter: "VII"
source_section: "5 (7.21)"
---

If $\varphi, \psi$ are bounded with bounds $M_1, M_2$ respectively, then for any $\lambda \in \mathbb{R}$:
$$\|(\lambda \varphi)x\| = |\lambda| \cdot \|\varphi x\| \leq |\lambda| M_1 \|x\|,$$
so $\lambda \varphi$ is bounded. By the triangle inequality,
$$\|(\varphi + \psi)x\| = \|\varphi x + \psi x\| \leq \|\varphi x\| + \|\psi x\| \leq (M_1 + M_2)\|x\|,$$
so $\varphi + \psi$ is bounded. Thus $B(E;E)$ is a linear subspace of $L(E;E)$.
