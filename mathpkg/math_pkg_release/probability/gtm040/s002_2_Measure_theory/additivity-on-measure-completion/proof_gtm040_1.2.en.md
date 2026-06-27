---
role: proof
locale: en
of_concept: additivity-on-measure-completion
source_book: gtm040
source_chapter: "1"
source_section: "2"
---
Let $A$ and $B$ be disjoint sets in $\mathcal{F}^*$ and pick $\{A_n\}$ and $\{B_n\}$ in $\mathcal{F}$ such that $A_n \to A$ and $B_n \to B$. Then since $\nu$ is additive on $\mathcal{F}$ and since $\mu$ agrees with $\nu$ on sets of $\mathcal{F}$, we have
$$\mu(A_n \cup B_n) + \mu(A_n \cap B_n) = \mu(A_n) + \mu(B_n).$$
By Lemma 1-25,
$$\mu(A \cup B) + \mu(A \cap B) = \mu(A) + \mu(B).$$
Since $A$ and $B$ are disjoint, $A \cap B = \varnothing$ and $\mu(\varnothing) = 0$, hence
$$\mu(A \cup B) = \mu(A) + \mu(B).$$
