---
role: proof
locale: en
of_concept: irreducible-trace-zero-semisimple
source_book: gtm009
source_chapter: "V"
source_section: "19.1"
---

Since $\mathfrak{gl}(V) = \mathfrak{sl}(V) \oplus (\text{scalars})$, and $\mathfrak{gl}(V)$ acts irreducibly on $V$ (it even acts transitively), it follows that $\mathfrak{sl}(V)$ also acts irreducibly on $V$. This observation serves as the prototype for the general argument.

Suppose $L \subset \mathfrak{sl}(V) \subset \mathfrak{gl}(V)$ acts irreducibly on $V$. We first show $L$ is reductive. Let $R = \operatorname{Rad} L$. Since $R$ is a solvable ideal of $L$ and $L$ acts irreducibly, Lie's Theorem implies that all elements of $R$ are simultaneously triangularizable, hence $[R, R]$ is nilpotent and acts nilpotently on $V$. But a nilpotent Lie algebra of trace-zero endomorphisms acting irreducibly must be zero (by Engel's Theorem and the fact that $V$ is irreducible). Thus $\operatorname{Rad} L$ is abelian.

Now any element $z \in \operatorname{Rad} L$ commuting with $L$ lies in $Z(L)$. Conversely, if $x \in Z(L)$, then $x$ is certainly in the radical. Hence $\operatorname{Rad} L = Z(L)$, so $L$ is reductive.

By Proposition 19.1(a), $L = [LL] \oplus Z(L)$ with $[LL]$ semisimple. Now $Z(L)$ consists of endomorphisms commuting with the irreducible action of $L$, so by Schur's Lemma, $Z(L)$ consists of scalar matrices. But $L \subset \mathfrak{sl}(V)$ forces each element to have trace $0$, so the only scalar matrix in $L$ is $0$. Therefore $Z(L) = 0$, and $L = [LL]$ is semisimple.
