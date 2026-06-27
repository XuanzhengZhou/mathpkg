---
role: proof
locale: en
of_concept: completion-theorem
source_book: gtm004
source_chapter: "VIII"
source_section: "8"
---

# Proof of Completion Theorem for Filtered Objects

**Theorem 8.5.** Given a filtered object $X$ as in (8.4), construct $X^\infty = \varinjlim_p X^p$ and then form the completion $Y = (X^\infty)_{-\infty} = \varprojlim_q (X^\infty)_q$ as in (8.9) and (8.10). The resulting filtration of $Y$ is complete, and

$$\operatorname{Gr} Y = \operatorname{Gr} X.$$

**Proof.** By construction (8.10), the filtration of $Y$ is obtained by first taking the colimit over the subobjects $X^p$ to form $X^\infty$, and then taking the limit over the quotient objects $(X^\infty)_q$. The second step — forming $(X^\infty)_{-\infty}$ as the limit of the $(X^\infty)_q$ — ensures, by the definition of the limit, that $Y = \varprojlim_q Y_q$, i.e., the filtration of $Y$ is **right complete**.

To see that the filtration of $Y$ is also **left complete**, we apply the dual of Proposition 8.2. Recall that $X^\infty = \varinjlim_p X^p$, so the cofiltration of $X^\infty$ is left complete. The dual of Proposition 8.2 (applied to the cofiltration rather than the filtration) guarantees that this left completeness is preserved upon passage to the limit over the quotients: the map $Y \to \varinjlim_p Y^p$ is an isomorphism. Hence $Y = \varinjlim_p Y^p$, establishing left completeness.

Thus the filtration of $Y$ is both left and right complete, i.e., complete.

It remains to show $\operatorname{Gr} Y = \operatorname{Gr} X$. In the notation of (8.4), the associated graded is given by

$$(\operatorname{Gr} X)_p = \operatorname{coker}(X^{p-1} \to X^p) = X^p / X^{p-1}.$$

Now, for each fixed $p$, consider the subquotients $X_q^p = X^p / X^q$. The graded piece $(\operatorname{Gr} X)_p$ is precisely $X_{p-1}^p$. The operations of taking limits and colimits commute in the sense that

$$\varprojlim_q \varinjlim_p X_q^p = \varinjlim_p \varprojlim_q X_q^p =: Y,$$

and the graded pieces of $Y$ coincide with those of $X$ because the passage from $X$ to $Y$ does not alter the subquotients $X_q^p$ for finite $p, q$; it only completes the filtration at infinity. Concretely, $Y^p / Y^{p-1} = X^p / X^{p-1}$ for all finite $p$, so $\operatorname{Gr} Y = \operatorname{Gr} X$ as claimed. $\square$
