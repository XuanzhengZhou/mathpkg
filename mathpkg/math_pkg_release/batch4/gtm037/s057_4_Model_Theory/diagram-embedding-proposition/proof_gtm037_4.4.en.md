---
role: proof
locale: en
of_concept: diagram-embedding-proposition
source_book: gtm037
source_chapter: "4"
source_section: "4"
---

We verify that the map $l \colon A \to B$ is injective and preserves operations.

**Injectivity.** Let $a, b \in A$ with $a \neq b$. The sentence $\neg \mathbf{c}_a = \mathbf{c}_b$ belongs to the $\mathcal{L}'$-diagram of $\mathfrak{A}$. Since $(\mathfrak{B}, l_a)_{a \in A}$ is a model of this diagram, we have $(\mathfrak{B}, l_a)_{a \in A} \models \neg \mathbf{c}_a = \mathbf{c}_b$. Hence $l_a \neq l_b$ in $\mathfrak{B}$, so $l(a) \neq l(b)$.

**Preservation of operations.** Let $\mathbf{O}$ be an $m$-ary operation symbol. Suppose $a_0, \ldots, a_{m-1} \in A$ and set $\mathbf{O}^{\mathfrak{A}}(a_0, \ldots, a_{m-1}) = b$. Then the sentence

$$\mathbf{O}(\mathbf{c}_{a_0}, \ldots, \mathbf{c}_{a_{m-1}}) = \mathbf{c}_b$$

is in the $\mathcal{L}'$-diagram of $\mathfrak{A}$. Therefore

$$(\mathfrak{B}, l_a)_{a \in A} \models \mathbf{O}(\mathbf{c}_{a_0}, \ldots, \mathbf{c}_{a_{m-1}}) = \mathbf{c}_b.$$

Interpreting the constants $\mathbf{c}_{a_i}$ as $l_{a_i}$ and $\mathbf{c}_b$ as $l_b$, this yields

$$\mathbf{O}^{\mathfrak{B}}(l_{a_0}, \ldots, l_{a_{m-1}}) = l_b = l(\mathbf{O}^{\mathfrak{A}}(a_0, \ldots, a_{m-1})).$$

Thus $l$ preserves the operation $\mathbf{O}$. Since $\mathbf{O}$ was arbitrary, $l$ is an embedding of $\mathfrak{A}$ into $\mathfrak{B}$.
