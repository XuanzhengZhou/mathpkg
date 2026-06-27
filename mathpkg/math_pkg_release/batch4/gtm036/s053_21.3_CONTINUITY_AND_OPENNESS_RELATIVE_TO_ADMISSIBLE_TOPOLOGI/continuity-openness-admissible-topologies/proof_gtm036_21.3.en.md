---
role: proof
locale: en
of_concept: continuity-openness-admissible-topologies
source_book: gtm036
source_chapter: "21"
source_section: "21.3"
---

**Proof of (i):** For each $A$ in $\mathcal{A}$ there is $B$ in $\mathcal{B}$ such that $A_0 + T'[H]_0 \supset T'[B]_0$, which implies that $(A_0 + T'[H]_0)^0 \subset T'[B]_0^0 = \overline{T'[B]}$. The first half of (i) now follows, because $A \cap \overline{T'[H]} \subset (A_0 + T'[H]_0)^0$.

**Proof of (ii):** Under the additional hypotheses of (ii), $w(F,E)$ is Hausdorff and, for each $B$ in $\mathcal{B}$, $T'[B]$ is $w(F,E)$-compact, since $T'$ is $w(H,G)$-$w(F,E)$ continuous (21.1); hence $T'[B]$ is $w(F,E)$-closed for each $B$ in $\mathcal{B}$. Using the result of the first half, we see that, for each $A$ in $\mathcal{A}$, $A \cap \overline{T'[H]} \subset T'[H]$, and, since $\mathcal{A}$ covers $F$, $\overline{T'[H]} \subset T'[H]$.

**Proof of (iii):** First observe that for each member $A$ of $\mathcal{A}$ we have $2A_0 + T'[H]_0 \supset A_0 + \langle T'[H]_0 \cup A_0 \rangle$, and the latter set contains the $\mathcal{T}_{\mathcal{A}}$-closure of $\langle T'[H]_0 \cup A_0 \rangle$. The topology $\mathcal{T}_{\mathcal{A}}$ is, under the hypothesis of the theorem, stronger than $w(E,F)$ and weaker than the Mackey topology $m(E,F)$; hence the members of $F$ represent all of $(E,\mathcal{T}_{\mathcal{A}})^*$, by 18.8. It follows from 17.1 that the $\mathcal{T}_{\mathcal{A}}$-closure of $\langle T'[H]_0 \cup A_0 \rangle$ equals its $w(E,F)$-closure, and the desired conclusion follows from polar computations.
