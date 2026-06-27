---
role: proof
locale: en
of_concept: residue-ring-not-necessarily-integrally-closed
source_book: gtm028
source_chapter: "V"
source_section: "3. Integrally closed rings"
---

Consider the polynomial ring $R = k[X_1, X_2]$ over a field $k$, which is a unique factorization domain and therefore integrally closed (by Example 1). Let $\mathfrak{p} = (X_1^2 - X_2^3)$ be a principal prime ideal in $R$, and set

$$A = R/\mathfrak{p} \cong k[x_1, x_2], \quad \text{where } x_1^2 = x_2^3.$$

The element $x_1/x_2$ belongs to the field of quotients of $A$. We have

$$\left(\frac{x_1}{x_2}\right)^2 = \frac{x_1^2}{x_2^2} = \frac{x_2^3}{x_2^2} = x_2 \in A,$$

so $x_1/x_2$ satisfies the monic polynomial equation $T^2 - x_2 = 0$ with coefficients in $A$. Hence $x_1/x_2$ is integral over $A$.

However, $x_1/x_2 \notin A$, because in $A \cong k[t^2, t^3]$ (under the map $x_1 \mapsto t^3$, $x_2 \mapsto t^2$), the element $x_1/x_2$ corresponds to $t^3/t^2 = t$, which is not in $k[t^2, t^3]$. Therefore $A$ is not integrally closed, despite being a residue class ring of the integrally closed domain $R$.
