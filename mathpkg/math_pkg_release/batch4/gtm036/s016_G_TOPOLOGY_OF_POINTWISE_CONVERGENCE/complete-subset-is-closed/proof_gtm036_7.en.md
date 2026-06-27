---
role: proof
locale: en
of_concept: complete-subset-is-closed
source_book: gtm036
source_chapter: "7"
source_section: ""
---

Let $A$ be a complete subset of a linear topological space $E$. Let $x \in \overline{A}$, the closure of $A$. There exists a net $\{x_\alpha\}_{\alpha \in D} \subset A$ such that $x_\alpha \to x$. Since every convergent net is a Cauchy net, $\{x_\alpha\}$ is a Cauchy net in $E$. Since $x_\alpha \in A$ for all $\alpha$, it is also a Cauchy net in $A$. By completeness of $A$, the Cauchy net converges to some point $a \in A$. Since the topology is Hausdorff (every linear topological space is assumed to have a Hausdorff vector topology, or limits are unique in a Hausdorff space), we must have $x = a$, so $x \in A$. Therefore $\overline{A} \subseteq A$, hence $A = \overline{A}$ and $A$ is closed.
