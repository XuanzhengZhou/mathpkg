---
role: proof
locale: en
of_concept: if-r-is-well-founded-on-a-and-well-orders-a-if
source_book: gtm001
source_chapter: "7"
source_section: ""
---

As the first step in our proof we will show that $G$ is single valued. For this purpose suppose that $\langle x, y_1 \rangle, \langle x, y_2 \rangle \in G$. Then

$$y_1 \in [A - W(x)] \land y_2 \in [A - W(x)]$$

and $[(A - W(x)) \cap (R^{-1})' \{y_1\}] = 0 \land [(A - W(x)) \cap (R^{-1})' \{y_2\}] = 0

From Proposition 7.48 it then follows that $\mathcal{W}(F) \subseteq A$ and $F$ is one-to-one. To prove that $F$ is onto we note that if $y \in \mathcal{W}(F)$ then $(\exists \alpha)[y = F^{\alpha}]$. Furthermore since $F^{\alpha}$ is the R-minimal element in $A - F^{\alpha}$

$$x R y \rightarrow x \notin [A - F^{\alpha}]$$

then

$$x \in A \land x R y \rightarrow x \in F^{\alpha} \rightarrow x \in \mathcal{W}(F).$$

Then $R, A$, and $\mathcal{W}(F)$ satisfy the hypotheses of Proposition 7.47:

$$R \text{ We } A \land R \text{ Wfr } A \land \mathcal{W}(F) \subseteq A \land (\forall x \in A)(\forall y \in \mathcal{W}(F))[x R y \rightarrow x \in \mathcal{W}(F)].$$

Consequently, from Proposition 7.47 we conclude that $\mathcal{W}(F) = A \lor (\exists x \in A)[\mathcal{W}(F) = A \cap (R^{-1})^{\{x\}}].$ But $\mathcal{W}(F)$ cannot be an R-initial segment of $A$ because R-initial segments of $A$ are sets, and $\mathcal{W}(F)$ being the one-to-one image of the proper class $On$ cannot be a set. Therefore $\mathcal{W}(F) = A$ and

$$F: \text{ On } \frac{1-1}{\text{ onto}} A.$$

Finally if $\alpha < \beta$ then $F^{\alpha} \subseteq F^{\beta}$ and hence $[A - F^{\alpha}] \subseteq [A - F^{\alpha}]$. Since $F^{\alpha} \in [A - F^{\beta}]$ it follows that $F^{\alpha} \in [A - F^{\alpha}]$. But $F^{\alpha}$ is the R-minimal element of $A - F^{\alpha}$. Hence

$$F^{\alpha} R F^{\beta}

That $F \upharpoonright \alpha$ is order preserving is proved as in the proof of Proposition 7.51 and is left to the reader. Then $(F \upharpoonright \alpha) \text{Isom}_{E, R}(\alpha, A)$. But $F \upharpoonright \alpha$ is a set, i.e. $(\exists f)[f = F \upharpoonright \alpha]$. Then $(\exists f)[f \text{Isom}_{E, R}(\alpha, A)]$.

The uniqueness argument is left to the reader.
