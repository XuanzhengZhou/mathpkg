---
role: proof
locale: en
of_concept: hyper-real-field-is-eta-one-field
source_book: gtm043
source_chapter: "13"
source_section: "13.8"
---
Apply Lemma 13.7 with $P = M$. Given countable $A < B$ in $C/M$, we obtain $v$ with $A \leq v \leq B$.

If $A$ has a maximum $a_0$, then $a_0 < B$ and we need $a_0 < v < B$. Since $C/M$ is an ordered field with no consecutive elements (e.g., $(a_0 + b_1)/2$ lies between), we can apply Lemma 13.7 to $\{a_0\}$ and $B$ to get strict inequality.

In general, if $v \in A$, then $v$ would be the maximum of $A$, but $A$ has no maximum by the reduction. Similarly $v \notin B$. Since $C/M$ has no consecutive elements, $A < v < B$ holds strictly.

Thus $C/M$ satisfies the $\eta_1$-set definition, and being an ordered field, is an $\eta_1$-field.