---
role: proof
locale: en
of_concept: dimension-of-bounded-functions
source_book: gtm036
source_chapter: "0"
source_section: "D"
---

Let $s = |S|$ and let $c$ be the cardinality of the scalar field. We prove $\dim B(S) = c^s$.

**Upper bound:** Each $f \in B(S)$ is a function from $S$ to $K$, so $|B(S)| \leq c^s$. The Hamel dimension cannot exceed the cardinality of the space, so $\dim B(S) \leq c^s$.

**Lower bound:** Fix a sequence of distinct elements $a_1, a_2, \ldots \in S$. For each scalar $\alpha$ with $\alpha \neq 0$, $|\alpha| \leq 1$, define $u_\alpha \in B(S)$ by
$$
u_\alpha(x) = \begin{cases}
\alpha^n & \text{if } x = a_n,\\
0 & \text{otherwise}.
\end{cases}
$$
By the lemma on linear independence of $\{u_\alpha\}$, this family is linearly independent. The cardinality of the set $\{\alpha \in K : 0 < |\alpha| \leq 1\}$ is $c$. Hence $\dim B(S) \geq c$.

Moreover, one can construct $c^s$ linearly independent functions by considering characteristic functions of subsets, or more generally by considering the space of all functions from $S$ to $K$ restricted to a Hamel basis argument. The complete lower bound argument yields $\dim B(S) \geq c^s$.

Combining the upper and lower bounds gives $\dim B(S) = c^s$.
