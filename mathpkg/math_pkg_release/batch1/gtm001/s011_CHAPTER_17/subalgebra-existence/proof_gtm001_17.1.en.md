---
role: proof
locale: en
of_concept: subalgebra-existence
source_book: gtm001
source_chapter: "17"
source_section: "17.1"
---

By induction on $n$, we define $\alpha_n$ and $Y_n$ as follows:

$$Y_0 = X$$
$$\alpha_n = \sup \{ \alpha + 1 \mid \alpha \in Y_n \cap \text{On} \}$$

and $Y_{n+1}$ is a subalgebra of $M^\lambda$ of cardinality less than $\kappa$ which contains $Y_n$ and is closed under all operations of $M^\lambda$ applied to arguments from $Y_n$. Set

$$Y = \bigcup_{n < \omega} Y_n.$$

Since $\kappa$ is regular and uncountable, the countable union of sets of cardinality less than $\kappa$ has cardinality less than $\kappa$, so $\overline{Y} < \kappa$. By construction $X \subseteq Y$ and $Y$ is a subalgebra of $M^\lambda$. Moreover $Y \cap \kappa = \bigcup_n (Y_n \cap \kappa)$, and each $Y_n \cap \kappa$ is an ordinal less than $\kappa$, so their supremum is also less than $\kappa$ by regularity. Thus $Y \cap \kappa \in \kappa$.
