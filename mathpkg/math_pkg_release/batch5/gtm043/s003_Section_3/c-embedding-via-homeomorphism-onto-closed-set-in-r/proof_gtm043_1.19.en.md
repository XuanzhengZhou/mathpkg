---
role: proof
locale: en
of_concept: c-embedding-via-homeomorphism-onto-closed-set-in-r
source_book: gtm043
source_chapter: "1"
source_section: "1.19"
---

Let $h$ denote the postulated function in $C(X)$. Then $\theta = (h|S)^{\leftarrow}$ is a continuous mapping from $H = h[S]$ onto $S$, with $\theta(h(s)) = s$ (for $s \in S$). Consider an arbitrary function $f$ in $C(S)$. The composition $f \circ \theta$ belongs to $C(H)$. Since $H$ is closed in $\mathbf{R}$, it is $C$-embedded (every closed set in $\mathbf{R}$ is $C$-embedded), and so there is a function $g$ in $C(\mathbf{R})$ that agrees with $f \circ \theta$ on $H$. Then $g \circ h$ is in $C(X)$, and for all $s \in S$,
$$(g \circ h)(s) = f(\theta(h(s))) = f(s),$$
i.e., $g \circ h$ is an extension of $f$.
