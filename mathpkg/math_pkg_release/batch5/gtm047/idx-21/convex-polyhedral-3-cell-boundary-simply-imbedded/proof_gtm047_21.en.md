---
role: proof
locale: en
of_concept: convex-polyhedral-3-cell-boundary-simply-imbedded
source_book: gtm047
source_chapter: ""
source_section: "21"
---

**Proof.** We have given a triangulation of $\operatorname{Bd} C^3$. We form the join of this complex with any point $v$ of $\operatorname{Int} C^3$, getting a triangulation $K$ of $C^3$. If $\sigma^3 \in K$, then $\sigma^3$ is free in $K$, in the sense that $\operatorname{Bd} \sigma^3 \cap \operatorname{Bd} |K|$ is a 2-cell (namely, the 2-face $\sigma^2$ of $\sigma^3$ that lies in $\operatorname{Bd} |K|$). Thus $\sigma^3$ can be deleted from $K$ (so that $\operatorname{Int} \sigma^2 \cup \operatorname{Int} \sigma^3$ is deleted from $|K|$) by a PLH $f_1: \mathbb{R}^3 \leftrightarrow \mathbb{R}^3$.

Now $f_1(C^3)$ is triangulated as the join of $v$ and a 2-cell $D_1$. $D_1$ has a free 2-simplex $\sigma^2_1$ (in the 2-dimensional sense defined in Section 3). It follows that $\sigma^3_1 = v\sigma^2_1$ is free in $f_1(C^3)$. Since $\sigma^3$ has the push property at the 2-cell $D_2 = \operatorname{Bd} \sigma^3_1 \cap \operatorname{Bd} f_1(C^3)$, it follows that $\sigma^3_1$ can be deleted from $f_1(C^3)$ by a PLH

$$f_2: \mathbb{R}^3 \leftrightarrow \mathbb{R}^3.$$

In a finite number of such steps, we reduce $C^3$ to a single 3-simplex, by a PLH

$$f = f_n f_{n-1} \dots f_2 f_1.$$

Given a convex open set $W$, containing $\operatorname{Bd} C^3$, we can choose each $f_i$ so that $f_i|(\mathbb{R}^3 - W)$ is the identity. Thus $\operatorname{Bd} C^3$ is simply imbedded.
