---
role: proof
locale: en
of_concept: cyclic-space-shift-basis-characterization
source_book: gtm023
source_chapter: "XIII"
source_section: "3"
---

If $E$ is cyclic and $a$ is a generator, then by Proposition III the vectors $a_v = \varphi^v(a)$ ($v = 0, \ldots, n-1$) form a basis and clearly $\varphi(a_v) = a_{v+1}$ for $v = 0, \ldots, n-2$.

Conversely, if such a basis exists, then for every vector $x = \sum \xi^v a_v$ define the polynomial $f_x(t) = \sum_{v=0}^{n-1} \xi^v t^v$. Then
$$f_x(\varphi) a_0 = x$$
as is easily checked, and so $E$ is cyclic.
