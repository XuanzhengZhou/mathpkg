---
role: proof
locale: en
of_concept: the-pairing-machine-mathcalp-has-the-collapsing-property
source_book: gtm001
source_chapter: "15"
source_section: ""
---

Let $\eta$ be an ordinal, let $X \subseteq \eta$ be a subalgebra of $\mathcal{P}_<^n$ and let $\pi: \xi \rightarrow X$ be the collapsing map of $X$. We want to show that $\pi: \xi \rightarrow \eta$ is a strong $\mathcal{P}_<$-map.

Let $Z = \{\alpha \in \text{On}^@ | J(\alpha) \in X\}$. Then, for any $\alpha = \langle \alpha_0, \ldots, \alpha_{n-1} \rangle$,

$$\alpha \in Z \rightarrow J(\alpha) \in X \subseteq \eta$$

$$\rightarrow \alpha_i = C_i^n(\langle J(\alpha) \rangle) \in X \quad \text{for all } i < n$$

$$\rightarrow \alpha \in X^@.$$

Hence $Z \subseteq X^@$.

$Z$ is an initial segment of $X^@$:

$$\alpha \in Z \land \beta

$\mathcal{P}^\eta < (X \cup H_\eta) \subseteq Y$. Clearly, $C_i^{\eta+1}(\langle \eta \rangle) \in H_\eta \cup \{\eta\} \subseteq Y$. Thus $Y$ is closed under $C_i^{\eta+1}$. It is easy to verify that $Y$ is closed under $F_0$ and $J$, so we leave it to the reader.

EXERCISE

Complete the discussion about $C_i$ in the above proof.
