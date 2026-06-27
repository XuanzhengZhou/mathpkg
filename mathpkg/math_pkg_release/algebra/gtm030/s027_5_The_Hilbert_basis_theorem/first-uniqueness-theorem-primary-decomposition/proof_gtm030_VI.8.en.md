---
role: proof
locale: en
of_concept: first-uniqueness-theorem-primary-decomposition
source_book: gtm030
source_chapter: "VI"
source_section: "8. Uniqueness theorems"
---

Let $\mathfrak{P}_1, \dots, \mathfrak{P}_r$ be the radicals of $\mathfrak{Q}_1, \dots, \mathfrak{Q}_r$ and $\mathfrak{P}_1', \dots, \mathfrak{P}_s'$ those of $\mathfrak{Q}_1', \dots, \mathfrak{Q}_s'$. Among the prime ideals $\mathfrak{P}_1, \dots, \mathfrak{P}_r$, pick one that is minimal with respect to inclusion; suppose it is $\mathfrak{P}_1$. Since $\mathfrak{P}_1$ is minimal, none of $\mathfrak{P}_2, \dots, \mathfrak{P}_r$ is contained in $\mathfrak{P}_1$.

We claim $\mathfrak{Q}_2 \cap \cdots \cap \mathfrak{Q}_r \not\subseteq \mathfrak{P}_1$. For if it were, then $\mathfrak{P}_j \subseteq \mathfrak{P}_1$ for some $j > 1$ by the properties of primary ideals, contradicting minimality of $\mathfrak{P}_1$. Hence $\mathfrak{Q}_2 \cap \cdots \cap \mathfrak{Q}_r \not\subseteq \mathfrak{P}_1$. By Lemma 3,
$$\mathfrak{Q}_1 : (\mathfrak{Q}_2 \cap \cdots \cap \mathfrak{Q}_r) = \mathfrak{Q}_1.$$
Now computing $\mathfrak{B} : (\mathfrak{Q}_2 \cap \cdots \cap \mathfrak{Q}_r)$ using both decompositions, we get that $\mathfrak{Q}_1$ is one of the $\mathfrak{Q}_i'$ (after possibly reordering). So $\mathfrak{P}_1$ appears among the $\mathfrak{P}_j'$.

Now suppose $\mathfrak{P}_1 = \mathfrak{P}_1'$. By Lemma 1 (intersection of primary ideals with the same radical), $\mathfrak{Q}_1 \cap \mathfrak{Q}_1'$ is primary with radical $\mathfrak{P}_1$. Then
$$\mathfrak{B} : (\mathfrak{Q}_1 \cap \mathfrak{Q}_1') = \mathfrak{Q}_2 \cap \cdots \cap \mathfrak{Q}_r = \mathfrak{Q}_2' \cap \cdots \cap \mathfrak{Q}_s',$$
and these are irredundant decompositions satisfying the hypotheses. By induction, the sets $\{\mathfrak{P}_2, \dots, \mathfrak{P}_r\}$ and $\{\mathfrak{P}_2', \dots, \mathfrak{P}_s'\}$ coincide. Hence $r = s$ and $\{\mathfrak{P}_1, \dots, \mathfrak{P}_r\} = \{\mathfrak{P}_1', \dots, \mathfrak{P}_r'\}$.
