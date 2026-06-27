---
role: proof
locale: en
of_concept: uniform-set-factorization
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $b = \sup(u)$. By Theorem 16.19, there exists $x_0 \in \mathcal{D}(u)$ with $u(x_0) = b$. Define $v \in V^{(\mathbf{B})}$ by $\mathcal{D}(v) = \{y \mid y \in \mathcal{D}(u) \land u(y) = b\}$ and $v(y) = 1$ for all $y \in \mathcal{D}(v)$. Then $v$ is definite by definition.

We need to show $\llbracket u = b \cdot v \rrbracket = 1$. For any $x \in \mathcal{D}(u)$:

1. Since $\{u(x), \neg u(x)\}$ is a partition of unity and $u$ is uniform (with complete domain), there exists $z \in \mathcal{D}(u)$ such that $z = u(x) \cdot x + (\neg u(x)) \cdot x_0$. By Theorem 16.14,
   $$u(z) = u(x) \cdot u(x) + (\neg u(x)) \cdot u(x_0) = u(x) + (\neg u(x)) \cdot b \geq b.$$
   Therefore $u(z) = b$ (since $b = \sup(u)$), so $z \in \mathcal{D}(v)$.

2. Then $u(x) \Rightarrow b \cdot \sum_{t \in \mathcal{D}(v)} \llbracket x = t \rrbracket \geq u(x) \Rightarrow b \cdot \llbracket x = z \rrbracket \geq b \cdot u(x) \Rightarrow b \cdot u(x)$, since $u(x) \leq \llbracket z = x \rrbracket$.

This shows $\llbracket u \subseteq b \cdot v \rrbracket = 1$ and $\llbracket b \cdot v \subseteq u \rrbracket = 1$, thus $\llbracket u = b \cdot v \rrbracket = 1$.
