---
role: proof
locale: en
of_concept: factorization-of-pseudopolynomials
source_book: gtm038
source_chapter: "III"
source_section: "6"
---

**Proof of Theorem 6.4.**

*Part 1.* If $\omega \in Q^0[u]$, then $\omega$ has the form
$$\omega = u^s + A_1 u^{s-1} + \cdots + A_s$$
with $A_i \in Q$ for $i = 1, \ldots, s$. Let
$$(\omega)_\zeta := u^s + (A_1)_\zeta u^{s-1} + \cdots + (A_s)_\zeta \in Q^0[u].$$
If $(\omega)_\zeta$ lies in $I^0[u]$ for all $\zeta \in G$, then it follows from the earlier considerations (concerning the injectivity of $\theta_\zeta$ and the relation between germs and holomorphy) that $A_1, \ldots, A_s$ are holomorphic functions; that is, $\omega \in A^0[u]$.

*Part 2.* Now let $\omega_1, \omega_2 \in Q^0[u]$ with $\omega_1 \cdot \omega_2 \in A^0[u]$. For each $\zeta \in G$, consider the germ map $\theta_\zeta : Q^0[u] \to I^0[u]$, where $I = I(G)$ is the stalk of germs of holomorphic functions at $\zeta$. Since $\omega_1 \cdot \omega_2 \in A^0[u]$, we have
$$(\omega_1 \cdot \omega_2)_\zeta = (\omega_1)_\zeta \cdot (\omega_2)_\zeta \in I^0[u]$$
for all $\zeta \in G$. By the properties of the stalk $I_\zeta$ (which is a unique factorization domain), if the product $(\omega_1)_\zeta \cdot (\omega_2)_\zeta$ belongs to $I^0[u]$, then each factor $(\omega_i)_\zeta$ belongs to $I^0[u]$. Applying Part 1 to each $\omega_i$ individually yields $\omega_1, \omega_2 \in A^0[u]$.
