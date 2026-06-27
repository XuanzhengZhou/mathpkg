---
role: proof
locale: en
of_concept: krull-intersection-domain-corollary
source_book: gtm028
source_chapter: "IV"
source_section: "§6. Krull's intersection theorem"
---

If $\mathfrak{m}^p = \mathfrak{m}^q$ for $p < q$, then $\mathfrak{m}^p = \mathfrak{m}^{p+1}$. Multiplying by $\mathfrak{m}$ gives $\mathfrak{m}^{p+2} = \mathfrak{m}^{p+1} = \mathfrak{m}^p$, and by induction $\mathfrak{m}^{p+n} = \mathfrak{m}^p$ for all $n \geq 0$. Then $\bigcap_n \mathfrak{m}^n = \mathfrak{m}^p \neq (0)$. But by Krull's Intersection Theorem, since $1 - \mathfrak{m}$ contains $1$ (which is not a zero-divisor in a domain), we would have $\bigcap_n \mathfrak{m}^n = (0)$, a contradiction. Hence $\mathfrak{m}^p \neq \mathfrak{m}^q$ for $p \neq q$.
