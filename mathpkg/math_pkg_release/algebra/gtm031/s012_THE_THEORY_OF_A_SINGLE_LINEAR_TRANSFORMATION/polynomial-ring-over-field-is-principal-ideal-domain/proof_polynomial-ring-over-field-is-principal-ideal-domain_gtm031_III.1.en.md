---
role: proof
locale: en
of_concept: polynomial-ring-over-field-is-principal-ideal-domain
source_book: gtm031
source_chapter: "III"
source_section: "1"
---

The statement is a standard result from ring theory and is cited as known in the text without proof. A proof uses the division algorithm: let $\mathfrak{a} \neq (0)$ be a nonzero ideal of $\Phi[\lambda]$. Choose a nonzero polynomial $d(\lambda) \in \mathfrak{a}$ of minimal degree. For any $f(\lambda) \in \mathfrak{a}$, the division algorithm gives $f = qd + r$ with $\deg r < \deg d$ or $r = 0$. Since $r = f - qd \in \mathfrak{a}$, minimality of $\deg d$ forces $r = 0$, so $f = qd$. Thus $\mathfrak{a} = (d(\lambda))$.
