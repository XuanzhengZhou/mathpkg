---
role: proof
locale: en
of_concept: matroid-fundamental-circuit-properties
source_book: gtm054
source_chapter: "X"
source_section: "B"
---

**Proof.**

**(a)** Let $B \in \mathcal{B}(\Lambda)$ and let $x \in V \setminus B$. Since $B \cup \{x\} \notin \mathcal{I}(\Lambda)$, there exists $M_x \in \mathcal{M}$ such that $M_x \subseteq B \cup \{x\}$ by Proposition B19. Since $M_x \not\subseteq B$, we must have $x \in M_x$. Now suppose that $x \in M \subseteq B \cup \{x\}$ for some $M \in \mathcal{M}$. If $M \neq M_x$, then $(M, M_x, x)$ is an admissible triple. By the cycle exchange property, there exists $M' \in \mathcal{M}$ such that $M' \subseteq (M \cup M_x) \setminus \{x\} \subseteq B$, which is impossible since $B$ is independent and no cycle is contained in an independent set. Hence $M = M_x$, establishing uniqueness.

**(b)** Let $M \in \mathcal{M}$ and let $x \in M$. Then $M \setminus \{x\} \in \mathcal{I}(\Lambda)$, and hence $M \setminus \{x\} \subseteq B_x$ for some $B_x \in \mathcal{B}(\Lambda)$. Since $M$ is a cycle (minimal dependent set) and $M \not\subseteq B_x$ (otherwise $M$ would be contained in the independent set $B_x$), we have $x \notin B_x$. Hence $M \subseteq B_x \cup \{x\}$.

**(c)** Let $S \in \mathcal{P}(V)$. 

($\Rightarrow$) Suppose $S \in \mathcal{S}(\Lambda)$ and let $x \in V \setminus S$. Then $S \cup \{x\}$ contains a basis $B$. Since $x \notin S$, we have $B \not\subseteq S$, so $x \in B$. By part (a), there exists a unique cycle $M_x \in \mathcal{M}$ such that $x \in M_x \subseteq B \cup \{x\}$. Since $B \subseteq S \cup \{x\}$, we have $M_x \subseteq S \cup \{x\}$.

($\Leftarrow$) Conversely, suppose to each $x \in V \setminus S$ there corresponds a cycle $M_x$ such that $x \in M_x \subseteq S \cup \{x\}$. Let $B$ be a maximal independent subset of $S$. If $B \notin \mathcal{B}(\Lambda)$, there exists $x \in V \setminus S$ such that $B \cup \{x\} \in \mathcal{I}(\Lambda)$. But then $M_x \subseteq S \cup \{x\}$ and $M_x \setminus \{x\} \subseteq S$ is independent, so $M_x \setminus \{x\}$ can be extended to a maximal independent subset of $S \cup \{x\}$ containing $x$, implying $B \cup \{x\}$ is independent and larger than $B$ within $S$ — contradiction to maximality. Hence $B \in \mathcal{B}(\Lambda)$ and $S \supseteq B$, so $S \in \mathcal{S}(\Lambda)$. $\square$
