---
role: proof
locale: en
of_concept: generators-contain-basis
source_book: gtm031
source_chapter: "IV"
source_section: "1-6"
---
Let $S$ be a set of generators for $\Re$. Let $P$ be the collection of linearly independent subsets of $S$. Then $P$ is a partially ordered set relative to the relation of inclusion. Let $L$ be a linearly ordered subcollection of $P$, and let $U$ be the logical sum of the sets belonging to $L$. We assert that $U$ is linearly independent. Otherwise $U$ contains a dependent set $u_1, u_2, \cdots, u_m$. Now $u_i \in A_i \in L$. Also for any $i, j$ either $A_i \subseteq A_j$ or $A_j \subseteq A_i$. Hence one of the $A$'s, say $A_m$, contains all the others. Thus every $u_i \in A_m$ and $A_m$ contains a finite linearly dependent subset. This contradicts the assumption that $A_m \in P$; hence $U \in P$. It is clear that this element serves as an upper bound for all the $A \in L$. We can now apply Zorn's lemma to conclude that $P$ contains a maximal element, and this means that the set of generators $S$ contains a maximal linearly independent subset $B$. It is now easy to see that $B$ is a basis for $\Re$. If $y$ is any member of $S$ not contained in $B$, then the set $B \cup \{y\}$ is a dependent set. This implies that $y$ is a linear combination of elements of $B$ (Lemma 1 on p. 11). Hence every $s \in S$ is a linear combination of elements of $B$. It follows that $B$ is a set of generators and, since $B$ is a linearly independent set, $B$ is, in fact, a basis.

