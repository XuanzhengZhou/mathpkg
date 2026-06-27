---
role: proof
locale: en
of_concept: chern-forms-are-closed
source_book: gtm020
source_chapter: "Appendix B"
source_section: "B.3"
---
First, we compute $d\,\text{Tr}(K^q)$ using the derivation property. Since $K$ is a matrix of $2$-forms, the graded Leibniz rule gives:
$$
d\,\text{Tr}(K^q) = \sum_{i+j=q-1} \text{Tr}(K^i (dK) K^j).
$$
By the Bianchi identity, $dK = [\theta, K] = \theta \wedge K - K \wedge \theta$. Substituting:
\begin{align*}
d\,\text{Tr}(K^q) &= \sum_{i+j=q-1} \text{Tr}(K^i (\theta \wedge K - K \wedge \theta) K^j) \\
&= \sum_{i+j=q-1} \left[\text{Tr}(K^i \theta \wedge K^{j+1}) - \text{Tr}(K^{i+1} \wedge \theta K^j)\right].
\end{align*}
Using the cyclic property of the trace and reindexing the second sum, the terms cancel pairwise, giving $d\,\text{Tr}(K^q) = 0$. 

Over a field of characteristic zero, every invariant polynomial $\phi \in \text{Inv}(n)$ can be expressed as a polynomial in the traces $\text{Tr}(X), \text{Tr}(X^2), \ldots, \text{Tr}(X^n)$. Since each $\text{Tr}(K^q)$ is closed and the exterior derivative is a derivation, it follows that $\phi(K)$ is closed for all invariant polynomials $\phi$. In particular, the Chern polynomials $c_q$ are invariant, so $c_q(K)$, and thus $c_q(E, \nabla) = \frac{1}{(2\pi i)^q} c_q(K)$, are closed.
