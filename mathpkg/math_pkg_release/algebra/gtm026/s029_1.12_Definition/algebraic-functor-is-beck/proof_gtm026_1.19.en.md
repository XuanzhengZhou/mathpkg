---
role: proof
locale: en
of_concept: algebraic-functor-is-beck
source_book: gtm026
source_chapter: "1"
source_section: "1.19"
---

**Proof.** Let $U: \mathcal{A} \rightarrow \mathcal{K}$ be algebraic. By 1.9, it suffices to show that $U$ creates limits. We may assume without loss of generality that $U = U^{\mathbf{T}}$ for some algebraic theory $\mathbf{T}$ in $\mathcal{K}$. Let $(\Delta, D)$ be a diagram in $\mathcal{A} = \mathcal{K}^{\mathbf{T}}$ and write $D_i = (K_i, \xi_i)$. Let $\psi_i: L \rightarrow K_i$ be a limit of $DU$ in $\mathcal{K}$.

We have $(\psi_i)^\# = \psi_i T \cdot \xi_i: LT \longrightarrow K_i$, which is a lower bound of $(\Delta, DU)$. Hence there exists a unique $\xi: LT \longrightarrow L$ such that $\xi \cdot \psi_i = \psi_i T \cdot \xi_i$ for all $i$. This defines a $\mathbf{T}$-algebra structure on $L$ making each $\psi_i$ a $\mathbf{T}$-homomorphism. The remaining details are similar to 1.4.27 and 2.1.11. $\square$
