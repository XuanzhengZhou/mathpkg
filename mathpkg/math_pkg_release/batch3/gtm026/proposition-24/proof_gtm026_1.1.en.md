---
role: proof
locale: en
of_concept: proposition-24
source_book: gtm026
source_chapter: "1"
source_section: "1.19"
---

Let $U: \mathcal{A} \rightarrow \mathcal{K}$ be algebraic. By 1.9, it suffices to show that $U$ creates limits. We may assume without loss of generality that $U = U^{\mathbf{T}}$ for some algebraic theory $\mathbf{T}$ in $\mathcal{K}$. Let $(\Delta, D)$ be a diagram in $\mathcal{A} = \mathcal{K}^{\mathbf{T}}$ and write $D_i = (K_i, \xi_i)$. Let $\psi_i: L \rightarrow K_i$ be a limit of $DU$ in $\

we have

which proves that $(\psi_i)^\# = \psi_i T. \xi_i: LT \longrightarrow K_i$ is a lower bound of $(\Delta, DU)$, and there exists a unique $\xi: LT \longrightarrow L$ such that

It is now worth our while to make explicit the following general lemma which includes 2.1.15 as a special case:

(1.20) If $\psi: L \longrightarrow D$ is a limit of $(\Delta, D)$ in $\mathcal{K}$ then the family $(\psi_i: L \longrightarrow D_i)$ is (collectively) mono in the sense that given any pair of maps $t, u: T \longrightarrow L$ such that $t.\psi_i = u.\psi_i$ for all $i, t = u$. The proof is trivial: the common value $t.\psi_i = u.\psi_i: T \longrightarrow D_i$ is a lower bound of $(\Delta, D)$ and $t, u$ are both the unique induced map.

The remaining details of 1.19 are too similar to 1.4.27 and 2.1.11 to bear repeating. $\square$

The following result is easily pieced together from the adjoint functor theorems 2.2.24, 2.2.29, and 1.9, 1.16, and 1.19. Notice, also, that if $U: \mathcal{A} \longrightarrow \mathcal{K}$ creates limits then $\mathcal{A}$ has and $U$ preserves whatever limits $\mathcal{K}$ has.
