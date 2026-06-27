---
role: proof
locale: en
of_concept: lemma-7-4-surjectivity-of-local-homomorphism
source_book: gtm052
source_chapter: "II"
source_section: "7"
---
Consider the ideal $\mathfrak{a} = \mathfrak{m}_A B$ of $B$. We have $\mathfrak{a} \subseteq \mathfrak{m}_B$, and by (2), $\mathfrak{a}$ contains a set of generators for $\mathfrak{m}_B/\mathfrak{m}_B^2$. Hence by Nakayama's lemma for the local ring $B$ and the $B$-module $\mathfrak{m}_B$, we conclude that $\mathfrak{a} = \mathfrak{m}_B$.

Now apply Nakayama's lemma to the $A$-module $B$. By (3), $B$ is a finitely generated $A$-module. The element $1 \in B$ gives a generator for $B/\mathfrak{m}_A B = B/\mathfrak{m}_B = A/\mathfrak{m}_A$ by (1), so we conclude that $1$ also generates $B$ as an $A$-module, i.e., $f$ is surjective.
