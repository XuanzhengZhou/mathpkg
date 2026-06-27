---
role: proof
locale: en
of_concept: uncoupling-lemma
source_book: gtm026
source_chapter: "1"
source_section: "1.11"
---

Since $p$ is constructed from the inductive rules (1.8) and (1.9) and has more than one symbol, it is clear that there exists a representation $p = p_1 \cdots p_n \omega$ as in the statement and that $n$ and $\omega$ are unique.

We must prove that if $p = q_1 \cdots q_n \omega$ is another such representation, then $p_i = q_i$ for all $i$. It is helpful to define the integer-valued valency map, $\operatorname{val}$ ([Cohn '65, p. 118]), on the set of all $\Omega$-words in $A$ by

$$\operatorname{val}(\tilde{\omega}) = 1 - m \quad (\text{for all } \tilde{\omega} \in \Omega_m)$$

$$\operatorname{val}(a) = 1 \quad (\text{for all } a \in A)$$

$$\operatorname{val}(b_1 \cdots b_m) = \operatorname{val}(b_1) + \cdots + \operatorname{val}(b_m)$$

Since an $\Omega$-term $q$ is constructed from (1.8) and (1.9), we have $\operatorname{val}(q) = 1$ and $\operatorname{val}(s) > 0$ for any proper left segment $s$ of $q$.

Now, suppose $p = p_1 \cdots p_n \omega = q_1 \cdots q_n \omega$. Consider the leftmost position where the two representations might differ. If $p_1 = q_1$ as words, we can cancel them and proceed inductively on the remaining suffix. The valency condition ensures that no proper left segment of an $\Omega$-term can have valency equal to that of a complete term, which forces the decomposition boundaries to align. Therefore $p_i = q_i$ for all $i$, establishing uniqueness.
