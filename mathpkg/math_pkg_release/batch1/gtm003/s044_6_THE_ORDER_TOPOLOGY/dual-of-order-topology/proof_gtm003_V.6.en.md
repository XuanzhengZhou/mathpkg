---
role: proof
locale: en
of_concept: dual-of-order-topology
source_book: gtm003
source_chapter: "V. Order Structures"
source_section: "6. The Order Topology"
---

The proof proceeds by considering the directed family $\mathcal{F}$ of all finite subsets of $A$, ordered by inclusion. For each $F \in \mathcal{F}$, let $L_F = \prod_{\alpha \in F} L_\alpha \times \prod_{\alpha \notin F} \{0\}$, and let $L_F^+$ be the corresponding subspace of the direct sum. Each $L_F$ inherits the order topology from the finite product, and the order topology on the full product (respectively, direct sum) is the locally convex inductive limit (respectively, projective limit) of the $L_F$.

Now, a linear form $f$ on $L$ is continuous for $\mathfrak{T}_0$ if and only if $f$ is bounded on order intervals. Indeed, if $f$ is $\mathfrak{T}_0$-continuous, then $f^{-1}((-1,1))$ is a $\mathfrak{T}_0$-neighborhood, hence absorbs every order interval; thus $f$ is bounded on each order interval. Conversely, if $f$ maps each order interval to a bounded set, then for any $\varepsilon > 0$, the set $\{x: |f(x)| < \varepsilon\}$ is convex and absorbs every order interval, hence is a $\mathfrak{T}_0$-neighborhood.

For the product case: if $W$ is a convex $0$-neighborhood in $(L, \mathfrak{T}_0)$, then for each projection $p_i: L \to L_i$, the image $p_i(W)$ is convex and absorbs the order interval $I_i$ in $L_i$, which proves that each $p_i(W)$ is a $\mathfrak{T}_{0,i}$-neighborhood, establishing the dual identification. This completes the proof.
