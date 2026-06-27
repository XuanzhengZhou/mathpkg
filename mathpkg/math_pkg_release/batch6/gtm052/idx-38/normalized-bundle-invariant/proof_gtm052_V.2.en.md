---
role: proof
locale: en
of_concept: normalized-bundle-invariant
source_book: gtm052
source_chapter: "V"
source_section: "2"
---

First write $X \cong \mathbf{P}(\mathcal{E}')$ for some locally free sheaf $\mathcal{E}'$ on $C$ (Proposition 2.2). Then we will replace $\mathcal{E}'$ by a twisted sheaf $\mathcal{E} = \mathcal{E}' \otimes \mathcal{L}$ for a suitable invertible sheaf $\mathcal{L}$, to achieve the normalization condition.

We require $H^0(\mathcal{E}) \neq 0$ but $H^0(\mathcal{E} \otimes \mathcal{M}) = 0$ for all $\mathcal{M}$ with $\deg \mathcal{M} < 0$. This is achieved by choosing $\mathcal{L}$ such that $\deg \mathcal{E}$ is minimal among all twists of $\mathcal{E}'$ that still admit a nonzero global section. The integer $e = -\deg \mathcal{E}$ is independent of the chosen normalized representative: if $\mathcal{E}_1$ and $\mathcal{E}_2$ are both normalized and give isomorphic ruled surfaces, then $\mathcal{E}_2 \cong \mathcal{E}_1 \otimes \mathcal{L}$ with $\deg \mathcal{L} = 0$ by (2.2), and the normalization conditions force $\mathcal{L} \cong \mathcal{O}_C$, so $\deg \mathcal{E}_1 = \deg \mathcal{E}_2$.

For the second statement, the surjection $\mathcal{E} \to \mathcal{O}_C \to 0$ giving a section is part of the normalization: since $H^0(\mathcal{E}) \neq 0$, pick a nonzero section, which corresponds to a map $\mathcal{O}_C \to \mathcal{E}$. The cokernel of this inclusion is an invertible sheaf $\mathcal{L}$, and the normalization condition forces $\deg \mathcal{L} \leq 0$, with equality iff the extension splits in a particular way. The image of the corresponding section gives $C_0$.
