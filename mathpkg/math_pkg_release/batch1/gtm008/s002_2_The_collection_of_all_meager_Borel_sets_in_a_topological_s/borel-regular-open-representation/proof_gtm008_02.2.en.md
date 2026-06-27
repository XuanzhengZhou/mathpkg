---
role: proof
locale: en
of_concept: borel-regular-open-representation
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

By Theorem 3.10 there exists an open set $G$ and meager sets $N_1$ and $N_2$ such that $B = (G + N_1) - N_2$. But

$$G = G^{-0} - (G^{-0} - G).$$

Hence

$$B = (G^{-0} + N_1) - [(G^{-0} - G - N_1) + N_2].$$

Since $G^{-0} - G$ is nowhere dense, the terms $N_1$ and $(G^{-0} - G - N_1) + N_2$ are meager, and $G^{-0}$ is regular open.
