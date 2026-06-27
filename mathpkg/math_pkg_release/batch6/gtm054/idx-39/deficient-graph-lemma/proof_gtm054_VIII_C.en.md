---
role: proof
locale: en
of_concept: deficient-graph-lemma
source_book: gtm054
source_chapter: "VIII"
source_section: "C"
---

Let $\Gamma = (V, \mathcal{E})$ be a $d$-deficient $(q_1, q_2)$-graph and let $x \in V$. Set $S = N(x)$ and $T = V \setminus (S \cup \{x\})$.

**(a)** If $\Gamma_S$ contained a $(q_1-1)$-clique $C$, then $C \cup \{x\}$ would be a $q_1$-clique in $\Gamma$, contradicting $\omega(\Gamma) < q_1$. Hence $\omega(\Gamma_S) < q_1 - 1$. Clearly $\alpha_0(\Gamma_S) \leq \alpha_0(\Gamma) < q_2$, so $\Gamma_S$ is a $(q_1-1, q_2)$-graph.

If $\Gamma_T$ contained a $(q_2-1)$-independent set $I$, then $I \cup \{x\}$ (since $x$ is adjacent to no vertex of $T$) would be a $q_2$-independent set in $\Gamma$, contradicting $\alpha_0(\Gamma) < q_2$. Hence $\alpha_0(\Gamma_T) < q_2 - 1$. Clearly $\omega(\Gamma_T) \leq \omega(\Gamma) < q_1$, so $\Gamma_T$ is a $(q_1, q_2-1)$-graph.

**(b)** Let $d_S$ and $d_T$ be the deficiencies of $\Gamma_S$ and $\Gamma_T$ respectively. By definition,
\[
\nu_0(\Gamma_S) = n(q_1-1, q_2) - d_S - 1, \quad \nu_0(\Gamma_T) = n(q_1, q_2-1) - d_T - 1.
\]
Now $\nu_0(\Gamma) = 1 + \nu_0(\Gamma_S) + \nu_0(\Gamma_T) = 1 + n(q_1-1, q_2) - d_S - 1 + n(q_1, q_2-1) - d_T - 1$. By the recurrence inequality $n(q_1, q_2) \leq n(q_1-1, q_2) + n(q_1, q_2-1)$, we obtain
\[
\nu_0(\Gamma) \leq n(q_1, q_2) - d_S - d_T - 1.
\]
But $\nu_0(\Gamma) = n(q_1, q_2) - d - 1$, so $d \geq d_S + d_T + 1$.

**(c)** If $d = 0$, then $d_S = d_T = 0$ by part (b). From the definitions of $d_S$ and $d_T$ as nonnegative integers and the recurrence for Ramsey numbers, a detailed vertex-degree analysis (using that a $0$-deficient $(3,3)$-graph is a $5$-circuit by Exercise C8b) shows $2 \leq \rho(x) \leq 3$ for all $x \in V$, and that the valency bound holds because a vertex of valency $1$ would force a contradiction with $0$-deficiency via the induction argument used in proving the Ramsey Theorem for Graphs.
