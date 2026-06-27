---
role: proof
locale: en
of_concept: forgetful-functor-creates-filtered-colimits-in-grp
source_book: gtm005
source_chapter: "IX"
source_section: "1. Filtered Limits"
---

We are given a filtered category $J$ and a functor $G: J \rightarrow \mathbf{Grp}$; it assigns to arrows $j \rightarrow k$ group morphisms $G_j \rightarrow G_k$; we shall write $G_j$ both for the group and its underlying set. We are also given a limiting cone $\mu$ for the composite functor $J \rightarrow \mathbf{Grp} \rightarrow \mathbf{Set}$; it has a set $S$ as vertex and assigns to each $j \in J$ a function $\mu_j: G_j \rightarrow S$.

We first show that there is a unique group structure on the set $S$ which will make all functions $\mu_j$ morphisms of groups. First note that to each $s \in S$ there is at least one index $j$ with a group element $g_j$ for which $\mu_j g_j = s$; otherwise we could omit $s$ from $S$ to have a cone with a smaller set $S'$ as vertex, an evident contradiction to the universality of $S$ (there would be two functions $S \rightrightarrows S$ having the same composite with $\mu$).

Now we define a product of any two elements $s, t \in S$. Write $s = \mu_j g_j$ and $t = \mu_k g_k$ for some $j, k \in J$; since $J$ is filtered, there is in $J$ a cone over $j, k$ with some vertex $i$. The image of this cone under $G$ is $G_j \rightarrow G_i \leftarrow G_k$, so $s$ and $t \in S$ both come from elements of the group $G_i$; define their product in $S$ to be $\mu_i$ of their product in $G_i$. This product is independent of the choice of $i$, because a different choice $i'$ is part of a cone $G_i \rightarrow G_m \leftarrow G_{i'}$ of group morphisms. Also, the product of three factors $r, s, t$ is associative, because we can choose $G_i$ to contain pre-images of all three, and multiplication is known to be associative in $G_i$.

The identity element of $S$ is $\mu_j(1_{G_j})$ for any $j \in J$, and inverses are defined similarly by transport to a common group. The verification of the group axioms follows from the filteredness of $J$ and the fact that each $G_j$ is a group. The universality of $S$ as a colimit in $\mathbf{Grp}$ then follows: any cone of group homomorphisms from $G$ to a group $H$ factors uniquely through $S$, because on underlying sets it factors through the set-colimit $S$, and the group structure on $S$ is uniquely determined by the requirement that the $\mu_j$ be homomorphisms.
