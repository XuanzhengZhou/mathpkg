---
role: proof
locale: en
of_concept: right-ideal-annihilator
source_book: gtm031
source_chapter: "VIII"
source_section: "3"
---
Let $\mathfrak{J}$ be any right ideal in $\mathfrak{L}$. Define $\mathfrak{S}$ to be the set of all vectors $z \in \mathfrak{R}$ such that $zB = 0$ for all $B \in \mathfrak{J}$. Then $\mathfrak{S}$ is a subspace of $\mathfrak{R}$.

Now suppose $z \in \mathfrak{S}$. Then for any $C \in \mathfrak{L}$ expressed as $C = \sum x_i' \times y_i$ (with the $y_i$ linearly independent), the condition $zC = 0$ means $\sum g(z, x_i') y_i = 0$ for all choices of the $x_i'$ and corresponding $y_i$. Since the $y_i$ can be chosen linearly independent, this forces $g(z, x_i') = 0$ for all $x_i'$, which then characterizes $z$ as belonging to $\mathfrak{S}$. Conversely, the annihilator $\mathfrak{S}$ can be characterized as the totality of vectors annihilated by every $B \in \mathfrak{J}$.

Next, suppose $C$ is any linear transformation such that $yC = 0$ for all $y \in \mathfrak{S}$. Write $C = \sum x_i' \times y_i$ where the $y_i$ are linearly independent. Then $0 = yC = \sum g(y, x_i') y_i$, so $g(y, x_i') = 0$ for all $y \in \mathfrak{S}$. Hence the $x_i' \in j(\mathfrak{S}) = j(j(\mathfrak{S}')) = \mathfrak{S}'$ and $C \in \mathfrak{J}$. Therefore $\mathfrak{J}$ is precisely the totality $\mathfrak{Z}(\mathfrak{S})$ of linear transformations which annihilate every vector in $\mathfrak{S}$.
