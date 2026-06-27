---
role: proof
locale: en
of_concept: fubini-theorem-for-ends
source_book: gtm005
source_chapter: "IX"
source_section: "8. Iterated Ends and Limits"
---

For each $\langle p, q \rangle \in P \times P$ we are given the end

$$\omega_{p, q}: \int_c S(p, q, c, c) \rightarrow S(p, q, -, -).$$

For any $x \in X$, each $P$-indexed family of arrows $\alpha_p: x \to \int_c S(p, p, c, c)$ determines a double family $\beta_{p,c}: x \to S(p, p, c, c)$ given by $\beta_{p,c} = \omega_{p,p,c} \circ \alpha_p$. Conversely, each double family $\beta$ with components $\beta_{p,c}: x \to S(p,p,c,c)$ determines by the universal property of $\int_c$ a family $\alpha_p: x \to \int_c S(p,p,c,c)$ such that $\omega_{p,p,c} \circ \alpha_p = \beta_{p,c}$. Consider the condition that $\alpha$ is a wedge in $p$ and the condition that $\beta$ is a wedge in $\langle p, c \rangle$. The condition for $\alpha$ to be a wedge states that for every arrow $s: p \to q$ in $P$,

$$\int_c S(s, s, c, c) \circ \alpha_p = \alpha_q.$$

Post-composing with $\omega_{q,q,c}$ gives an equivalent condition on $\beta$. Form the cubical diagram with front and back squares involving the wedge conditions for $\alpha$ and $\beta$, and side faces involving the naturality of $\omega$. By construction, the four side faces commute, so the front square commutes if and only if the back square commutes for all $c$. Therefore $\varrho$ is a wedge (in $p$) if and only if $\xi$ is a wedge (in $\langle p, c \rangle$), so that wedges from $x$ to $\int_c S(-, -, c, c)$ correspond one-to-one to wedges from $x$ to $S$. Since the end is a universal wedge, and since a universal is determined up to isomorphism, this gives the isomorphism $\theta$ of the proposition.

The essential point: this proposition reduces double to iterated integrals provided the inner integral $\int_c S(p, q, c, c)$ exists for all pairs $\langle p, q \rangle$ (not just for $p = q$). The case of limits involves no such refinement.
