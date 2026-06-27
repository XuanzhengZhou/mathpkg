---
role: proof
locale: en
of_concept: subgraph-connectivity-reduction
source_book: gtm054
source_chapter: "VI"
source_section: "C"
---

**Vertex case.** If $\Gamma_{(x)}$ is complete, then $\kappa(\Gamma_{(x)}) = |V| - 2 \geq \kappa(\Gamma) - 1$ by C3. If $\Gamma_{(x)}$ is not complete, let $S \in \mathcal{P}_{m-2}(V \setminus \{x\})$. Since $|S \cup \{x\}| = m - 1$, the subgraph $(\Gamma_{(x)})_{(S)} = \Gamma_{(S \cup \{x\})}$ is connected (because $\Gamma$ is $m$-connected). Hence $\Gamma_{(x)}$ is $(m - 1)$-connected.

**Edge case.** Let $E = \{x, y\}$, and suppose that $\Gamma_{(E)}$ is not $(m - 1)$-connected. Since $\Gamma$ is $m$-connected, $|V| \geq m + 1$ by C3. Hence there exists $S \in \mathcal{P}_{m-2}(V)$ such that $\Gamma_{(S \cup \{E\})}$ is not connected. Select $a$ and $z$ in different components of $\Gamma_{(S \cup \{E\})}$. We may choose $\{a, z\} \neq \{x, y\}$, for otherwise $V = S \cup \{x, y\}$, which implies that $|V| \leq |S| + 2 = m$. We may suppose $x \notin \{a, z\}$. Now $S$ does not separate $z$ from $a$ in $\Gamma$. It follows that every $az$-path in $\Gamma$ must include $E$, and hence include $x$. But then $S \cup \{x\}$ separates $z$ from $a$ in $\Gamma$, and $|S \cup \{x\}| = m-1$, contradicting that $\Gamma$ is $m$-connected.
