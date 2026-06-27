---
role: proof
locale: en
of_concept: p-adic-integer-exact-sequence
source_book: gtm007
source_chapter: "II"
source_section: "1"
---

Clearly the kernel of $\varepsilon_n$ contains $p^n \mathbb{Z}_p$. Conversely, if $x = (x_m)$ belongs to $\ker(\varepsilon_n)$, then $x_m \equiv 0 \pmod{p^n}$ for all $m \geq n$. This means there exists a well-defined element $y_{m-n}$ of $A_{m-n}$ such that its image under the isomorphism $A_{m-n} \cong p^n \mathbb{Z}/p^m\mathbb{Z} \subset A_m$ satisfies $x_m = p^n y_{m-n}$. The $(y_i)$ define an element $y \in \mathbb{Z}_p = \varprojlim A_i$, and one checks that $p^n y = x$, proving exactness.
