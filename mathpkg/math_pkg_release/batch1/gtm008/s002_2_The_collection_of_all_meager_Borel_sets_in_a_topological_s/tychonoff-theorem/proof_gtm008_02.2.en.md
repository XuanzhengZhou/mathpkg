---
role: proof
locale: en
of_concept: tychonoff-theorem
source_book: gtm008
source_chapter: "Chapter 2: Topological Spaces"
source_section: "2. The Collection of All Meager Borel Sets in a Topological Space"
---

Let $S$ be a collection of closed subsets of $\prod_{a \in A} X_a$ with the finite intersection property. We must show $\bigcap(S) \neq 0$.

Let $T$ be the collection of all families of subsets of $\prod_{a \in A} X_a$ that contain $S$ and have the finite intersection property. Order $T$ by inclusion.

If $\{B_b \mid b \in I_0\}$ is a subset of $T$, linearly ordered by inclusion, then $\bigcup_{b \in I_0} B_b$ still has the finite intersection property: any finite subfamily is contained in some $B_b$ (since the union is linearly ordered), and $B_b$ has the finite intersection property. Thus $\bigcup_{b \in I_0} B_b \in T$.

By Zorn's Lemma, $T$ contains a maximal element $B$ -- a family with the finite intersection property that has no proper extension with the finite intersection property.

For each $a \in A$, the family $\{p_a(C) \mid C \in B\}$ has the finite intersection property. Let
$$C_a = \{p_a(C)^- \mid C \in B\}.$$
Then $C_a$ is a collection of closed subsets of $X_a$ with the finite intersection property. Since $\langle X_a, T_a \rangle$ is compact, Theorem 3.17 gives $\bigcap(C_a) \neq 0$, i.e., there exists $b_a \in \bigcap(C_a)$.

Let $b = \prod_{a \in A} \{b_a\}$. For any neighborhood $N(b)$ in the product topology, $b_a \in p_a(N(b)) \in T_a$. Since $(\forall C \in B)[b_a \in p_a(C)^-]$, we have
$$(\forall C \in B)[p_a(N(b)) \cap p_a(C) \neq 0].$$
Consequently,
$$(\forall C \in B)[N(b) \cap C \neq 0].$$
In particular, since $S \subseteq B$,
$$(\forall A \in S)[N(b) \cap A \neq 0].$$
Thus $b \in A^-$ for all $A \in S$. Since each $A \in S$ is closed, $b \in \bigcap(S)$. Hence $\bigcap(S) \neq 0$, proving compactness by Theorem 3.17.
