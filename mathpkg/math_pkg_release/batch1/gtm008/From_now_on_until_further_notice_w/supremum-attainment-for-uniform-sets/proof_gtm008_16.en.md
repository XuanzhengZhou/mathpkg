---
role: proof
locale: en
of_concept: supremum-attainment-for-uniform-sets
source_book: gtm008
source_chapter: "16"
source_section: "The Maximum Principle"
---

If we do not require $x \in \mathcal{D}(u)$, the theorem follows from the Maximum Principle. We use the same argument to obtain $x \in \mathcal{D}(u)$.

Let $\langle x_\xi \mid \xi < \alpha \rangle$ be an enumeration of $\mathcal{D}(u)$. Put
$$b_\xi = u(x_\xi) \cdot \prod_{\eta < \xi} (\neg u(x_\eta))$$
for $\xi < \alpha$. Then the $b_\xi$ are pairwise disjoint and
$$\sum_{\xi < \alpha} b_\xi = \sum_{x \in \mathcal{D}(u)} u(x) = \sup(u).$$

Adding $b_\alpha = \neg \sup(u)$, the family $\langle b_\xi \mid \xi \leq \alpha \rangle$ is a partition of unity. Since $\mathcal{D}(u)$ is complete, there exists $x \in \mathcal{D}(u)$ such that $b_\xi \leq \llbracket x = x_\xi \rrbracket$ for all $\xi < \alpha$ (by the partition-of-unity property). Hence

\begin{align*}
u(x) = \llbracket x \in u \rrbracket &= \sum_{\xi < \alpha} u(x_\xi) \cdot \llbracket x = x_\xi \rrbracket \\
&\geq \sum_{\xi < \alpha} b_\xi = \sup(u) \geq u(x)
\end{align*}
by definition of the $b_\xi$ and $\sup(u)$. Therefore $u(x) = \sup(u)$.
