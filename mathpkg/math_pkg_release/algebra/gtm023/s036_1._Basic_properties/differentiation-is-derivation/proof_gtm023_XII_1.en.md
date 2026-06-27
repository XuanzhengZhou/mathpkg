---
role: proof
locale: en
of_concept: differentiation-is-derivation
source_book: gtm023
source_chapter: "XII"
source_section: "1"
---

For $p, q \geq 1$: $d(t^p \cdot t^q) = d(t^{p+q}) = (p+q)t^{p+q-1} = pt^{p-1}t^q + t^p q t^{q-1} = dt^p \cdot t^q + t^p \cdot dt^q$. For $p=0$ or $q=0$, the formula holds trivially since $d(1)=0$. Since $\{t^p\}$ is a basis, for any $f = \sum \alpha_p t^p$ and $g = \sum \beta_q t^q$, we have $d(fg) = d(\sum_{p,q} \alpha_p\beta_q t^{p+q}) = \sum_{p,q} \alpha_p\beta_q (p+q)t^{p+q-1} = \sum_{p,q} \alpha_p\beta_q(pt^{p-1}t^q + t^p q t^{q-1}) = d(f)g + f d(g)$. For uniqueness: if $\partial$ is any derivation with $\partial(t)=1$, then $\partial(1)=\partial(1\cdot1)=2\partial(1)$ implies $\partial(1)=0$, and by induction $\partial(t^p)=pt^{p-1}=d(t^p)$, so $\partial=d$ on the basis and hence everywhere.
