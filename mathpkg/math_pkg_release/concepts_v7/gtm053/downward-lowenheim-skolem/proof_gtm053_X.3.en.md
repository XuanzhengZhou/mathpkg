---
role: proof
locale: en
of_concept: downward-lowenheim-skolem
source_book: gtm053
source_chapter: "X"
source_section: "3"
---

# Proof of Downward Löwenheim-Skolem Theorem

**Theorem 3.4 (Downward Löwenheim-Skolem).** Let $\mathbf{A}$ be an $L$-structure with domain $A$. For any infinite cardinal $\kappa$ with $|L| \leq \kappa \leq |A|$ and any subset $B_0 \subseteq A$ with $|B_0| \leq \kappa$, there exists an elementary substructure $\mathbf{B} \preceq \mathbf{A}$ such that $B_0 \subseteq B$ and $|B| = \kappa$.

*Proof.* Fix a nonempty subset $B_0 \subseteq A$ of cardinality $\kappa$. Fix some $a_0 \in B_0$. For each $L$-formula $P(v_1, \ldots, v_n)$, define a *Skolem function* $g_P : A^{n-1} \to A$ by

$$g_P(a_1, \ldots, a_{n-1}) = \begin{cases}
\text{an element } a \in A \text{ such that } \mathbf{A} \models P(a_1, \ldots, a_{n-1}, a), & \text{if such } a \text{ exists}, \\
a_0, & \text{otherwise}.
\end{cases}$$

Let $B$ be the closure of $B_0$ under all the Skolem functions $g_P$ (for all formulas $P$ of all arities $n \geq 1$). Note that $B$ is also closed under all $L$-operations $f$: an $(n-1)$-ary function $f$ coincides with the Skolem function $g_{f(v_1,\ldots,v_{n-1})=v_n}$.

Since there are $|L| + \aleph_0$ formulas in $L$, the number of Skolem functions is $|L| + \aleph_0 \leq \kappa$. Closing $B_0$ (of size $\kappa$) under at most $\kappa$ finitary operations yields a set $B$ of cardinality $\kappa$.

Let $\mathbf{B}$ be the substructure of $\mathbf{A}$ induced on $B$. We claim $\mathbf{B} \preceq \mathbf{A}$. We prove by induction on formula complexity that for any $L$-formula $Q(v_1, \ldots, v_n)$ and any $b_1, \ldots, b_n \in B$,

$$\mathbf{B} \models Q(b_1, \ldots, b_n) \iff \mathbf{A} \models Q(b_1, \ldots, b_n).$$

- **Atomic formulas**: Holds because $\mathbf{B}$ is a substructure of $\mathbf{A}$.
- **Boolean connectives**: Immediate from the induction hypothesis.
- **Existential quantifier**: Suppose $\mathbf{A} \models \exists v_n\, Q(b_1, \ldots, b_{n-1}, v_n)$. Then for the Skolem function $g_Q$, we have $\mathbf{A} \models Q(b_1, \ldots, b_{n-1}, g_Q(b_1, \ldots, b_{n-1}))$. Since $b_i \in B$ and $B$ is closed under $g_Q$, we have $g_Q(b_1, \ldots, b_{n-1}) \in B$. By induction hypothesis, $\mathbf{B} \models Q(b_1, \ldots, b_{n-1}, g_Q(b_1, \ldots, b_{n-1}))$, hence $\mathbf{B} \models \exists v_n\, Q(b_1, \ldots, b_{n-1}, v_n)$. The converse direction ($\mathbf{B} \models \exists v\, Q$ implies $\mathbf{A} \models \exists v\, Q$) is immediate from the induction hypothesis.

Thus $\mathbf{B} \preceq \mathbf{A}$ with $|B| = \kappa$ and $B_0 \subseteq B$. $\square$
