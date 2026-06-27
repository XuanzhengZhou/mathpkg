---
role: proof
locale: en
of_concept: homotopy-invariance-of-collapsing
source_book: gtm020
source_chapter: "10. Relative K-Theory"
source_section: "1. Collapsing of Trivialized Bundles"
---

**Proof.** View the homotopy $t_s$ as a single trivialization $t$ of the product bundle $\xi \times I$ over $A \times I$, defined by $t(x, s) = t_s(x)$. Consider the collapsing $(\xi \times I)/t$ over $(X \times I)/(A \times I)$. Since the quotient spaces $(X \times I)/(A \times I)$ and $(X/A) \times I$ are naturally homeomorphic (the quotient by $A \times I$ collapses $A$ in each time slice independently), we can identify $(\xi \times I)/t$ with a vector bundle over $(X/A) \times I$.

Now restrict this bundle to the two endpoints: $\xi/t_0$ is isomorphic to $((\xi \times I)/t)|_{(X/A) \times \{0\}}$, and $\xi/t_1$ is isomorphic to $((\xi \times I)/t)|_{(X/A) \times \{1\}}$. But any vector bundle over $(X/A) \times I$ is isomorphic to the product of its restriction to $(X/A) \times \{0\}$ with the interval $I$ (since vector bundles are homotopy-invariant over paracompact base spaces). That is, $(\xi \times I)/t \cong \eta \times I$ for some vector bundle $\eta$ over $X/A$. Therefore $\xi/t_0 \cong \eta \cong \xi/t_1$, establishing the isomorphism.
