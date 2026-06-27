---
role: proof
locale: en
of_concept: corollary-16-10-inverse-of-adjoint
source_book: gtm055
source_chapter: "16"
source_section: "16.3"
---

If $T \in \mathcal{L}(\mathcal{E}, \mathcal{F})$ is invertible, then $T \circ T^{-1} = I_{\mathcal{F}}$ and $T^{-1} \circ T = I_{\mathcal{E}}$. Taking adjoints and using the fact that $(S \circ T)^* = T^* \circ S^*$ and $I^* = I$, we obtain

$$(T^{-1})^* \circ T^* = (T \circ T^{-1})^* = I_{\mathcal{F}}^* = I_{\mathcal{F}^*},$$
$$T^* \circ (T^{-1})^* = (T^{-1} \circ T)^* = I_{\mathcal{E}}^* = I_{\mathcal{E}^*}.$$

Thus $(T^{-1})^*$ is a two-sided inverse of $T^*$, so $T^*$ is invertible and $(T^*)^{-1} = (T^{-1})^*$.
