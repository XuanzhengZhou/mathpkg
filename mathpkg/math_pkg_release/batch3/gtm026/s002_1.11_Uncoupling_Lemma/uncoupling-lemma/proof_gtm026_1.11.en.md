---
role: proof
locale: en
of_concept: uncoupling-lemma
source_book: gtm026
source_chapter: "1"
source_section: "1.11"
---

Since $p$ is constructed from (1.8) and (1.9) and has more than one symbol, it is clear that there exists a representation $p = p_1 \cdots p_n \omega$ as in the statement and that $n$ and $\omega$ are unique. We must prove that if $p = q_1 \cdots q_n \omega$ is another such representation, then $p_i = q_i$ for all $i$.

It is helpful to define the integer-valued valency map, $\operatorname{val}$ (see Cohn '65, p. 118), on the set of all $\Omega$-words in $A$ by:
$$\operatorname{val}(\tilde{\omega}) = 1 - m \quad (\text{for all } \tilde{\omega} \in \Omega_m),$$
$$\operatorname{val}(a) = 1 \quad (\text{for all } a \in A),$$
$$\operatorname{val}(b_1 \cdots b_m) = \operatorname{val}(b_1) + \cdots + \operatorname{val}(b_m).$$

Since an $\Omega$-formula $q$ can be constructed from (1.8) and (1.9), one proves by induction on the construction that $\operatorname{val}(q) = 1$ and that $\operatorname{val}(s) > 0$ for any proper left segment $s$ of $q$ (where, if $q = b_1 \cdots b_m$, a left segment is a prefix $b_1 \cdots b_k$ with $1 \leq k < m$).

Now suppose $p = p_1 \cdots p_n \omega = q_1 \cdots q_n \omega$. Consider the valency along the word. At the point where $p_1$ ends and $p_2$ begins, the cumulative valency must be exactly $1$ (since $\operatorname{val}(p_1) = 1$). More generally, for any $\Omega$-word $r$, $\operatorname{val}(r) = 1$, and any proper left segment of $r$ has strictly positive valency. By comparing the two factorizations and using the valency properties, the initial segments $p_1$ and $q_1$ must coincide, for otherwise one would obtain a contradiction with the valency being $1$ at the end of each $p_i$ and $q_i$. Proceeding inductively yields $p_i = q_i$ for all $i = 1, \ldots, n$.
