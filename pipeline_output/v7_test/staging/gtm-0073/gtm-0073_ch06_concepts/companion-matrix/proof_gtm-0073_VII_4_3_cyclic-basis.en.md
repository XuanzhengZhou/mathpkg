---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.4"
proof_technique: cyclic-basis
locale: en
content_hash: ""
written_against: ""
---
($\Rightarrow$) If $E$ is $\phi$-cyclic, then $E = K[x]v$ for some $v \in E$. The set $\{v, \phi(v), \ldots, \phi^{r-1}(v)\}$ is a $K$-basis: it spans $E$ since every element is $f(\phi)(v)$ and $q(\phi) = 0$ allows reduction to degree $< r$; it is linearly independent because a dependence $k_0v + \cdots + k_{r-1}\phi^{r-1}(v) = 0$ gives a polynomial of degree $< r$ annihilating $v$, contradicting minimality of $q$. The matrix of $\phi$ in this basis is the companion matrix since $\phi(\phi^i(v)) = \phi^{i+1}(v)$ for $i < r-1$ and $\phi(\phi^{r-1}(v)) = \phi^r(v) = -\sum_{j=0}^{r-1} a_j \phi^j(v)$.

($\Leftarrow$) If $\phi$ has companion matrix $A$ in basis $V = \{v_1, \ldots, v_r\}$, let $v = v_1$. Then $v_i = \phi^{i-1}(v)$ and the last row of $A$ shows that $\phi^r(v)$ is expressed in terms of $\{v, \ldots, \phi^{r-1}(v)\}$, so $E = K[x]v$ and $q$ is the minimal polynomial.
