---
role: proof
locale: en
of_concept: saturated-implies-homogeneous
source_book: gtm037
source_chapter: "28"
source_section: "Saturated Structures"
---

Assume that $\mathfrak{A}$ is an $m$-saturated $\mathcal{L}$-structure, $\alpha < m$, $x \in {}^\alpha A$, $y \in {}^\alpha A$, $(\mathfrak{A}, x_\xi)_{\xi < \alpha} \equiv_{\text{ee}} (\mathfrak{A}, y_\xi)_{\xi < \alpha}$, and $c \in A$. Let $\mathcal{L}'$ be the expansion of $\mathcal{L}$ to a language for $(\mathfrak{A}, x_\xi)_{\xi < \alpha}$. Set

$$\Delta = \{\varphi \in \text{Fmla}^1_{\mathcal{L}'} : (\mathfrak{A}, x_\xi)_{\xi < \alpha} \models \varphi[c]\}.$$

By the elementary equivalence assumption, every finite subset of $\Delta$ can be realized in $(\mathfrak{A}, y_\xi)_{\xi < \alpha}$. Since $\mathfrak{A}$ is $m$-saturated, $\Delta$ can be realized in $(\mathfrak{A}, y_\xi)_{\xi < \alpha}$. Thus there exists $d \in A$ such that $(\mathfrak{A}, x_\xi, c)_{\xi < \alpha} \equiv_{\text{ee}} (\mathfrak{A}, y_\xi, d)_{\xi < \alpha}$, establishing $m$-homogeneity.
