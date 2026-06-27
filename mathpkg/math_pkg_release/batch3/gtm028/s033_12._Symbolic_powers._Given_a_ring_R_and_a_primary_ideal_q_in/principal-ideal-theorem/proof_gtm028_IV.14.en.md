---
role: proof
locale: en
of_concept: principal-ideal-theorem
source_book: gtm028
source_chapter: "IV"
source_section: "14"
---

The second assertion follows from the characterization of isolated prime ideals of an ideal (Theorem 7, §5): it suffices to take for $a$ any non-zero element of $\mathfrak{p}$.

For the first assertion, by passage to the quotient ring $R_{\mathfrak{p}}$ (Theorem 19, §11) we may suppose that $\mathfrak{p}$ is a maximal ideal, and that every element outside of $\mathfrak{p}$ is a unit in $R$. Suppose there exists a proper prime ideal $\mathfrak{v}$ in $R$ such that $\mathfrak{v} \subsetneq \mathfrak{p}$. Consider the infinite strictly decreasing sequence $\mathfrak{q}_1 \supsetneq \mathfrak{q}_2 \supsetneq \mathfrak{q}_3 \supsetneq \cdots$ of primary ideals belonging to $\mathfrak{v}$, where $\mathfrak{q}_n = \mathfrak{v}^{(n)}$ is the $n$-th symbolic power of $\mathfrak{v}$. By the properties of symbolic powers, we obtain:
$$\mathfrak{q}_n = \mathfrak{q}_{n+1} + \mathfrak{q}_n a.$$

Pass to the residue class ring $R' = R/\mathfrak{q}_{n+1}$, denote by $a'$ the residue class of $a$, and by $\mathfrak{q}'$ the ideal $\mathfrak{q}_n/\mathfrak{q}_{n+1} \neq (0)$. The equality above gives $\mathfrak{q}' = \mathfrak{q}'a'$. Using Lemma 2 of §7, there exists an element $x'$ in $R'$ such that $(1 - x'a')\mathfrak{q}' = (0)$. By hypothesis on $R$, $R'$ admits a unique maximal ideal, and $a'$ belongs to that ideal; thus $1 - x'a'$ is a unit in $R'$, and we have $\mathfrak{q}' = (0)$---a contradiction.

Alternatively, one may use the determinant method: if $\{x_1, \ldots, x_s\}$ is a finite basis of $\mathfrak{q}_n$, there exist $y_i \in \mathfrak{q}_{n+1}$ and $z_{ij} \in R$ such that $x_i = y_i + \sum_j a z_{ij} x_j$, i.e., $\sum_j (\delta_{ij} - a z_{ij}) x_j \in \mathfrak{q}_{n+1}$. Let $d = \det(\delta_{ij} - a z_{ij})$. Then $d x_j \in \mathfrak{q}_{n+1}$, so $d \mathfrak{q}_n \subset \mathfrak{q}_{n+1}$. But $d = 1 - ba$ for some $b \in R$, hence $d$ is a unit, yielding $\mathfrak{q}_n \subset \mathfrak{q}_{n+1}$, contradiction.
