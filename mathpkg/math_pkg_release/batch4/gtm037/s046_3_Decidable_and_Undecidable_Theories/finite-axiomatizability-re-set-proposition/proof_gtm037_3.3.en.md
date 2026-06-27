---
role: proof
locale: en
of_concept: finite-axiomatizability-re-set-proposition
source_book: gtm037
source_chapter: "3"
source_section: "3"
---

We can assume that the language has only finitely many nonlogical constants, and we list all members of $M$ as follows. Begin listing all finite $\mathcal{L}$-structures with universe $m \in \omega \setminus \{1\}$ (any finite $\mathcal{L}$-structure will be isomorphic to one of this form). Simultaneously start listing all sentences. For each finite $\mathcal{L}$-structure $\mathfrak{A}$, check if $\mathfrak{A}$ is a model of $\Gamma$; since $\Gamma$ is finitely axiomatizable, this can be done in finitely many steps. If $\mathfrak{A}$ is determined to be a model of $\Gamma$, check each sentence already listed for truth in $\mathfrak{A}$. For those sentences of the form $\neg \varphi$ determined to hold in $\mathfrak{A}$ we put $g^{+} \varphi$ on our output list. Clearly this gives an effective enumeration of $M$. Thus the claim holds. A rigorous proof would be rather lengthy, but is clearly possible (by Church's thesis).
