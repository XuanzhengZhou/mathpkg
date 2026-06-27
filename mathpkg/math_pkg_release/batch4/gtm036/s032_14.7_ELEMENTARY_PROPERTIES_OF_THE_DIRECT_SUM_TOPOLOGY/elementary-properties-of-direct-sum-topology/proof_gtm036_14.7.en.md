---
role: proof
locale: en
of_concept: elementary-properties-of-direct-sum-topology
source_book: gtm036
source_chapter: "14"
source_section: "14.7"
---

**Proof of part (iv).** We write $x(t)$ for $x_t$. Let $\{x_\alpha : \alpha \in D\}$ be a Cauchy net in the direct sum $E = \sum \{E_t : t \in A\}$. Because projection into each coordinate space $E_t$ is continuous, $\{x_\alpha(t) : \alpha \in D\}$ is a Cauchy net in $E_t$ and hence converges to one or more points of $E_t$. Select $x(t)$ to be one of the points to which $\{x_\alpha(t)\}$ converges, taking care to select $0$ if possible. For each $t$ such that $x(t) \neq 0$, let $U_t$ be a closed convex neighborhood of $0$ in $E_t$ such that $x(t) \notin U_t$, and, for $t$ for which $x(t) = 0$, let $U_t = E_t$.

Since $\{x_\alpha\}$ is Cauchy, there is $\beta$ in $D$ such that $\gamma \geq \beta$ implies $x_\gamma - x_\beta \in U$, where $U = \sum \{U_t : t \in A\}$ is a neighborhood of $0$ in the direct sum topology. Let $B = \{t : x(t) \neq 0\}$; then $x$ belongs to the $\mathcal{P}$-closure of $U \cap \left(\sum \{E_t : t \in B\}\right)$. (This is a consequence of the fact that, if $z \in U$, then a point obtained from $z$ by replacing one or more coordinates of $z$ by $0$ is still in $U$.) The set $B$ is finite, and the direct sum topology relativized to $\sum \{E_t : t \in B\}$ is identical to the relativized $\mathcal{P}$-topology; hence $x \in U^{-}$. Since the direct sum topology is stronger than $\mathcal{P}$, $U^{-}$ is $\mathcal{P}$-closed. Therefore the Cauchy net converges, establishing completeness.
