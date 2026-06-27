---
role: proof
locale: en
of_concept: burnsides-counting-lemma
source_book: gtm006
source_chapter: "I. Review of Basic Algebra"
source_section: "1. Introduction"
---

If $x$ is an element of $\mathcal{S}$ and $\alpha$ an element of $\Gamma$, then we call the ordered pair $(x, \alpha)$ a flag if $x^\alpha = x$; we wish to count the flags. On the one hand, for each $x$ in $\mathcal{S}$, there are $|\Gamma_x|$ elements $\alpha$ such that $(x, \alpha)$ is a flag, so the number of flags is $\sum_{x \in \mathcal{S}} |\Gamma_x|$. But the sum of $|\Gamma_x|$ over an orbit is $|\Gamma|$, so summing over all orbits $t$ gives $t|\Gamma|$ flags. On the other hand, for each $\alpha$, there are $f(\alpha)$ elements $x$ with $(x, \alpha)$ a flag, so the total is also $\sum_{\alpha} f(\alpha)$. Equating yields the result.
