---
role: proof
locale: en
of_concept: enlargement-consistency
source_book: gtm022
source_chapter: "VIII"
source_section: "3"
---

Suppose $\mathcal{T}^\sigma \vdash F$. Then $A_0 \vdash_{\mathcal{T}} F$ for some finite subset $A_0$ of $A_\sigma$. Let $A_0 = \{ \rho_j(x_{ij}, c_{\rho_j}) \mid i = 1, \ldots, r_j; j = 1, \ldots, n \}$, where $x_{ij} \in D_{\rho_j}$. Since $\{x_{1j}, \ldots, x_{r_j j}\}$ is a finite subset of $D_{\rho_j}$, there exists $b_j \in D_{\rho_j}$ such that $\rho_j(x_{ij}, b_j)$ holds for all $i = 1, \ldots, r_j$. Replacing each constant $c_{\rho_j}$ by $b_j$, each axiom in $A_0$ becomes a true statement in $\mathbb{S}$, hence a theorem of $\mathcal{T}$. Thus $A_0$ is redundant in $\mathcal{T}^\sigma$, and $\mathcal{T} \vdash F$. Since $\mathcal{T}$ is consistent, $F$ cannot be $F$ (false). Therefore $\mathcal{T}^\sigma$ is consistent.
