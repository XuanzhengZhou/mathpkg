---
role: proof
locale: en
of_concept: downward-lowenheim-skolem
source_book: gtm053
source_chapter: "3"
source_section: "3.4"
---

Start with a nonempty subset $B_0 \subseteq A$ of cardinality $\kappa$. Fix some $a_0 \in B_0$. For each $L$-formula $P(v_1, \ldots, v_n)$ define a Skolem function $g_P : A^{n-1} \to A$ by

$$g_P(a_1, \ldots, a_{n-1}) = \begin{cases}
\text{an element } a \in A \text{ such that } A \models P(a_1, \ldots, a_{n-1}, a), & \text{if such exists,} \\
a_0, & \text{if not.}
\end{cases}$$

Let $B$ be the closure of $B_0$ under all the Skolem functions $g_P$. Then $B$ is closed under all the $L$-operations $f$, since any $(n-1)$-ary $f$ coincides with the Skolem function $g_{f(v_1, \ldots, v_{n-1}) = v_n}$.

Let $\mathcal{B}$ be the substructure on $B$ induced from $A$. We prove by induction on the complexity of formulas that for any $L$-formula $Q(v_1, \ldots, v_n)$ and any $b_1, \ldots, b_n \in B$,

$$\mathcal{B} \models Q(b_1, \ldots, b_n) \iff A \models Q(b_1, \ldots, b_n).$$

The atomic case holds because $\mathcal{B}$ is a substructure. The Boolean connectives are trivial. For the existential quantifier: if $A \models \exists y\, Q(\bar{b}, y)$, then by definition of the Skolem function $g_{\exists y Q}$, the element $b' = g_{\exists y Q}(\bar{b})$ belongs to $B$ and satisfies $A \models Q(\bar{b}, b')$. By the induction hypothesis, $\mathcal{B} \models Q(\bar{b}, b')$, hence $\mathcal{B} \models \exists y\, Q(\bar{b}, y)$. The converse direction is immediate from the induction hypothesis.

Thus $\mathcal{B} \preceq A$. Since $|B_0| = \kappa$ and there are only $|L| + \aleph_0$ many $L$-formulas, the closure $B$ has cardinality $\kappa$, as required.
