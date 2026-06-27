---
role: proof
locale: en
of_concept: subspace-coordinate-sum-projection
source_book: gtm054
source_chapter: "2"
source_section: "IIA"
---

(a) Let $\mathcal{A} = \mathcal{B} \oplus \mathcal{C}$ and $B = \operatorname{Fnd}(\mathcal{B})$. By these assumptions and A11, $\mathcal{B} \subseteq \mathcal{P}(B) \cap \mathcal{A} \subseteq \pi_B[\mathcal{A}]$. It suffices to show that $\pi_B[\mathcal{A}] \subseteq \mathcal{B}$.

Let $S \in \mathcal{A}$. Then $S = S_1 + S_2$ for some $S_1 \in \mathcal{B}$ and $S_2 \in \mathcal{C}$. By definition of $\oplus$, $B \cap S_2 = \varnothing$. Hence
$$\pi_B(S) = S \cap B = S_1 \in \mathcal{B}.$$

(b) Let $B \in \mathcal{P}(U)$ and assume that $\pi_B[\mathcal{A}] = \mathcal{P}(B) \cap \mathcal{A}$. By A11, $\mathcal{P}(U \setminus B) \cap \mathcal{A} \subseteq \pi_{U \setminus B}[\mathcal{A}]$. The reverse inclusion and the decomposition of $\mathcal{A}$ follow from the assumption and standard properties of projections and coordinate sums.
