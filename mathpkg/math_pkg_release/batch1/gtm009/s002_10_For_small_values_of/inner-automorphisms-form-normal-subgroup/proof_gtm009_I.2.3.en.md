---
role: proof
locale: en
of_concept: inner-automorphisms-form-normal-subgroup
source_book: gtm009
source_chapter: "I"
source_section: "2.3"
---
First verify the conjugation formula: for any $y \in L$,
$$\phi(\operatorname{ad} x)\phi^{-1}(y) = \phi([x, \phi^{-1}(y)]) = [\phi(x), y] = \operatorname{ad} \phi(x)(y).$$
Thus $\phi(\operatorname{ad} x)\phi^{-1} = \operatorname{ad} \phi(x)$ as endomorphisms of $L$. Now apply the exponential:
$$\phi \exp(\operatorname{ad} x)\phi^{-1} = \phi \left( \sum_{n=0}^{\infty} \frac{(\operatorname{ad} x)^n}{n!} \right) \phi^{-1} = \sum_{n=0}^{\infty} \frac{\phi (\operatorname{ad} x)^n \phi^{-1}}{n!} = \sum_{n=0}^{\infty} \frac{(\operatorname{ad} \phi(x))^n}{n!} = \exp(\operatorname{ad} \phi(x)).$$
Since $\exp(\operatorname{ad} \phi(x)) \in \operatorname{Int} L$, the conjugate of any generator lies in $\operatorname{Int} L$, hence the conjugate of any element of $\operatorname{Int} L$ (which is a product of such generators) also lies in $\operatorname{Int} L$. Therefore $\operatorname{Int} L \trianglelefteq \operatorname{Aut} L$.
