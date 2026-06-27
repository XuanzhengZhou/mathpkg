---
role: proof
locale: en
of_concept: subset-criterion-by-continuous-linear-forms
source_book: gtm015
source_chapter: "3"
source_section: "34"
---

# Proof of Criterion for subset inclusion via continuous linear forms

Let $E$ be a locally convex TVS over $\mathbb{R}$, $A$ a nonempty closed convex set in $E$, and $S$ a subset of $E$. In order that $S \subset A$ it is necessary and sufficient that $g(S) \subset g(A)$ for every continuous linear form $g$ on $E$.

The necessity of the condition is trivial: if $S \subset A$, then $g(S) \subset g(A)$ for any function $g$.

Conversely, suppose the condition holds. If $b \notin A$, then by (34.3) there exist a continuous linear form $g$ and a real number $\beta$, such that $g \le \beta$ on $A$ and $g(b) > \beta$, and therefore $g(b) \notin g(A)$. Since $g(S) \subset g(A)$ by hypothesis, it follows that $b \notin S$. Thus $\complement A \subset \complement S$, i.e., $S \subset A$.
