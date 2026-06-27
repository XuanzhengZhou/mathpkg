---
role: proof
locale: en
of_concept: nonorientable-3-manifold-2-fold-covering
source_book: gtm047
source_chapter: "7"
source_section: "24"
---

**Proof.** Let $K$ be a triangulation of $M$, and let $P_0$ be a vertex of $K$. Take a fixed orientation $C^3 = \sum \alpha_i \sigma_i^3$ of the complex $\text{St } P_0$, as in the discussion just before Theorem 23.14. If $P_0v$ is an edge of $K$, then $C^3$ gives an orientation of $\text{St } P_0 \cap \text{St } v$, and this in turn determines an orientation of $\text{St } v$. Inductively, every simplicial path in the 1-skeleton $K^1$, from $P_0$ to a vertex $v_i$ of $K$, determines an orientation of $\text{St } v_i$.

Now consider a path of the type $r_i = p_i q_i$, from $P_0$ to a point $Q_i$, where $p_i$ is simplicial, from $P_0$ to a vertex $v_i$ of $K$, such that $v_i$ lies in the simplex of smallest dimension that contains $Q_i$, and $q_i$ is rectilinear from $v_i$ to $Q_i$. Two such paths $r_1, r_2$ are defined to be equivalent if they have the same terminal point $Q$ and $p_1$ and $p_2$ determine the same orientation of $\text{St } v_1 \cap \text{St } v_2$. (The latter is a triangulation of a 3-cell, because $v_1$ and $v_2$ are the end-points of an edge of $K$.)

Let $P_0 = v_0 \in J$. We now construct the 2-fold covering $g: \tilde{M} \rightarrow M$ that was used in the proof of Theorem 7, using $b^2K$ as our triangulation of $M$. Let $\tilde{P}_0$ be any point of $g^{-1}(P_0)$, let $g_0^*$ be as in Theorem 2, and let $\pi_0 = g_0^*(\pi(\tilde{M}, \tilde{P}_0))$. Let $p$ be a simplicial closed path in $\text{CP}(M, P_0)$, traversing $J$ exactly once. Then $\overline{p} \in \pi_0$, because $\overline{p} = \overline{e}$. By Theorem 3, $p$ has a lifting $\tilde{p} \in \text{CP}(\tilde{M}, \tilde{P}_0)$. Thus, given an orientation of $\text{St } P_0$ (in $b^2K$), $p$ induces the same orientation of $\text{St } P_0$. Thus $N = \bigcup_i |\text{St } v_i|$ is orientable, which was to be proved.
