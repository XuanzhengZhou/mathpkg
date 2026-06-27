---
role: proof
locale: en
of_concept: field-of-sets-properties
source_book: gtm037
source_chapter: "9"
source_section: "Part 2: Elements of Logic"
---
(i) Since $\bigcup \mathcal{A} \in \mathcal{A}$ and $\mathcal{A}$ is closed under relative complements, we have $\bigcup \mathcal{A} \sim \bigcup \mathcal{A} \in \mathcal{A}$, i.e., $0 \in \mathcal{A}$.

(ii) Let $X, Y \in \mathcal{A}$. By closure under relative complements, $\bigcup \mathcal{A} \sim X \in \mathcal{A}$ and $\bigcup \mathcal{A} \sim Y \in \mathcal{A}$. By closure under finite unions,
$$(\bigcup \mathcal{A} \sim X) \cup (\bigcup \mathcal{A} \sim Y) \in \mathcal{A}.$$
Taking the relative complement again,
$$\bigcup \mathcal{A} \sim ((\bigcup \mathcal{A} \sim X) \cup (\bigcup \mathcal{A} \sim Y)) \in \mathcal{A}.$$
By De Morgan's laws, this set equals $X \cap Y$. Hence $X \cap Y \in \mathcal{A}$.
