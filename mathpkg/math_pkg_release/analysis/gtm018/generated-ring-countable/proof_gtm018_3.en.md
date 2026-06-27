---
role: proof
locale: en
of_concept: generated-ring-countable
source_book: gtm018
source_chapter: "I"
source_section: "3"
---

For any class $\mathbf{C}$ of sets, write $\mathbf{C}^*$ for the class of all finite unions of differences of sets of $\mathbf{C}$. If $\mathbf{C}$ is countable, then $\mathbf{C}^*$ is countable, and if $0 \in \mathbf{C}$, then $\mathbf{C} \subset \mathbf{C}^*$.

Assume without loss of generality that $0 \in \mathbf{E}$ (adjoin the empty set if necessary; this does not affect countability). Define

$$\mathbf{E}_0 = \mathbf{E}, \quad \mathbf{E}_n = \mathbf{E}_{n-1}^*, \quad n = 1, 2, \dots.$$

It is clear that

$$\mathbf{E} \subset \bigcup_{n=0}^{\infty} \mathbf{E}_n \subset \mathbf{R}(\mathbf{E}),$$

and that the class $\bigcup_{n=0}^{\infty} \mathbf{E}_n$ is countable (it is a countable union of countable classes). We complete the proof by showing that $\bigcup_{n=0}^{\infty} \mathbf{E}_n$ is a ring.

Since $\mathbf{E} = \mathbf{E}_0 \subset \mathbf{E}_1 \subset \mathbf{E}_2 \subset \cdots$, for any two sets $A$ and $B$ in $\bigcup_{n=0}^{\infty} \mathbf{E}_n$ there exists a positive integer $n$ such that both $A$ and $B$ belong to $\mathbf{E}_n$. Then

$$A - B \in \mathbf{E}_{n+1} = \mathbf{E}_n^*,$$

and, since $0 \in \mathbf{E}_0 \subset \mathbf{E}_n$,

$$A \cup B = (A - 0) \cup (B - 0) \in \mathbf{E}_n^* = \mathbf{E}_{n+1}.$$

Thus both $A - B$ and $A \cup B$ belong to $\bigcup_{n=0}^{\infty} \mathbf{E}_n$, proving that $\bigcup_{n=0}^{\infty} \mathbf{E}_n$ is closed under the formation of unions and differences, i.e., it is a ring. Since this ring contains $\mathbf{E}$ and is contained in $\mathbf{R}(\mathbf{E})$, it must equal $\mathbf{R}(\mathbf{E})$, which is therefore countable.
