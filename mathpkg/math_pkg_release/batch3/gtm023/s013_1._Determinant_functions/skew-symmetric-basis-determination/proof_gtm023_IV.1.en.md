---
role: proof
locale: en
of_concept: skew-symmetric-basis-determination
source_book: gtm023
source_chapter: "IV"
source_section: "§1. Determinant functions"
---

Choose a basis $a_1, \ldots, a_n$ of $E$ and write
$$x_\lambda = \sum_{v=1}^{n} \xi_\lambda^v a_v \quad (\lambda = 1, \ldots, n).$$
By $n$-linearity,
$$\Phi(x_1, \ldots, x_n) = \sum_{v_1, \ldots, v_n} \xi_1^{v_1} \cdots \xi_n^{v_n} \Phi(a_{v_1}, \ldots, a_{v_n}).$$
In the sum over all $n$-tuples $(v_1, \ldots, v_n)$, only those where all indices are distinct can contribute (otherwise, by skew symmetry, $\Phi(a_{v_1},\ldots,a_{v_n}) = 0$). Hence the nonzero terms correspond precisely to permutations $\sigma \in S_n$, giving
\begin{align*}
\Phi(x_1, \ldots, x_n) &= \sum_{\sigma \in S_n} \xi_1^{\sigma(1)} \cdots \xi_n^{\sigma(n)} \Phi(a_{\sigma(1)}, \ldots, a_{\sigma(n)}) \\
&= \left( \sum_{\sigma \in S_n} \varepsilon_\sigma \xi_1^{\sigma(1)} \cdots \xi_n^{\sigma(n)} \right) \cdot \Phi(a_1, \ldots, a_n).
\end{align*}
The factor in parentheses is the determinant of the coefficient matrix $(\xi_\lambda^v)$ and does not depend on $\Phi$. Therefore $\Phi(x_1,\ldots,x_n)$ is completely determined by the single value $\Phi(a_1,\ldots,a_n)$. In particular, if $\Phi(a_1,\ldots,a_n) = 0$, then $\Phi = 0$ everywhere.
