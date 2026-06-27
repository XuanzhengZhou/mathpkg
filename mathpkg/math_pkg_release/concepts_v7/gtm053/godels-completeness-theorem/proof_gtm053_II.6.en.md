---
role: proof
locale: en
of_concept: godels-completeness-theorem
source_book: gtm053
source_chapter: "II"
source_section: "6"
---

# Proof of Gödel's Completeness Theorem

**Theorem 6.2 (Gödel's Completeness Theorem).** Let $\mathcal{E}$ be a set of closed formulas in a first-order language $L$. If $\mathcal{E}$ is consistent (i.e., no contradiction is deducible from $\mathcal{E}$), then $\mathcal{E}$ has a model. Equivalently: if $\mathcal{E} \models P$ (every model of $\mathcal{E}$ satisfies $P$), then $\mathcal{E} \vdash P$.

*Proof.* The proof proceeds by constructing a model for any consistent set of formulas using Henkin's method, as presented by Smullyan.

**Step 1: Extending the language.** Add a countable set of new constant symbols to $L$ to obtain a language $L^{(\infty)}$ with $|L^{(\infty)}| = |L| + \aleph_0$. 

**Step 2: Constructing a maximally consistent set with witnesses (Henkin set).** By Lemma 6.8 (Lindenbaum's Theorem extended), the consistent set $\mathcal{E}$ can be extended to a set $\mathcal{E}^{(\infty)}$ of $L^{(\infty)}$-formulas that is:
- Maximally consistent (complete): for every closed formula $P$, either $P \in \mathcal{E}^{(\infty)}$ or $\neg P \in \mathcal{E}^{(\infty)}$;
- Deductively closed: if $\mathcal{E}^{(\infty)} \vdash P$, then $P \in \mathcal{E}^{(\infty)}$;
- Has witnesses: for every formula $\exists x\, P(x)$, there exists a constant $c$ such that $(\exists x\, P(x) \Rightarrow P(c)) \in \mathcal{E}^{(\infty)}$.

This construction proceeds by iteratively adding "Henkin axioms" $\exists x\, P(x) \Rightarrow P(c_P)$ for new constants and extending to a complete set using Lindenbaum's Theorem (Zorn's Lemma) at each step.

**Step 3: Building the canonical model (Lemma 6.5).** Define an interpretation $\phi^{(\infty)}$ as follows:
- The domain $M^{(\infty)}$ consists of equivalence classes $[t]$ of variable-free terms of $L^{(\infty)}$, where $t_1 \sim t_2$ iff $(t_1 = t_2) \in \mathcal{E}^{(\infty)}$.
- For a relation symbol $p$ of arity $n$: $p^{\phi}([t_1], \ldots, [t_n])$ holds iff $p(t_1, \ldots, t_n) \in \mathcal{E}^{(\infty)}$.
- For a function symbol $f$: $f^{\phi}([t_1], \ldots, [t_n]) = [f(t_1, \ldots, t_n)]$.
- For a constant $c$: $c^{\phi} = [c]$.

One verifies by induction on formula complexity that for every closed formula $P$,
$$\phi^{(\infty)} \models P \iff P \in \mathcal{E}^{(\infty)}.$$
The base case for atomic formulas follows from the definition. The inductive steps for $\wedge$, $\neg$, and $\forall$ follow from the maximal consistency and the witness property of $\mathcal{E}^{(\infty)}$.

**Step 4: Restricting to the original language.** The restriction $\phi$ of $\phi^{(\infty)}$ to the original language $L$ is a model of $\mathcal{E}$, since $\mathcal{E} \subseteq \mathcal{E}^{(\infty)}$ and every formula in $\mathcal{E}$ is true in $\phi^{(\infty)}$, hence in $\phi$. The cardinality of the model does not exceed $|L| + \aleph_0$, giving the downward Löwenheim-Skolem theorem as a corollary. $\square$
