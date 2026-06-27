---
role: proof
locale: en
of_concept: minimalization-closure-under-special-functions
source_book: gtm037
source_chapter: "3"
source_section: "Recursive Functions; Turing Computability"
---

Suppose $f$ is $m$-ary, $m > 1$. We proceed by induction on $m$; the case $m = 2$ is given by (26). Inductively assume that $m > 2$. Define $f'$ by

$$f'(x_0, \ldots, x_{m-2}) = f(\mathrm{Exc}\, x_0, L x_0, x_1, \ldots, x_{m-2}).$$

Then $f'$ is $(m-1)$-ary and special. Let $g'$ be obtained from $f'$ by minimalization. By the induction hypothesis, $g' \in A$. The function $g$ obtained from $f$ by minimalization satisfies

$$g(x_1, \ldots, x_{m-1}) = g'(J(x_1, 0), x_2, \ldots, x_{m-1})$$

where $J$ is the pairing function. Since $J \in A$ and $A$ is closed under $K_1^1$, we conclude $g \in A$.
