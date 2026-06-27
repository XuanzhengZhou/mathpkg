---
role: proof
locale: en
of_concept: right-multiplication-ring-homomorphism
source_book: gtm030
source_chapter: "2"
source_section: "14"
---

For any $x, a, b \in \mathfrak{A}$ we compute:

$$x(a + b)_r = x(a + b) = xa + xb = xa_r + xb_r = x(a_r + b_r).$$

Since this holds for all $x$, we obtain $(a + b)_r = a_r + b_r$.

Similarly,

$$x(ab)_r = x(ab) = (xa)b = (xa_r) b_r = x(a_r b_r).$$

Since this holds for all $x$, we obtain $(ab)_r = a_r b_r$.

These two identities establish that the correspondence $a \mapsto a_r$ preserves both addition and multiplication, hence is a ring homomorphism from $\mathfrak{A}$ into the endomorphism ring $\mathfrak{E}$ of $(\mathfrak{A}, +)$.
