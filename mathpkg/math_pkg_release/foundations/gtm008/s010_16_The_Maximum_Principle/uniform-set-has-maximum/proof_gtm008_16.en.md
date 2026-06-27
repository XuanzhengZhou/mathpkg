---
role: proof
locale: en
of_concept: uniform-set-has-maximum
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

Let $\langle x_\xi \mid \xi < \alpha \rangle$ be an enumeration of $\mathcal{D}(u)$, i.e.,

$$\mathcal{D}(u) = \{x_\xi \mid \xi < \alpha\}$$

and put $b_\xi = u(x_\xi) \cdot \prod_{\eta < \xi} (-u(x_\eta))$ for $\xi < \alpha$. Then the $b_\xi$'s are pairwise disjoint and

$$\sum_{\xi < \alpha} b_\xi = \sum_{x \in \mathcal{D}(u)} u(x) = \sup(u).$$

Therefore, adding $b_\alpha = -\sup(u)$, $\langle b_\xi \mid \xi \leq \alpha \rangle$ is a partition of unity. Since $\mathcal{D}(u)$ is complete, $(\forall \xi < \alpha)[b_\xi \leq \llbracket x = x_\xi \rrbracket]$ for some $x \in \mathcal{D}(u)$. Hence

$$u(x) = \llbracket x \in u \rrbracket = \sum_{\xi < \alpha} u(x_\xi) \cdot \llbracket x = x_\xi \rrbracket$$
$$\geq \sum_{\xi < \alpha} b_\xi = \sup(u) \geq u(x)$$

by definition of $b_\xi$ and $\sup(u)$. Therefore

$$u(x) = \sup(u).$$
