---
role: proof
locale: en
of_concept: closed-class-characterization
source_book: gtm043
source_chapter: "12"
source_section: "12.4"
---
The necessity of (i)-(iii) is obvious from the definition. Conversely, suppose $\mathfrak{C}$ satisfies them.

Let $\mathfrak{m} \in \mathfrak{C}$. The successor of $\mathfrak{m}$ is $\leq 2^{\mathfrak{m}}$, hence in $\mathfrak{C}$ by (iii) and (i).

Given $\mathfrak{m}$ cardinals $\mathfrak{n}_s$ in $\mathfrak{C}$, let $\mathfrak{n} = \sum_s \mathfrak{n}_s$. Then $\mathfrak{n} \in \mathfrak{C}$ by (ii). Since $\sup_s \mathfrak{n}_s \leq \mathfrak{n}$, we have $\sup_s \mathfrak{n}_s \in \mathfrak{C}$ by (i).

Furthermore,
$$\prod_s \mathfrak{n}_s \leq \prod_s 2^{\mathfrak{n}_s} = 2^{\mathfrak{n}} \in \mathfrak{C},$$
so $\prod_s \mathfrak{n}_s \in \mathfrak{C}$ by (i).

Finally, if $\mathfrak{l} \in \mathfrak{C}$, then $\mathfrak{l}^{\mathfrak{m}} \leq 2^{\mathfrak{l} \cdot \mathfrak{m}} \in \mathfrak{C}$, so $\mathfrak{l}^{\mathfrak{m}} \in \mathfrak{C}$.