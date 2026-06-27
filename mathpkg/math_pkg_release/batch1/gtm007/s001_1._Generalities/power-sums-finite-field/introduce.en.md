---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This lemma computes the sum of the $u$-th powers of all elements in a finite field $K$ of order $q$. If $u = 0$, the sum is $q \cdot 1 = 0$ (since $\operatorname{char}(K) = p$). If $u \geq 1$ is a multiple of $q-1$, every nonzero element satisfies $x^u = 1$ by the cyclicity of $K^*$, giving $S(X^u) = -1$. Otherwise, picking $y \in K^*$ with $y^u \neq 1$ shows $S(X^u) = y^u S(X^u)$, forcing $S(X^u) = 0$. This result is a fundamental tool for evaluating polynomial sums over finite fields.
