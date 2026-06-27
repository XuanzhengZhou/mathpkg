---
role: proof
locale: en
of_concept: elliptic-ruled-surfaces
source_book: gtm052
source_chapter: "V"
source_section: "2"
---

According to Theorem 2.12, for an indecomposable bundle over an elliptic curve ($g = 1$), we must have $-2 \leq e \leq 0$, so $e = 0, -1, -2$.

If $e = 0$, then we have an exact sequence

$$0 \rightarrow \mathcal{O}_C \rightarrow \mathcal{E} \rightarrow \mathcal{L} \rightarrow 0$$

with $\deg \mathcal{L} = 0$. This extension corresponds to a nonzero element $\xi \in H^1(C, \mathcal{L}^{-1})$. In particular, $H^1(C, \mathcal{L}^{-1}) \neq 0$. By Serre duality, $H^1(C, \mathcal{L}^{-1}) \cong H^0(C, \mathcal{L} \otimes \omega_C)^\vee = H^0(C, \mathcal{L})^\vee$ (since $\omega_C \cong \mathcal{O}_C$ for an elliptic curve). Thus we must have $H^0(C, \mathcal{L}) \neq 0$, which for a degree $0$ invertible sheaf on a curve implies $\mathcal{L} \cong \mathcal{O}_C$.

Conversely, taking $\mathcal{L} = \mathcal{O}_C$, we have $\dim H^1(\mathcal{O}_C) = 1$, so there is just one choice of nonzero $\xi \in H^1(\mathcal{O}_C)$, up to isomorphism, which is a nontrivial extension

$$0 \rightarrow \mathcal{O}_C \rightarrow \mathcal{E} \rightarrow \mathcal{O}_C \rightarrow 0.$$

Clearly this $\mathcal{E}$ is normalized. Furthermore, this $\mathcal{E}$ is indecomposable, because if $\mathcal{E}$ were decomposable, being normalized, it would be isomorphic to $\mathcal{O}_C \oplus \mathcal{L}$ for some $\mathcal{L}$, by Theorem 2.12(a). But $\bigwedge^2 \mathcal{E} \cong \mathcal{O}_C$, so $\mathcal{L} \cong \mathcal{O}_C$, so in fact this extension would have to split, which it doesn't. Thus we get exactly one elliptic ruled surface $X$ with $e = 0$ and $\mathcal{E}$ indecomposable.

If $e = -1$, then we have $\deg \mathcal{L} = -1$. The exact sequence $0 \to \mathcal{O}_C \to \mathcal{E} \to \mathcal{L} \to 0$ corresponds to an element in $H^1(C, \mathcal{L}^{-1})$, where $\deg \mathcal{L}^{-1} = 1$. By Riemann-Roch, $\dim H^1(C, \mathcal{L}^{-1}) = \dim H^0(C, \mathcal{L} \otimes \omega_C) = \dim H^0(C, \mathcal{L})$ (since $\omega_C \cong \mathcal{O}_C$). But $\deg \mathcal{L} = -1$, so $H^0(C, \mathcal{L}) = 0$, and $\dim H^1(C, \mathcal{L}^{-1}) = 1$ by Riemann-Roch. Thus there is a unique nontrivial extension, giving a unique ruled surface with $e = -1$.

The case $e = -2$ is excluded by a more refined argument using the stronger restrictions mentioned in Theorem 2.12(b) and Exercise 2.5. Essentially, an indecomposable bundle with $e = -2$ over an elliptic curve cannot satisfy the normalization condition.
