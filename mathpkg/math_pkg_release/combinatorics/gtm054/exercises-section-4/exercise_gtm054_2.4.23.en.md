---
role: exercise
locale: en
chapter: "2"
section: "4"
exercise_number: 23
---

(Sperner [s.7]). Show that any largest incommensurable subcollection of $\mathcal{P}(U)$ has cardinality

$$\begin{pmatrix} |U| \\ \left[ \frac{|U|}{2} \right] \end{pmatrix}$$

(Hint: Let $\mathcal{C}$ be the set of $(|U| + 1)$-chains in $(\mathcal{P}(U), \subseteq)$. For each $S \in \mathcal{P}(U)$, let $\mathcal{C}_S$ consist of those chains in $\mathcal{C}$ of which $S$ is an element. Begin by showing that if $S \subseteq \mathcal{P}(U)$ is incommensurable, then $|\mathcal{C}| \geq \sum_{S \in \mathcal{S}} |\mathcal{C}_S|$.

A pair $(V, D)$, where $V$ is a set and $D \subseteq (V \times V) + \{(v, v): v \in V\}$, is called a directed graph. The elements of $V$ are called vertices and the elements of $D$ are called edges. A sequence of vertices and edges of the form

$$v_0, (v_0, v_1), v

Now suppose $v \leq w$ and $w \leq v$. A repetition of the above construction yields a $vv$-path, and if $v \neq w$, this path will have positive length. Hence if $(V, D)$ is acyclic, then $\leq$ is antisymmetric. Conversely, if there exists a directed circuit through distinct vertices $v$ and $w$, then $v \leq w$ and $w \leq v$.

From the previous result we have that every acyclic directed graph uniquely determines a partially-ordered set. Conversely, every partially-ordered set can be obtained in this way. However, a given partially-ordered set may be determined by many different directed graphs. For let $(V, \leq)$ be a partially-ordered set and let $D = \{(v, w) \in V \times V : v \leq w\}$. Clearly $(V, D)$ is an acyclic directed graph which yields $(V, \leq)$ in the manner of the proof of the previous proposition. In this case, $(V, D)$ is the directed graph of $(V, \leq)$ which has the largest possible number of edges.

Given $(V, \leq)$, we say that $w$ is a successor of $v$ if $v < w$ and if $v \leq x \leq w$ implies $x = v$ or $x = w$.
