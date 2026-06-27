---
role: proof
locale: en
of_concept: open-mapping-theorem-topological-groups
source_book: gtm027
source_chapter: "6"
source_section: "R"
---

# Proof of the Open Mapping Theorem for Topological Groups

Dually, let $g: H \to G$ be a homomorphism of Hausdorff topological groups such that:

(i)* the graph of $g$ is closed in $H \times G$;

(ii)* $\overline{g[V]} \in \mathcal{U}$ whenever $V \in \mathcal{V}$.

The proof is dual to the closed graph theorem, applying Lemma 6.36 to the relation $g$ (rather than $f^{-1}$). Specifically, we view $g$ as a relation from $H$ to $G$ whose graph is closed, and condition (ii)* says that the image of each $V \in \mathcal{V}$ has closure which is a neighborhood of $e_G$.

The lemma ensures that $g$ carries neighborhoods to neighborhoods, i.e., $g$ is open.

More explicitly: for any open $W \subset H$, write $W = \bigcup_{h \in W} hV$ for some $V \in \mathcal{V}$. Then $g[W] = \bigcup_h g(h)g[V]$. Since $g[V]$ has interior (by condition (ii)* and the Baire category argument), $g(h)g[V]$ has interior, and thus $g[W]$ is open.

The proof uses a right-invariant metric for $H$, completeness of $H$ relative to its right uniformity, and the device of Lemma 6.36 applied to the homomorphism $g$.
