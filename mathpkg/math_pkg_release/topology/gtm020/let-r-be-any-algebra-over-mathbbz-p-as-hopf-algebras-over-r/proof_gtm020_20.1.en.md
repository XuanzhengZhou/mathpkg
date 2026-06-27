---
locale: en
of_concept: let-r-be-any-algebra-over-mathbbz-p-as-hopf-algebras-over-r
role: proof
source_book: gtm020
source_chapter: 20. General Theory of Characteristic Classes
source_section: '1'
---

The equivalence of (1) and (2) follow immediately from the exact sequence involving $H_{(p)}$ mentioned after (5.1).

For (1) implies (3) observe that the pair $(\Omega S^{2n+1}, F_n(p))$ localized at $p$ is $(2pn-1)$-connected and by (1) we have elements $[u] \in \pi_{2pn-1}(F_n(p))_{(p)}$ and $[v] \in \pi_{2pn-2}(\Omega F_n(p))_{(p)}$ related by the usual isomorphism and mapping to a nonzero element of $Z/p$ in the following commutative diagram.

$$[u] \in \pi_{2pn-1}(F_n(p))_{(p)} \rightarrow \pi_{2pn-1}(\Omega S^{2n+1})_{(p)} \rightarrow \pi_{2pn-1}(\Omega S^{2n+1}, F_n(p))_{(p)} = 0$$

$$[v] \in \pi_{2pn-2}(\Omega F_n(p))_{(p)} \rightarrow \pi_{2pn-2}(\Omega^2 S^{2n+1})_{(p)}$$

$$\pi_{2pn-2}(\Omega^2 S^{2n+1}, S^{2n-1})_{(p)} \xrightarrow{H_{(p)}} Z/p$$

Form $X = F_n(p) \cup u e^{2pn}$ and view $S^{2n} \subset F_n(p) \subset X$. Then we have maps $S^{2n-1} \rightarrow \Omega F_n(p) \cup v e^{2pn-1} \rightarrow \Omega X$. By (5.3) and the homological properties of $u$ and $v$ it follows that the composite is an isomorphism.

$$H_i(S^{2n-1}) \rightarrow H_i(\Omega F_n(p) \cup v e^{2pn-1}) \rightarrow H_i(\Omega X)$$

over $Z_{(p)}$ for $i < 2(p+1)n-3$. By

is zero for $n > 1$ when $p > 2$ (result originally of Luilevicius, Shimada, and Yamoshita) and for $n \neq 1, 2, 4$ when $p = 2$ (Adams). The case $p = 2$ is contained in (5.2) and (4.9). Now we show that $H_{(p)}: \pi_{2p}(S^3)_{(p)} \rightarrow \mathbf{Z}/p$ is nonzero (the case $n = 1$). This can be seen in different ways and we consider two. Let $P_n$ denote the complex projective $n$ space.

**Proof (1).** Map $g_m: S^2 \times \dots \times S^2 \rightarrow P_m$ by the relation

$$g_m((a_1, b_1), \dots, (a_m, b_m)) = \prod_{j=1}^{m} (a_j z + b_j)$$

where the coordinates of $P_m$ are coefficients of nonzero polynomials of degree $\leq m$ up to scalar factor. The map $g_m$ has degree $m!$, and $S(g_m): S(S^2 \times \dots \times S^2) \rightarrow SP_m$ restricts to the top cell $S^{2m+1}$ in the wedge decomposition given by (3.1) to a map $S^{2m+1} \rightarrow SP_m$ of degree $m!$. Hence for $m < p$, localized at $p$ we have a homotopy equivalence $SP_{m-1} \vee e^{2m+1} \rightarrow SP_m$. Again localized at $p$, we can split and map

$$SP_p \simeq (S^3 \vee S^5 \vee \cdots \vee S^{2p-1}) \cup_\alpha e^{2p+1} \xrightarrow{f} S^3 \cup_\alpha e^{2p+1}$$

where $f^*$ is a monomorphism on cohomology. The $p$th power $= \mathcal{P}^1$ for $

$$\text{ord}_p(k^{m(p-1)} - 1) = \begin{cases} \text{ord}_p(m) + 1 & \text{for } p > 2 \\ 1 & \text{for } p = 2, m \text{ odd} \\ \text{ord}_2(m) + 2 & \text{for } p = 2, m \text{ even} \end{cases}$$

Moreover $\text{ord}_p(k^{m(p-1)} - 1) \geq m$ if and only if $m = 1$ for $p > 2$ and $m = 1, 2$, or $4$ for $p = 2$.
