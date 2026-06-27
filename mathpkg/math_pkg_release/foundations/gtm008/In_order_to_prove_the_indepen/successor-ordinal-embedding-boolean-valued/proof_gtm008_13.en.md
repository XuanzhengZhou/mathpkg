---
role: proof
locale: en
of_concept: successor-ordinal-embedding-boolean-valued
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

We need to verify that for all $\gamma \in V^{(B)}$, the equivalence holds with Boolean value $1$. By Definition 13.3:
$$[\![\check{\gamma} \in \check{\alpha} \vee \check{\gamma} = \check{\alpha}]\!] = \left( \sum_{\delta \in \alpha} [\![\check{\delta} = \check{\gamma}]\!] \right) + [\![\check{\alpha} = \check{\gamma}]\!]$$
$$= \sum_{\delta \in (\alpha + 1)} [\![\check{\delta} = \check{\gamma}]\!]$$
(since $\alpha + 1 = \alpha \cup \{\alpha\}$ as an ordinal)
$$= [\![\check{\gamma} \in (\alpha + 1)^{\check{}}]\!].$$

By Corollary 13.23 (which follows from the characterization of bounded quantifiers in $V^{(B)}$), the universal quantifier over all $\gamma \in V^{(B)}$ of this equivalence evaluates to $1$, since it holds termwise.
