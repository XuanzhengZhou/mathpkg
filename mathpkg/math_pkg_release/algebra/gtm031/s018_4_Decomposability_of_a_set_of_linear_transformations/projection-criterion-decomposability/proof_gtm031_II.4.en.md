---
role: proof
locale: en
of_concept: projection-criterion-decomposability
source_book: gtm031
source_chapter: "II"
source_section: "4"
---

($\Rightarrow$) Suppose $\Omega$ is decomposable, so $\mathfrak{R} = \mathfrak{R}_1 \oplus \mathfrak{R}_2 \oplus \cdots \oplus \mathfrak{R}_s$ with each $\mathfrak{R}_i \neq 0$, $s > 1$, and each $\mathfrak{R}_i$ invariant under $\Omega$. Let $E_i$, $i = 1, 2, \cdots, s$, be the projections determined by this decomposition: if

$$x = x_1 + x_2 + \cdots + x_s$$

with $x_i \in \mathfrak{R}_i$, then $E_i$ is the mapping $x \mapsto x_i$. These projections satisfy

$$E_i^2 = E_i, \quad E_iE_j = 0 \text{ for } i \neq j, \quad E_1 + E_2 + \cdots + E_s = 1.$$

Moreover, for any $A \in \Omega$ and $x_i \in \mathfrak{R}_i$, we have $x_i = xE_i$ and $x_iA = xE_iA = (xA)E_i \in \mathfrak{R}_i$, so $E_i$ commutes with every $A \in \Omega$. Since $s > 1$, each $E_i \neq 1$, and since each $\mathfrak{R}_i \neq 0$, each $E_i \neq 0$. Thus there exist projections $\neq 0, \neq 1$ commuting with $\Omega$.

($\Leftarrow$) Conversely, suppose $E_1$ is a projection $\neq 0, \neq 1$ which commutes with every $A \in \Omega$. Set $E_2 = 1 - E_1$. Then $E_2$ is also a projection $\neq 0, \neq 1$, and $E_2$ commutes with every $A \in \Omega$. Moreover, $E_1$ and $E_2$ are orthogonal: $E_1E_2 = E_1(1 - E_1) = E_1 - E_1^2 = E_1 - E_1 = 0$, and similarly $E_2E_1 = 0$. Hence $1 = E_1 + E_2$ is a decomposition of the identity into orthogonal projections commuting with $\Omega$. Then $\mathfrak{R} = \mathfrak{R}E_1 \oplus \mathfrak{R}E_2$, and for any $A \in \Omega$ and $x_i \in \mathfrak{R}E_i$, we have $x_i = xE_i$ so $x_iA = xE_iA = (xA)E_i \in \mathfrak{R}E_i$. Thus $\mathfrak{R}E_1$ and $\mathfrak{R}E_2$ are proper invariant subspaces, giving a proper decomposition. $\square$
