---
role: proof
locale: en
of_concept: theorem-4-2-class-group-quotient
source_book: gtm059
source_chapter: "5"
source_section: "4"
---

*Proof.* Apply Theorem 4.1 to the $\mathbb{Z}_p$-extension $K_\infty / K_n$ (which replaces the base field $K$ by $K_n$). By the semidirect product description, the Galois group $G_n = \operatorname{Gal}(M_\infty/K_n)$ satisfies $G_n = G_{n+1} \rtimes I_n$ where $I_n$ is the inertia group. 

By class field theory, $C_n \cong \operatorname{Gal}(L_n/K_n)$ where $L_n$ is the $p$-Hilbert class field of $K_n$. The norm map $N_{K_{n+1}/K_n}: C_{n+1} \to C_n$ corresponds to the restriction map on Galois groups. Using the semidirect product structure, one shows this map is surjective and its kernel is $U_{n+1}$ as described.

Passing to the inverse limit gives $C = \varprojlim C_n$, which is a finitely generated $\Lambda$-module. The isomorphism $C_n \cong C/\nu_n C$ follows from the structure theory of $\Lambda$-modules, specifically the fact that $C_n$ is the $\Gamma_n$-coinvariant quotient of $C$ where $\Gamma_n = \operatorname{Gal}(K_\infty/K_n) \cong p^n\mathbb{Z}_p$.
