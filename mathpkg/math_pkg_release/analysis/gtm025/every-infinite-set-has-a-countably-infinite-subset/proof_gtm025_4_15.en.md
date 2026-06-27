---
role: proof
locale: en
of_concept: "every-infinite-set-has-a-countably-infinite-subset"
source_book: gtm025
source_chapter: "Unknown Chapter"
source_section: "4.15"
---

Let $A$ be any infinite set. We show by induction that for each $n \in N$ there exists a set $A_n \subset A$ such that $\bar{A}_n = n$. Indeed $A \neq \emptyset$ so there exists an $A_1 \subset A$. If $A_n \subset A$ and $\bar{A}_n = n$, then, since $A$ is infinite, there exists an element $x \in A \cap A'$. Letting $A_{n+1} = A_n \cup \{x\}$, we have $A_{n+1} \subset A$ and $\bar{A}_{n+1} = n + 1$.

Next let $\{A_n\}_{n \in N}$ be any family of subsets of $A$ as described above. [Notice the use of the axiom of choice in selecting this family.] For each $n \in N$, define

$$B_n = A_{2n} \cap \left( \bigcup_{k=0}^{n

Since each positive integer is a power of 2 [possibly the $0^{th}$ power] times an odd integer, $f$ is onto $N$. We see that $f$ is one-to-one, for otherwise there would be an integer which is both even and odd. $\square$
