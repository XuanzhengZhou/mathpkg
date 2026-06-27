---
role: proof
locale: en
of_concept: dimension-of-direct-sum
source_book: gtm023
source_chapter: "1"
source_section: "1.21"
---

Let $x_1, \ldots, x_p$ be a basis of $E_1$ and $x_{p+1}, \ldots, x_{p+q}$ be a basis of $E_2$. Then the vectors $x_1, \ldots, x_{p+q}$ form a basis of $E$. They generate $E$ since every vector in $E$ is a sum of a vector in $E_1$ and a vector in $E_2$, each expressible in their respective bases. They are linearly independent because if a linear combination vanishes, grouping terms from each subspace gives a vector in $E_1 \cap E_2 = \{0\}$, forcing all coefficients to be zero. Hence $\dim E = p + q = \dim E_1 + \dim E_2$.
