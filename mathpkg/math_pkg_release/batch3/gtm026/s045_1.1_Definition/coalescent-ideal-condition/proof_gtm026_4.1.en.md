---
role: proof
locale: en
of_concept: coalescent-ideal-condition
source_book: gtm026
source_chapter: "4"
source_section: "1"
---

*Proof.* If $I$ is coalescent, then for $p$ in $I$, the left multiplication $L_p: I \rightarrow I$ is injective. Since $I$ is minimal, $pI = I$, so $L_p$ is also surjective, hence a bijection of $I$. Let $a$ be the preimage of an idempotent $e$ under $L_p$, so that $pa = e$. Then $e$ is a left unit for elements of $I$ and the condition holds.

Conversely, suppose for every $p$ in $I$ there exists $a$ in $I$ with $ap$ idempotent. If $pq = pr$ for $p, q, r$ in $I$, then left-multiplying by $a$ gives $(ap)q = (ap)r$. Since $ap$ is an idempotent acting as a left identity on $I$, we obtain $q = r$, proving $I$ is coalescent. $\square$
