---
role: proof
locale: en
of_concept: subset-decomposition
source_book: gtm002
source_chapter: "1"
source_section: "1"
---
Let $E$ be any subset of $\mathbb{R}$. By the line decomposition theorem, there exists a partition $\mathbb{R} = A \cup B$ where $A$ is of first category and $B$ is a nullset, with $A \cap B = \emptyset$. Then
$$E = (E \cap A) \cup (E \cap B).$$

Now $E \cap A \subset A$, and since $A$ is of first category, the class of first category sets being a $\sigma$-ideal (closed under taking subsets) implies that $E \cap A$ is also of first category. Similarly, $E \cap B \subset B$, and since $B$ is a nullset and the class of nullsets is a $\sigma$-ideal, $E \cap B$ is also a nullset. Thus every subset of the line is the union of a nullset and a set of first category.
