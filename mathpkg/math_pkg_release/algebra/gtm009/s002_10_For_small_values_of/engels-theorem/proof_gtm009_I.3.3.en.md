---
role: proof
locale: en
of_concept: engels-theorem
source_book: gtm009
source_chapter: "I"
source_section: "3.3"
---
The proof uses induction on $\dim L$, with the cases $\dim L = 0$ or $1$ being obvious.

\textbf{Step 1}: Suppose $K \subsetneqq L$ is any proper subalgebra. By Lemma 3.2 (ad-nilpotent action of $K$ on $L$), $K$ acts as a Lie algebra of nilpotent linear transformations on the vector space $L$, hence also on $L/K$. Since $\dim K < \dim L$, the induction hypothesis guarantees a nonzero vector $x + K \in L/K$ killed by $K$, i.e., $[K, x] \subset K$ but $x \notin K$. This means $K \subsetneqq N_L(K)$.

\textbf{Step 2}: Take $K$ to be a maximal proper subalgebra of $L$. Then $N_L(K) = L$, so $K$ is an ideal. If $\dim L/K > 1$, the inverse image in $L$ of a 1-dimensional subalgebra of $L/K$ would properly contain $K$, contradicting maximality. Hence $\dim L/K = 1$, and $L = K + Fz$ for any $z \in L \setminus K$.

\textbf{Step 3}: By induction on $\dim V$, $W = \{v \in V \mid K.v = 0\}$ is nonzero. Since $K$ is an ideal, $W$ is $L$-stable: for $x \in L$, $y \in K$, $w \in W$, we have $yx.w = xy.w - [x, y].w = 0$. Choose $z \in L \setminus K$; the nilpotent endomorphism $z$ acting on $W$ has an eigenvector, i.e., there exists nonzero $v \in W$ with $z.v = 0$. Then $L.v = (K + Fz).v = 0$, completing the proof.
