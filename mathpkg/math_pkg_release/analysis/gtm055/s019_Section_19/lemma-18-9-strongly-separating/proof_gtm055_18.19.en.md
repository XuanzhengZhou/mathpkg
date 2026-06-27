---
role: proof
locale: en
of_concept: lemma-18-9-strongly-separating
source_book: gtm055
source_chapter: "18"
source_section: "19"
---

Since $\mathcal{A}$ is strongly separating, there exist functions $h_1, h_2 \in \mathcal{A}$ such that $h_1(x_1) \neq h_1(x_2)$ and $h_2(x_i) \neq 0$ for $i = 1, 2$. One can then form linear combinations of $h_1, h_2$ and the constant function $1$ (which belongs to $\mathcal{A}$ since it is strongly separating and thus contains a function nonzero at each point, from which the constant functions can be recovered via the lattice operations) to obtain a function $f$ with the desired values at $x_1$ and $x_2$.

More explicitly, let $g \in \mathcal{A}$ satisfy $g(x_1) \neq g(x_2)$. Define
$$f(x) = t_1 + \frac{t_2 - t_1}{g(x_2) - g(x_1)}(g(x) - g(x_1)).$$
Since $\mathcal{A}$ is an algebra containing constants, $f \in \mathcal{A}$ and $f(x_i) = t_i$ for $i = 1, 2$.
