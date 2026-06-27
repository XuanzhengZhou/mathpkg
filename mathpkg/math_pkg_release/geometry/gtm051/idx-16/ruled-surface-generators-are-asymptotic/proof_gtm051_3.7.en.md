---
role: proof
locale: en
of_concept: ruled-surface-generators-are-asymptotic
source_book: gtm051
source_chapter: "3"
source_section: "3.7"
---

**Proof.**

(i) In $(s, t)$-parameters, $f_{ss} = 0$ (since $f(s, t) = s X(t) + c(t)$ is linear in $s$). Therefore

$$h_{11} = II(f_s, f_s) = -n_s \cdot f_s = n \cdot f_{ss} = 0,$$

and so the Gauss curvature is

$$K = -\frac{h_{12}^2}{\det(g_{ij})} \leq 0.$$

Since $h_{11} = 0$, the generators ($t = \text{constant}$ curves, tangent to $f_s$) are asymptotic curves.

(ii) In $(s, t)$-parameters, we have shown in (i) that $n_s \cdot f_s = 0$. Therefore if $f(s, t)$ is a ruled surface, we have the chain of equivalences:

$$n_s = 0 \;\Leftrightarrow\; n_s \cdot f_t = n_s \cdot f_s = 0 \;\Leftrightarrow\; n_s \cdot f_t = 0 \;\Leftrightarrow\; n \cdot f_{st} = 0 \;\Leftrightarrow\; h_{12} = 0 \;\Leftrightarrow\; K = -\frac{h_{12}^2}{\det(g_{ij})} = 0.$$

The condition $n_s = 0$ is precisely the definition of a developable surface. The condition $n \cdot f_{st} = 0$ means $f_{st}$ is orthogonal to $n$, hence $f_{st}$ is a linear combination of $f_s$ and $f_t$ (since $f_s, f_t$ span the tangent space). $\square$
