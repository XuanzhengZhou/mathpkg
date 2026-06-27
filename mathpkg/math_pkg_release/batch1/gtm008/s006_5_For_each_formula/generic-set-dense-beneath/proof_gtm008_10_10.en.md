---
role: proof
locale: en
of_concept: generic-set-dense-beneath
source_book: gtm008
source_chapter: "10"
source_section: "10"
---

Under the given hypothesis, define
$$
S' = S \cup \{q \in P \mid \neg \operatorname{Comp}(p, q)\},
$$
where $\operatorname{Comp}(p, q)$ means $p$ and $q$ are compatible. Then $S' \in M$ and $S'$ is dense in $P$. Since $G$ is $P$-generic over $M$, we have $G \cap S' \neq \varnothing$.

Now any two elements of $G$ are compatible (by the definition of a filter), so $G$ cannot contain any $q$ that is incompatible with $p$. Therefore $G \cap \{q \in P \mid \neg \operatorname{Comp}(p, q)\} = \varnothing$, and consequently $G \cap S \neq \varnothing$.
