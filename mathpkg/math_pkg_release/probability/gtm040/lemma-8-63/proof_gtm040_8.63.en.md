---
role: proof
locale: en
of_concept: lemma-8-63
source_book: gtm040
source_chapter: "8"
source_section: "63"
---

**Proof:** By dominated convergence,

$$M_i[z^{(\infty)}] = \lim M_i[z^{(n)}],$$

and by Theorem 4-11 with the random time $n$,

$$\{M_i[z^{(n)}]\} = P^n \{M_i[z]\} = P^n h.$$

Hence

$$M_i[z^{(\infty)}] = \lim P^n h.$$

By Theorem 5-10,

$$h_i = (Nf)_i + M_i[z^{(\infty)}].$$

Thus $h = Nf$ if and only if $M_i[z^{(\infty)}] = 0$ for every $i$. Since $z^{(\infty)} \geq 0$, $M_i[z^{(\infty)}] = 0$ for all $i$ if and only if $z^{(\infty)} = 0$ a.e.
