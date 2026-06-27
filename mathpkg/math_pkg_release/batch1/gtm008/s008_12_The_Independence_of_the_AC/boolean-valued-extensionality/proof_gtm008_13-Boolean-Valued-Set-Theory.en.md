---
role: proof
locale: en
of_concept: boolean-valued-extensionality
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

Let $u, v \in V_\alpha^{(B)}$. We compute
$$[\![(\forall x)[x \in u \leftrightarrow x \in v]]\!]_{\alpha} = \prod_{x \in V_\alpha^{(B)}} ([\![x \in u]\!] \Leftrightarrow [\![x \in v]\!]).$$
Using the definition of Boolean implication and the properties of the Boolean sum and product, one shows that $[\![u = v]\!] \leq [\![(\forall x)(x \in u \leftrightarrow x \in v)]\!]_{\alpha}$ (by the definition of equality) and also $[\![(\forall x)(x \in u \leftrightarrow x \in v)]\!]_{\alpha} \leq [\![u = v]\!]$ (by taking $x$ to be elements of the domains). Hence $[\![(\forall x)(x \in u \leftrightarrow x \in v) \rightarrow u = v]\!]_{\alpha} = 1$, verifying extensionality.
