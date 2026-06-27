---
role: proof
locale: en
of_concept: sierpinski-erdos-decomposition-lemma
source_book: gtm002
source_chapter: "19"
source_section: "The Sierpinski-Erdos Duality Theorem"
---

Let $A = \{\alpha : 0 \leq \alpha < \Omega\}$ be the set of ordinals of first or second class, that is, all ordinals less than the first ordinal $\Omega$ that has uncountably many predecessors. Then $A$ has power $\aleph_1$, and there exists a mapping $\alpha \mapsto G_{\alpha}$ of $A$ onto $G$. For each $\alpha \in A$ define

$$H_{\alpha} = \bigcup_{\beta \leq \alpha} G_{\beta} \quad \text{and} \quad K_{\alpha} = H_{\alpha} - \bigcup_{\beta < \alpha} H_{\beta}.$$

Put $B = \{\alpha \in A : K_{\alpha} \text{ is uncountable}\}$. Properties (a), (c), and (d) imply that $B$ has no upper bound in $A$. Therefore there exists a one-to-one order-preserving map $\phi$ of $A$ onto $B$. For each $\alpha \in A$, define

$$X_{\alpha} = H_{\phi(\alpha)} - \bigcup_{\beta < \alpha} H_{\phi(\beta)}.$$

By construction, the sets $X_{\alpha}$ are disjoint, each has power $\aleph_1$, and they decompose $X$. For any $E \in K$, $E$ is contained in some $G_{\gamma}$ by (c), hence $E \subseteq H_{\gamma}$; since $B$ has no upper bound, $\gamma \leq \phi(\alpha)$ for some $\alpha$, so $E$ is contained in a countable union of the $X_{\alpha}$. Conversely, any countable union of the $X_{\alpha}$ is contained in some $H_{\phi(\beta)}$, which belongs to $K$ since $K$ is a $\sigma$-ideal containing all $G_{\alpha}$.
