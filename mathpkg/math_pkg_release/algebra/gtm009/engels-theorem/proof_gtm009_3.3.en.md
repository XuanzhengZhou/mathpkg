---
role: proof
locale: en
of_concept: engels-theorem
source_book: gtm009
source_chapter: "3"
source_section: "3.3"
---

\textbf{Proof.} Use induction on $\dim L$. If $\dim L = 0$ (or $\dim L = 1$), the result is obvious.

Suppose $K \neq L$ is any subalgebra of $L$. According to a lemma on nilpotent actions, $K$ acts (via ad) as a Lie algebra of nilpotent linear transformations on $L$, hence also on $L/K$. By induction hypothesis, there exists $x + K \neq K$ in $L/K$ killed by the image of $K$ in $\mathfrak{gl}(L/K)$. This means $[y x] \in K$ for all $y \in K$, while $x \notin K$. In other words, $K$ is properly contained in $N_L(K)$.

Now take $K$ to be a maximal proper subalgebra of $L$. The preceding argument forces $N_L(K) = L$, so $K$ is an ideal of $L$. If $\dim L/K > 1$, the inverse image in $L$ of a one-dimensional subalgebra of $L/K$ would be a proper subalgebra properly containing $K$, contradicting maximality. Therefore $K$ has codimension one, and $L = K + \mathbb{F}z$ for any $z \in L \setminus K$.

By induction, $W = \{v \in V \mid K.v = 0\}$ is nonzero. Since $K$ is an ideal, $W$ is stable under $L$: for $x \in L, y \in K, w \in W$, we have $y x.w = x y.w - [x, y].w = 0$. Choose $z \in L \setminus K$ as above; the nilpotent endomorphism $z$ acting on $W$ has a nonzero eigenvector with eigenvalue 0, i.e., there exists nonzero $v \in W$ with $z.v = 0$. Finally, $L.v = 0$.
