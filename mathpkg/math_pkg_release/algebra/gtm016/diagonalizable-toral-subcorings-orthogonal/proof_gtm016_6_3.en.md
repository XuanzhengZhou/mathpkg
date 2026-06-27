---
role: proof
locale: en
of_concept: diagonalizable-toral-subcorings-orthogonal
source_book: gtm016
source_chapter: "6"
source_section: "6.3"
---

For $\alpha, \beta \in \mathbf{R}^S$, it follows that $\mathbf{R}^S - \varepsilon_T = \{\alpha - \varepsilon_T \mid \alpha \in \mathbf{R}^S\}$ is a $\pi$-subspace of $T^*_\pi$. Thus, $\mathbf{R}^S - \varepsilon_T = (\mathbf{R}^S - \varepsilon_T)^{\perp \perp}$ where
$$
(\mathbf{R}^S - \varepsilon_T)^{\perp} = \{t \in T_\pi \mid (\alpha - \varepsilon_T)(t) = 0 \text{ for } \alpha \in \mathbf{R}^S\}
$$
$$
= \{t \in T_\pi \mid t \in H(K/K^S)\}
$$
$$
= T_\pi \cap \langle S \rangle \quad (\text{see 6.3.6})
$$
and
$$
(\mathbf{R}^S - \varepsilon_T)^{\perp \perp} = ((\mathbf{R}^S - \varepsilon_T)^{\perp})^{\perp} = (T_\pi \cap \langle S \rangle)^{\perp} = \{\beta \in T^*_\pi \mid \beta(t) = 0 \text{ for } t \in T_\pi \cap \langle S \rangle\}.
$$
Thus, $\mathbf{R}^S - \varepsilon_T = \{\beta \in T^*_\pi \mid \beta(t) = 0 \text{ for } t \in T_\pi \cap \langle S \rangle\}$ and
$$\mathbf{R}^S = \{\alpha \in T^*_\pi \mid (\alpha - \varepsilon_T)(t) = 0 \text{ for all } t \in T_\pi \cap \langle S \rangle\}.$$
