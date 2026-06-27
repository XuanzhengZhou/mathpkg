---
role: proof
locale: en
of_concept: lebesgue-covering-lemma
source_book: gtm027
source_chapter: "5"
source_section: "Lebesgue's Covering Lemma"
---

# Proof of Lebesgue's Covering Lemma

**Theorem 26 (Lebesgue's Covering Lemma).** If $\mathcal{U}$ is an open cover of a compact subset $A$ of a pseudo-metric space $(X, d)$, then there is a positive number $r$ such that the open $r$-sphere about each point of $A$ is contained in some member of $\mathcal{U}$.

*Proof.* Let $\{U_1, \dots, U_n\}$ be a finite subcover of the open cover $\mathcal{U}$ of $A$ (using compactness). For each $i = 1, \dots, n$ and each $x \in X$, define

$$f_i(x) = d(x, X \setminus U_i) = \inf\{d(x, y) : y \in X \setminus U_i\},$$

with the convention that $d(x, \emptyset) = +\infty$ if $U_i = X$. Each $f_i$ is a continuous function on $X$ (the distance to a fixed set is continuous in a pseudo-metric space). For each $x \in A$, there exists some $i$ such that $x \in U_i$, and since $U_i$ is open, $x$ is not in the closure of $X \setminus U_i$, hence $f_i(x) > 0$.

Now define $f(x) = \max\{f_1(x), \dots, f_n(x)\}$ for $x \in X$. Then $f$ is continuous (maximum of finitely many continuous functions). For each $x \in A$, $f(x) \geq f_i(x) > 0$ for the index $i$ with $x \in U_i$. Hence $f[A]$ is a compact subset of the positive real numbers (since $A$ is compact and $f$ is continuous). Consequently, there exists a positive real number $r$ such that $f(x) > r$ for all $x \in A$.

Now fix any $x \in A$. Since $f(x) > r$, there is some index $i$ such that $f_i(x) > r$. This means $d(x, X \setminus U_i) > r$, which implies that every point $y$ with $d(x, y) < r$ satisfies $y \notin X \setminus U_i$, i.e., $y \in U_i$. Thus the open $r$-sphere about $x$ is contained in $U_i$, which is a member of $\mathcal{U}$. $\square$
