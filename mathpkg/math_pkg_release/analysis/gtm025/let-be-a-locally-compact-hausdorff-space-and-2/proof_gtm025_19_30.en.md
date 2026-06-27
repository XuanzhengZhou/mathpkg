---
role: proof
locale: en
of_concept: "let-be-a-locally-compact-hausdorff-space-and-2"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.30"
---

Let $\mathfrak{X}$ be the collection of all families $\mathcal{F}$ of subsets of $X$ enjoying the following properties:

(1) the sets in $\mathcal{F}$ are compact and have positive $\iota$-measure;

(2) the sets in $\mathcal{F}$ are pairwise disjoint;

(3) if $F \in \mathcal{F}$ and $U$ is an open subset of $X$ for which $U \cap F \neq \emptyset$, then $\iota(U \cap F) \neq 0$.

Clearly $\

and (10.31) implies that $U \cap F_0$ and $(U \cap F_0)' = D$ are $\iota$-measurable. Up to this point in the proof, we have not needed the maximality of $F_0$. To prove that $D$ is locally $\iota$-null, we need this property. If $D$ is not locally $\iota$-null, then by definition there is a compact set $C$ such that $\iota(C \cap D) > 0$, and from (10.30) and the fact that $D$ is $\iota$-measurable, we infer the existence of a compact set $H$ such that $H \subset C \cap D$ and $\iota(H) > 0$. Consider the family $U$ of all open sets $U$ such that $\iota(U \cap H) = 0$. Then $\iota(H \cap (U \cup U)) = 0$, for otherwise $H \cap (U \cup U)$ would contain a compact set $E$ of positive $\iota$-measure (10.30), and $E$ would be covered by a finite number of sets $U \cap H$, each of zero $\iota$-measure. The set $H \cap (U \cup U)'$ is compact and contained in $D$, and

$$\iota(H \cap (U \cup U))' = \iota(H) - \iota(H \cap (U \cup U)) = \iota(H) > 0.$$

Also if $V$ is open and $V \cap H \cap (U \cup U)' \neq \varnothing$, then $V \notin U$, so that

$$\iota(V \cap H \cap (U \cup U')) = \iota(V \cap H) - \iota(V \cap H \cap (U \cup U)) = \iota(V \cap H) > 0.$$

Therefore we can adjoin $H \cap (U \cup U)'$ to $F_0$ and still preserve properties (1)–(3). This contradicts the maximality of $F_0$.

It remains only to prove (vi), to do which we appeal to (10

We now present our version of the LEBESGUE-RADON-NIKODYM theorem for locally compact Hausdorff spaces.
