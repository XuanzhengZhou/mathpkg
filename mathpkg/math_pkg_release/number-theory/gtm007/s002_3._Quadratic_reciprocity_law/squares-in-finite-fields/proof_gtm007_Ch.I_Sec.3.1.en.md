---
role: proof
locale: en
of_concept: squares-in-finite-fields
source_book: gtm007
source_chapter: "I"
source_section: "§3.1"
---

Case (a) follows from the fact that $x \mapsto x^2$ is an automorphism of $F_q$.

In case (b), let $\Omega$ be an algebraic closure of $F_q$; if $x \in F_q^*$, let $y \in \Omega$ be such that $y^2 = x$. We have:
$$y^{q-1} = x^{(q-1)/2} = \pm 1$$
since $x^{q-1} = 1$.

For $x$ to be a square in $F_q$ it is necessary and sufficient that $y$ belongs to $F_q^*$, i.e. $y^{q-1} = 1$. Hence $F_q^{*2}$ is the kernel of $x \mapsto x^{(q-1)/2}$. Moreover, since $F_q^*$ is cyclic of order $q-1$, the index of $F_q^{*2}$ is equal to $2$.
