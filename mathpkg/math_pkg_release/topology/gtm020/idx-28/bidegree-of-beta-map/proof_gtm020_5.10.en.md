---
role: proof
locale: en
of_concept: bidegree-of-beta-map
source_book: gtm020
source_chapter: "5"
source_section: "10"
---

Since $\beta(x)y = -\alpha(x)y$, the map $\beta$ is the composition of $\alpha$ with the antipodal map $y \mapsto -y$. The antipodal map on $S^{n-1}$ has degree $(-1)^n$. For the bidegree computation, the first component (degree of $x \mapsto \beta(x)y_0$ for fixed $y_0$) is unchanged from the alpha case because the factor $-1$ acts on the output but does not depend on $x$: the degree of $x \mapsto -\alpha(x)y_0$ equals the degree of $x \mapsto \alpha(x)y_0$, which is $+1 + (-1)^n$.

The second component changes: for fixed $x$, the map $y \mapsto \beta(x)y = -\alpha(x)y$ is the composition of a hyperplane reflection (degree $-1$) with the antipodal map (degree $(-1)^n$). Hence its degree is $(-1) \cdot (-1)^n = -(-1)^n$. Thus the bidegree is $(+1 + (-1)^n, -(-1)^n)$.
