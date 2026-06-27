---
role: proof
locale: en
of_concept: ext-independent-of-presentation
source_book: gtm004
source_chapter: "III"
source_section: "2. The Functor Ext"
---

# Proof of Ext is Independent of the Choice of Projective Presentation

Let $A$ be a $\Lambda$-module and let $R \xrightarrow{\mu} P \xrightarrow{\varepsilon} A$ and $R' \xrightarrow{\mu'} P' \xrightarrow{\varepsilon'} A$ be two projective presentations of $A$. We claim that there is a natural equivalence between the functors $\operatorname{Ext}_A^\varepsilon(-, -)$ and $\operatorname{Ext}_A^{\varepsilon'}(-, -)$.

Consider the identity map $1_A : A \to A$. By the projectivity of $P$ and $P'$, there exist lifting maps $\pi : P \to P'$ and $\pi' : P' \to P$ such that $\varepsilon'\pi = \varepsilon$ and $\varepsilon\pi' = \varepsilon'$. These liftings induce maps $\sigma : R \to R'$ and $\sigma' : R' \to R$ making the obvious diagrams commute.

By Lemma 2.1, the induced maps

$$
\pi^* : \operatorname{Ext}_A^{\varepsilon'}(A, B) \to \operatorname{Ext}_A^\varepsilon(A, B),\qquad
(\pi')^* : \operatorname{Ext}_A^\varepsilon(A, B) \to \operatorname{Ext}_A^{\varepsilon'}(A, B)
$$

are well-defined and depend only on $1_A$, not on the particular choices of liftings.

Now $\pi' \circ \pi : P \to P$ and $1_P : P \to P$ are two liftings of $1_A$. By Lemma 2.1 again, $(\pi' \circ \pi)^* = 1_P^* = 1$, i.e., $\pi^* \circ (\pi')^* = 1$. Similarly, $(\pi')^* \circ \pi^* = 1$. Hence $\pi^*$ and $(\pi')^*$ are inverse natural isomorphisms.

Thus $\operatorname{Ext}_A^\varepsilon(A, B) \cong \operatorname{Ext}_A^{\varepsilon'}(A, B)$ via a natural isomorphism that is independent of choices. This natural equivalence allows us to drop the superscript $\varepsilon$ and write simply $\operatorname{Ext}_\Lambda(A, B)$. By this natural equivalence we are allowed to drop the superscript $\varepsilon$ and to write, simply, $\operatorname{Ext}_\Lambda(A, B)$.
