---
role: proof
locale: en
of_concept: truth-depends-only-on-free-variables
source_book: gtm053
source_chapter: "II"
source_section: "2.10"
---

(a) Let $t$ be a term, and suppose that for any variable $x$ in $t$ we have $x^\xi = x^{\xi'}$. Then by Lemma 1.4 (Unique Reading) and induction on the length of $t$, we obtain $t^\xi = t^{\xi'}$.

(b) For atomic formulas $P$ of the form $p(t_1, \ldots, t_r)$, we have
$$|P|(\xi) = \begin{cases} 1, & \text{if } \langle t_1^\xi, \ldots, t_r^\xi \rangle \in \phi(p), \\ 0, & \text{otherwise}, \end{cases}$$
and similarly for $|P|(\xi')$. Since $\xi$ and $\xi'$ agree on all variables occurring in $P$ (all of which are free in an atomic formula), they agree on all variables in the $t_i$, so $t_i^\xi = t_i^{\xi'}$ by part (a). Hence $|P|(\xi) = |P|(\xi')$.

(c) For non-atomic formulas, we proceed by induction on the number of connectives and quantifiers. The cases for $\neg, \Leftrightarrow, \Rightarrow, \vee, \wedge$ follow directly from the induction hypothesis. For $\forall x Q$ and $\exists x Q$, the truth value at $\xi$ is determined by the values of $Q$ at variations $\xi'$ of $\xi$ along $x$. Since $\xi$ and the original point agree on all variables except possibly $x$, and $x$ is bound (not free) in the quantified formula, the condition on free variables is preserved for $Q$ at each variation. The proposition follows by induction.
