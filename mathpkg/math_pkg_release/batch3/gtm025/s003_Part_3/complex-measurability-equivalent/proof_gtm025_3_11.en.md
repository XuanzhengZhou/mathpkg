---
role: proof
locale: en
of_concept: complex-measurability-equivalent
source_book: gtm025
source_chapter: "3"
source_section: "11"
---

**Proof.** (i) $\Rightarrow$ (iii): The family $\{B \subset \mathbb{C} : f^{-1}(B) \in \mathcal{A}\}$ is a $\sigma$-algebra. For any open rectangle $U_1 \times U_2$,
$$f^{-1}(U_1 \times U_2) = f_1^{-1}(U_1) \cap f_2^{-1}(U_2) \in \mathcal{A}$$
since $f_1 = \operatorname{Re} f$ and $f_2 = \operatorname{Im} f$ are measurable. As open rectangles generate $\mathcal{B}(\mathbb{C})$, (iii) follows. (iii) $\Rightarrow$ (ii) is trivial. (ii) $\Rightarrow$ (i): $\{f_1 > a\} = f^{-1}(\{z : \operatorname{Re} z > a\})$, and the set $\{z : \operatorname{Re} z > a\}$ is open in $\mathbb{C}$. $\square$
