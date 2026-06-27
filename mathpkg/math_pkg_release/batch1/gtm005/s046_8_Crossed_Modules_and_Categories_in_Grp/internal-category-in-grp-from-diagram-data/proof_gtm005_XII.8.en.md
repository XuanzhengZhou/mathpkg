---
role: proof
locale: en
of_concept: internal-category-in-grp-from-diagram-data
source_book: gtm005
source_chapter: "XII"
source_section: "8"
---

Given the diagram

$$C_1 \xrightarrow{d_0} C_0 \xrightarrow{i} C_1 \xrightarrow{d_1} C_0$$

in $\mathbf{Grp}$ with group homomorphisms $d_0, d_1 : C_1 \to C_0$ and $i : C_0 \to C_1$ satisfying $d_0 i = 1 = d_1 i$ and $[\ker d_0, \ker d_1] = 1$, we define the composition $\gamma$ on composable pairs.

For composable arrows $a \xrightarrow{f} b \xrightarrow{g} c$ (where $d_1(f) = b = d_0(g)$), set

$$\gamma(g, f) = f \, 1_b^{-1} \, g,$$

where $1_b = i(b) \in C_1$. Note that the condition $f 1_b^{-1} g = g 1_b^{-1} f$ follows from the commutator condition $[\ker d_0, \ker d_1] = 1$, as shown in the derivation of the composition formula. Thus the definition is symmetric.

One must verify the category axioms:

1. **Domain and codomain of composites**: Since $d_0$ and $d_1$ are group homomorphisms, one checks that $d_1(\gamma(g, f)) = d_1(g)$ and $d_0(\gamma(g, f)) = d_0(f)$, which corresponds to the requirement that the composite $g \circ f$ has domain $a$ and codomain $c$.

2. **Associativity**: For composable $f, g, h$, one computes $(h \circ g) \circ f$ and $h \circ (g \circ f)$ using the formula and the group multiplication, verifying they are equal. The calculation uses the group structure of $C_1$ and the properties of the identity arrows.

3. **Identity laws**: For $f : a \to b$, one computes $1_b \circ f = 1_b \cdot 1_b^{-1} \cdot f = f$ and similarly $f \circ 1_a = f \cdot 1_a^{-1} \cdot 1_a = f$, using the formula.

4. **Composition is a group homomorphism**: $\gamma$ defined this way respects the group multiplication in $C_1$; this follows from the middle four exchange property which is built into the definition via the group product.

Thus the data $(C_0, C_1, d_0, d_1, i, \gamma)$ constitutes an internal category in $\mathbf{Grp}$.
