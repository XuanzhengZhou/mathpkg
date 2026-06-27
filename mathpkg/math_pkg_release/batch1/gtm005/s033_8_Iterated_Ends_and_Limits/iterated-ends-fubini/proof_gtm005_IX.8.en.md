---
role: proof
locale: en
of_concept: iterated-ends-fubini
source_book: gtm005
source_chapter: "IX"
source_section: "8. Iterated Ends and Limits"
---

**Proof.** For each $\langle p, q \rangle \in P \times P$ we are given the end

$$\omega_{p, q}: \int_c S(p, q, c, c) \to S(p, q, -, -).$$

For any $x \in X$, each $P$-indexed family of arrows $\alpha_p: x \to \int_c S(p, p, c, c)$ determines a family

$$\beta_{\langle p, c \rangle} = \omega_{p, p, c} \circ \alpha_p: x \to S(p, p, c, c).$$

The family $\alpha$ is a wedge in $p$ (making $\int_p \int_c S$) if and only if for every arrow $s: p \to q$ in $P$, the following square commutes:

$$\begin{CD}
x @>{\alpha_p}>> \int_c S(p, p, c, c) \\
@V{\alpha_q}VV @VV{\int_c S(s, q, c, c)}V \\
\int_c S(q, q, c, c) @>>{\int_c S(p, s, c, c)}> \int_c S(p, q, c, c)
\end{CD}$$

Also, this square commutes precisely when it commutes after composition with the arrows $\omega_{p,q,c}$ for all objects $c$. Form the cubical diagram with these two squares as front and back faces and with edges $1_x$, $\omega_{p,p,c}$, $\omega_{p,q,c}$, and $\omega_{q,q,c}$ (front to back). By our definitions the four side faces involving these edges commute; hence the front square commutes if and only if the back square commutes for all $c$.

Therefore $\varrho$ is a wedge (in $p$) if and only if $\xi$ is a wedge (in $\langle p, c \rangle$), so that wedges from $x$ to $\int_c S(-, -, c, c)$ correspond one-to-one to wedges from $x$ to $S$. Since the end is a universal wedge, and since a universal is determined up to isomorphism, this gives the isomorphism $\theta$ of the proposition.

Note one essential point: This proposition reduces double to iterated integrals provided the inner integral $\int_c S(p, q, c, c)$ exists for all pairs $\langle p, q \rangle$ (not just for $p = q$). The case of limits involves no such refinement.
