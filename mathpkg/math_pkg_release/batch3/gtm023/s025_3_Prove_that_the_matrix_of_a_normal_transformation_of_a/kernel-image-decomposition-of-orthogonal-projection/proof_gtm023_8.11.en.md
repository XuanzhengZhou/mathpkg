---
role: proof
locale: en
of_concept: kernel-image-decomposition-of-orthogonal-projection
source_book: gtm023
source_chapter: "VIII"
source_section: "8.11"
---

Since $\pi^2 = \pi$, every $x \in E$ can be written as $x = \pi x + (x - \pi x)$. Clearly $\pi x \in \operatorname{Im} \pi$, and $\pi(x - \pi x) = \pi x - \pi^2 x = \pi x - \pi x = 0$, so $x - \pi x \in \ker \pi$. Thus $E = \ker \pi + \operatorname{Im} \pi$.

If $y \in \ker \pi \cap \operatorname{Im} \pi$, then $y = \pi z$ for some $z$ and $\pi y = 0$. But $\pi y = \pi(\pi z) = \pi^2 z = \pi z = y$, so $y = 0$. Hence $\ker \pi \cap \operatorname{Im} \pi = \{0\}$, giving $E = \ker \pi \oplus \operatorname{Im} \pi$.

Moreover, since $\pi$ is selfadjoint, for $u \in \ker \pi$ and $v \in \operatorname{Im} \pi$ (with $v = \pi w$): $(u, v) = (u, \pi w) = (\pi u, w) = (0, w) = 0$, so the direct sum is orthogonal.

Finally, for any $y \in \operatorname{Im} \pi$, $y = \pi z$, so $\pi y = \pi^2 z = \pi z = y$, i.e., the restriction of $\pi$ to $\operatorname{Im} \pi$ is the identity.
