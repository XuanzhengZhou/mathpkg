---
role: proof
locale: en
of_concept: saturation-of-seminorm-set
source_book: gtm015
source_chapter: "3"
source_section: "37"
---

# Proof of Characterization of the saturation of a set of seminorms

Let $E$ be a vector space over $\mathbb{K}$ and let $\mathcal{F}$ be any set of seminorms on $E$. Let $\mathcal{G}$ be the set of all seminorms $p$ such that $p \leq p_1 + \cdots + p_n$ for suitable $p_1, \ldots, p_n \in \mathcal{F}$.

Since $\mathcal{F} \subset \mathcal{F}^*$ and $\mathcal{F}^*$ is saturated, clearly $\mathcal{G} \subset \mathcal{F}^*$. On the other hand, it is elementary that $\mathcal{G}$ is saturated (if $q$ is continuous for $\tau(\mathcal{G})$, then $q \leq M(p_1 + \cdots + p_n)$ for some $p_k \in \mathcal{F}$, hence $q \in \mathcal{G}$), and $\mathcal{G} \supset \mathcal{F}$, therefore $\mathcal{G} \supset \mathcal{F}^*$. Thus $\mathcal{G} = \mathcal{F}^*$.
