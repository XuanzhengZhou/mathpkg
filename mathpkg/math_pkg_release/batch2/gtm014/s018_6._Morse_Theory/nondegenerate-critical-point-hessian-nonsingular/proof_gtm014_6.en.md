---
role: proof
locale: en
of_concept: nondegenerate-critical-point-hessian-nonsingular
source_book: gtm014
source_chapter: "6"
source_section: "6. Morse Theory"
---

$J^1(U, \mathbb{R}) \cong U \times \mathbb{R} \times \operatorname{Hom}(\mathbb{R}^n, \mathbb{R})$. Note that the projection $\pi: J^1(U, \mathbb{R}) \to \operatorname{Hom}(\mathbb{R}^n, \mathbb{R})$ is a submersion and $\pi^{-1}(0) = S_1$. Now apply Lemma 4.3; that is, $j^1 f \pitchfork S_1$ at $p$ iff $\pi \circ j^1 f$ is a submersion at $p$. But $\pi \circ j^1 f$ at $x$ is

$$(df)_x = \left(\frac{\partial f}{\partial x_1}(x), \ldots, \frac{\partial f}{\partial x_n}(x)\right)$$

in the standard coordinates on $\operatorname{Hom}(\mathbb{R}^n, \mathbb{R})$. Thus $\pi \circ j^1 f$ is a submersion at $p$ iff the mapping of $\mathbb{R}^n \to \mathbb{R}^n$ given by

$$x \mapsto \left(\frac{\partial f}{\partial x_1}(x), \ldots, \frac{\partial f}{\partial x_n}(x)\right)$$

is a submersion at $p$, which holds iff $\left(\frac{\partial^2 f}{\partial x_i \partial x_j}\right)(p)$ is nonsingular. $\square$
