---
role: proof
locale: en
of_concept: pointwise-limits
source_book: gtm005
source_chapter: "V"
source_section: "3. Limits with Parameters"
---

**Proof.** Let $T : J \times P \rightarrow X$ be a bifunctor such that for each $p \in P$, the limit $\operatorname{Lim}_j T(j, p)$ exists. Instead of proving the statement directly, we replace functors $P \rightarrow X$ by objects of the functor category $X^P$. This replaces $T : J \times P \rightarrow X$ by its adjunct $S : J \rightarrow X^P$ under the adjunction

$$\operatorname{Cat}(J \times P, X) \cong \operatorname{Cat}(J, X^P).$$

Recall that for each object $p \in P$ there is an evaluation functor $E_p : X^P \rightarrow X$, given for objects $H$ and arrows (natural transformations) $\sigma : H \rightarrow H'$ of $X^P$ by

$$E_p H = H_p, \quad E_p \sigma = \sigma_p : H_p \rightarrow H'_p.$$

Now suppose $S : J \rightarrow X^P$ has a limiting cone $\tau : L \rightarrow S$ in $X^P$. For each $p \in P$, applying $E_p$ yields a cone $E_p \tau : E_p L \rightarrow E_p S$ in $X$. We claim this is a limiting cone. Given any other cone $\sigma : M \rightarrow E_p S$ in $X$, we need a unique arrow $M \rightarrow E_p L$ making the appropriate diagram commute. Since $L$ is a limit in $X^P$, for each $p$ the other cone there are unique arrows $M_p \rightarrow L_p$ because $L_p$ is a limit; they combine to give a unique natural transformation $M \rightarrow L$.

The conclusion may be written

$$E_p(\operatorname{Lim} S) = \operatorname{Lim}(E_p S).$$

In a functor category, limits may be calculated pointwise (provided the pointwise limits exist). $\square$
