---
role: proof
locale: en
of_concept: common-free-extension-of-multiple-configurations
source_book: gtm006
source_chapter: "11"
source_section: "3. Generation"
---

Apply Lemma 11.7 iteratively. For $n = 2$, Lemma 11.7 provides a configuration $\mathcal{C}$ which is a common free extension of $\mathcal{A}_1$ and $\mathcal{A}_2$.

For general $n$, we proceed by induction. By the induction hypothesis, there exists a configuration $\mathcal{C}_{n-1}$ that is a common free extension of $\mathcal{A}_1, \ldots, \mathcal{A}_{n-1}$. Since $\mathcal{A}_n$ is contained in a free extension of each $\mathcal{A}_i$ (by hypothesis), and all share the free closure $\mathcal{P} = \mathcal{F}(\mathcal{A}_i)$, we can apply Lemma 11.7 to $\mathcal{C}_{n-1}$ and $\mathcal{A}_n$ to obtain a configuration $\mathcal{B}$ that is a common free extension of both, hence of all $\mathcal{A}_i$.

For uniqueness, suppose $\mathcal{B}_1$ and $\mathcal{B}_2$ are both free extensions of all $\mathcal{A}_i$ and are minimal with this property. Since $\mathcal{B}_1$ is a free extension of all $\mathcal{A}_i$, it contains some free extension of $\mathcal{B}_2$ (by minimality of $\mathcal{B}_2$), and symmetrically, $\mathcal{B}_2$ contains a free extension of $\mathcal{B}_1$. Since both are sub-configurations of $\mathcal{P}$, they must be equal by the structure of free extensions within a common free closure.
