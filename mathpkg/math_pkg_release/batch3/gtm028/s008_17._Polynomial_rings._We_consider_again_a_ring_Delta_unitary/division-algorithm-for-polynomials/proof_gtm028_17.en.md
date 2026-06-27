---
role: proof
locale: en
of_concept: division-algorithm-for-polynomials
source_book: gtm028
source_chapter: "I"
source_section: "17"
---

**Proof.** If $\partial f < n$, we take $k = 0$, $q = 0$, $r = f$. Suppose $\partial f = m \geq n$ and let the leading term of $f$ be $a x^m$. Since $b_n$ is regular, we consider $b_n f(x) - a x^{m-n} g(x)$, whose degree is less than $m$. By induction on $m$, there exists $k$ and $q_1, r$ such that $b_n^k(b_n f - a x^{m-n} g) = q_1 g + r$ with $\partial r < n$. Then $b_n^{k+1} f = (a x^{m-n} b_n^k + q_1) g + r$, establishing existence.

Now suppose $b_n$ is regular and that we have also $b_n^{k'} f = q' g + r'$ with $\partial r' < n$. We may assume $k = k'$ by multiplying the equation with smaller $k$ by an appropriate power of $b_n$. Then $(q - q') g = r' - r$. If $q - q' \neq 0$, then the left side has degree at least $n$, since the leading coefficient of $g(x)$ is regular. But this is impossible since $\partial(r' - r) < n$. Hence $q - q' = 0$ and $r' - r = 0$.
