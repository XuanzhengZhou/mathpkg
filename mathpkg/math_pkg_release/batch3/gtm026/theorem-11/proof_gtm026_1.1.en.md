---
role: proof
locale: en
of_concept: theorem-11
source_book: gtm026
source_chapter: "1"
source_section: "1.26"
---

We use 1.24. It suffices to show that $U$ creates limits and that $U$ creates quotients of congruences. Let $(\Delta, D)$ be a diagram of $(\Omega, E)$-algebras and write $D_i = (X_i, \delta_i)$. Assume that $(L, \psi)$ is a limit of $DU$ in Set. Let $\omega \in \Omega_n$. If $\alpha \in \Delta(i, j)$ we have

$$\psi_j^n$$
$$L^n$$
$$\psi_i^n$$
$$D_\alpha^n$$
$$\delta_i, \omega$$
$$\psi_i$$
$$X_i$$
$$D_\alpha$$
$$X_j$$
$$\psi_j$$

which shows that $(\psi_i^n.\delta_i, \omega).D_\alpha = \psi_j^n.\delta_j, \omega$, i.e., that $(L^n, \psi^n.\delta_{-}, \omega)$ is a lower bound of $DU$. It follows that there exists unique $\delta_\omega: L^n \rightarrow L$ such that $\delta_\omega.\psi_i = \psi_i^n.\delta_i, \omega$ for all $i$; or, in other words, that there exists a unique $\Omega$-algebra structure $\delta$ on $L$ such that $\psi_i: (L, \delta) \rightarrow (X_i, \delta_i)$ is an $\Omega$-homomorphism for all $i$. If $p, q: U^m \rightarrow U$ with $\{p, q\} \in E$ then for all $i$ we have $(L, \delta)p.\psi_i = \psi_i^n.(X_i, \delta_i)p = \psi_i^n.(X_i, \delta

Let $R$ be a congruence on the $(\Omega, E)$-algebra $(X, \delta)$ with coordinate projections $p, q:R \longrightarrow X$. By definition (1.11—) there exists an $(\Omega, E)$-structure $(R, \gamma)$ such that $p, q:(R, \gamma) \longrightarrow (X, \delta)$ are $\Omega$-homomorphisms. For each $\omega \in \Omega_n$, define $\bar{\delta}_{\omega}:(X/R)^n \longrightarrow X/R$ by $(x_i\theta)\bar{\delta}_{\omega} = (x_i)\delta_{\omega}\theta$. If $(x_i, y_i) \in R^n$ then $(x_i)\delta_{\omega} = (x_i, y_i)p^n\delta_{\omega} = (x_i, y_i)\gamma_{\omega}p$ and $(y_i)\delta_{\omega} = (x_i, y_i)\gamma_{\omega}q$ similarly, so that $(x_i)\delta_{\omega}, (y_i)\delta_{\omega}) = (x_i, y_i)\gamma_{\omega} \in R$, which proves that $\bar{\delta}_{\omega}$ is well defined. As $\theta^n:X^n \longrightarrow (X/R)^n$ is onto, $\bar{\delta}$ is the unique $\Omega$-algebra structure on $X/R$ making $\theta$ an $\Omega$-homomorphism. The facts that $(X/R, \bar{\delta})$ satisfies $E$ and that $\theta:(X, \delta) \longrightarrow (X/R, \bar{\delta})$ is co-optimal both follow from the fact that $\theta^n$ is onto for every set $n$, as is clear from the following two diagrams:

Let $\mathcal{A}$ be the category of complete Boolean algebras of 1.5.48 and let $U:\mathcal{A} \longrightarrow \mathbf{Set}$ be the underlying set functor. We proved in 1.5.48 that $U$ is

not algebraic. On the other hand, the proof of 1.26 shows that an equational presentation, tractable or not, always has an underlying set functor $(\Omega, E)$-alg $\longrightarrow$ Set which creates limits and which creates quotients of congruences. The problem with complete Boolean algebras is tractability.
