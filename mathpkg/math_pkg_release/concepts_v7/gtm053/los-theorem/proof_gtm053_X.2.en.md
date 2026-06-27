---
role: proof
locale: en
of_concept: los-theorem
source_book: gtm053
source_chapter: "X"
source_section: "2"
---

# Proof of Loś's Theorem (Ultraproduct)

**Theorem 2.10 (Loś's Theorem).** Let $\mathbf{A}_i = (A_i, L)$, $i \in I$, be a family of $L$-structures, $U$ an ultrafilter on $I$, and $\prod_{i \in I} \mathbf{A}_i / U$ the ultraproduct along $U$. For every $L$-formula $P(x_1, \ldots, x_n)$ with free variables $x_1, \ldots, x_n$ and for every $\varphi_1, \ldots, \varphi_n \in \prod_{i \in I} A_i$,

$$\prod_{i \in I} \mathbf{A}_i / U \models P(\tilde{\varphi}_1, \ldots, \tilde{\varphi}_n) \iff \{i \in I : \mathbf{A}_i \models P(\varphi_1(i), \ldots, \varphi_n(i))\} \in U,$$

where $\tilde{\varphi}$ denotes the equivalence class of $\varphi$ in the ultraproduct.

*Proof.* The proof proceeds by induction on the complexity of the formula $P$.

**Base case: atomic formulas.** This holds by definition of the interpretation of relation symbols and function symbols in the ultraproduct. For a relation symbol $p$, the interpretation is defined by: $p(\tilde{\varphi}_1, \ldots, \tilde{\varphi}_n)$ holds in the ultraproduct iff $\{i : \mathbf{A}_i \models p(\varphi_1(i), \ldots, \varphi_n(i))\} \in U$, i.e., $\mathbf{A}_i \models p(\varphi_1(i), \ldots, \varphi_n(i))$ for almost all $i$ (with respect to $U$). Similarly, equality $f(\tilde{\varphi}_1, \ldots, \tilde{\varphi}_n) = \tilde{\varphi}_{n+1}$ holds iff the corresponding equalities hold in almost all $\mathbf{A}_i$.

**Inductive step for $\wedge$ and $\neg$.** If the formula is of the form $P \wedge Q$:

$$\prod \mathbf{A}_i / U \models (P \wedge Q)(\tilde{\varphi}) \iff \prod \mathbf{A}_i / U \models P(\tilde{\varphi}) \text{ and } \prod \mathbf{A}_i / U \models Q(\tilde{\varphi})$$
$$\iff \{i : \mathbf{A}_i \models P(\varphi(i))\} \in U \text{ and } \{i : \mathbf{A}_i \models Q(\varphi(i))\} \in U$$
$$\iff \{i : \mathbf{A}_i \models P(\varphi(i))\} \cap \{i : \mathbf{A}_i \models Q(\varphi(i))\} \in U$$
$$\iff \{i : \mathbf{A}_i \models (P \wedge Q)(\varphi(i))\} \in U.$$

The crucial step uses the ultrafilter property: the intersection of two sets is in $U$ iff both sets are in $U$.

For negation $\neg P$:

$$\prod \mathbf{A}_i / U \models \neg P(\tilde{\varphi}) \iff \prod \mathbf{A}_i / U \not\models P(\tilde{\varphi})$$
$$\iff \{i : \mathbf{A}_i \models P(\varphi(i))\} \notin U$$
$$\iff I \setminus \{i : \mathbf{A}_i \models P(\varphi(i))\} \in U$$
$$\iff \{i : \mathbf{A}_i \not\models P(\varphi(i))\} \in U$$
$$\iff \{i : \mathbf{A}_i \models \neg P(\varphi(i))\} \in U,$$

where we use the ultrafilter property that a set is not in $U$ iff its complement is in $U$.

**Inductive step for $\exists$.** If the formula is $\exists v\, P(v, \tilde{\varphi})$, then the ultraproduct satisfies it iff there exists $\tilde{\psi}$ such that $\prod \mathbf{A}_i / U \models P(\tilde{\psi}, \tilde{\varphi})$. By the induction hypothesis, this is equivalent to $\{i : \mathbf{A}_i \models P(\psi(i), \varphi(i))\} \in U$ for some $\psi$.

One direction: if $\{i : \mathbf{A}_i \models \exists v\, P(v, \varphi(i))\} \in U$, then by the Axiom of Choice we can select, for each $i$ in this set, an element $\psi(i) \in A_i$ witnessing the existential quantifier (and assign arbitrary values for other $i$). Then $\{i : \mathbf{A}_i \models P(\psi(i), \varphi(i))\} \supseteq \{i : \mathbf{A}_i \models \exists v\, P(v, \varphi(i))\} \cap \{\text{witness set}\} \in U$, so the ultraproduct satisfies $\exists v\, P(v, \tilde{\varphi})$.

Conversely, if the ultraproduct satisfies $\exists v\, P$, then by induction hypothesis $\{i : \mathbf{A}_i \models P(\psi(i), \varphi(i))\} \in U$ for some $\psi$. Since $P(\psi(i), \varphi(i))$ implies $\exists v\, P(v, \varphi(i))$ in each $\mathbf{A}_i$, the set $\{i : \mathbf{A}_i \models \exists v\, P(v, \varphi(i))\}$ is a superset of a set in $U$, hence itself in $U$.

This completes the induction, establishing Loś's Theorem for all first-order formulas. $\square$
