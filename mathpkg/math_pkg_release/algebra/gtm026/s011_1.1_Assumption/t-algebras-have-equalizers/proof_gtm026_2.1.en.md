---
role: proof
locale: en
of_concept: t-algebras-have-equalizers
source_book: gtm026
source_chapter: "2"
source_section: "1"
---

Let $f, g: (A, \xi) \longrightarrow (B, \theta)$ be $\mathbf{T}$-homomorphisms and let $i: E \longrightarrow A = \mathrm{eq}(f, g)$ be the equalizer of the underlying morphisms in $\mathcal{K}$.

To verify the $\mathbf{T}$-algebra structure on $E$: The diagram chase shows that
$$(iT.\xi).f = iT.(\xi.f) = iT.fT.\theta = (i.f)T.\theta = (i.g)T.\theta = \cdots = (iT.\xi).g,$$
where we use the fact that $f$ and $g$ are $\mathbf{T}$-homomorphisms (so $\xi.f = fT.\theta$ and $\xi.g = gT.\theta$) and that $i.f = i.g$ since $i$ equalizes $f$ and $g$.

Since $iT.\xi$ equalizes $f$ and $g$, the universal property of $E = \mathrm{eq}(f, g)$ in $\mathcal{K}$ provides a unique $\mathcal{K}$-morphism $\xi': ET \longrightarrow E$ such that $\xi'.i = iT.\xi$. This $\xi'$ defines the $\mathbf{T}$-algebra structure on $E$, and the universal property of the equalizer in $\mathcal{K}^{\mathbf{T}}$ follows by the same reasoning as for products.
