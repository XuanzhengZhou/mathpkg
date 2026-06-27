---
role: proof
locale: en
of_concept: isomorphism-via-equivalent-transition-functions
source_book: gtm020
source_chapter: "5"
source_section: "2"
---

Let $f: \eta \rightarrow \eta'$ be an isomorphism of fibre bundles or vector bundles. From the relation $h_j(b, y) = h_i(b, g_{i,j}(b)y)$, it follows that $f h_j(b, y) = f h_i(b, g_{i,j}(b)y)$, and $\{(V_i, f h_i)\}$ is an atlas for $\eta'$ with transition functions $\{g_{i,j}\}$. By applying Proposition 2.5 to the atlases $\{V_i, h'_i\}$ and $\{(V_i, f h_i)\}$, we find that $\{g'_{i,j}\}$ and $\{g_{i,j}\}$ are equivalent sets of transition functions.

Conversely, let $g'_{i,j}(b) = r_i(b)^{-1} g_{i,j}(b) r_j(b)$ for each $b \in V_i \cap V_j$. We define $f_i: V_i \times Y \rightarrow V_i \times Y$ by $f_i(b, y) = (b, r_i(b)^{-1} y)$, and we define $f: \eta \rightarrow \eta'$ by requiring that $f|(\eta|V_i) = h'_i f_i h_i^{-1}$ or $h'_i f_i = f h_i$ on $V_i \times Y$. For $b \in V_i \cap V_j$ the two definitions of $f$ lead to the same map. To see this, we choose $(b, y) \in (V_i \cap V_j) \times Y$ and verify that $h'_j f_j(b, y) = f h_j(b, y)$ implies $h'_i f_i(b, y) = f h_i(b, y)$ by using the equivalence relation of the transition functions and the cocycle condition.
