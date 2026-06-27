---
role: proof
locale: en
of_concept: banach-category-theorem
source_book: gtm002
source_chapter: "16"
source_section: "16. The Banach Category Theorem"
---

Let $G$ be the union of a family $\mathcal{G}$ of non-empty open sets of first category. Let $\mathcal{F} = \{U_\alpha : \alpha \in A\}$ be a maximal family of disjoint non-empty open sets with the property that each is contained in some member of $\mathcal{G}$. Then the closed set $\bar{G} - \bigcup \mathcal{F}$ is nowhere dense. (Otherwise $\mathcal{F}$ would not be maximal.) Each set $U_\alpha$ can be represented as a countable union of nowhere dense sets, say $U_\alpha = \bigcup_{n=1}^{\infty} N_{\alpha,n}$. Put $N_n = \bigcup_{\alpha \in A} N_{\alpha,n}$. If an open set $U$ meets $N_n$, then it meets some $N_{\alpha,n}$ and there exists a non-empty open set $V \subset (U \cap U_\alpha) - N_{\alpha,n}$. Hence $V \subset U - N_n$, and so $N_n$ is nowhere dense. Therefore

$$G \subset (\bar{G} - \bigcup \mathcal{F}) \cup \bigcup_{\alpha \in A} U_\alpha = (\bar{G} - \bigcup \mathcal{F}) \cup \bigcup_{n=1}^{\infty} N_n$$

is of first category.

