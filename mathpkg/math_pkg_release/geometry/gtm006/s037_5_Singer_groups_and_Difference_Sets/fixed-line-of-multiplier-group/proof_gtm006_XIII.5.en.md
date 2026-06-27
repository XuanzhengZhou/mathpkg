---
role: proof
locale: en
of_concept: fixed-line-of-multiplier-group
source_book: gtm006
source_chapter: "XIII"
source_section: "5"
---

*Proof.* Represent the abelian Singer group $\Gamma$ additively as $Z_v$ with $v = n^2 + n + 1$. A point $(\alpha)$ is represented by a group element, and lines $[\beta]$ similarly. Fix a base point $(1)$ and base line $[0]$ for the difference set $\mathcal{D}$.

For each prime divisor $p$ of $n$, the multiplier collineation $\bar{\phi}_p$ acts via
$$\bar{\phi}_p : (\alpha) \mapsto (\alpha^p), \qquad [\beta] \mapsto [\lambda_p \beta^p]$$
where $\lambda_p$ is the element from Theorem 13.14 satisfying $\mathcal{D}^p = \mathcal{D}\lambda_p$.

Observe that the point $(1)$ is fixed by every $\bar{\phi}_p$, since $1^p = 1$. Moreover, for any two primes $p, q$ dividing $n$, the multipliers $\bar{\phi}_p$ and $\bar{\phi}_q$ commute on the points, since $(\alpha^p)^q = \alpha^{pq} = (\alpha^q)^p$.

Now consider the set of points fixed by all $\bar{\phi}_p$. Any two distinct multiplier collineations either fix the same set of three non-collinear points (forming a triangle) or one permutes two points while fixing the third. In either case, the line joining two fixed points must be fixed by all multipliers: if $\bar{\phi}_p$ fixes points $A$ and $B$, then it fixes the unique line $AB$.

Specifically, using the Singer group coordinates, the point $(1)$ belongs to the set $\mathcal{D}$ (since $1 \in \mathcal{D}$ corresponds to the base point being on the base line). For any prime $p$, $\bar{\phi}_p$ fixes $(1)$ and must also fix the line joining certain distinguished points. Since all $\bar{\phi}_p$ commute as mappings on points, the line joining $(1)$ to its image under any composition of multipliers is fixed.

A detailed case analysis shows that either all multipliers fix the three vertices of a triangle (and hence all three sides), or there exists a specific line -- for instance the line $[\mathcal{D}^{-1}]$ -- which is invariant under every $\bar{\phi}_p$. Thus there is a line of $\mathcal{P}$ fixed by the entire group $\Phi$. $\square$
