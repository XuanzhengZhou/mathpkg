---
role: proof
locale: en
of_concept: partitions-and-surjections-c24-c24
source_book: gtm054
source_chapter: "1"
source_section: "IA"
---

Let $\varphi: \text{sur}(M^U) \to \mathbb{P}_m(U)$ by defining $\varphi(f)$ to be the partition of $f$. By Proposition B8, $\varphi(f)$ is a $|f[U]|-$partition. Since $f$ is a surjection, $\varphi(f)$ is an $m$-partition. Since $\varphi$ is clearly a surjection, we also have from B8 that $\{\varphi^{-1}[\mathcal{Q}]: \mathcal{Q} \in \mathbb{P}_m(U)\}$ is a partition of $\text{sur}(M^U)$. Thus

$$|\text{sur}(M^U)| = \sum_{\mathcal{Q} \in \mathbb{P}_m(U)} |\varphi^{-1}[\mathcal{Q}]|.$$

It remains only to show that $|\varphi^{-1}[\mathcal{Q}]| = m!$ for all $\mathcal{Q} \in \mathbb{P}_m(U)$.

Fix $\mathcal{Q} \in \mathbb{P}_m(U)$ and $g \in \varphi^{-1}[\mathcal{Q}
