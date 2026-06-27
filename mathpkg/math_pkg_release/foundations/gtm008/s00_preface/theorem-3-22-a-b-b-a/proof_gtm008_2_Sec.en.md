---
role: proof
locale: en
of_concept: theorem-3-22-a-b-b-a
source_book: gtm008
source_chapter: "2"
source_section: "2 The collection of all meager Borel sets in a topological spa"
---
If $A$ is an open set in $X$ and $a \in A$ then since $\langle X, T \rangle$ is locally compact $\exists N(a), N(a)^-$ is compact. If

$$M = (N(a)^- \cap A)^0$$

then $M^-$ is also compact. If

$$T' = \{M^- \cap A \mid A \in T\}$$

then $\langle M^-, T' \rangle$ is a compact Hausdorff space. In this space $M^- - M$ is closed and hence compact. Moreover

$$(\forall y \in M^- - M)

Therefore

$$M(a) \subseteq M^- - [N(y_1) \cup \cdots \cup N(y_n)]$$

But since $N(y_1) \cup \cdots \cup N(y_n)$ is open $M^- - [N(y_1) \cup \cdots \cup N(y_n)]$ is closed. Hence

$$M(a)^- \subseteq M^- - [N(y_1) \cup \cdots \cup N(y_2)]$$

Therefore

$$M(a)^- \cap [N(y_1) \cup \cdots \cup N(y_n)] = 0$$

and

$$M(a)^- \subseteq M = (N(a)^- \cap A)^0.$$

But since $M(a) \in T'$,

$$(\exists N \in T)[M(a) = M^- \cap N].$$

And since $M(x) \subseteq M = M^0$

$$M(a) = M \cap N \in T.$$

**Theorem 3.23.** (The Baire Category Theorem.) Every open meager set in a locally compact Hausdorff space is empty.

**Proof.** If $B$ is an open meager set in the locally compact Hausdorff space $\langle X, T \rangle$ then there exists an $\omega$-sequence of nowhere dense sets

$$A_0, A_1, \ldots$$

such that

$$B = \bigcup_{\alpha < \omega} A_\alpha.$$

If $B \neq 0$ then by Theorem 3.22

$$(\exists N_1 \in T)[N_1^- \subseteq B]$$

and since $A_1$ is nowhere dense

$$(\exists N_2 \subseteq N_1)[N_2 \cap A_1 = 0]$$

for otherwise $N_1 \subseteq A_1^{-0}$. Then

$$(\exists N_3 \in T)[N_3^- \subseteq N_2].$$

Inductively we define a nested sequence of neighborhoods such that

$$N_{n+1} \subseteq N_{

But then $\forall n \in \omega$

$$x \in N_{2n+1} \land N_{2n+1} \cap A_n = 0.$$

Therefore $x \notin \bigcup_{\alpha \in \omega} A_\alpha$. This is a contradiction that compels the conclusion $B = 0$.

**Theorem 3.24.** If $B$ is the Boolean $\sigma$-algebra of all Borel sets in the locally compact Hausdorff space $\langle X, T \rangle$ and if $I$ is the $\sigma$-ideal of all meager Borel sets then $B/I$ is isomorphic to $B'$, the complete Boolean algebra of all regular open sets in $X$.

**Proof.** If

$$F(G) = G/I, \quad G \in |B'|$$

then $F(G_1) = F(G_2) \iff G_1 - G_2 \in I \land G_2 - G_1 \in I$. Then $G_1 - G_2^-$ is meager and open. Thus, by the Baire Category Theorem

$$G_1 - G_2^- = 0.$$

Similarly

$$G_2 - G_1^- = 0.$$

Then $G_1 \subseteq G_2^- \land G_2 \subseteq G_1^-$. Since $G_1$ and $G_2$ are each regular open

$$G_1 = G_1^0 \subseteq G_2^{-0} = G_2 \quad \text{and} \quad G_2 = G_2^0 \subseteq G_1^{-0} = G_1.$$

Therefore $G_1 = G_2$ and hence $F$ is one-to-one.

If $G \in |B|$ then by Corollary 3.11 there exists a regular open set $G'$ and meager sets $N_1, N_2$ such that

$$G = (G' + N_1) - N_2.$$

Then $G - G' \subseteq N_1 - N_2$ i.e., $G

Furthermore

$$(\forall A, B \in S) \left[ \left[ U_n \subseteq A \right] \wedge \left[ U_n \subseteq B \right] \rightarrow A = B \right].$$

Therefore $S$ is countable.
