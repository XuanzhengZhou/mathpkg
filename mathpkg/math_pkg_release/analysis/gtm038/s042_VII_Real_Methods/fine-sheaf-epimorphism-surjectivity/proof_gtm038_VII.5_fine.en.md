---
role: proof
locale: en
of_concept: fine-sheaf-epimorphism-surjectivity
source_book: gtm038
source_chapter: "VII"
source_section: "5"
---

**1.** Let $s' \in \Gamma(X, \mathcal{S}')$, $x \in X$. Then there exist a $\sigma \in \mathcal{S}_x$ with $\varphi(\sigma) = s'(x)$, a neighborhood $W(x) \subset X$ and a section $s^* \in \Gamma(W, \mathcal{S})$ with $s^*(x) = \sigma$, so that $\varphi \circ s^*(x) = s'(x)$. We can find a neighborhood $U_x(x) \subset W$ with $\varphi \circ s^*|U_x = s'|U_x$. Let $s_{(x)} := s^*|U_x$.

**2.** $\mathfrak{U} = \{U_x : x \in X\}$ is an open covering of $X$. Let $(t_{(x)})_{x \in X}$ be a subordinate partition of unity. For $x \in X$, $t_{(x)} \cdot s_{(x)}$ is an element of $\Gamma(X, \mathcal{S})$. Since the system of sets $\mathrm{Supp}(t_{(x)})$ is locally finite, the sum

$$s := \sum_{x \in X} t_{(x)} \cdot s_{(x)}$$

is a well-defined global section in $\Gamma(X, \mathcal{S})$. Moreover, since $\varphi$ is a sheaf morphism of $\mathcal{T}$-modules,

$$\varphi(s) = \varphi\left(\sum_{x \in X} t_{(x)} \cdot s_{(x)}\right) = \sum_{x \in X} t_{(x)} \cdot \varphi(s_{(x)}) = \sum_{x \in X} t_{(x)} \cdot s'|_{U_x} = s',$$

where the last equality holds because $(t_{(x)})$ is a partition of unity subordinate to the covering on which each $s_{(x)}$ coincides with $s'$. Thus $s$ is a preimage of $s'$ under $\varphi_*$, establishing surjectivity.
