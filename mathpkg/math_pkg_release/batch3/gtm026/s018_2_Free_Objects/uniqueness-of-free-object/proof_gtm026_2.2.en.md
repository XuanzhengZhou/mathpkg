---
role: proof
locale: en
of_concept: uniqueness-of-free-object
source_book: gtm026
source_chapter: "2"
source_section: "2"
---

Since $(F, \eta)$ is free over $K$ with respect to $U$, applying its universal property to the pair $(F', \eta')$ yields a unique $\mathcal{A}$-morphism $g: F \longrightarrow F'$ such that $\eta \cdot gU = \eta'$. Symmetrically, since $(F', \eta')$ is free over $K$, applying its universal property to the pair $(F, \eta)$ yields a unique $\mathcal{A}$-morphism $h: F' \longrightarrow F$ such that $\eta' \cdot hU = \eta$.

Now consider the composite $gh: F \longrightarrow F$. We have
$$
\eta \cdot (gh)U = \eta \cdot gU \cdot hU = \eta' \cdot hU = \eta = \eta \cdot (\mathrm{id}_F)U.
$$
Both $gh$ and $\mathrm{id}_F$ are $\mathcal{A}$-morphisms from $F$ to $F$ whose image under $U$ post-composed with $\eta$ yields $\eta$. By the uniqueness clause of the universal property of $(F, \eta)$ applied to the pair $(F, \eta)$, we conclude $gh = \mathrm{id}_F$.

Symmetrically, $hg = \mathrm{id}_{F'}$. Therefore, $g$ and $h$ are mutually inverse isomorphisms whose images under $U$ convert each universal morphism into the other.
