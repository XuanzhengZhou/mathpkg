---
role: proof
locale: en
of_concept: uniform-set-representation
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $u \in V^{(B)}$ be uniform with $b = \sup(u)$. By Theorem 16.19, there exists $x_0 \in \mathcal{D}(u)$ such that $u(x_0) = b$. For an arbitrary $x \in \mathcal{D}(u)$, since $\{u(x), \neg u(x)\}$ is a partition of unity and $u$ is uniform, there exists $z \in \mathcal{D}(u)$ such that $z = u(x)x + (\neg u(x))x_0$. By Theorem 16.14,

$$u(z) = u(x)u(x) + (\neg u(x))u(x_0) = u(x) + (\neg u(x))b \geq b.$$

Therefore $u(z) = b$ (since $b = \sup(u)$), so $z \in \mathcal{D}(v)$. One then verifies that $\llbracket u = b \cdot v \rrbracket = 1$ by checking the Boolean-valued equality condition.
