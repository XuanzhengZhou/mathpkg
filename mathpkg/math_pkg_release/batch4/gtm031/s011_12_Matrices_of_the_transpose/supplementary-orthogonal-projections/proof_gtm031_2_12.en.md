---
role: proof
locale: en
of_concept: supplementary-orthogonal-projections
source_book: gtm031
source_chapter: "2"
source_section: "12"
---

For the forward direction: From the definition of $E_i$, if $x_i \in \mathfrak{R}_i$, the representation of $x = x_i$ is $x_i = x_i$, so $x_i E_i = x_i$ and $x_i E_j = 0$ for $j \neq i$. Since $\mathfrak{R}_i = \mathfrak{R}E_i$, we have $E_i E_i = E_i$ and $E_i E_j = 0$ for $i \neq j$. The sum condition $E_1 + \cdots + E_r = 1$ was already established.

For the converse: Let $E_1, \ldots, E_r$ satisfy the three conditions. Set $\mathfrak{R}_i = \mathfrak{R}E_i$. For any $x \in \mathfrak{R}$, $x = x \cdot 1 = x(\sum E_i) = xE_1 + \cdots + xE_r \in \mathfrak{R}_1 + \cdots + \mathfrak{R}_r$. Hence $\mathfrak{R} = \mathfrak{R}_1 + \cdots + \mathfrak{R}_r$. To show the sum is direct, suppose $z_i = z_1 + \cdots + z_{i-1} + z_{i+1} + \cdots + z_r$ with $z_j \in \mathfrak{R}_j$. Since $z_j = y_j E_j$, operating on the left with $E_i$ gives $z_i$ on the left-hand side and $0$ on the right-hand side. Hence $z_i = 0$, proving $\mathfrak{R}_i \cap (\mathfrak{R}_1 + \cdots + \mathfrak{R}_{i-1} + \mathfrak{R}_{i+1} + \cdots + \mathfrak{R}_r) = 0$. Thus $\mathfrak{R} = \mathfrak{R}_1 \oplus \cdots \oplus \mathfrak{R}_r$, and the projections determined by this decomposition are exactly the $E_i$.
