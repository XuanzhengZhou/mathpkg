---
role: proof
locale: en
of_concept: equalizer-is-monic
source_book: gtm026
source_chapter: "1"
source_section: "1.15"
---

Let $i: E \to A$ be the equalizer of $f, g: A \to B$, and suppose $t, u: E' \to E$ satisfy $t.i = u.i$. Let $i'$ denote the common value $t.i = u.i$. Then $i': E' \to A$ satisfies

$$i'.f = (t.i).f = t.(i.f) = t.(i.g) = (t.i).g = i'.g,$$

so $i'$ equalizes $f$ and $g$. By the universal property of the equalizer $i$, there exists a unique morphism $h: E' \to E$ such that $h.i = i'$. Both $t$ and $u$ satisfy this equation, so by uniqueness $t = u$.
