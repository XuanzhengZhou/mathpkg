---
role: exercise
locale: en
chapter: "1"
section: "2"
exercise_number: 6
---

Show that a system $\Lambda$ is “$T_1$” if and only if $\Lambda^*$ has the property that no block contains any other block.

A system of blocksize 2 is called a multigraph. If it is also a set system, it is called a graph. The blocks of a multigraph are called edges. Some mathematicians, taking the reverse approach from the one adopted here, have begun with a study of multigraphs and subsequently treated systems as generalizations of multigraphs. In particular, Berge [b.5] has defined the term hypergraph to denote a system $(V, f, E)$ with the two additional properties that $f(e) \neq \emptyset$ for all $e \in E$ and that $f^*(x) \neq \emptyset$ for all $x \in V$.

A graph $(V, \mathcal{E})$ is said to be bipartite if $|V| \leq 1$ or if there exists a partition $\{V_1, V_2\} \in \mathbb{P}_2(V)$ such that $|E \cap V_1| = |E \cap V_2| = 1$ for all $E \in \mathcal{E}$. If $(V, \mathcal{E})$ is a bipartite graph, the partition $\{V_1, V_2\}$ need not be unique. When we wish to specify the partition we shall write: $(V, \mathcal{E})$ is a bipartite graph with respect to

$M_1$ by row- or column-permutations. Clearly if $M$ is an incidence matrix for $\Lambda$, then the transpose of $M$ (denoted by $M^*$) is an incidence matrix for $\Lambda^*$.

A system $\Omega = (W, g, F)$ is a subsystem of the system $\Lambda = (V, f, E)$ if: $W \subseteq V, F \subseteq E$, and for all $e \in F$ it holds that $g(e) = f(e) \subseteq W$. For example, let $\Lambda = (V, f, E)$ and suppose $F \subseteq E$. Then $\Lambda_F = (W, g, F)$, where $W = \bigcup_{d \in F} f(d)$ and $g = f|_F$, is a subsystem of $\Lambda$. $\Lambda_F$ is called the subsystem induced by $F$. We let $\Lambda_{(F)} = (V, f|_{E+F}, E+F)$. If $W \subseteq V$, the subsystem induced by $W$ is the subsystem $\Lambda_W = (W, g, F)$ where $F = \{e \in E: f(e) \subseteq W\}$ and $g = f|_F$. We let $\Lambda_{(W)} = \Lambda_{V+W}$.
