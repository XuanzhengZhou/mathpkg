---
role: proof
locale: en
of_concept: truth-depends-on-free-variables
source_book: gtm053
source_chapter: "II"
source_section: "2"
---

(a) Let $t$ be a term, and suppose that for any variable $x$ in $t$ we have $x^\xi = x^{\xi'}$. Then Lemma 1.4 and induction on the length of $t$ give $t^\xi = t^{\xi'}$.

(b) Assertion 2.10 holds for atomic formulas $P$ of the form $p(t_1, \ldots, t_r)$. In fact,
$$|P|(\xi) = \begin{cases} 1, & \text{if } \langle t_1^\xi, \ldots, t_r^\xi \rangle \in \phi(P), \\ 0, & \text{otherwise}, \end{cases}$$
and similarly for $|P|(\xi')$. But if $\xi$ and $\xi'$ coincide on all the variables in $P$ (all of which occur freely), then a fortiori they coincide on all the variables in $t_i$, and therefore $t_i^\xi = t_i^{\xi'}$ by part (a). Hence the truth values coincide.

(c) The induction step through connectives is straightforward, since the truth value of a compound formula is a function of the truth values of its subformulas, and the induction hypothesis applies.

(d) For quantifiers: if $P = \forall x Q$ (or $\exists x Q$), then the truth value at $\xi$ depends on $|Q|(\xi')$ for variations $\xi'$ of $\xi$ along $x$. Since $\xi$ and $\xi'$ differ only on variables that do not occur freely in $Q$ (all free variables of $Q$ are either $x$ or occur freely in $P$), and on $x$, the induction hypothesis allows us to compare the relevant truth values. The proposition is proved.
