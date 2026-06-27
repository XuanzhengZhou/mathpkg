---
role: proof
locale: en
of_concept: different-formula
source_book: gtm028
source_chapter: "V"
source_section: "§11. Different and discriminant"
---

By definition, $\mathfrak{D}_{R'/R} = \mathcal{C}^{-1}$, where $\mathcal{C}$ is the complementary module. Since the formation of the complementary module commutes with localization (as shown in the proof of Theorem 27), it suffices to work locally.

Let $R$ be a DVR and $R'$ a Dedekind domain with finitely many prime ideals $\mathfrak{P}_1, \dots, \mathfrak{P}_g$. The complementary module $\mathcal{C}$ is a fractionary ideal; write $\mathcal{C} = \prod_i \mathfrak{P}_i^{-m_i}$ as a product of prime powers. Then $\mathfrak{D} = \prod_i \mathfrak{P}_i^{m_i}$.

Using the definition $\mathcal{C} = \{z \in K' : T(zR') \subset R\}$, one checks element-wise conditions. For the tame ramification case where the characteristic of $R/\mathfrak{p}$ does not divide $e(\mathfrak{P})$, a direct computation using the trace on the vector space $R'/\mathfrak{P}$ shows $m(\mathfrak{P}) = e(\mathfrak{P}) - 1$. The proof involves checking that an element has trace in $R$ if and only if its $\mathfrak{P}$-adic valuation is at least $1 - e(\mathfrak{P})$.
