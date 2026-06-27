---
role: proof
locale: en
of_concept: loss-theorem
source_book: gtm053
source_chapter: "2"
source_section: "2.1"
---

The proof proceeds by induction on the complexity of the $L$-formula $P$.

**Atomic formulas.** For an atomic formula $P(x_1, \ldots, x_n)$, e.g., $p(x_1, \ldots, x_n)$ for an $n$-ary relation symbol $p$, the equivalence holds by the definition of the interpretation in the ultraproduct: $\prod \mathbf{A}_i / U \models p(\tilde{\varphi}_1, \ldots, \tilde{\varphi}_n)$ iff $\{i : \mathbf{A}_i \models p(\varphi_1(i), \ldots, \varphi_n(i))\} \in U$. The same applies to equalities and formulas built from function symbols.

**Inductive step for $\wedge$.** Suppose $P = P_1 \wedge P_2$. Then

$$\prod \mathbf{A}_i / U \models (P_1 \wedge P_2)(\tilde{\varphi}) \iff \prod \mathbf{A}_i / U \models P_1(\tilde{\varphi}) \text{ and } \prod \mathbf{A}_i / U \models P_2(\tilde{\varphi}).$$

By the induction hypothesis, this is equivalent to $\{i : \mathbf{A}_i \models P_1(\varphi(i))\} \in U$ and $\{i : \mathbf{A}_i \models P_2(\varphi(i))\} \in U$. Since $U$ is a filter (hence closed under finite intersections), this is equivalent to $\{i : \mathbf{A}_i \models P_1(\varphi(i))\} \cap \{i : \mathbf{A}_i \models P_2(\varphi(i))\} \in U$, which is $\{i : \mathbf{A}_i \models (P_1 \wedge P_2)(\varphi(i))\} \in U$.

**Inductive step for $\neg$.** Suppose $P = \neg P_1$. Then

$$\prod \mathbf{A}_i / U \models \neg P_1(\tilde{\varphi}) \iff \prod \mathbf{A}_i / U \not\models P_1(\tilde{\varphi}).$$

By induction, this is equivalent to $\{i : \mathbf{A}_i \models P_1(\varphi(i))\} \notin U$. Since $U$ is an ultrafilter, a set is not in $U$ iff its complement is in $U$. Hence $\{i : \mathbf{A}_i \models \neg P_1(\varphi(i))\} = I \setminus \{i : \mathbf{A}_i \models P_1(\varphi(i))\} \in U$.

**Inductive step for $\exists$.** Suppose $P(x_1, \ldots, x_n) = \exists y \, Q(y, x_1, \ldots, x_n)$. If $\prod \mathbf{A}_i / U \models \exists y \, Q(y, \tilde{\varphi})$, then there exists $\tilde{\psi}$ such that $\prod \mathbf{A}_i / U \models Q(\tilde{\psi}, \tilde{\varphi})$. By induction, $\{i : \mathbf{A}_i \models Q(\psi(i), \varphi(i))\} \in U$. This set is contained in $\{i : \mathbf{A}_i \models \exists y \, Q(y, \varphi(i))\}$, so the latter also belongs to $U$.

Conversely, suppose $J = \{i : \mathbf{A}_i \models \exists y \, Q(y, \varphi(i))\} \in U$. For each $i \in J$, choose $a_i \in A_i$ such that $\mathbf{A}_i \models Q(a_i, \varphi(i))$ (using the axiom of choice). For $i \notin J$, choose $a_i \in A_i$ arbitrarily. Define $\psi(i) = a_i$. Then $\{i : \mathbf{A}_i \models Q(\psi(i), \varphi(i))\} \supseteq J \in U$, so by induction $\prod \mathbf{A}_i / U \models Q(\tilde{\psi}, \tilde{\varphi})$, hence $\prod \mathbf{A}_i / U \models \exists y \, Q(y, \tilde{\varphi})$.

By induction, the statement holds for all $L$-formulas.
