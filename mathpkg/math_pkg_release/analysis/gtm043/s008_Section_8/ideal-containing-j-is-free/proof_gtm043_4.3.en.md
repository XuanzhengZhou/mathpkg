---
role: proof
locale: en
of_concept: ideal-containing-j-is-free
source_book: gtm043
source_chapter: "4"
source_section: "4.3"
---

Let $I$ be any ideal in $C^*(\mathbf{N})$ that contains $j$, where $j(n) = 1/n$. The function $j$ satisfies $j(n) > 0$ for all $n \in \mathbf{N}$ and $j(n) \to 0$ as $n \to \infty$. In particular, $Z(j) = \emptyset$, so $j$ has no zeros on $\mathbf{N}$.

However, for any $n_0 \in \mathbf{N}$, consider the function $j - j(n_0) \in C^*(\mathbf{N})$. This function vanishes at $n = n_0$ but $j(n_0) \neq 0$. Nevertheless, we must show that $\bigcap Z[I] = \emptyset$.

Suppose, for contradiction, that there exists $m \in \mathbf{N}$ such that $f(m) = 0$ for every $f \in I$. In particular, $j(m) = 0$, which contradicts the fact that $j(n) = 1/n \neq 0$ for all $n$. Therefore no such $m$ exists, and $\bigcap Z[I] = \emptyset$. Hence $I$ is free.

Since $j$ is not a unit of $C^*(\mathbf{N})$ (it is not bounded away from zero), there exist maximal ideals containing $j$, and by the above, every such maximal ideal is free.
