---
role: proof
locale: en
of_concept: pointwise-convergence-not-metrizable
source_book: gtm036
source_chapter: "G"
source_section: "G"
---

Suppose that $\{U_{T_i, \varepsilon_i}\}_{i=1}^{\infty}$ is a countable local base for the topology of pointwise convergence on $E = C([0,1])$. Each $T_i$ is a finite subset of $S = [0,1]$, so the countable union $\bigcup_{i=1}^{\infty} T_i$ is at most countable. Since $S = [0,1]$ is uncountable, there exists a point $s \in S$ such that $s \notin \bigcup_{i=1}^{\infty} T_i$.

Consider the basic open neighborhood $U_{\{s\}, 1} = \{ x \in E : |x(s)| < 1 \}$. For any index $i$, since $s \notin T_i$, we can construct a continuous function $x \in E$ such that $x(t) = 0$ for all $t \in T_i$ but $x(s) \geq 1$ (for example, a "spike" function supported near $s$ that vanishes on $T_i$). Then $x \in U_{T_i, \varepsilon_i}$ but $x \notin U_{\{s\}, 1}$. Hence $U_{T_i, \varepsilon_i} \not\subseteq U_{\{s\}, 1}$ for every $i$.

Therefore no countable family of basic neighborhoods can form a local base, contradicting the assumption that the topology is first countable. Since every metrizable topology is first countable, the topology of pointwise convergence on $E$ cannot be metrizable.
