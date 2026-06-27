---
role: proof
locale: en
of_concept: isomorphism-iff-equivalent-transition-functions
source_book: gtm020
source_chapter: "5"
source_section: "2"
---

Let $f: \eta \to \eta'$ be an isomorphism of fibre bundles or vector bundles. From the relation $h_j(b, y) = h_i(b, g_{i,j}(b)y)$, it follows that $f h_j(b, y) = f h_i(b, g_{i,j}(b)y)$, and $\{(V_i, f h_i)\}$ is an atlas for $\eta'$ with transition functions $\{g_{i,j}\}$. By applying Proposition 2.5 to the atlases $\{(V_i, h_i')\}$ and $\{(V_i, f h_i)\}$, we find that $\{g_{i,j}'\}$ and $\{g_{i,j}\}$ are equivalent sets of transition functions.

Conversely, let $g_{i,j}'(b) = r_i(b)^{-1} g_{i,j}(b) r_j(b)$ for each $b \in V_i \cap V_j$. We define $f_i: V_i \times Y \to V_i \times Y$ by $f_i(b, y) = (b, r_i(b)^{-1} y)$, and we define $f: \eta \to \eta'$ by requiring that $f|_{(\eta|_{V_i})} = h_i' f_i h_i^{-1}$ or $h_i' f_i = f h_i$ on $V_i \times Y$. For $b \in V_i \cap V_j$ the two definitions of $f$ lead to the same map. To see this, we choose $(b, y) \in (V_i \cap V_j) \times Y$ and verify that $h_j' f_j(b, y) = f h_j(b, y)$ implies $h_i' f_i(b, y) = f h_i(b, y)$. This follows by direct computation using the transition function relations.
