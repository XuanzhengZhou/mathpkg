---
role: proof
locale: en
of_concept: baire-category-theorem
source_book: gtm015
source_chapter: "V"
source_section: "46"
---

# Proof of the Baire Category Theorem

Let $X$ be a complete metric space with metric $d$. By hypothesis, $X = \bigcup_{1}^{\infty} A_n$, where $\operatorname{int}(\overline{A}_n) = \varnothing$ for all $n$. Replacing $A_n$ by the possibly larger sets $\overline{A}_n$ (which are also meager), it suffices to show that $X \setminus \bigcup_{1}^{\infty} \overline{A}_n$ is dense. Thus, changing notation, we can suppose that the $A_n$ are closed sets with $\operatorname{int}(A_n) = \varnothing$.

Note that if $U$ is any nonempty open set, then the open sets $U \cap (X \setminus A_n)$ are nonempty; indeed, $U \cap (X \setminus A_n) = \varnothing$ would imply $U \subset A_n$, contrary to $\operatorname{int}(A_n) = \varnothing$.

Let $V$ be any nonempty open set in $X$; it is to be shown that $V \cap (X \setminus \bigcup_{1}^{\infty} A_n) \neq \varnothing$, i.e., $\bigcap_{1}^{\infty} V \cap (X \setminus A_n) \neq \varnothing$. To this end, we construct a sequence $U_n$ of nonempty open sets such that:
(i) $\overline{U}_{n+1} \subset U_n \cap (X \setminus A_n)$,
(ii) $\operatorname{diam}(\overline{U}_n) < 1/n$.

Let $U_1$ be any nonempty open set with $\overline{U}_1 \subset V$ and $\operatorname{diam}(\overline{U}_1) < 1$ (e.g., $U_1$ can be a suitable open ball). Since $U_1 \cap (X \setminus A_1)$ is a nonempty open set, there exists a nonempty open set $U_2$ with $\overline{U}_2 \subset U_1 \cap (X \setminus A_1)$ and $\operatorname{diam}(\overline{U}_2) < 1/2$. Suppose, inductively, that $U_1, U_2, \ldots, U_n$ have been constructed. Then $U_n \cap (X \setminus A_n)$ is nonempty and open, so there exists a nonempty open set $U_{n+1}$ with $\overline{U}_{n+1} \subset U_n \cap (X \setminus A_n)$ and $\operatorname{diam}(\overline{U}_{n+1}) < 1/(n+1)$.

The decreasing sequence of closed sets $\overline{U}_n$ has diameters tending to $0$, so by completeness, $\bigcap_{1}^{\infty} \overline{U}_n$ consists of exactly one point $x$. From $\overline{U}_{n+1} \subset X \setminus A_n$ we have $x \notin A_n$ for all $n$, and from $\overline{U}_1 \subset V$ we have $x \in V$. Thus $x \in V \cap (X \setminus \bigcup_{1}^{\infty} A_n)$, completing the proof. $\square$
