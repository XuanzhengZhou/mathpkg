---
role: proof
locale: en
of_concept: mathcal-subseteq-mathbb-b16
source_book: gtm054
source_chapter: "2"
source_section: "IIC"
---

Let $\mathcal{R}_1, \mathcal{R}_2 \in \mathbb{P}(U)$ and suppose $\mathcal{S} \leq \mathcal{R}_1$ and $\mathcal{S} \leq \mathcal{R}_2$. We show that $\mathcal{S} \leq \mathcal{R}_1 \mathcal{R}_2$. An arbitrary cell of $\mathcal{R}_1 \mathcal{R}_2$ is of the form $R_1 \cap R_2$ where $R_i \in \mathcal{R}_i$. Let $S \in \mathcal{S}$. If $S \cap R_i \neq \emptyset$, then $S \subseteq R_i$ by the definition of refinement. It is immediate that either $S \subseteq R_1 \cap R_2$ or $S \cap R_1 \cap R_2 = \emptyset$. Hence $\{ \mathcal{Q} \in \mathbb{P}(U) : \mathcal{S} \leq \mathcal{Q} \}$ is closed under multiplication. By B15 it contains a minimum element.

To complete the proof, we define a relation $\sim$ on $U$ whereby $x \sim y$ if
