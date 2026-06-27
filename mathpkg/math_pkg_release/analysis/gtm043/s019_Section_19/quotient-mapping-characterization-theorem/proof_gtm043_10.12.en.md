---
role: proof
locale: en
of_concept: quotient-mapping-characterization-theorem
source_book: gtm043
source_chapter: "10"
source_section: "10.12"
---

**Necessity.** If $f \in A$, then there exists $g \in \mathbf{R}^{Y}$ such that $f = g \circ \tau$. Let $F$ be a closed set in $\mathbf{R}$. The set

$$\tau^{\leftarrow}[g^{\leftarrow}[F]],$$

that is, $f^{\leftarrow}[F]$, is closed, by continuity of $f$. Hence $g^{\leftarrow}[F]$ is closed, since $\tau$ is a quotient mapping. Thus, $g$ is continuous, so that $f = \tau'g \in \tau'[C(Y)]$.

**Sufficiency.** Since $\tau$ is onto $Y$, the mapping $g \mapsto g \circ \tau$ from $\mathbf{R}^{Y}$ ($= \mathbf{R}^{Y_{\tau}}$) into $\mathbf{R}^{X}$ is one-one. By hypothesis, the image of $C(Y)$ under this induced mapping is $A$. Since the topology of $Y_{\tau}$ contains that of $Y$, so that $C(Y_{\tau}) \supset C(Y)$, the image of $C(Y_{\tau})$ is also $A$. Thus the identity map $Y_{\tau} \to Y$ induces an isomorphism of the corresponding function rings, which implies the topologies coincide, so $\tau$ is a quotient mapping.
