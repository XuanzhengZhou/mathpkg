---
role: proof
locale: en
of_concept: lemma-lemma-11
source_book: gtm042
source_chapter: "11.3"
source_section: "A converse to Brauer"
---

Let $S(x)$ be the set of conjugates of $x$. Then

$$\psi'(x) = \frac{\text{Card } Z(x)}{\text{Card } H} \sum_{y \in S(x) \cap H} \psi(y).$$

Let $(Y_i)_{i \in I}$ be the distinct H-conjugacy classes contained in $S(x) \cap H$, and choose an element $y_i$ in each $Y_i$. The number of conjugates of $y_i$ in $H$ is equal to $Card Y_i$, and also equal to $(H: H \cap Z(y_i))$. Therefore

$$\psi'(x) = \frac{\text{Card } Z(x)}{\text{Card } H} \sum_{i \in I} \text{Card } Y_i \cdot \psi(y_i),$$

$$= \sum_{i \in I} n_i \psi(y_i),$$ with $n_i = \frac{\text{Card } Z(y_i)}{\text{Card}(H \cap Z(y_i))}.$$

Suppose we have $n_i \neq 0 \pmod{p}$ for some $i \in I

In other words, the family of elementary subgroups is "the smallest" for which Brauer's theorem is true.

11.4 The spectrum of $A \otimes R(G)$

Recall that if $C$ is a commutative ring, then the spectrum of $C$, denoted $Spec(C)$, is the set of prime ideals of $C$, cf. Bourbaki, Alg. Comm., Ch. II.

We want to determine the spectrum of the ring $A \otimes R(G)$. (We could also describe that of $R(G)$, but it would be more complicated.)

Let $Cl(G)$ be the set of conjugacy classes of $G$. The ring $A^{Cl(G)}$ can be identified with the ring of class functions on $G$ with values in $A$; if $f$ belongs to this ring, and if $c$ is a conjugacy class, let $f(c)$ denote the value of $f$ on an arbitrary element of $c$. The injections $A \rightarrow A \otimes R(G) \rightarrow A^{Cl(G)}$ define maps

$$Spec(A^{Cl(G)}) \rightarrow Spec(A \otimes R(G)) \rightarrow Spec(A).$$

These maps are surjective; this follows, for example, from the fact that $A^{Cl(G)}$ is integral over $A$ (and even over $Z$), cf. Bourbaki, Alg. Comm., Ch. IV, §2.

On the other hand, we know that $Spec(A)$ consists of the ideal 0 and the maximal ideals of $A$. Moreover, if $M$ is maximal in $A$, the field $A/M$ is finite; its characteristic is called the residue characteristic of $M$.

The spectrum of $A^{Cl(G)}$ can be identified with $Cl(G) \times Spec(A)$: with each $c \in Cl(G)$ and each $M \in Spec(A)$ we associate the prime ideal $M_c$ consisting of those $f \in A^{Cl(G)}$ such that $f(c) \in M$. The image of $M_c$ in $Spec(A \otimes R(G))$ is the prime ideal $P_{M,c} = M_c \cap (A \otimes R(G))$.

Proposition 3

11.4: The spectrum of $A \otimes R(G)$

To prove (i) we must show that, if $c_1 \neq c_2$, then there exists an element $f \in A \otimes R(G)$ such that $f(c_1) \neq 0$ and $f(c_2) = 0$, and this is clear (take for $f$ the function equal to $g$ on $c_1$ and 0 elsewhere).

If $M$ has characteristic $p$, an easy argument, analogous to the proof of lemma 7, shows that $P_{M,c_1} = P_{M,c'_1}$ (cf. ex. 10.4). On the other hand, lemma 8 shows that $P_{M,c'_1} \neq P_{M,c'_2}$ if $c'_1 \neq c'_2$. Whence (ii).

Remarks

(1) Let $I$ be an ideal of $A \otimes R(G)$. To show that $I$ is equal to $A \otimes R(G)$, it suffices to show that $I$ is not contained in any of the prime ideals $P_{M,c}$; this is the approach taken in the proof of Brauer’s theorem (see also ex. 11.7 below).

(2) We can represent $Spec(A \otimes R(G))$ graphically as a union of “lines” $D_c$ corresponding to the various classes $c$, each of these lines representing $Spec(A)$. These lines “intersect” in the following way: $D_{c_1}$ and $D_{c_2}$ have a common point above a maximal ideal $M$ of $A$ with residue characteristic $p$ if and only if the $p'$-components of $c_1$ and $c_2$ are equal.
