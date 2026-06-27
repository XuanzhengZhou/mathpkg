---
role: proof
locale: en
of_concept: self-adjoint-spectrum-real
source_book: gtm015
source_chapter: "Chapter 7: C*-Algebras"
source_section: "58. Preliminaries"
---

# Proof of Self-Adjoint Elements Have Real Spectrum

Proof. By an elementary algebraic maneuver, it suffices to show that $x - i1$ is invertible (cf. the proof of (57.24)). Assume to the contrary that $i \in \sigma(x)$. Then, for every complex number $\lambda$, we have

$$\lambda + 1 = \lambda - i^2 \in \sigma(\lambda 1 - ix),$$

therefore $|\lambda + 1| \leq \|\lambda 1 - ix\|$. In particular, if $\lambda$ is real then

$$(\lambda + 1)^2 \leq \|\lambda 1 - ix\|^2 = \|(\lambda 1 - ix)^*((\lambda 1 - ix))\|$$

$$= \|\lambda^2 1 + x^2\| \leq \lambda^2 + \|x\|^2;$$

thus $1 + 2\lambda \leq \|x\|^2$ for all real $\lambda$, which is absurd.
