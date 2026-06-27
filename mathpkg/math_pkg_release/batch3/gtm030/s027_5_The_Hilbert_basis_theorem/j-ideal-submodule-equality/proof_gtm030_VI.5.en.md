---
role: proof
locale: en
of_concept: j-ideal-submodule-equality
source_book: gtm030
source_chapter: "VI"
source_section: "5. The Hilbert basis theorem"
---

Let $y = b_1 x_1 + b_2 x_2 + \cdots + b_r x_r \in \mathfrak{P}$. Since $\mathfrak{J}_1(\mathfrak{N}) = \mathfrak{J}_1(\mathfrak{P})$, we can find $b_1'$ such that
$$b_1' x_1 + b_2' x_2 + \cdots + b_r' x_r \in \mathfrak{N}$$
with $b_1 = b_1'$. Then $y - (b_1' x_1 + \cdots + b_r' x_r) = (b_2 - b_2') x_2 + \cdots + (b_r - b_r') x_r$ is an element of $\mathfrak{P}$ whose coefficient of $x_1$ is $0$. Since $\mathfrak{J}_2(\mathfrak{N}) = \mathfrak{J}_2(\mathfrak{P})$, there exists an element $b_2'' x_2 + \cdots + b_r'' x_r \in \mathfrak{N}$ with $b_2'' = b_2 - b_2'$. Subtracting this from the previous expression yields an element of $\mathfrak{P}$ whose first two coefficients vanish. Continuing this process, after $r$ steps we obtain $y \in \mathfrak{N}$. Hence $\mathfrak{P} \subseteq \mathfrak{N}$, so $\mathfrak{N} = \mathfrak{P}$.
