---
role: proof
locale: en
of_concept: star-preserves-finite-relations
source_book: gtm022
source_chapter: "VIII"
source_section: "4"
---

If $\rho$ is finite, we can give a description which lists its members and it follows that $*\rho = \rho$. If $\rho$ is infinite, put

$$u_i(x) = (\exists x_1) \cdots (\exists x_{i-1})(\exists x_{i+1}) \cdots (\exists x_n)(\rho(x_1, \ldots, x_{i-1}, x, x_{i+1}, \ldots, x_n)).$$

Each $u_i$ is an infinite definable subset of $\mathbb{S}$. By the argument used in the proof of Corollary 4.5, each $u_i$ gives rise to a concurrent relation whose witness provides a new element in $*u_i$, and thus there exist tuples in $*\rho$ that are not in $\rho$. Hence $*\rho \neq \rho$.
