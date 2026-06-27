---
role: proof
locale: en
of_concept: "the-space-with-its-usual-topology-is-connected"
source_book: gtm025
source_chapter: "Topology"
source_section: "6.9"
---

Let $A$ be a nonvoid subset of $R$ which is both open and closed. Assume that $A \neq R$ and let $c \in R \cap A'$. Since $A \neq \emptyset$, we have either $A \cap ] - \infty, c [ \neq \emptyset$ or $A \cap ] c, \infty [ \neq \emptyset$. Suppose that $B = A \cap ] - \infty, c [ \neq \emptyset$ and let $a$ be the supremum of this set (5.33). It is clear that $a \leq c$. If $\varepsilon > 0$, then $a - \varepsilon$ is not an upper bound for $B$, and so there is some $x \in B$ such that $a - \varepsilon < x \leq a$. This proves that every neighborhood of $a$ meets $A$ so, since $A$ is closed, $a$ is in $A$. Since $A$ is open, there is a $\delta > 0$ such that $] a - \delta, a + \delta [ \subset A$. Choose any $b \in R$ such that $a < b < \min \{a + \delta, c\}$. [Note that $a \neq c$ since $c \in A'$.] It follows that $b \in A$ and $b < c$, so that $b \in B$. The inequality $b > a$ contradicts the choice of $a$. A similar contradiction is obtained if $A \cap ] c, \infty [ \neq \emptyset$. We are thus forced to the conclusion that $A = R$.

It is often convenient to define a topology not by specifying all of the open sets but only some of them.
