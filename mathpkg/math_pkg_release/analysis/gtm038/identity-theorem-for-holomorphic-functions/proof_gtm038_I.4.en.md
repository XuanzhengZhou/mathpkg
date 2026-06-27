---
role: proof
locale: en
of_concept: identity-theorem-for-holomorphic-functions
source_book: gtm038
source_chapter: "I"
source_section: "3. The Cauchy Integral"
---
**Proof.** Let $B_0$ be the interior of the set $\{\mathfrak{z} \in G : f_1(\mathfrak{z}) = f_2(\mathfrak{z})\}$ and $W_0 := G - B_0$. Because $B \subset B_0$, $B_0 \neq \emptyset$. Since $G$ is connected it suffices to show that $W_0$ is open, for then $B_0 = G$ follows. Let us assume $W_0$ contains a point $\mathfrak{z}_0$ which is not an interior point. Then for every polycylinder $P$ about $\mathfrak{z}_0$ with $\bar{P} \subset G$, $P \cap B_0 \neq \emptyset$. Let $r \in \mathbb{R}$ and $P := \{\mathfrak{z} : |z_j - z_j^0| < r\} = \{\mathfrak{z} : \operatorname{dist}'(\mathfrak{z}, \mathfrak{z}_0) < r\}$ be such a polycylinder. Let $P' := \{\mathfrak{z} : \operatorname{dist}'(\mathfrak{z}, \mathfrak{z}_0) < r/2\}$. Then there is a point $\mathfrak{z}_1 \in P' \cap B_0$. The power series expansions of $f_1$ and $f_2$ about $\mathfrak{z}_1$ agree on a neighborhood of $\mathfrak{z}_1$, hence they agree on the whole polycylinder $P$ about $\mathfrak{z}_0$ (since $\mathfrak{z}_0$ lies within the domain of convergence from $\mathfrak{z}_1$). Thus $\mathfrak{z}_0 \in B_0$, contradiction. Therefore $W_0$ is open, and $B_0 = G$. $\square$
