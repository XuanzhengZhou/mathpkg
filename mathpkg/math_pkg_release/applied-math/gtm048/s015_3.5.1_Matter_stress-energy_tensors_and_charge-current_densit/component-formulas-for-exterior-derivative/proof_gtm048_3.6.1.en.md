---
role: proof
locale: en
of_concept: component-formulas-for-exterior-derivative
source_book: gtm048
source_chapter: "3"
source_section: "3.6.1"
---

We verify the formula for 1-forms; the higher-degree cases follow similarly. Write $\eta = \eta_k dx^k$. From the formula $d\eta = \omega^i \wedge D_{X_i} \eta$ (Observation (i)), using $\{X_i = \partial_i\}$ and $\{\omega^i = dx^i\}$, we have

$$d\eta = dx^i \wedge D_{\partial_i}(\eta_k dx^k) = dx^i \wedge (\eta_{k|i} dx^k) = \eta_{k|i} \, dx^i \wedge dx^k.$$

Since $dx^i \wedge dx^k = -dx^k \wedge dx^i$, we can antisymmetrize:

$$d\eta = \frac{1}{2}(\eta_{k|i} - \eta_{i|k}) dx^i \wedge dx^k.$$

Thus $(d\eta)_{ik} = \frac{1}{2}(\eta_{k|i} - \eta_{i|k})$, which is the stated formula with indices $i,j$ (renaming $k \to j$).

For a 2-form $\eta = \frac{1}{2} \eta_{ab} dx^a \wedge dx^b$, applying the same method:

$$d\eta = dx^i \wedge D_{\partial_i}\left(\frac{1}{2} \eta_{ab} dx^a \wedge dx^b\right) = \frac{1}{2} \eta_{ab|i} \, dx^i \wedge dx^a \wedge dx^b.$$

Antisymmetrizing over the three indices yields the cyclic formula with factor $\frac{1}{3}$. The 3-form case proceeds analogously with antisymmetrization over four indices.
