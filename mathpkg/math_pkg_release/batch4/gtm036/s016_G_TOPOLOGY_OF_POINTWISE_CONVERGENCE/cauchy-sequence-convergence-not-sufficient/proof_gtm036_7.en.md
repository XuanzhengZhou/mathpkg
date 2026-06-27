---
role: proof
locale: en
of_concept: cauchy-sequence-convergence-not-sufficient
source_book: gtm036
source_chapter: "7"
source_section: ""
---

Let $E = \prod_{t \in (0,1)} \mathbb{R}$ with the product topology (topology of pointwise convergence). Each factor $\mathbb{R}$ is complete, so the product $E$ is complete. Define
$$
F = \{ f \in E : f(t) = 0 \text{ for all but countably many } t \in (0,1) \}.
$$

**$F$ is dense in $E$:** For any $g \in E$ and any basic open neighborhood $U = \prod_{t} U_t$ where only finitely many coordinates $t_1, \ldots, t_n$ are restricted, define $f \in F$ by $f(t_i) = g(t_i)$ for $i = 1, \ldots, n$ and $f(t) = 0$ otherwise. Then $f \in U \cap F$, proving density.

**Every Cauchy sequence in $F$ converges in $F$:** Let $\{f_n\} \subset F$ be a Cauchy sequence. For each $t \in (0,1)$, $\{f_n(t)\}$ is a Cauchy sequence in $\mathbb{R}$, hence converges to some limit $f(t)$. The limit function $f$ belongs to $E$. Each $f_n$ vanishes outside a countable set $C_n$, so $f$ vanishes outside $\bigcup_n C_n$, which is a countable union of countable sets, hence countable. Thus $f \in F$. Since the product topology is the topology of pointwise convergence, $f_n \to f$ in $E$, hence in $F$.

**$F$ is not complete:** Since $F$ is a proper dense subspace of the Hausdorff space $E$, it cannot be closed in $E$. But a complete subset of a Hausdorff space must be closed. Therefore $F$ is not complete. Explicitly, a Cauchy net in $F$ converging to a limit in $E \setminus F$ is given by the net of restrictions to finite subsets: for each finite $I \subset (0,1)$, define $f_I \in F$ as the characteristic function of $I$; this net is Cauchy in $F$ but converges in $E$ to the constant function $1$, which is not in $F$.
