---
role: proof
locale: en
of_concept: existence-orthogonal-basis
source_book: gtm007
source_chapter: "IV"
source_section: "§1.3 Isotropic vectors"
---

We use induction on $n = \dim V$, the case $n = 0$ being trivial. If $V$ is isotropic (i.e., $Q(x) = 0$ for all $x$), all bases of $V$ are orthogonal. Otherwise, choose an element $e_1 \in V$ such that $e_1 \cdot e_1 \neq 0$. The orthogonal complement $H$ of $e_1$ is a hyperplane and since $e_1$ does not belong to $H$, one has

$$V = k e_1 \;\hat{\oplus}\; H.$$

In view of the inductive hypothesis, $H$ has an orthogonal basis $(e_2, \dots, e_n)$, and $(e_1, \dots, e_n)$ has the desired property.
