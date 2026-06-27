---
role: proof
locale: en
of_concept: classification-of-numerable-bundles-over-product-with-interval
source_book: gtm020
source_chapter: "4. General Fibre Bundles"
source_section: "9.8"
---

Observe that $r^*(\xi)$ and $(\xi|(B \times \{1\})) \times I$ are $(B \times I)$-isomorphic principal $G$-bundles, where $r(b, t) = (b, 1)$. By Corollary 9.7, $r^*(\xi)$ and $\xi$ are $(B \times I)$-isomorphic. Hence $\xi$ and $(\xi|(B \times \{1\})) \times I$ are $G$-isomorphic over $B \times I$.

For the second statement, applying the naturality of pullbacks with respect to the retraction $r$ and the inclusion $\varepsilon_0$, we obtain that $\varepsilon_0^*(\xi) = \varepsilon_0^*(r^*(\xi))$ is isomorphic to $\varepsilon_1^*(\xi)$, since both factor through the same homotopy class. More precisely, note that the composition $r \circ \varepsilon_0 = \varepsilon_1$, hence $\varepsilon_0^*(\xi) \cong \varepsilon_0^*(r^*(\xi)) \cong (r \circ \varepsilon_0)^*(\xi) = \varepsilon_1^*(\xi)$.

For a locally compact space $W$, the construction $(x, w)s = (xs, w)$ defines a right $G$-space structure on $X \times W$, where $X$ is the total space of $\xi$. The translation map $\tau_1$ for $X \times W$ satisfies $\tau_1((x, w), (x', w)) = \tau(x, x')$, where $\tau$ is the translation map for $X$ modulo $G$. The identification $X \times W \rightarrow (X \times W)/G$ factors through the homeomorphism $\phi: (X \times W)/G \rightarrow (X/G) \times W$ given by $\phi((x, w)G) = (xG, w)$. Applying this with $W = I = [0, 1]$ yields the required isomorphisms.
