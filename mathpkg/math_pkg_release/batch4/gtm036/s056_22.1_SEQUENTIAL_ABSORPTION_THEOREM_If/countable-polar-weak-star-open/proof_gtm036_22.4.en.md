---
role: proof
locale: en
of_concept: countable-polar-weak-star-open
source_book: gtm036
source_chapter: "22"
source_section: "22.1"
---
Let $\{U_n : n = 1, 2, \cdots\}$, with $U_1 = E$, be a decreasing sequence of sets forming a local base for $E$, and suppose that $W$ satisfies the hypothesis of the lemma. The proof involves an induction, which in turn depends on the following pre-lemma: if $U$ and $V$ are neighborhoods of $0$ in $E$, and $A$ is a subset of $E$ such that $A^0 \cap U^0 \subset W$, then there is a finite subset $B$ of $U$ such that $(A \cup B)^0 \cap V^0 \subset W$.

This pre-lemma is established as follows. The set $U^0$ is the intersection of the sets $\{x\}^0$, for $x$ in $U$, by the definition of polar. Since $A^0 \cap U^0 \subset W$, it follows that
$$V^0 \cap A^0 \cap U^0 = \bigcap \{V^0 \cap A^0 \cap \{x\}^0 : x \in U\}$$
is a subset of $W$. But $V^0 \cap A^0 \cap U^0$ is the intersection of a family of sets, each of which is weak* closed and contained in the weak* compact set $V^0$. Because $W \cap V^0$ is weak* open in $V^0$ and contains this intersection, there must be a finite collection, say $x_1, \cdots, x_k$, of points of $U$ such that
$$\bigcap \{V^0 \cap A^0 \cap \{x_i\}^0 : i = 1, \cdots, k\} \subset W.$$
Then $B = \{x_1, \cdots, x_k\}$ is the required finite set.

Now to prove the lemma, choose $A_0 = \emptyset$, so that $A_0^0 \cap U_1^0 \subset W$ since $U_1 = E$. For each $n$, assuming $A_{n-1}$ has been chosen so that $A_{n-1}^0 \cap U_n^0 \subset W$, apply the pre-lemma with $U = U_n$, $V = U_{n+1}$, and $A = A_{n-1}$ to obtain a finite subset $B_n$ of $U_n$ such that, setting $A_n = A_{n-1} \cup B_n$, we have $A_n^0 \cap U_{n+1}^0 \subset W$. Let $S = \bigcup \{B_n : n = 1, 2, \cdots\}$. Then $S$ is countable. Ordering the points of $S$ so that those of $B_1$ come first, then those of $B_2$, and so on, yields a sequence converging to $0$ because $U_n$ is a local base. Finally, $S^0 = \bigcap \{A_n^0 : n\} \subset \bigcap \{A_n^0 \cap U_{n+1}^0\} \subset W$.
