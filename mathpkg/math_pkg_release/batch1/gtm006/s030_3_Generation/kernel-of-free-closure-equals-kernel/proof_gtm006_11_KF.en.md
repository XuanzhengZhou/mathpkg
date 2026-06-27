---
role: proof
locale: en
of_concept: kernel-of-free-closure-equals-kernel
source_book: gtm006
source_chapter: "11"
source_section: "3. Generation"
---

The inclusion $\mathcal{K}(\mathcal{B}) \subseteq \mathcal{K}(\mathcal{F}(\mathcal{B}))$ follows trivially from $\mathcal{B} \subseteq \mathcal{F}(\mathcal{B})$.

For the reverse inclusion, suppose $X \in \mathcal{K}(\mathcal{F}(\mathcal{B}))$, so $X$ has at least three incidences in $\mathcal{F}(\mathcal{B})$. Since $\mathcal{F}(\mathcal{B})$ is constructed as the union of a sequence of free full one-step extensions $\mathcal{B} = \mathcal{B}_0 < \mathcal{B}_1 < \mathcal{B}_2 < \cdots$, each new element introduced at any stage $\mathcal{B}_{i+1} \setminus \mathcal{B}_i$ is incident with exactly two elements (the pair of like elements that it was created to connect). Therefore, no element outside $\mathcal{B}$ can ever acquire three or more incidences. Hence $X$ must belong to $\mathcal{B}$ and have at least three incidences already in $\mathcal{B}$, so $X \in \mathcal{K}(\mathcal{B})$. Thus $\mathcal{K}(\mathcal{F}(\mathcal{B})) = \mathcal{K}(\mathcal{B})$.
