---
role: proof
locale: en
of_concept: godels-completeness-theorem
source_book: gtm053
source_chapter: "I"
source_section: "6"
---

The proof proceeds via the Fundamental Lemma (6.5) and three auxiliary lemmas (6.6, 6.7, 6.8).

**Step 1: Fundamental Lemma (6.5).** If a set of formulas $\mathcal{E}$ in a language $L$ is consistent and complete and contains $\operatorname{Ax} L$, and if the alphabet of $L$ is sufficient for $\mathcal{E}$, then $\mathcal{E}$ has a model with cardinality $\leqslant \operatorname{card}(\text{alphabet of } L) + \aleph_0$.

*Proof of the Fundamental Lemma (6.9):* Construct the interpretation $\phi$ of $L$ explicitly. By a constant term we mean a term in $L$ that does not contain any symbols for variables. Let $M = \{ \bar{t} \mid t \text{ is a constant term} \}$ be a "second copy" of the set of constant terms, and define the primary mappings of the interpretation $\phi$ of $L$ in $M$ as follows:

$$\phi(c) = \bar{c} \quad \text{(for any constant } c \text{)};$$
$$\phi(f)(\bar{t}_1, \ldots, \bar{t}_r) = \overline{f(t_1, \ldots, t_r)} \quad \text{(for each operation symbol } f \text{ of degree } r \text{ and all constant terms } t_1, \ldots, t_r \text{)};$$
$$\langle \bar{t}_1, \ldots, \bar{t}_r \rangle \in \phi(p) \text{ if and only if } p(t_1, \ldots, t_r) \in \mathcal{E} \quad \text{(for each relation } p \text{ of degree } r \text{ and all constant terms } t_1, \ldots, t_r \text{)}.$$

Then one proves by induction on the structure of formulas that for any closed formula $P$, $|P|_{\phi} = 1$ if and only if $P \in \mathcal{E}$. The key case is $P = \forall x Q$ where $x$ occurs freely in $Q$. If $|P| = 1$ but $P \notin \mathcal{E}$, then $\neg P \in \mathcal{E}$, i.e., $\neg \forall x Q(x) \in \mathcal{E}$. Since the alphabet is sufficient for $\mathcal{E}$, we have $\neg \forall x Q(x) \Rightarrow \neg Q(c_Q) \in \mathcal{E}$, yielding $Q(c_Q) \notin \mathcal{E}$ by consistency, which contradicts $|P| = 1$. Conversely, if $|P| = 0$ but $P \in \mathcal{E}$, then for some constant term $t$, $Q(t) \notin \mathcal{E}$, so $\neg Q(t) \in \mathcal{E}$ by completeness, which contradicts $P \in \mathcal{E}$ via the specialization axiom.

**Step 2: Lemma 6.6.** If $\mathcal{E}$ is consistent and contains $\operatorname{Ax} L$, then there exists a consistent and complete set of formulas $\mathcal{E}' \supset \mathcal{E}$.

**Step 3: Lemma 6.7.** If $\mathcal{E}$ is consistent and contains $\operatorname{Ax} L$, then there exist a language $L'$ whose alphabet is obtained from the alphabet of $L$ by adding a set of new constants having cardinality $\leqslant \operatorname{card}(\text{alphabet of } L) + \aleph_0$, and a set of formulas $\mathcal{E}'$ in $L'$ such that $\mathcal{E}' \supset \mathcal{E}$, $\mathcal{E}'$ is consistent, and the alphabet of $L'$ is sufficient for $\mathcal{E}'$.

**Step 4: Lemma 6.8 (Iteration).** Starting from $(L^{(0)}, \mathcal{E}^{(0)}) = (L, \mathcal{E})$, define inductively:
$$L^{(i+1)} = (L^{(i)})', \quad \mathcal{E}^{(i+1)} = (\mathcal{E}^{(i)})' \text{ (applying Lemma 6.7)},$$
and then let
$$L^{(i+2)} = L^{(i+1)}, \quad \mathcal{E}^{(i+2)} = \text{completion of } \mathcal{E}^{(i+1)} \text{ in } L^{(i+1)} \text{ (applying Lemma 6.6)}.$$
Finally set
$$L^{(\infty)} = \bigcup_{i=0}^{\infty} L^{(i)}, \quad \mathcal{E}^{(\infty)} = \bigcup_{i=0}^{\infty} \mathcal{E}^{(i)}.$$
The set $\mathcal{E}^{(\infty)}$ is consistent (any deduction of a contradiction would be obtained at some finite level), complete (every closed formula in $L^{(\infty)}$ is written in the alphabet of $L^{(i)}$ for some $i$, and $\mathcal{E}^{(i+1)}$ contains the completion of $\mathcal{E}^{(i)}$ in $L^{(i)}$), and the alphabet of $L^{(\infty)}$ is sufficient for $\mathcal{E}^{(\infty)}$.

**Step 5: Deduction of Theorem 6.2 (Section 6.13).** Let $T$ be a Gödelian set of formulas in $L$. Applying Lemma 6.8 to $T$, embed $(L,T)$ in $(L^{(\infty)}, T^{(\infty)})$, where the pair satisfies Lemma 6.5. Let $\phi^{(\infty)}$ be an interpretation of $L^{(\infty)}$ from Lemma 6.5. The cardinality of $M^{(\infty)}$ does not exceed $\operatorname{card}(\text{alphabet of } L) + \aleph_0$. The restriction $\phi$ of $\phi^{(\infty)}$ to $L$ satisfies $T \subset T_{\phi}L$. To prove $T = T_{\phi}L$: let $P \in T_{\phi}L$. If $P$ is closed, then $P \in T$, since either $P$ or $\neg P$ lies in $T$ by completeness, and $\neg P \notin T$ because $P$ is $\phi$-true. If $P$ is not closed, its closure is in $T$ by the same reasoning. This establishes part (a). Part (b) follows directly from Lemma 6.8.
