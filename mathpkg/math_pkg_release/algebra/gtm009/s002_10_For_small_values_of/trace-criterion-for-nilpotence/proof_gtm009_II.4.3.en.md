---
role: proof
locale: en
of_concept: trace-criterion-for-nilpotence
source_book: gtm009
source_chapter: "II"
source_section: "4.3"
---
Let $x = s + n$ ($s = x_s$, $n = x_n$) be the Jordan decomposition of $x$. Choose a basis of $V$ so that $s$ is diagonal: $s = \operatorname{diag}(a_1, \ldots, a_m)$. We need to show that the $F$-vector subspace $E$ of $F$ spanned by the $a_i$ is zero. If not, let $f: E \to F$ be any nonzero $F$-linear map. Define $y \in \operatorname{End} V$ by $y = \operatorname{diag}(f(a_1), \ldots, f(a_m))$ with respect to the same basis. Since $s = x_s$ is a polynomial in $x$ with zero constant term, and $s$ is diagonal in this basis, one can verify that $[y, B] \subset A$, i.e., $y \in M$.

Now compute $\operatorname{Tr}(xy) = \sum_i a_i f(a_i) + \operatorname{Tr}(ny) = \sum_i a_i f(a_i)$, since $n$ is nilpotent and commutes with $y$, so their product is nilpotent with zero trace. But $\sum_i a_i f(a_i) \neq 0$ by choice of $f$ (take $f$ to be the projection onto a basis element of $E$). This contradicts the hypothesis $\operatorname{Tr}(xy) = 0$ for all $y \in M$. Hence $E = 0$, so all $a_i = 0$, meaning $x = n$ is nilpotent.
