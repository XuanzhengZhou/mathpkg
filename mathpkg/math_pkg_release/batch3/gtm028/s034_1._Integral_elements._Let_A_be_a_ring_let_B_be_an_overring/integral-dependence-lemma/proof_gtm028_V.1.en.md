---
role: proof
locale: en
of_concept: integral-dependence-lemma
source_book: gtm028
source_chapter: "V"
source_section: "1"
---

Let $M = \sum_{i} A m_i$ be a finite set of generators for $M$ over $A$. From $xM \subset M\mathfrak{q}$ we have $xM \subset \sum_i A m_i \mathfrak{q} = \sum_i \mathfrak{q} m_i$. In particular, there exist elements $q_{ji} \in \mathfrak{q}$ such that

$$x m_j = \sum_i q_{ji} m_i \qquad \text{for each } j.$$

This yields a system of $n$ linear homogeneous equations in the $m_i$:

$$\sum_i (\delta_{ji} x - q_{ji}) m_i = 0,$$

where $\delta_{ji}$ are the Kronecker symbols. Let

$$d = \det(\delta_{ji} x - q_{ji}).$$

Multiplying the system by the adjugate matrix gives $d m_i = 0$ for every $i$, hence $d M = (0)$. Therefore $d z = 0$ for all $z \in M$. By condition (2'), we must have $d = 0$ in $A[x]$.

Expanding the determinant $\det(\delta_{ji} x - q_{ji})$, we obtain

$$d = x^n + q_{n-1} x^{n-1} + \cdots + q_1 x + q_0$$

where each $q_i \in \mathfrak{q}$. Since $d = 0$, this is an equation of integral dependence of the required form. $\square$
