---
role: proof
locale: en
of_concept: norm-and-trace-via-isomorphisms
source_book: gtm028
source_chapter: "I"
source_section: "10"
---
Let $K^\star$ be the least normal extension of $k$ containing $K$, and let $\{\varphi_i\}_{i=1}^{m_0}$ be the set of $k$-isomorphisms of $K$ into $K^\star$, where $m_0 = [K:k]_s$ is the separable degree.

Let $n = [k(x):k]$, $n_0 = [k(x):k]_s$, and $p^e = [k(x):k]_i$. Let $\{x_j\}_{j=1}^{n_0}$ be the distinct conjugates of $x$ in $K^\star$, with $x_1 = x$.

By Lemma 2 of §6, each of the $n_0$ $k$-isomorphisms of $k(x)$ into $K^\star$ has exactly $m_0/n_0$ extensions among the $\varphi_i$. Hence each conjugate $x_j$ occurs exactly $m_0/n_0$ times in the multiset $\{x^{\varphi_i} \mid i = 1, \dots, m_0\}$.

Now applying the tower formulas (8) and (9), we have:
$$N_{K/k}(x) = [N_{k(x)/k}(x)]^{[K:k(x)]}, \quad T_{K/k}(x) = [K:k(x)] \cdot T_{k(x)/k}(x).$$

From formulas (15) and (16) for the simple extension $k(x)/k$:
$$N_{k(x)/k}(x) = \left(\prod_{j=1}^{n_0} x_j\right)^{p^e}, \quad T_{k(x)/k}(x) = p^e \cdot \sum_{j=1}^{n_0} x_j.$$

Since $[K:k(x)] \cdot p^e = p^f$ where $p^f = [K:k]_i$, and $[K:k(x)] \cdot n_0 = m_0$, combining these yields:
$$N_{K/k}(x) = \left(\prod_{j=1}^{n_0} x_j\right)^{p^f \cdot m_0/n_0} = \left(\prod_{i=1}^{m_0} x^{\varphi_i}\right)^{p^f},$$
$$T_{K/k}(x) = p^f \cdot \frac{m_0}{n_0} \cdot \sum_{j=1}^{n_0} x_j = p^f \cdot \sum_{i=1}^{m_0} x^{\varphi_i}.$$
