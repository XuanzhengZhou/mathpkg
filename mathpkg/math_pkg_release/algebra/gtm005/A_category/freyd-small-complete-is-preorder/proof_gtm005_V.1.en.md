---
role: proof
locale: en
of_concept: freyd-small-complete-is-preorder
source_book: gtm005
source_chapter: "V"
source_section: "1. Creation of Limits"
---

Suppose $C$ is not a preorder. Then there exist objects $a, b \in C$ with two distinct arrows $f \neq g : a \to b$. For any small set $J$, form the product $\prod_J b$ of $|J|$ copies of $b$. An arrow $h: a \to \prod_J b$ is determined by its components $p_j \circ h: a \to b$ for each $j \in J$. Each component can be chosen to be either $f$ or $g$, giving at least $2^{|J|}$ distinct arrows $a \to \prod_J b$. If we choose $J$ with $|J| > |\operatorname{arr}(C)|$, then $2^{|J|} > |\operatorname{arr}(C)|$, a contradiction since $\prod_J b$ is an object of $C$ and there can be at most $|\operatorname{arr}(C)|$ arrows from $a$ to any object. Therefore $C$ must be a preorder.

In a preorder, a product is precisely a greatest lower bound (meet), and an equalizer always exists trivially (as the unique arrow from the object to itself). Hence small-completeness reduces to the existence of all small meets.
