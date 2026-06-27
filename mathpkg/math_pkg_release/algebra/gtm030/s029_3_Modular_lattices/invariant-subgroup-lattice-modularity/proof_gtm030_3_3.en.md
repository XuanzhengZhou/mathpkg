---
role: proof
locale: en
of_concept: invariant-subgroup-lattice-modularity
source_book: gtm030
source_chapter: "3"
source_section: "3"
---

Let $\mathfrak{G}$ be the given group and let $\mathfrak{H}_1, \mathfrak{H}_2, \mathfrak{H}_3$ be invariant subgroups such that $\mathfrak{H}_1 \geq \mathfrak{H}_2$ (i.e., $\mathfrak{H}_1 \supseteq \mathfrak{H}_2$). Consider the intersection $\mathfrak{H}_1 \cap (\mathfrak{H}_2 \cup \mathfrak{H}_3)$. An element of this belongs to $\mathfrak{H}_1$ and has the form $h_2 h_3$ where $h_2 \in \mathfrak{H}_2$, $h_3 \in \mathfrak{H}_3$. Hence it is $h_2 h_3 \in \mathfrak{H}_1$. Since $h_2 \in \mathfrak{H}_2 \subseteq \mathfrak{H}_1$, we have $h_2^{-1} \in \mathfrak{H}_1$, and therefore $h_3 = h_2^{-1} (h_2 h_3) \in \mathfrak{H}_1$. Thus $h_3 \in \mathfrak{H}_1 \cap \mathfrak{H}_3$. Writing $h_2 h_3 = h_2 (h_3)$, where $h_2 \in \mathfrak{H}_2$ and $h_3 \in \mathfrak{H}_1 \cap \mathfrak{H}_3$, shows the element belongs to $\mathfrak{H}_2 \cup (\mathfrak{H}_1 \cap \mathfrak{H}_3)$. We have therefore proved the inequality

$$\mathfrak{H}_1 \cap (\mathfrak{H}_2 \cup \mathfrak{H}_3) \leq \mathfrak{H}_2 \cup (\mathfrak{H}_1 \cap \mathfrak{H}_3).$$

The reverse inequality $\mathfrak{H}_1 \cap (\mathfrak{H}_2 \cup \mathfrak{H}_3) \geq \mathfrak{H}_2 \cup (\mathfrak{H}_1 \cap \mathfrak{H}_3)$ is a general lattice-theoretic property (since $\mathfrak{H}_2 \leq \mathfrak{H}_1$ and $\mathfrak{H}_2 \leq \mathfrak{H}_2 \cup \mathfrak{H}_3$, while $\mathfrak{H}_1 \cap \mathfrak{H}_3 \leq \mathfrak{H}_1$ and $\mathfrak{H}_1 \cap \mathfrak{H}_3 \leq \mathfrak{H}_3 \leq \mathfrak{H}_2 \cup \mathfrak{H}_3$). Hence equality holds,

$$\mathfrak{H}_1 \cap (\mathfrak{H}_2 \cup \mathfrak{H}_3) = \mathfrak{H}_2 \cup (\mathfrak{H}_1 \cap \mathfrak{H}_3),$$

and the theorem is proved.
