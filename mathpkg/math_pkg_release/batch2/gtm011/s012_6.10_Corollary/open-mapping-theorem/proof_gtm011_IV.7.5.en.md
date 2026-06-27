---
role: proof
locale: en
of_concept: open-mapping-theorem
source_book: gtm011
source_chapter: "IV"
source_section: "7.5"
---

To show $f(U)$ is open, it suffices to show that for each $a \in U$, there is a $\delta > 0$ such that $B(\alpha; \delta) \subset f(U)$ where $\alpha = f(a)$.

Since the zeros of an analytic function are isolated, we can choose $\epsilon > 0$ such that $\epsilon < \frac{1}{2}R$ (where $R$ is the radius of a disk about $a$ contained in $U$), $f(z) = \alpha$ has no solutions with $0 < |z-a| < 2\epsilon$, and $f'(z) \neq 0$ if $0 < |z-a| < 2\epsilon$. Let $\gamma(t) = a + \epsilon \exp(2\pi i t)$ for $0 \leq t \leq 1$, and put $\sigma = f \circ \gamma$.

Now $\alpha \notin \{\sigma\}$, so there is a $\delta > 0$ such that $B(\alpha; \delta) \cap \{\sigma\} = \emptyset$. Thus $B(\alpha; \delta)$ is contained in some component of $\mathbb{C} - \{\sigma\}$. For any $\zeta$ with $|\alpha - \zeta| < \delta$,

$$n(\sigma; \alpha) = n(\sigma; \zeta) = \sum_{k=1}^{p} n(\gamma; z_k(\zeta))$$

where $z_k(\zeta)$ are the solutions of $f(z) = \zeta$ inside $B(a; \epsilon)$. Since $n(\gamma; z)$ is either $0$ or $1$ for points inside the circle, the sum counts the number of solutions. Because $f(z) - \alpha$ has a zero of some multiplicity $m \geq 1$ at $a$ (since $f$ is non-constant), there are exactly $m$ solutions to $f(z) = \zeta$ inside $B(a; \epsilon)$ for $\zeta$ sufficiently close to $\alpha$. Hence $B(\alpha; \delta) \subset f(B(a; \epsilon)) \subset f(U)$, proving $f(U)$ is open.
