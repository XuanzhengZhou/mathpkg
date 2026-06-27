---
role: proof
locale: en
of_concept: theorem-3-10-b-g-n-1-n-2
source_book: gtm008
source_chapter: "2"
source_section: "2 The collection of all meager Borel sets in a topological spa"
---
If $B$ is open then $B = (B + 0) - 0$. If $B$ is closed

$$B = [B^0 + (B - B^0)] - 0.$$

Thus in the notation of Theorem 3.6, the result holds for each element of $A_0$. If it holds for each element of $A_\alpha$ and if $B \in A_{\alpha+1}$ then there is an $\omega$-sequence $B_0, B_1, \ldots$, of elements in $A_\alpha$, such that $B = \sum_{i < \omega} B_i$ or $

Since $-G$ is closed $-G - (-G)^0$ is meager and hence

$$B = [(-G)^0 + (-G - (-G)^0) + N_2] - (N_1 - N_2)$$

where $(-G - (-G)^0) + N_2$ and $N_1 - N_2$ are meager.

**Corollary 3.11.** If $B$ is a Borel set of the topological space $\langle X, T \rangle$ then there exists a regular open set $G$ and meager sets $N_1$ and $N_2$ such that

$$B = (G + N_1) - N_2.$$

**Proof.** By Theorem 3.10 there exists an open set $G$ and meager sets $N_1$ and $N_2$ such that $B = (G + N_1) - N_2$. But

$$G = G^{-0} - (G^{-0} - G).$$

Hence

$$B = (G^{-0} + N_1) - [(G^{-0} - G - N_1) + N_2].$$

**Definition 3.12.** $A$ is a compact set in the topological space $\langle X, T \rangle$ iff $A \subseteq X$ and

$$(\forall S \subseteq T) \left[ A \subseteq \bigcup (S) \rightarrow (\exists S' \subseteq S) \left[ \text{Fin}^* (S') \wedge A \subseteq \bigcup (S') \right] \right].$$

**Definition 3.13.** A topological space $\langle X, T \rangle$ is

1. a Hausdorff space

iff $(\forall a, b \in X) [a \neq b \rightarrow (\exists N(a)) (\exists N'(b)) [N(a) \cap N'(b) = 0]]$,

2. a compact space iff $X$ is a compact set,

3. a locally compact space iff $\forall a \in X, \exists N(a), N

and a neighborhood of each such point

$$N(a_1), \ldots, N(a_n)$$

such that

$$A \subseteq N(a_1) \cup \cdots \cup N(a_n)$$

and $b \notin N(a_1)^-, b \notin N(a_2)^-, \cdots, b \notin N(a_n)^-$. Therefore

$$(\exists N_1(b))[N_1(b) \cap N(a_1) = 0]$$

$$(\exists N_2(b))[N_2(b) \cap N(a_2) = 0]$$

$$\vdots$$

$$(\exists N_n(b))[N_n(b) \cap N(a_n) = 0]$$.

If

$$N(b) = N_1(b) \cap \cdots \cap N_n(b)$$

then $N(b) \cap A = 0$. But this contradicts the fact that $b \in A^-$.

Therefore $A^- - A = 0$ i.e., $A$ is closed.

2. If $A$ is a closed set in the compact space $\langle X, T \rangle$ and if

$$[S \subseteq T] \wedge [A \subseteq \bigcup(S)]$$

then

$$(\forall a \in X - A)[\exists N(a) \subseteq X - A]$$.

Consequently $X \subseteq \bigcup(S) \cup \bigcup\{N(a) \mid a \in X - A \land N(a) \subseteq X - A\}$. Since $\langle X, T \rangle$ is compact there exists a finite collection of sets in $S$

$$D_1, \ldots, D_n$$

and a finite collection of sets in $\{N(a) \mid [a \in X - A] \land [N(a) \subseteq X - A]\}$

$$N(a_1), \ldots, N(a_m)$$

such that

$$X \subseteq D_1 \cup \cdots \cup D_n \cup N(a_1) \cup \cdots \cup N(a_m).$$

Then

$$

Since $X - A$ is open for each $A \in S$ and $\langle X, T \rangle$ is compact $\exists A_0, \ldots, A_n \in S$

$$X = \bigcup_{i \leq n} (X - A_i) = X - \bigcap_{i \leq n} A_i.$$

Therefore $\bigcap_{i \leq n} A_i = 0$. This is a contradiction.

Conversely suppose that every collection of closed sets $S$ with the finite intersection property also has the property $\bigcap(S) \neq 0$. Suppose also that there exists a collection of open sets $T'$ such that

$$X \subseteq \bigcup(T')$$

but $\forall A_1, \ldots, A_n \in T'$

$$X \not\subseteq \bigcup_{i \leq n} A_i.$$

Then

$$\bigcap_{i \leq n} (X - A_i) = X - \bigcup_{i \leq n} A_i \neq 0.$$

Thus $\{X - A \mid A \in T'\}$ is a collection of closed sets with the finite intersection property. Then

$$X - \bigcup_{A \in T'} A = \bigcap_{A \in T'} (X - A) \neq 0$$

i.e.,

$$X \not\subseteq \bigcup(T').$$

This is a contradiction.

**Theorem 3.18.** If $\langle X, T \rangle$ is a topological space, if $X' \subseteq X$ and $T' = \{X' \cap N \mid N \in T\}$ then $\langle X', T' \rangle$ is a topological space. Furthermore

1. $\langle X', T' \rangle$ is a compact space if $X'$ is a compact set,
2. $\langle X', T' \rangle$ is a Hausdorff space if $\langle X, T \rangle$ is Hausdorff.

**Proof.** Left to the reader.

**Definition 3.19.** If $\langle X, T \rangle$ is a topological

Proof. 1. If $A$ is open in $T$ then

$$(\forall a \in A \cap X') (\exists N(a) \in T) [N(a) \subseteq A].$$

Then $N(a) \cap X' \in T'$ and $a \in N(a) \cap X' \subseteq A \cap X'$. Thus $A \cap X'$ is open in $T'$.

2. If $a \in X'$ and $(\forall N(a) \in T') [N(a) \cap (A \cap X') \neq 0]$ then

$$(\forall N(a) \in T) [N(a) \cap X' \cap A \neq 0].$$

Thus

$$(\forall N(a) \in T) [N(a) \cap A \neq 0].$$

Since $A$ is closed $a \in A$ and hence $a \in A \cap X'$ i.e., $A \cap X'$ is closed in $T'$.

3. If $A$ is both open and closed in $T$ then by 1 and 2 above $A \cap X'$ is both open and closed in $T'$.
