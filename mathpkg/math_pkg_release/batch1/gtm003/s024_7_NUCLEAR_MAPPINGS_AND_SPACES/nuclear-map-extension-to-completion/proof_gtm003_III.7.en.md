---
role: proof
locale: en
of_concept: nuclear-map-extension-to-completion
source_book: gtm003
source_chapter: "III"
source_section: "7. Nuclear Mappings and Spaces"
---

The first stated property (existence and uniqueness of a continuous extension to the completion) is shared by $u$ with all compact maps on $E$ into $F$. Indeed, if $U$ is a $0$-neighborhood in $E$ such that $u(U) \subset C$ where $C$ is compact in $F$, then since $u$ is uniformly continuous, its restriction to $U$ has a unique continuous extension to $\bar{U}$ (the closure of $U$ in $\tilde{E}$). By linearity, this yields a unique continuous linear extension $\bar{u}: \tilde{E} \to F$.

To show that $\bar{u}$ is nuclear, observe that $\bar{u}$ satisfies the same factorization property as $u$: there exist $U$ and $B$ as in (7.1) such that $u = \psi_B \circ u_0 \circ \phi_U$ with $u_0$ nuclear between Banach spaces. Taking closures in the completion, the same factorization holds for $\bar{u}$, hence $\bar{u}$ is nuclear by definition.
