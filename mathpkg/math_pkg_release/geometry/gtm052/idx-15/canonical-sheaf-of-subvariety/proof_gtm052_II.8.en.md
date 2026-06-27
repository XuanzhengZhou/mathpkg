---
role: proof
locale: en
of_concept: canonical-sheaf-of-subvariety
source_book: gtm052
source_chapter: "II"
source_section: "8"
---

From Theorem 8.17, since $Y$ is a nonsingular subvariety of $X$, we have the exact sequence of locally free sheaves on $Y$:

$$0 \to \mathcal{I}/\mathcal{I}^2 \to \Omega_{X/k} \otimes \mathcal{O}_Y \to \Omega_{Y/k} \to 0.$$

Let $n = \dim X$ and $n - r = \dim Y$. Taking determinants (highest exterior powers) of this exact sequence and using the fact that for an exact sequence $0 \to \mathcal{E}' \to \mathcal{E} \to \mathcal{E}'' \to 0$ of locally free sheaves we have $\bigwedge^{\operatorname{rank} \mathcal{E}} \mathcal{E} \cong \bigwedge^{\operatorname{rank} \mathcal{E}'} \mathcal{E}' \otimes \bigwedge^{\operatorname{rank} \mathcal{E}''} \mathcal{E}''$, we obtain

$$\bigwedge^n (\Omega_{X/k} \otimes \mathcal{O}_Y) \cong \bigwedge^r (\mathcal{I}/\mathcal{I}^2) \otimes \bigwedge^{n-r} \Omega_{Y/k}.$$

But $\bigwedge^n (\Omega_{X/k} \otimes \mathcal{O}_Y) \cong \omega_X \otimes \mathcal{O}_Y$ and $\bigwedge^{n-r} \Omega_{Y/k} \cong \omega_Y$. Since $\bigwedge^r (\mathcal{I}/\mathcal{I}^2) \cong (\bigwedge^r \mathcal{N}_{Y/X})^{-1}$, rearranging gives $\omega_Y \cong \omega_X \otimes \bigwedge^r \mathcal{N}_{Y/X}$.
