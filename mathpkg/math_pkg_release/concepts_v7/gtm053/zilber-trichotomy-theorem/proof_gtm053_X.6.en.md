---
role: proof
locale: en
of_concept: zilber-trichotomy-theorem
source_book: gtm053
source_chapter: "X"
source_section: "6"
---

# Proof of the Classification Theorem for Zariski Structures (Zilber Trichotomy)

**Theorem 6.9 (Hrushovski-Zilber, 1993).** For any nonlinear Zariski geometry $\mathbf{M}$, there exist an algebraically closed field $\mathbf{F}$ and a nonconstant continuous function $f : \mathbf{M} \to \mathbf{F}$ (in the sense of the Zariski topology) such that $\mathbf{F}$ is interpretable in $\mathbf{M}$ and the structure on $\mathbf{M}$ is essentially controlled by the field $\mathbf{F}$. In particular, the only relations on $\mathbf{F}$ induced from $\mathbf{M}$ are the constructible ones.

*Proof sketch.* The proof proceeds through several major steps, constructing a field from the geometric structure of the Zariski geometry.

**Step 1: Constructing a one-dimensional group.** Starting from a strongly minimal subset of $\mathbf{M}$ of type (iii) (non-locally-modular, i.e., nonlinear), one studies the family of curves on $\mathbf{M}$. The branches of these curves at a point give rise to local functions $X \to X$ defined in a neighborhood of a point. By composing these local functions and factorizing by the tangency relation, one obtains a one-dimensional group $(\mathbf{F}, \cdot)$ endowed with a Zariski structure induced from $\mathbf{M}$.

**Step 2: Obtaining a field.** Applying the same construction with $\mathbf{F}$ in place of $X$ yields a one-dimensional Zariski field $(\mathbf{F}, +, \cdot)$. By a "Liouville argument" using the dimension theory of Zariski geometries, this field must be algebraically closed. The key insight is that the Zariski topology restricts the possible algebraic structures — a one-dimensional Zariski field can only be an algebraically closed field.

**Step 3: Bezout's Theorem.** One develops intersection theory in the Zariski geometry and proves a form of Bézout's theorem: the intersection of properly intersecting closed subsets can be counted with multiplicities, and the total multiplicity is determined by the dimensions. This provides control over the solution sets of systems of equations.

**Step 4: Chao's Theorem.** Using the intersection theory, one proves a generalization of Chao's theorem: every closed subset $S$ of the projective space $\mathbf{F}\mathbb{P}^n$ is the zero-set of a system of homogeneous polynomial equations. This establishes that the closed sets in the Zariski topology on $\mathbf{F}^n$ are precisely the algebraic sets.

**Step 5: Conclusion.** The final statement of the classification theorem follows: the only relations on $\mathbf{F}$ induced from $\mathbf{M}$ are the constructible ones (Boolean combinations of zero-sets of polynomials). This means that the field $\mathbf{F}$ is a pure algebraically closed field, and the structure $\mathbf{M}$ is interpreted in it as an algebraic variety.

**Corollary (Trichotomy Principle).** The trichotomy holds for strongly minimal structures definable in:
- (a) Differentially closed fields of characteristic zero,
- (b) Hasse-differentially closed fields of positive characteristic,
- (c) Algebraically closed difference fields,
- (d) Compact complex manifolds.

These applications connect the abstract classification to concrete mathematical structures, including new proofs of the Mordell-Lang conjecture (function fields) and the Manin-Mumford conjecture. $\square$
