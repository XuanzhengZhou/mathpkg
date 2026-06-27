---
role: exercise
locale: en
chapter: "1"
section: "2"
exercise_number: 2
---

Show that system-isomorphism is an equivalence relation.

Whenever $(V, f, E)$ and $(W, g, F)$ are isomorphic systems, then $f$ and $g$ are isomorphic functions. The converse of this statement is false, since a bijection from $\mathcal{P}(V)$ onto $\mathcal{P}(W)$ need not be induced by a bijection from $V$ onto $W$.

If $\Lambda = (V, f, E)$ is a system and if $f$ is an injection, then $\Lambda$ is called a set system. For example, if $\mathcal{E} \subseteq \mathcal{P}(K)$ and if the "inclusion function" $j: \mathcal{E} \rightarrow \mathcal{P}(V)$ is defined by $j(S) = S$ for each $S \in \mathcal{E}$, then $(V, j, \mathcal{E})$ is a set system. In this case, the function $j$ is suppressed and the set system is denoted simply by the pair $(V, \mathcal{E})$.

Let $(V, f, E)$ be any set system. Let $\mathcal{E} = f[E]$ and let $j: \mathcal{E} \rightarrow \mathcal{P}(V)$ be the inclusion function. Since $f$ is an injection, $f': E \rightarrow \mathcal{E}$ given by $f'(e) = f(e)$ for all $e \in E$ is a bijection. Then the pair $(f', 1_V)$ is a system-isomorphism between $(V, f, E)$ and $(V, \mathcal{E}) = (V, f[E])$.

If $V$ and $E$ are sets and $f: E \rightarrow \mathcal{P}(V)$, the function $f^*: V \rightarrow \mathcal{P}(E)$ given by $f^*(x) = \{e \in E: x \in f(e)\}$ is called the transpose of $f$. Since
