---
role: proof
locale: en
of_concept: substitution-theorem-pred
source_book: gtm022
source_chapter: "IV"
source_section: "4"
---

(a) Let $p_1, \ldots, p_n$ be a proof from $A$. By induction on $n$, $\alpha(p_1), \ldots, \alpha(p_n)$ is a proof from $\alpha(A)$. The key case is when $p_n = (\forall x)w$ by Generalisation. Since $x \notin \operatorname{var}(A_0)$ and $\beta$ is injective on the relevant variables, $\beta(x) \notin \operatorname{var}(\alpha(A_0))$, so Generalisation applies.
(b) Similar induction over the proof using the semantic definitions.
