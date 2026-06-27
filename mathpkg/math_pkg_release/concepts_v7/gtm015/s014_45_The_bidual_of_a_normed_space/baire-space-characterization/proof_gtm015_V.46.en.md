---
role: proof
locale: en
of_concept: baire-space-characterization
source_book: gtm015
source_chapter: "V"
source_section: "46"
---

# Proof of Characterizations of Baire Spaces

Let $X$ be a topological space. The conditions are:
(a) The complement of every meager subset of $X$ is dense in $X$.
(b) Every nonempty open subset of $X$ is nonmeager.
(c) The intersection of any countable family of dense open sets is dense.
(d) If $(F_n)$ is a countable family of closed sets with $\bigcup F_n$ having nonempty interior, then at least one $F_n$ has nonempty interior.

**(a) $\Rightarrow$ (b):** Let $U$ be a nonempty open set. If $U$ were meager, then $X \setminus U$ would be dense (by (a)), but $U \cap (X \setminus U) = \varnothing$, contradicting that a dense set meets every nonempty open set.

**(b) $\Rightarrow$ (c):** Let $(G_n)$ be a countable family of dense open sets. Suppose $\bigcap G_n$ is not dense. Then there exists a nonempty open set $U$ with $U \cap \bigcap G_n = \varnothing$, i.e., $U \subset \bigcup (X \setminus G_n)$. Each $X \setminus G_n$ is closed with empty interior (since $G_n$ is dense open), so the complement is a meager set. But then $U$ is contained in a meager set, hence $U$ is meager, contradicting (b).

**(c) $\Rightarrow$ (d):** Let $(F_n)$ be closed sets with $\bigcup F_n$ having nonempty interior. Let $G_n = X \setminus F_n$. If every $F_n$ had empty interior, then each $G_n$ would be dense open. By (c), $\bigcap G_n$ is dense. But $\bigcap G_n = X \setminus \bigcup F_n$, so $X \setminus \bigcup F_n$ is dense, contradicting that $\bigcup F_n$ has nonempty interior. Thus some $F_n$ has nonempty interior.

**(d) $\Rightarrow$ (a):** Let $A$ be meager: $A = \bigcup A_n$ with $\overline{A_n}$ having empty interior for each $n$. Let $F_n = \overline{A_n}$. Then each $F_n$ is closed with empty interior. By the contrapositive of (d), $\bigcup F_n = \bigcup \overline{A_n}$ has empty interior. Thus $X \setminus \bigcup \overline{A_n}$ is dense, and since $X \setminus \bigcup \overline{A_n} \subset X \setminus A$, $X \setminus A$ is dense. $\square$
