---
role: proof
locale: en
of_concept: bidual-isomorphism
source_book: gtm007
source_chapter: "VI"
source_section: "§1.1"
---

Since $G$ and $\widehat{\widehat{G}}$ have the same order (by Proposition 2 applied twice), it suffices to prove that the evaluation homomorphism $\varepsilon: G \to \widehat{\widehat{G}}$ is injective.

Let $x \in \ker(\varepsilon)$. This means $\chi(x) = 1$ for all characters $\chi \in \widehat{G}$. We must show $x = 1$. Suppose $x \neq 1$. Consider the cyclic subgroup $H = \langle x \rangle$ of $G$. Define a character $\chi_0$ on $H$ by $\chi_0(x) = e^{2\pi i / \text{ord}(x)}$, which is nontrivial since $\text{ord}(x) > 1$. By Proposition 1, $\chi_0$ extends to a character $\chi$ of $G$. Then $\chi(x) = \chi_0(x) \neq 1$, contradicting $x \in \ker(\varepsilon)$. Hence $\ker(\varepsilon) = \{1\}$ and $\varepsilon$ is injective, thus an isomorphism.
