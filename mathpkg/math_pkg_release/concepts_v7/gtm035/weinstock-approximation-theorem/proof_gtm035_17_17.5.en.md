---
role: proof
locale: en
of_concept: weinstock-approximation-theorem
source_book: gtm035
source_chapter: "Chapter 17"
source_section: "17.5"
---
# Proof of Weinstock Approximation Theorem

**Theorem 17.5 (Weinstock).** Let $\Sigma$ be a $k$-dimensional sufficiently smooth submanifold of $\mathbb{C}^n$ without complex tangents, and let $X \subset \Sigma$ be a compact polynomially convex set. Then for any sufficiently small $C^1$ perturbation of $\Sigma$, the approximation property $P(X) = C(X)$ persists.

> **Note.** The full statement and proof of Theorem 17.5 are not present in the stitched section file `s017_Section_17.md`, which is truncated. The section text ends mid-sentence during the completion of the proof of Theorem 17.1. Theorem 17.5 is mentioned in Note 2 of Theorem 17.1: "After proving Theorem 17.1, we shall use it in Theorem 17.5 to solve a certain perturbation problem."

> According to the historical notes (Section 18), Theorem 17.5 was proved by Hörmander and Wermer in *Uniform approximation on compact sets in $\mathbb{C}^n$*, Math. Scand. 23 (1968). The case $n = 1$ was proved earlier by Wermer in *Approximation on a disk*, Math. Ann. 155 (1964). An elementary proof based on a certain integral transform was given by Weinstock in [Wei1].

*Proof sketch.* Theorem 17.5 is a perturbation result that follows from Theorem 17.1. The idea is that if $\tilde{\Sigma}$ is a sufficiently small $C^1$ perturbation of $\Sigma$, then $\tilde{\Sigma}$ also has no complex tangents (the no-complex-tangents condition is stable under $C^1$-small perturbations), and a compact polynomially convex subset $\tilde{X}$ of $\tilde{\Sigma}$ close to $X$ will also satisfy $P(\tilde{X}) = C(\tilde{X})$.
