---
role: proof
locale: en
of_concept: tychonoff-lemma
source_book: gtm027
source_chapter: "4"
source_section: "Existence of Continuous Functions"
---

# Proof of Tychonoff Lemma: Regular Lindelöf Spaces are Normal

Suppose $A$ and $B$ are closed disjoint subsets of $X$. Because $X$ is regular, for each point of $A$ there is a neighborhood whose closure fails to intersect $B$ and consequently the family $\mathfrak{u}$ of all open sets whose closures do not intersect $B$ is a cover of $A$. Similarly, the family $\mathfrak{v}$ of all open sets whose closures do not intersect $A$ is a cover of $B$, and $\mathfrak{u} \cup \mathfrak{v} \cup \{X \sim (A \cup B)\}$ is a cover of $X$.

Since $X$ is Lindelöf, this open cover has a countable subcover. There is then a sequence $\{U_n, n \in \omega\}$ of members of $\mathfrak{u}$ which covers $A$, and a sequence $\{V_n, n \in \omega\}$ of members of $\mathfrak{v}$ which covers $B$.

Let $U_n' = U_n \sim \bigcup \{V_p^{-}: p \leq n\}$ and let $V_n' = V_n \sim \bigcup \{U_p^{-}: p \leq n\}$. Then $U_n'$ and $V_n'$ are open sets, $U_n' \subset U_n$, and $V_n' \subset V_n$.

Define $U = \bigcup \{U_n': n \in \omega\}$ and $V = \bigcup \{V_n': n \in \omega\}$. Then $U$ and $V$ are open. Since each $U_n \in \mathfrak{u}$, we have $U_n^{-} \cap B = \varnothing$, and therefore $A \subset U$. Similarly $B \subset V$.

To show $U \cap V = \varnothing$, suppose $x \in U_m' \cap V_k'$ for some $m, k$. If $m \leq k$, then $x \in U_m' \subset U_m$, but $V_k' = V_k \sim \bigcup \{U_p^{-}: p \leq k\}$ and since $m \leq k$, we have $U_m^{-} \subset \bigcup \{U_p^{-}: p \leq k\}$, so $x \notin V_k'$, contradiction. If $k \leq m$, the symmetric argument yields a contradiction. Hence $U \cap V = \varnothing$.

Thus $U$ and $V$ are disjoint open neighborhoods of $A$ and $B$ respectively, proving $X$ is normal.
