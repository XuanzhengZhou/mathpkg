---
role: proof
locale: en
of_concept: equivalence-crossed-modules-internal-categories-grp
source_book: gtm005
source_chapter: "XII"
source_section: "8"
---

The equivalence between crossed modules and category objects in $\mathbf{Grp}$ is established by proving two directions.

**Direction 1 (Internal category $\Rightarrow$ Crossed module).** Given an internal category in $\mathbf{Grp}$ with groups $C_0, C_1$ and homomorphisms $d_0, d_1 : C_1 \to C_0$, $i : C_0 \to C_1$ satisfying $d_0 i = 1 = d_1 i$ and $[\ker d_0, \ker d_1] = 1$, define

$$H = \ker d_0, \quad P = C_0, \quad \alpha = d_1|_{\ker d_0} : H \to P.$$

The sequence $1 \to \ker d_0 \to C_1 \xrightarrow{d_0} C_0 \to 1$ is exact (surjectivity of $d_0$ follows from $d_0 i = 1$). This short exact sequence endows $P = C_0$ with a conjugation action on $H = \ker d_0$. One verifies the crossed module axioms using the commutator condition. This is detailed in the proof for concept `crossed-module-from-internal-category-in-grp`.

**Direction 2 (Diagram data $\Rightarrow$ Internal category).** Conversely, given group homomorphisms $d_0, d_1 : C_1 \to C_0$ and $i : C_0 \to C_1$ satisfying $d_0 i = 1 = d_1 i$ and $[\ker d_0, \ker d_1] = 1$, define the composition of a composable pair $a \xrightarrow{f} b \xrightarrow{g} c$ by

$$\gamma(g, f) = f 1_b^{-1} g = g 1_b^{-1} f,$$

where $1_b = i(b)$. This composition satisfies the category axioms (associativity, identity laws) and is a group homomorphism (by the middle four exchange). This is detailed in the proof for concept `internal-category-in-grp-from-diagram-data`.

**The crucial step.** The derivation that the composition must be given by the formula $g \circ f = f 1_b^{-1} g$ uses the fact that inversion $(\cdot)^{-1} : C \to C$ is a functor for a group object, together with the middle four exchange $(g_1 g_2) \circ (f_1 f_2) = (g_1 \circ f_1)(g_2 \circ f_2)$. Applying these to the identity arrow $1_b$ yields the formula, from which the commutator condition $[\ker d_0, \ker d_1] = 1$ is seen to be both necessary and sufficient. This is detailed in the proof for concept `composition-formula-internal-category-grp`.

Together, these constructions establish the one-to-one correspondence between crossed modules and internal categories in $\mathbf{Grp}$.
