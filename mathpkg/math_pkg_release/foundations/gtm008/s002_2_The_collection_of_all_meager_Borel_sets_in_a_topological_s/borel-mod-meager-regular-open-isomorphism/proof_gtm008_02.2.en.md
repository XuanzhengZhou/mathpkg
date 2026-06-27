---
role: proof
locale: en
of_concept: borel-mod-meager-regular-open-isomorphism
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

Define $F(G) = G/I$ for $G \in |B'|$.

If $F(G_1) = F(G_2)$, then $G_1 - G_2 \in I$ and $G_2 - G_1 \in I$. Then $G_1 - G_2^-$ is meager and open. By the Baire Category Theorem,
$$G_1 - G_2^- = 0.$$
Similarly, $G_2 - G_1^- = 0$. Thus $G_1 \subseteq G_2^-$ and $G_2 \subseteq G_1^-$. Since $G_1$ and $G_2$ are each regular open,
$$G_1 = G_1^0 \subseteq G_2^{-0} = G_2 \quad \text{and} \quad G_2 = G_2^0 \subseteq G_1^{-0} = G_1.$$
Therefore $G_1 = G_2$ and $F$ is one-to-one.

For surjectivity: if $G \in |B|$, then by Corollary 3.11 there exists a regular open set $G'$ and meager sets $N_1, N_2$ such that $G = (G' + N_1) - N_2$. Then $G - G' \subseteq N_1 - N_2$, so $G - G'$ is meager. Similarly $G' - G$ is meager. Hence $G/I = G'/I = F(G')$, proving $F$ is onto.
