---
role: proof
locale: en
of_concept: dimension-of-entire-modular-forms-space
source_book: gtm041
source_chapter: "6"
source_section: "6.4"
---
By Theorem 6.3, the products $G_{k-12r} \Delta^r$ for $r = 0, 1, \ldots, [k/12]$ form a basis for $M_k$. The number of such products is $[k/12] + 1$, except when $k \equiv 2 \pmod{12}$, in which case the term with $r = [k/12]$ would involve $G_2$. Since $G_2$ is not an entire modular form, this term must be excluded, giving one fewer basis element. Therefore
$$
\dim M_k = \begin{cases}
\left[ \frac{k}{12} \right] & \text{if } k \equiv 2 \pmod{12}, \\[6pt]
\left[ \frac{k}{12} \right] + 1 & \text{if } k \not\equiv 2 \pmod{12}.
\end{cases}
$$
Another basis for $M_k$ is the set of products $G_4^a G_6^b$ where $a \geq 0$, $b \geq 0$ and $4a + 6b = k$ (see Exercise 6.12).
