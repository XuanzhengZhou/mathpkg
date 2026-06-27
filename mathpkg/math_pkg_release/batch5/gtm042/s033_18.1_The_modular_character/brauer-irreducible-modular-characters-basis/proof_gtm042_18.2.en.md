---
role: proof
locale: en
of_concept: brauer-irreducible-modular-characters-basis
source_book: gtm042
source_chapter: "18"
source_section: "18.2"
---

**Proof of Theorem 42 (R. Brauer).**

(a) We prove first that the $\phi_E$ ($E \in S_k$) are linearly independent over $K$.

Indeed, suppose we had a relation $\sum a_E \phi_E = 0$, with $a_E \in K$, not all zero. Multiplying the $a_E$ by some element of $K$, we can assume that they all belong to the ring $A$, and that at least one does not belong to $\mathfrak{m}$.

By reduction modulo $\mathfrak{m}$, we then have
$$\sum_{E \in S_k} \bar{a}_E \; \overline{\phi_E(s)} = 0 \qquad \text{for all } s \in G_{\text{reg}},$$
where the bar denotes reduction modulo $\mathfrak{m}$, and one of the $\bar{a}_E$ is not zero.

From formula (v) of the preceding section, we get
$$\sum \bar{a}_E \operatorname{Tr}(t_E) = 0 \qquad \text{for all } t \in G,$$
thus also for all $t \in k[G]$.

However, since $K$ is sufficiently large, the modules $E$ are absolutely simple, so by the density theorem, the homomorphism
$$k[G] \longrightarrow \bigoplus_{E \in S_k} \operatorname{End}_k(E)$$
is surjective.

Now let $E \in S_k$ be such that $\bar{a}_E \neq 0$, and let $u \in \operatorname{End}_k(E)$ be an element whose trace is not zero (e.g., a projection onto a one-dimensional subspace). By the surjectivity above, there exists $t \in k[G]$ mapping to $(0, \dots, 0, u, 0, \dots, 0)$ (with $u$ in the $E$-component and zero elsewhere). For this $t$, the trace relation gives $\bar{a}_E \operatorname{Tr}(u) = 0$, hence $\operatorname{Tr}(u) = 0$, a contradiction.

Thus the $\phi_E$ are linearly independent over $K$.

(b) The fact that they span the space of class functions on $G_{\text{reg}}$ follows by a dimension count using the linear independence just proved together with properties of the decomposition map and the Cartan matrix, which will be established later in the chapter. Equivalent formulations include Theorem 42' (the number of irreducible modular characters equals the number of $p$-regular conjugacy classes), which appears as Corollary 3. $\square$
