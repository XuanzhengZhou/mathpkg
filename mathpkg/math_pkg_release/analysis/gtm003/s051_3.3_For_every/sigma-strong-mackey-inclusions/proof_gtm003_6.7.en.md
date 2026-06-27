---
role: proof
locale: en
of_concept: sigma-strong-mackey-inclusions
source_book: gtm003
source_chapter: "6"
source_section: "6.7"
---

For each $\varphi \in V_+$, from Schwarz' inequality we obtain ($e$ the unit of $W$)

$$|\varphi(x)| = |\varphi(xe)| \leq \sqrt{\varphi(x^*x)} \sqrt{\varphi(e)} = \|x\|_\varphi \sqrt{\|\varphi\|}.$$

Therefore, $\sigma(W, V)$ is coarser than $s(W, V)$.

By (IV, 3.2) Corollary 1, the Mackey topology $\tau(W, V)$ is the topology of uniform convergence on all $\sigma(V, W)$-compact subsets of $V$. Now if $\mathfrak{J}$ is any filter on $U$ that $\tau(W, V)$-converges to $0$, then for any fixed $\varphi \in V_+$ $\lim_{\mathfrak{J}} = 0$ uniformly on $U\varphi = \{y\varphi : y \in U\}$, because $U\varphi$ is $\sigma(V, W)$-compact by (6.6). It follows that $\lim_{\mathfrak{J}} \|x\|_\varphi^2 = \lim_{\mathfrak{J}} (x^*\varphi)(x) = 0$. Therefore, every $s(W, V)$-continuous linear form on $W$ is $\tau(W, V)$-continuous on $U$, and thus on $W$ (cf. 6.1); we conclude that $s(W, V)$ is consistent with $\langle W, V \rangle$ and so, $s(W, V) \subset \tau(W, V)$.

The (joint) continuity of $(x, y) \mapsto xy$ for $s(W, V)$ follows from inequalities bounding $\|xy - uv\|_\varphi$ in terms of $\|x - u\|_\varphi$ and $\|y - v\|_\varphi$ when $x, u$ range over a bounded set.
