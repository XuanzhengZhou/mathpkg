---
role: proof
locale: en
of_concept: right-adjoint-preserves-limits
source_book: gtm005
source_chapter: "V"
source_section: "5. Adjoints on Limits"
---

**Proof.** Let $\langle F, G, \eta, \varepsilon \rangle : X \rightleftarrows A$ be an adjunction, and let $J$ be any index category. Form the functor categories and the induced adjunction $\langle F^J, G^J, \eta^J, \varepsilon^J \rangle : X^J \rightleftarrows A^J$ where $F^J(S) = F \circ S$ for $S : J \rightarrow X$, with analogous definitions for $G^J$, $\eta^J$, $\varepsilon^J$. The triangular identities for $\eta, \varepsilon$ yield the same identities for $\eta^J, \varepsilon^J$, confirming this is indeed an adjunction.

Now consider the diagram of adjoint pairs (where $\Delta$ denotes the diagonal functor):

$$\xymatrix{
X^J \ar@<0.5ex>[r]^{F^J} & A^J \ar@<0.5ex>[l]^{G^J} \\
X \ar@<0.5ex>[r]^{F} \ar[u]^{\Delta} & A \ar@<0.5ex>[l]^{G} \ar[u]^{\Delta}
}$$

The definition of the diagonal functors shows immediately that $F^J \Delta = \Delta F$, so the square of left adjoints commutes. Since $\operatorname{Lim}$ is right adjoint to $\Delta$ in both $X$ and $A$, the composites $\operatorname{Lim} \circ G^J$ and $G \circ \operatorname{Lim}$ are both right adjoint to $\Delta \circ F = F^J \circ \Delta$. Since the right adjoint of a given functor is unique up to natural isomorphism,

$$\operatorname{Lim} \circ G^J \cong G \circ \operatorname{Lim}.$$

This means that for any functor $T : J \rightarrow A$, the limit of $G \circ T$ is (naturally isomorphic to) $G$ applied to the limit of $T$:

$$G(\operatorname{Lim} T) \cong \operatorname{Lim}(G \circ T).$$

Thus $G$ preserves all limits that exist in $A$. Dually, the left adjoint $F$ preserves all colimits. $\square$
