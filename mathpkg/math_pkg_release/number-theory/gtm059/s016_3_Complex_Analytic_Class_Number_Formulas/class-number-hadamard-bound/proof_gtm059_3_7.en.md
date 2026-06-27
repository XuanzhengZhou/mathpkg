---
role: proof
locale: en
of_concept: class-number-hadamard-bound
source_book: gtm059
source_chapter: "3"
source_section: "7"
---

By Theorem 7.1, the class number $h_p^+$ equals the absolute value of the determinant of $D_p$, whose entries are $a_{gh} = R(gh^{-1}) - R(-gh^{-1})$ for $g, h \in S$, where $S$ represents $(\mathbb{Z}/p\mathbb{Z})^{\times}/\{\pm 1\}$ and has $r = \frac{p-3}{2}$ elements.

For any $x$ coprime to $p$, $R(x)$ is the smallest positive residue, so $1 \leq R(x) \leq p-1$ and $R(-x) = p - R(x)$. Hence

$$|R(x) - R(-x)| = |2R(x) - p|.$$

Since $R(x)$ is the *smallest* positive residue, we have $R(x) \leq p/2$ when $R(x) < p/2$, but when $R(x) > p/2$, the smallest positive residue of $-x$ is $p - R(x) < p/2$. Consequently each entry $a_{gh}$ satisfies $|a_{gh}| \leq 1$.

The Euclidean norm of each row satisfies $\|\text{row}_i\|_2^2 = \sum_{j=1}^r a_{ij}^2 \leq r$. Hadamard's inequality yields

$$h_p^+ = |\det D_p| \leq \prod_{i=1}^r \|\text{row}_i\|_2 \leq r^{r/2} = \left(\frac{p-3}{2}\right)^{\frac{p-3}{4}}.$$
