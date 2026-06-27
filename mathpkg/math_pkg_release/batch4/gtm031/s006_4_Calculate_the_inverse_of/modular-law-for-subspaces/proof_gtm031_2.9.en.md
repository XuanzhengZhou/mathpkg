---
role: proof
locale: en
of_concept: modular-law-for-subspaces
source_book: gtm031
source_chapter: "II: Finite Dimensional Vector Spaces"
source_section: "9: Factor Spaces"
---

Assume $\mathfrak{S}_1 \supseteq \mathfrak{S}_2$. We prove the two inclusions.

First, $\mathfrak{S}_1 \cap (\mathfrak{S}_2 + \mathfrak{S}_3) \supseteq \mathfrak{S}_1 \cap \mathfrak{S}_2 + \mathfrak{S}_1 \cap \mathfrak{S}_3$:
Since $\mathfrak{S}_1 \cap \mathfrak{S}_2 \subseteq \mathfrak{S}_1 \cap (\mathfrak{S}_2 + \mathfrak{S}_3)$ and $\mathfrak{S}_1 \cap \mathfrak{S}_3 \subseteq \mathfrak{S}_1 \cap (\mathfrak{S}_2 + \mathfrak{S}_3)$, their sum is also contained in $\mathfrak{S}_1 \cap (\mathfrak{S}_2 + \mathfrak{S}_3)$.

Second, $\mathfrak{S}_1 \cap (\mathfrak{S}_2 + \mathfrak{S}_3) \subseteq \mathfrak{S}_1 \cap \mathfrak{S}_2 + \mathfrak{S}_1 \cap \mathfrak{S}_3$:
Let $x \in \mathfrak{S}_1 \cap (\mathfrak{S}_2 + \mathfrak{S}_3)$. Then $x \in \mathfrak{S}_1$ and $x = y + z$ with $y \in \mathfrak{S}_2$, $z \in \mathfrak{S}_3$. Since $\mathfrak{S}_1 \supseteq \mathfrak{S}_2$, we have $y \in \mathfrak{S}_2 \subseteq \mathfrak{S}_1$. Then $z = x - y \in \mathfrak{S}_1$ because $x, y \in \mathfrak{S}_1$. Therefore $y \in \mathfrak{S}_1 \cap \mathfrak{S}_2$ and $z \in \mathfrak{S}_1 \cap \mathfrak{S}_3$, so $x = y + z \in \mathfrak{S}_1 \cap \mathfrak{S}_2 + \mathfrak{S}_1 \cap \mathfrak{S}_3$.

Since $\mathfrak{S}_1 \supseteq \mathfrak{S}_2$, we also have $\mathfrak{S}_1 \cap \mathfrak{S}_2 = \mathfrak{S}_2$, so the modular law can be written as
$$
\mathfrak{S}_1 \cap (\mathfrak{S}_2 + \mathfrak{S}_3) = \mathfrak{S}_2 + (\mathfrak{S}_1 \cap \mathfrak{S}_3).
$$
