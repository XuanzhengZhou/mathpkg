---
role: proof
locale: en
of_concept: quadric-in-hyperplane-orthogonality
source_book: gtm049
source_chapter: "5"
source_section: "7"
---

Let $Q(\sigma) \subseteq H$. Take $A \in Q(\sigma)$ and any point $B \notin H$. The line $AB$ intersects $Q$ only at $A$, because if it contained another point $C \in Q$, then $C \in H$ (since $Q \subseteq H$), which would force the entire line $AB$ to lie in $H$, contradicting $B \notin H$. Thus the restriction $\sigma_{AB}$ is degenerate, meaning $A$ is orthogonal to $B$ with respect to $\sigma$. Since the points $B \notin H$ span $V$, we have $A \in V^\perp$ for every $A \in Q(\sigma)$. Hence $Q(\sigma) \subseteq V^\perp$.
