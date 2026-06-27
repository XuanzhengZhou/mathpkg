---
role: proof
locale: en
of_concept: infinite-set-has-countable-subset
source_book: gtm025
source_chapter: "1"
source_section: "4"
---
By induction, for each \(n \in N\) there exists \(A_n \subset A\) with \(\overline{A_n} = n\). Using the Axiom of Choice to select this family, define \(B_n = A_{2n} \setminus \bigcup_{k=0}^{n-1} A_{2k}\). Then \(\{B_n\}_{n=1}^{\infty}\) is a pairwise disjoint family of nonvoid finite sets, and \(\bigcup_{n=1}^{\infty} B_n\) is countably infinite.