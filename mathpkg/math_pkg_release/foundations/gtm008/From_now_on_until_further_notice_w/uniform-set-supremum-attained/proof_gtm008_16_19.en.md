---
role: proof
locale: en
of_concept: uniform-set-supremum-attained
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $\langle x_\xi \mid \xi < \alpha \rangle$ be an enumeration of $\mathcal{D}(u)$ and put $b_\xi = u(x_\xi) \cdot \prod_{\eta < \xi} (-u(x_\eta))$ for $\xi < \alpha$. Then the $b_\xi$'s are disjoint and $\sum_{\xi < \alpha} b_\xi = \sum_{x \in \mathcal{D}(u)} u(x) = \sup(u)$. Adding $b_\alpha = -\sup(u)$, $\langle b_\xi \mid \xi \leq \alpha \rangle$ is a partition of unity. Since $\mathcal{D}(u)$ is complete, $(\forall \xi < \alpha)[b_\xi \leq \llbracket x = x_\xi \rrbracket]$ for some $x \in \mathcal{D}(u)$. Hence

$$u(x) = \llbracket x \in u \rrbracket = \sum_{\xi < \alpha} u(x_\xi) \cdot \llbracket x = x_\xi \rrbracket \geq \sum_{\xi < \alpha} b_\xi = \sup(u) \geq u(x).$$

Therefore $u(x) = \sup(u)$.
