---
role: proof
locale: en
of_concept: rational-open-discs-countable-base
source_book: gtm027
source_chapter: "1"
source_section: "O"
---

# Proof that Open Discs with Rational Centers and Radii Form a Countable Base

**Proposition.** The usual topology of the Euclidean plane has a base consisting of all open discs
$$\{(x,y) : (x-a)^2 + (y-b)^2 < r^2\}$$
where $a, b,$ and $r$ are rational numbers.

*Proof.* Let $\mathcal{B}$ be the collection of all such open discs with rational parameters $(a,b,r) \in \mathbb{Q}^3$, $r > 0$.

**Countability:** $\mathbb{Q}^3$ is countable (finite product of countable sets), so $\mathcal{B}$ is countable.

**Base property:** Let $U \subseteq \mathbb{R}^2$ be open in the usual topology and let $p = (x_0, y_0) \in U$. Since $U$ is open, there exists $\varepsilon > 0$ such that the open disc $B_\varepsilon(p) = \{(x,y) : (x-x_0)^2 + (y-y_0)^2 < \varepsilon^2\} \subseteq U$.

Choose a rational number $r$ with $0 < r < \varepsilon/3$. Choose rational numbers $a, b$ such that $|a - x_0| < r$ and $|b - y_0| < r$ (possible since $\mathbb{Q}$ is dense in $\mathbb{R}$).

Then for any $(x,y)$ with $(x-a)^2 + (y-b)^2 < r^2$, by the triangle inequality:
$$\sqrt{(x-x_0)^2 + (y-y_0)^2} \leq \sqrt{(x-a)^2 + (y-b)^2} + \sqrt{(a-x_0)^2 + (b-y_0)^2} < r + \sqrt{2}r < 3r < \varepsilon.$$

Thus $(x,y) \in B_\varepsilon(p) \subseteq U$, so the rational disc $B_r(a,b)$ satisfies:
$$p \in B_r(a,b) \subseteq U.$$

This shows $\mathcal{B}$ is a base for the usual topology of the plane. $\square$
