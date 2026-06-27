---
role: proof
locale: en
of_concept: bochner-integral-existence
source_book: gtm055
source_chapter: "17"
source_section: "18"
---

First define $L_0$ on the linear manifold of integrable simple $\mathcal{E}$-valued mappings by

$$L_0\left(\sum_{i=1}^{N} \chi_{E_i} v_i\right) = \sum_{i=1}^{N} \mu(E_i) v_i,$$

where the sets $E_i$ are pairwise disjoint measurable sets of finite measure. To show $L_0$ is well-defined, note that if the sets $E_i$ are chosen to be pairwise disjoint, then $N_\Sigma(x) = \sum_{i=1}^{N} \|v_i\| \chi_{E_i}(x)$, whence

$$\|L_0(\Sigma)\| \leq \sum_{i=1}^{N} \|v_i\| \mu(E_i) = \|N_\Sigma\|_1 = \|\Sigma\|_1.$$

Thus $L_0$ is bounded (by one) and therefore possesses a unique bounded linear extension $L$ to $\mathcal{L}_1(X; \mathcal{E})$ (that is also bounded by one).
