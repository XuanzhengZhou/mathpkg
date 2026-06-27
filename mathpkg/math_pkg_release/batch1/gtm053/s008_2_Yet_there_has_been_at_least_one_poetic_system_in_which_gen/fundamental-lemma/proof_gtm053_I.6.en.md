---
role: proof
locale: en
of_concept: fundamental-lemma
source_book: gtm053
source_chapter: "I"
source_section: "6"
---

We explicitly construct the interpretation $\phi$ of $L$ that will be the model for $\mathcal{E}$.

**Construction of the term model.** By a *constant term* we mean a term in $L$ that does not contain any symbols for variables. Let

$$M = \{ \bar{t} \mid t \text{ is a constant term} \}$$

be a "second copy" of the set of constant terms, and define the primary mappings of the interpretation $\phi$ of $L$ in $M$ as follows:

$$\phi(c) = \bar{c} \quad \text{(for any constant } c \text{)};$$

$$\phi(f)(\bar{t}_1, \ldots, \bar{t}_r) = \overline{f(t_1, \ldots, t_r)} \quad \text{(for each operation symbol } f \text{ of degree } r \text{ and all constant terms } t_1, \ldots, t_r \text{)};$$

$$\langle \bar{t}_1, \ldots, \bar{t}_r \rangle \in \phi(p) \text{ if and only if } p(t_1, \ldots, t_r) \in \mathcal{E} \quad \text{(for each relation } p \text{ of degree } r \text{ and all constant terms } t_1, \ldots, t_r \text{)}.$$

The cardinality of $M$ clearly does not exceed the number of constant terms, which is at most $\operatorname{card}(\text{alphabet of } L) + \aleph_0$.

**Claim.** Let $P$ be a closed formula. Then $|P|_{\phi} = 1$ if and only if $P \in \mathcal{E}$.

This claim implies that $\phi$ is a model for $\mathcal{E}$: if $P \in \mathcal{E}$ is not closed, then its closure $\forall x_1 \cdots \forall x_n P$ is deducible from $\mathcal{E}$ using Gen, and hence, since $\mathcal{E}$ is complete and consistent, $\forall x_1 \cdots \forall x_n P \in \mathcal{E}$; the claim then gives $|\forall x_1 \cdots \forall x_n P|_{\phi} = 1$, which means that $|P|_{\phi}(\xi) = 1$ for all $\xi \in \overline{M}$.

We prove the claim by induction on the number of connectives and quantifiers in $P$.

**Case 1: $P$ is atomic.** If $P$ has the form $p(t_1, \ldots, t_r)$, the claim follows directly from the definition of $\phi(p)$ and the fact that $\mathcal{E}$ is complete: either $p(t_1, \ldots, t_r) \in \mathcal{E}$ or $\neg p(t_1, \ldots, t_r) \in \mathcal{E}$, and $|p(t_1, \ldots, t_r)|_{\phi} = 1$ exactly when $p(t_1, \ldots, t_r) \in \mathcal{E}$ by construction. If $P$ has the form $t_1 = t_2$, the equality axioms together with consistency and completeness of $\mathcal{E}$ ensure the equivalence.

**Case 2: $P = \neg Q$.** $|P| = 1$ iff $|Q| = 0$ iff (by induction) $Q \notin \mathcal{E}$ iff (by completeness of $\mathcal{E}$) $\neg Q \in \mathcal{E}$ iff $P \in \mathcal{E}$.

**Case 3: $P = Q_1 \land Q_2$ (or other connectives).** Follows similarly by induction and the deductive closure properties of $\mathcal{E}$.

**Case 4: $P = \forall x Q$, where $x$ does not occur freely in $Q$.** Then $|P| = 1$ is equivalent to $|Q| = 1$, i.e., by the induction assumption, to $Q \in \mathcal{E}$. But $Q \in \mathcal{E}$ is equivalent to $\forall x Q \in \mathcal{E}$: in one direction using Gen, and in the other direction using the axiom of specialization with $t = x$ and then MP.

**Case 5: $P = \forall x Q$, where $x$ occurs freely in $Q$.**

*Subcase 5a:* Assume $|P| = 1$ but $P \notin \mathcal{E}$, and derive a contradiction. If $P \notin \mathcal{E}$, then $\neg P \in \mathcal{E}$ by completeness, i.e., $\neg \forall x Q(x) \in \mathcal{E}$. Since the alphabet of $L$ is sufficient for $\mathcal{E}$, it follows that $\mathcal{E}$ contains the formula

$$\neg \forall x Q(x) \Rightarrow \neg Q(c_Q).$$

Applying MP, we obtain $\mathcal{E} \vdash \neg Q(c_Q)$; since $\mathcal{E}$ is consistent, we have $Q(c_Q) \notin \mathcal{E}$. By the induction assumption, $|Q(c_Q)| = 0$ (note that $Q(c_Q)$ is closed). This means that $|Q(x)|(\xi) = 0$ for $\xi \in \overline{M}$ with $x^{\xi} = \overline{c_Q}$, contradicting the assumption that $|P| = 1$.

*Subcase 5b:* Assume $|P| = 0$ but $P \in \mathcal{E}$, and derive a contradiction. Since $|P| = 0$, there exists some $\xi \in \overline{M}$ with $|Q(x)|(\xi) = 0$. Let $t$ be the constant term for which $x^{\xi} = \bar{t}$. Clearly $t$ is free for $x$ in $Q$, so

$$0 = |Q(x)|(\xi) = |Q(t)|.$$

Hence $Q(t) \notin \mathcal{E}$ by the induction assumption, and $\neg Q(t) \in \mathcal{E}$ by completeness. But from $P \in \mathcal{E}$, i.e., $\forall x Q(x) \in \mathcal{E}$, the specialization axiom gives $Q(t) \in \mathcal{E}$ (since $t$ is free for $x$ in $Q$), contradicting consistency.

All cases are verified, completing the proof of the claim and hence of the Fundamental Lemma.
