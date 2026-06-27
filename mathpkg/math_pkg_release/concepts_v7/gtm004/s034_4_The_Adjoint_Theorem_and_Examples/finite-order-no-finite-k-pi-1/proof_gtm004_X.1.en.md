---
role: proof
locale: en
of_concept: finite-order-no-finite-k-pi-1
source_book: gtm004
source_chapter: "X"
source_section: "1. Homological Algebra and Algebraic Topology"
---

# Proof of Finite-Order Elements Imply No Finite-Dimensional $K(\pi,1)$

**Theorem 1.1.** If $\pi$ has an element of finite order, then there can be no finite-dimensional model for $K(\pi, 1)$.

**Proof.** First consider $K(C_m, 1)$, where $C_m$ is a cyclic group of order $m \geq 2$. Since $C(\widetilde{K}(C_m, 1))$ is a free $C_m$-resolution of $\mathbb{Z}$, and since $C_m$ has nonzero integral homology groups in all odd dimensions (see Section 7 of Chapter VI),

$$H_{2k+1}(C_m, \mathbb{Z}) \cong \mathbb{Z}/m\mathbb{Z} \neq 0, \quad k = 0, 1, 2, \dots,$$

it follows that $\widetilde{K}(C_m, 1)$, and hence $K(C_m, 1)$, must have cells in arbitrarily high dimensions. Indeed, if $K(C_m, 1)$ were finite-dimensional, say of dimension $N$, then the chain complex $C(\widetilde{K}(C_m, 1))$ would be zero above dimension $N$, forcing $H_n(C_m, \mathbb{Z}) = 0$ for all $n > N$, contradicting the nonvanishing in all odd dimensions. Therefore $K(C_m, 1)$ must be infinite-dimensional.

Now let $\pi$ have an element of order $m$. This element generates a cyclic subgroup $C_m \leq \pi$. The universal cover $\widetilde{K}(\pi, 1)$ is a free $\pi$-space; by restriction, it is also a free $C_m$-space. Hence $C(\widetilde{K}(\pi, 1))$ is a free $C_m$-resolution of $\mathbb{Z}$, since a free $\pi$-module restricts to a free $C_m$-module (Lemma 1.3 of Chapter VI).

If $K(\pi, 1)$ admitted a finite-dimensional model, say of dimension $N$, then $C(\widetilde{K}(\pi, 1))$ would be a free $C_m$-resolution of $\mathbb{Z}$ concentrated in dimensions $\leq N$, implying $H_n(C_m, \mathbb{Z}) = 0$ for all $n > N$. But this contradicts the fact that $C_m$ has nonvanishing homology in arbitrarily high odd dimensions. Hence no finite-dimensional $K(\pi, 1)$ can exist. $\square$
