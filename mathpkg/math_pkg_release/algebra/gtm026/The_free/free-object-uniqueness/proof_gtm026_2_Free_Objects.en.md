---
role: proof
locale: en
of_concept: free-object-uniqueness
source_book: gtm026
source_chapter: "2"
source_section: "Free Objects"
---

By the universal property of $(F, \eta)$, there exists a unique $\mathcal{A}$-morphism $g: F \longrightarrow F'$ such that $\eta' = \eta \cdot (gU)$. By the universal property of $(F', \eta')$, there exists a unique $\mathcal{A}$-morphism $h: F' \longrightarrow F$ such that $\eta = \eta' \cdot (hU)$.

Now consider the composite $gh: F \longrightarrow F$. We have:

$$\eta \cdot (gh)U = \eta \cdot gU \cdot hU = \eta' \cdot hU = \eta$$

But also $\eta = \eta \cdot (\mathrm{id}_F)U$. By the uniqueness clause of the universal property applied to $(F, \eta)$ itself, we conclude $gh = \mathrm{id}_F$. Symmetrically, $hg = \mathrm{id}_{F'}$.

Therefore $g$ and $h$ are mutually inverse isomorphisms, and $g$ is the unique isomorphism with $\eta' = \eta \cdot (gU)$.
