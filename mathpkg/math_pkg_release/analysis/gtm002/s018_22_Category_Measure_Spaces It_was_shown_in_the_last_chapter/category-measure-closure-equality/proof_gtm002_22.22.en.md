---
role: proof
locale: en
of_concept: category-measure-closure-equality
source_book: gtm002
source_chapter: "22"
source_section: "22"
---

Let $E$ have the property of Baire. Then $E = G \triangle P$ where $G$ is an open set and $P$ is of first category (Theorem 4.6, also a consequence of the Banach-Mazur game). By Theorem 22.2, $P$ is nowhere dense, hence $\mu(P) = 0$. Thus $\mu(E) = \mu(G)$. 

Now $\bar{G} - G$ is nowhere dense (it is the boundary of $G$), so $\mu(\bar{G} - G) = 0$, giving $\mu(\bar{G}) = \mu(G) = \mu(E)$. Moreover, $E \subset G \cup P$, so $\bar{E} \subset \bar{G} \cup \bar{P}$. Since $P$ is nowhere dense, $\bar{P}$ has empty interior and $\mu(\bar{P}) = 0$. Therefore $\mu(\bar{E}) = \mu(\bar{G}) = \mu(E)$.

For the second equality, $E'^{-'} = \bar{E}'^{-'}$ (taking interior of closure), and we apply the same reasoning: the boundary $\bar{E} - E'^{-'}$ is nowhere dense, hence has measure zero. Thus $\mu(E'^{-'}) = \mu(\bar{E}) = \mu(E)$.
