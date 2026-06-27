---
role: proof
locale: en
of_concept: empty-set-properties
source_book: gtm001
source_chapter: "5"
source_section: "5"
---

(1) Since $(\forall x)[x = x]$ holds for every individual, no $x$ satisfies $x \neq x$. By Definition 5.14, $0 = \{x \mid x \neq x\}$, hence $(\forall x)[x \notin 0]$.

(2) By definition of class inequality,

$$a \neq 0 \leftrightarrow (\exists x)[x \in 0 \land x \notin a] \lor (\exists x)[x \in a \land x \notin 0].$$

From part (1), we have $(\forall x)[x \notin 0]$, so the first disjunct $(\exists x)[x \in 0 \land x \notin a]$ is false. The second disjunct $(\exists x)[x \in a \land x \notin 0]$ simplifies to $(\exists x)[x \in a]$ since $x \notin 0$ is always true by part (1). Therefore

$$a \neq 0 \leftrightarrow (\exists x)[x \in a].$$
