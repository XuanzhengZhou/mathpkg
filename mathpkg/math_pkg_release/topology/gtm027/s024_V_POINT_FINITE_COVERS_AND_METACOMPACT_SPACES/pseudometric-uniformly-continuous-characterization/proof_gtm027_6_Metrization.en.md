---
role: proof
locale: en
of_concept: pseudometric-uniformly-continuous-characterization
source_book: gtm027
source_chapter: "6"
source_section: "Metrization"
---

# Proof of Uniform Continuity Characterization of Pseudo-Metrics on Uniform Spaces (Theorem 6.11)

**Theorem 6.11.** Let $(X, \mathcal{U})$ be a uniform space and let $d$ be a pseudo-metric for $X$. Then $d$ is uniformly continuous on $X \times X$ (relative to the product uniformity) if and only if $V_{d,r} = \{(x,y) : d(x,y) < r\} \in \mathcal{U}$ for each positive $r$.

**Proof.** Recall that for the product uniformity on $X \times X$, the family of sets of the form $\{(x,u,y,v) : (x,u) \in U \text{ and } (y,v) \in U\}$ for $U \in \mathcal{U}$ is a base.

($\Rightarrow$) If $d$ is uniformly continuous on $X \times X$, then for each positive $r$ there is $U \in \mathcal{U}$ such that, if $(x,u) \in U$ and $(y,v) \in U$, then $|d(x,y) - d(u,v)| < r$. In particular, letting $(u,v) = (y,y)$, it follows that if $(x,y) \in U$, then $|d(x,y) - d(y,y)| = d(x,y) < r$. Hence $U \subset V_{d,r}$, and consequently $V_{d,r} \in \mathcal{U}$.

($\Leftarrow$) Conversely, suppose $V_{d,r} \in \mathcal{U}$ for each positive $r$. Let $r > 0$ be given and set $U = V_{d,r/2} \in \mathcal{U}$. If $(x,u) \in U$ and $(y,v) \in U$, then

$$d(x,y) \leq d(x,u) + d(u,v) + d(y,v) < r/2 + d(u,v) + r/2 = d(u,v) + r$$

and similarly $d(u,v) \leq d(x,u) + d(x,y) + d(y,v) < r + d(x,y)$. Hence $|d(x,y) - d(u,v)| < r$.

Thus $d$ is uniformly continuous on $X \times X$.
