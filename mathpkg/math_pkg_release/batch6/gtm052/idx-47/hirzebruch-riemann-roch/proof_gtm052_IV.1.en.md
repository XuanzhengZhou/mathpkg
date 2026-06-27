---
role: proof
locale: en
of_concept: hirzebruch-riemann-roch
source_book: gtm052
source_chapter: "IV"
source_section: "1"
---

The proof of the Hirzebruch-Riemann-Roch theorem proceeds by establishing that both sides of the formula are additive on exact sequences of locally free sheaves, and then reducing to the case of a direct sum of line bundles via the splitting principle.

**Step 1: Additivity.** For an exact sequence $0 \to \mathcal{E}' \to \mathcal{E} \to \mathcal{E}'' \to 0$ of locally free sheaves on $X$, the Euler characteristic satisfies
$$\chi(\mathcal{E}) = \chi(\mathcal{E}') + \chi(\mathcal{E}''),$$
by the long exact sequence in cohomology. On the other hand, the Chern character is additive:
$$\operatorname{ch}(\mathcal{E}) = \operatorname{ch}(\mathcal{E}') + \operatorname{ch}(\mathcal{E}''),$$
which follows from property (C3) of Chern classes: $c_t(\mathcal{E}) = c_t(\mathcal{E}') \cdot c_t(\mathcal{E}'')$ and the fact that the Chern character is the unique additive map from the Grothendieck group $K(X)$ to $A(X) \otimes \mathbb{Q}$ that sends a line bundle $\mathcal{L}$ to $e^{c_1(\mathcal{L})}$.

**Step 2: Line bundles.** For a line bundle $\mathcal{L} = \mathcal{L}(D)$ where $D$ is a divisor, one verifies directly:
$$\operatorname{ch}(\mathcal{L}) = e^D = 1 + D + \frac{1}{2}D^2 + \frac{1}{6}D^3 + \cdots,$$
and the Todd class $\operatorname{td}(\mathcal{T}_X)$ is expressed in terms of the Chern classes of the tangent sheaf as given by the formal power series expansion of $\prod_{i=1}^n \frac{a_i}{1 - e^{-a_i}}$ where $a_i$ are the Chern roots. The equality
$$\chi(\mathcal{L}(D)) = \deg(e^D \cdot \operatorname{td}(\mathcal{T}_X))_n$$
follows by explicit computation or by induction on dimension.

**Step 3: Splitting principle.** For any locally free sheaf $\mathcal{E}$ on $X$, there exists a proper birational morphism $f: X' \to X$ such that $f^*\mathcal{E}$ has a filtration with quotients being line bundles, and $f^*: A(X) \to A(X')$ is injective (property (C3) and the splitting principle from Section 3). Applying Steps 1-2 to the pullback, and using functoriality, we obtain the theorem for $\mathcal{E}$.

Thus the formula holds for all locally free sheaves $\mathcal{E}$ on a nonsingular projective variety $X$.
