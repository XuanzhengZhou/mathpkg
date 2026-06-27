---
role: proof
locale: en
of_concept: filtered-colimits-in-grp
source_book: gtm005
source_chapter: "IX"
source_section: "Special Limits"
---

Let $J$ be a filtered category and $G : J \to \mathbf{Grp}$ a functor. Let $\mu$ be a limiting cone for the composite $U \circ G : J \to \mathbf{Grp} \to \mathbf{Set}$, with vertex set $S$ and components $\mu_j : G_j \to S$ (writing $G_j$ for both the group and its underlying set).

First, every $s \in S$ has a preimage in some $G_j$. If not, omitting $s$ from $S$ would yield a strictly smaller cone, contradicting universality.

Define multiplication on $S$: for $s, t \in S$, write $s = \mu_j(g_j)$, $t = \mu_k(g_k)$. Since $J$ is filtered, there exist arrows $j \to i \leftarrow k$; applying $G$ yields $G_j \to G_i \leftarrow G_k$. Let $g_i, h_i \in G_i$ be the images of $g_j, g_k$ respectively. Define $s \cdot t = \mu_i(g_i \cdot h_i)$. This is well-defined: if another $i'$ is chosen, filteredness gives a cone $G_i \to G_m \leftarrow G_{i'}$, and the definition via $i$ and $i'$ agree after pushing to $G_m$. Associativity holds because any three elements can be represented in a single group $G_i$, where associativity is known.

The identity of $S$ is $\mu_j(e_j)$ for any $j$ (filteredness ensures independence of choice). Inverses are defined similarly. All $\mu_j$ are group homomorphisms by construction. The universal property follows from the universal property in $\mathbf{Set}$: any cone of group homomorphisms from $G$ yields a cone of functions, hence a unique function from $S$, which is easily seen to be a group homomorphism.
