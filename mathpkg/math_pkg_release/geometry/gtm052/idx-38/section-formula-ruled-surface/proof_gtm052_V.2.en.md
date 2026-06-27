---
role: proof
locale: en
of_concept: section-formula-ruled-surface
source_book: gtm052
source_chapter: "V"
source_section: "2"
---

Let $D$ be a section corresponding to the surjection $\mathcal{E} \to \mathcal{L} \to 0$. By the properties of $\mathbf{P}(\mathcal{E})$, we have $\mathcal{L}(D) \cong \mathcal{O}_X(1) \otimes \pi^*\mathcal{L}^{-1} \otimes \pi^*\bigwedge^2\mathcal{E} \cong \mathcal{L}(C_0) \otimes \pi^*\mathcal{L}(-\mathfrak{d} + \mathfrak{e})$ using Notation 2.8.1. Thus $D \sim C_0 + (\mathfrak{d} - \mathfrak{e})f$ as divisors on $X$.

For the intersection number: $C_0.D = C_0.(C_0 + (\mathfrak{d} - \mathfrak{e})f) = C_0^2 + (\deg \mathfrak{d} - \deg \mathfrak{e})$. But on the other hand, $D$ corresponds to the surjection $\mathcal{E} \to \mathcal{L}$, and $C_0$ corresponds to a surjection $\mathcal{E} \to \mathcal{M}$ with $\deg \mathcal{M} = -\deg \mathfrak{e}$ (since $\mathcal{M} = \bigwedge^2\mathcal{E}$). Computing intersection via (II.7.9) gives $C_0.D = \deg \mathfrak{d}$. Hence $\deg \mathfrak{d} = C_0^2 + \deg \mathfrak{d} - \deg \mathfrak{e}$, which yields $C_0^2 = \deg \mathfrak{e} = -e$.

Wait, the sign convention gives $e = -\deg \mathfrak{e}$, so $C_0^2 = -e$? Let me re-check: $C_0^2 = \deg \mathfrak{e}$ according to the computation, and $e = -\deg \mathfrak{e}$ by definition (2.8), so $C_0^2 = -e$. However the standard Hartshorne convention has $C_0^2 = -e$, which simplifies various formulas. (Some sources write $C_0^2 = -e$; the text states $C_0^2 = -\deg \mathfrak{e} = e$ using the sign convention $e = -\deg \mathfrak{e}$.)
