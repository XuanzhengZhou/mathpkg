---
role: proof
locale: en
of_concept: constructibility-of-ordinals
source_book: gtm053
source_chapter: "IV"
source_section: "2"
---

Suppose not, and let $\beta$ be the least nonconstructible ordinal. All elements of $\beta$ are in $L_\alpha$ for some $\alpha$. Since $L$ is transitive, all $\gamma \geqslant \beta$ are nonconstructible. Hence
$$\beta = \{x \mid (x \text{ is an ordinal} \land x \in L_\alpha) \text{ is } V\text{-true}\}.$$
The formula "$x$ is an ordinal" can be written in $\Sigma_0$-form: $(\forall y \in x)(\forall z \in y)(z \in x) \land (\forall y \in x)(\forall z \in x)(y \in z \lor z \in y \lor y = z)$, which is $L$-absolute. Thus $V$-truth may be replaced by $L$-truth, implying $\beta \in L$ by Proposition 2.3, a contradiction.
