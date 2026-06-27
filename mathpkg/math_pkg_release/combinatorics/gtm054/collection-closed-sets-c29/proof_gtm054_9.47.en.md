---
role: proof
locale: en
of_concept: collection-closed-sets-c29
source_book: gtm054
source_chapter: "9"
source_section: "XD"
---

Suppose that $U_2$ is a successor of $U_1$ and choose $x \in U_2 + U_1$. Since $U_1 + \{x\} \subseteq U_2$, we have $U_1 \subset c(U_1 + \{x\}) \subseteq c(U_2) = U_2$. Since $U_2$ is a successor of $U_1$, we cannot have $c(U_1 + \{x\}) \subseteq U_2$.

Conversely, suppose that $U_2 = c(U_1 + \{x_1\})$ for some $x_1 \in U_2 + U_1$. We must show that if $

$c(\{x\})$. For any $y \in U + c(\varnothing)$, we have $c(\varnothing) < c(\{y\}) \leq c(\{x\})$. Thus $y \in c(\varnothing + \{x\})$ and $y \notin c(\varnothing)$. By C11, $x \in c(\{y\})$ and so $c(\{x\}) = c(\{y\})$. If $U \in \mathcal{C}$, then by C10, $c(\{x\}) \subseteq U$ for all $x \in U$. Thus $U = c(\varnothing) + \bigcup_{x \in U + c(\varnothing)} \{x\} = \bigcup_{x \in U + c(\varnothing)} c(\{x\}) = c(\bigcup_{x \in U + c(\varnothing)} c(\{x\})) = \bigvee_{x \in U + c(\varnothing)} c(\{x\})$. Thus each element of $\mathcal{C}$ is the join of a set of atoms.

To prove semimodularity, let $U_1, U_2 \in \mathcal{C}$ be distinct successors of $U = U_1 \cap U_2$. By C29, there exists $x_i \in U_i + U$ such that $U_i = c(U + \{x_i\})$ for $i = 1, 2$. Suppose $x_1 \in U_2$. Then $U \subset U_1 = c(U + \{x_1\}) \subseteq c(U_2) = U_2$, and since $U_2$ is a successor of $U$, we have $U_2 = U_1$, contrary to assumption. Thus $x_1 \notin U_2$ and similarly $x_2 \notin U_1$. By C29 again, $c(U_1 + \{x_2\}) = c(U + \{x_1, x_2\}) = c(U_2 + \{x_1\})$ is a successor of both $U_1$ and
