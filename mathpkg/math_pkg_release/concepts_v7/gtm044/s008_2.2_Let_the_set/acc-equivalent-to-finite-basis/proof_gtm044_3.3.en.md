---
role: proof
locale: en
of_concept: acc-equivalent-to-finite-basis
source_book: gtm044
source_chapter: "3"
source_section: "3.3"
---

# Proof of a.c.c. Equivalent to Every Ideal Having a Finite Basis

**Lemma 3.3.** $R$ satisfies the a.c.c. iff every ideal of $R$ has a finite basis.

**Proof.** ($\Rightarrow$) Assume $R$ satisfies the a.c.c. on ideals. Let $\mathfrak{a}$ be any ideal of $R$. We construct a finite basis for $\mathfrak{a}$ inductively. Pick any $a_1 \in \mathfrak{a}$. If $(a_1) = \mathfrak{a}$, we are done. Otherwise, there exists $a_2 \in \mathfrak{a} \setminus (a_1)$. Then

$$(a_1) \subsetneq (a_1, a_2).$$

If $(a_1, a_2) = \mathfrak{a}$, we are done. Otherwise, pick $a_3 \in \mathfrak{a} \setminus (a_1, a_2)$, yielding

$$(a_1) \subsetneq (a_1, a_2) \subsetneq (a_1, a_2, a_3).$$

This process either terminates after finitely many steps, yielding a finite basis, or produces a strictly ascending infinite chain

$$(a_1) \subsetneq (a_1, a_2) \subsetneq (a_1, a_2, a_3) \subsetneq \cdots$$

which contradicts the a.c.c. Hence the process must terminate, so $\mathfrak{a} = (a_1, \ldots, a_n)$ has a finite basis.

($\Leftarrow$) Assume every ideal of $R$ has a finite basis. Let

$$\mathfrak{a}_1 \subseteq \mathfrak{a}_2 \subseteq \mathfrak{a}_3 \subseteq \cdots$$

be an ascending chain of ideals. Define $\mathfrak{a} = \bigcup_{i=1}^{\infty} \mathfrak{a}_i$. It is easy to verify that $\mathfrak{a}$ is an ideal of $R$: if $x, y \in \mathfrak{a}$, then $x \in \mathfrak{a}_i$, $y \in \mathfrak{a}_j$ for some $i, j$, so $x - y \in \mathfrak{a}_{\max(i,j)} \subseteq \mathfrak{a}$; and if $r \in R$, $x \in \mathfrak{a}_i$, then $rx \in \mathfrak{a}_i \subseteq \mathfrak{a}$.

By hypothesis, $\mathfrak{a}$ has a finite basis: $\mathfrak{a} = (b_1, \ldots, b_n)$. Each $b_j$ belongs to $\mathfrak{a}$, hence $b_j \in \mathfrak{a}_{i_j}$ for some index $i_j$. Set $N = \max\{i_1, \ldots, i_n\}$. Then $b_1, \ldots, b_n \in \mathfrak{a}_N$, so

$$\mathfrak{a} = (b_1, \ldots, b_n) \subseteq \mathfrak{a}_N \subseteq \mathfrak{a}_{N+1} \subseteq \cdots \subseteq \mathfrak{a}.$$

Thus $\mathfrak{a}_N = \mathfrak{a}_{N+1} = \cdots = \mathfrak{a}$, and the chain stabilizes after $\mathfrak{a}_N$. Hence $R$ satisfies the a.c.c. $\square$
