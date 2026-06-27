---
role: proof
locale: en
of_concept: factorization-colimit-theorem
source_book: gtm026
source_chapter: "7"
source_section: "7.1"
---

*Proof.* To show that every diagram $D$ in $\mathcal{C}$ has a colimit, it suffices to construct a small solution set for lower bounds of $D$. Let $(A, \psi)$ be an arbitrary lower bound of $D$ in $\mathcal{C}^{\Delta}$, with $\psi_i: D_i \to A$ admissible in $\mathcal{C}$. Apply the $E$-$M$ factorization in $\mathcal{K}$ to each $\psi_i$, obtaining $(e_i: D_i \twoheadrightarrow E_i, m_i: E_i \rightarrowtail A)$. By diagonal fill-in, $E$ becomes a $\Delta$-diagram in $\mathcal{K}$ and $(A, m_i)$ is a lower bound of $E$.

Let $(C, \tau)$ be a quasi-colimit of $E$ in $\mathcal{K}$, so there exists $t: C \to A$ with $\tau_i t = m_i$. Let $(F, \eta)$ be free over $C$ with respect to $U$ (using the left adjoint), and let $t^{\#}: F \to A$ be the unique $\mathcal{C}$-admissible extension of $t$. Apply the $E$-$M$ factorization to $t^{\#}$ in $\mathcal{K}$, obtaining $(e, m)$ with $m$ a monomorphism. By hypothesis, $m$ admits an optimal lift to a $\mathcal{C}$-object $S$, and we define $\Gamma_i = e_i \tau_i \eta e$. Since $\Gamma_i m = \psi_i$ is admissible and $m$ is optimal, each $\Gamma_i$ is admissible, and $(S, \Gamma)$ is a lower bound of $D$. 

The object $S$ is determined by the family $(E_i)_{i \in N(\Delta)}$, which ranges over a small set because $\mathcal{K}$ is $E$-co-well-powered and $\Delta$ is small. Hence the mediating $\Gamma_i$ range over the small set $\bigcup_{S \in \mathcal{S}} \bigcup_{i \in N(\Delta)} \mathcal{C}(D_i, S)$. Thus the solution set condition is satisfied, and by Theorem 7.4, $D$ has a colimit. $\square$
