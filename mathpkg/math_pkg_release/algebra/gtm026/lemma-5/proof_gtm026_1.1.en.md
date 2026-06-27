---
role: proof
locale: en
of_concept: lemma-5
source_book: gtm026
source_chapter: "1"
source_section: "1.31"
---

Let $f, g : A_1 \longrightarrow A_2$ be admissible morphisms in $\mathcal{A}$. Let $S = \{(a_1 f, a_1 g) : a_1 \in A_1 U\}$. Let $R$ be the intersection of all congruences (defined in (1.11−) on $A_2$ containing $S$. We argue that $R$ is a congruence as follows: Let $(R_i : i \in I)$ be the set of all congruences on $A_2$ which contain $S$. Define a diagram scheme $\Delta$ with $N(\Delta) = I \cup \{t, t'\}$ where $t, t' \notin I$ and such that $\Delta(i, j)$ has exactly one element if $i \in I$ and $j

Since $f.h = g.h$, $S$ is a subset of $E$. Therefore, $R$ is also a subset of $E$, and $\bar{p}.h = \bar{q}.h$ inducing the desired unique $\psi$. $\psi$ is admissible by 2.1.56.

1.32 Examples of Algebraic Homomorphisms over Set. By 1.29 and 1.31, every homomorphism $U:(\mathcal{A}, W) \longrightarrow (\mathcal{B}, V)$ with $W: \mathcal{A} \longrightarrow \mathcal{Set}$ and $V: \mathcal{B} \longrightarrow \mathcal{Set}$ algebraic is itself algebraic $U: \mathcal{A} \longrightarrow \mathcal{B}$ and in particular has a left adjoint $F: \mathcal{B} \longrightarrow \mathcal{A}$. We give a few specific examples. Let $\mathcal{A}$ be rings (with unit) and unitary ring homomorphisms, let $\mathcal{B}$ be monoids, and let $U$ be the obvious forgetful functor. If $M$ is a monoid, $MF$ is usually called the monoid ring over $M$; this is best known when $M$ is a group and then $MF$ is called the integral group ring over $M$. [Mac Lane ’63, Chapter IV, section 1]. Or, let $\mathcal{A}$ be associative linear algebras over a fixed commutative ring $R$ with unit and let $\mathcal{B}$ be Lie algebras over $R$. There is a well-known homomorphism $U$ which transforms the associative algebra $A$ into a Lie algebra on the same underlying set with Lie bracket given by $[x, y] = xy - yx$. For a Lie algebra $L$, $LF$ is called the universal enveloping algebra over $L$ [Jacobson ’62, Chapter V]. Our previous Example 2.2.7 arises from $\mathcal{A} = abelian groups$ and $\mathcal{B} = groups$. Compact abelian groups (1.23) admits obvious homomorphisms to, say, compact spaces, abelian groups,

which is again a coequalizer in $\mathcal{A}$. Similarly applying $FU$, we have

$$AU \xrightarrow{fU} BU \xrightarrow{fFU} KFU$$

that $fFU = \text{coeq}(fU, gU)$ and there exists a unique isomorphism $\psi$: $KFU \longrightarrow K$ in $\mathcal{K}$ such that $fFU.\psi = h$. By the definition of “replete” in 2.3.2, $\psi:KFU \longrightarrow K$ has a unique lift $\bar{\psi}:KF \longrightarrow A$. The remaining details are clear. $\square$
