---
role: proof
locale: en
of_concept: compactness-and-representation-via-polar
source_book: gtm036
source_chapter: "16"
source_section: "16.4"
---

Let $T$ be the canonical map of $E$ into the algebraic dual $F'$ of $F$, let $E$ have the topology $w(E,F)$, and let $F'$ have the topology $w(F',F)$. The set $B$ is compact if and only if $T[B]$ is compact, in view of the definition of $w(E,F)$. But bounded subsets of $F'$ are totally bounded by 16.1(vi), and $F'$ is complete because it is a closed subset of a product of complete spaces. Consequently $B$ is compact if and only if $T[B]$ is bounded and closed in $F'$.

The set $B^{o}$ is radial at $0$ if and only if $B$ is bounded, by 16.4, and $B$ is bounded if and only if $T[B]$ is bounded because of the definition of $w(E,F)$.

Finally, each linear functional bounded on $B^{o}$ is represented by a member of $E$ if and only if the polar of $B^{o}$ in $F'$ is contained in $T[E]$. But $B^{o}$ is identical with the polar of $T[B]$ in $F$, by a direct verification, and the second polar of $T[B]$ is the closure of $T[B]$ in $F'$ by 16.3(iv). Hence each linear functional bounded on $B^{o}$ is representable by a member of $E$ if and only if the closure of $T[B]$ is contained in $T[E]$. But $B$ was supposed to be closed; hence $\overline{T[B]} \subset T[E]$ if and only if $T[B]$ is closed. The results of the last three paragraphs yield the theorem.
