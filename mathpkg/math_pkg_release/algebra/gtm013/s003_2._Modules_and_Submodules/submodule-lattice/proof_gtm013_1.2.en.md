---
role: proof
locale: en
of_concept: submodule-lattice
source_book: gtm013
source_chapter: "1"
source_section: "2"
---

Let $M$ be a left $R$-module. The partial order $\leq$ on $\mathcal{S}(M)$ coincides with set inclusion, so $L \leq N$ iff $L \subseteq N$. The submodules $0$ and $M$ are the unique smallest and largest elements of $\mathcal{S}(M)$.

If $\mathcal{A}$ is any non-empty subset of $\mathcal{S}(M)$, then by (2.3) the intersection $\bigcap \mathcal{A}$ is a submodule of $M$. Since $\bigcap \mathcal{A}$ must be the greatest lower bound of $\mathcal{A}$, we infer that $\mathcal{S}(M)$ is a complete lattice.

The join of $\mathcal{A}$ is not generally the union (the union of two submodules is rarely a submodule). Instead, the join is the sum $\Sigma \mathcal{A}$. By Proposition 2.2, the sum $\Sigma \mathcal{A}$ of a set $\mathcal{A}$ of submodules is again a submodule. If $N$ is any submodule of $M$ containing all submodules in $\mathcal{A}$, then by (2.3) $N$ must contain the sum $\Sigma \mathcal{A}$. Therefore $\Sigma \mathcal{A}$ is the least upper bound of $\mathcal{A}$ in $\mathcal{S}(M)$.

For the modular law: let $H$, $K$, and $L$ be submodules of $M$. By set-theoretic inclusion one always has $H \cap (K + L) \geq (H \cap K) + (H \cap L)$. In general this inequality may be strict, so $\mathcal{S}(M)$ need not be distributive. However, if $H \geq K$ and $h \in H$, $k \in K$, $l \in L$ with $h = k + l$, then since $k \in K \subseteq H$, we have $l = h - k \in H$ and thus $l \in H \cap L$. Therefore $h = k + l \in K + (H \cap L)$, establishing the reverse inclusion and thus the modular identity $H \cap (K + L) = K + (H \cap L)$ when $K \leq H$.
