---
role: proof
locale: en
of_concept: universal-function-not-in-closed-class
source_book: gtm037
source_chapter: "3"
source_section: "3.1"
---

Assume that $f \in A$. Define a unary function $g$ by

$$gm = f(m, m) + 1$$

for all $m \in \omega$. Since $A$ is closed under elementary recursive operations (in particular under composition), and $f \in A$, we have $g \in A$. Now, since $f$ is universal for unary members of $A$, there exists $m \in \omega$ such that $f(m, n) = gn$ for all $n \in \omega$. Evaluating at $n = m$ gives

$$gm = f(m, m) = f(m, m) + 1,$$

which is a contradiction. Therefore $f \notin A$.
