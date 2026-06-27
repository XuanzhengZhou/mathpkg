---
role: proof
locale: en
of_concept: fundamental-group-is-a-group
source_book: gtm047
source_chapter: "14"
source_section: "14"
---

**Proof.** The group axioms are verified as follows:

*Associativity:* For $\bar{p}, \bar{q}, \bar{r} \in \pi(X, P_0)$, we have $(pq)r \cong p(qr)$ via a reparametrization homotopy that adjusts the speeds at which the three loops are traversed.

*Identity:* Let $e(t) = P_0$ for all $t \in [0,1]$ be the constant path. Then for any $p \in \operatorname{CP}(X, P_0)$, $pe \cong p$ and $ep \cong p$ via homotopies that "stretch" the constant portion.

*Inverse:* For $p \in \operatorname{CP}(X, P_0)$, define $p^{-1}(t) = p(1-t)$. Then $pp^{-1} \cong e$ via a homotopy that progressively cancels the forward and backward traversals, and similarly $p^{-1}p \cong e$.

Thus $\pi(X, P_0)$ with the induced multiplication is a group.
