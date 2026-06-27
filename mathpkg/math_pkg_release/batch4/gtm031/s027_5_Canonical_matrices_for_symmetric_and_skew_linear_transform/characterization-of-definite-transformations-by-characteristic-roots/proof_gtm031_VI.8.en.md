---
role: proof
locale: en
of_concept: characterization-of-definite-transformations-by-characteristic-roots
source_book: gtm031
source_chapter: "VI"
source_section: "8"
---

By Theorem 4, since $A$ is symmetric there exists a Cartesian basis $(y_1, \ldots, y_n)$ such that $y_i A = \rho_i y_i$. Write any vector as $x = \sum_{i=1}^n \xi_i y_i$. Then

$$\begin{align*}
(xA, x) &= \left( \sum_{i=1}^{n} \xi_i y_i A, \sum_{j=1}^{n} \xi_j y_j \right) \\
&= \left( \sum_{i=1}^{n} \xi_i \rho_i y_i, \sum_{j=1}^{n} \xi_j y_j \right) \\
&= \sum_{i=1}^{n} \rho_i \xi_i^2.
\end{align*}$$

If all the $\rho_i$ are $> 0$, this is $> 0$ unless each $\xi_i = 0$. Hence $\rho_i > 0$ for all $i$ ensures positive definiteness. Conversely, if $A$ is positive definite, then for each eigenvector $y_i$ we have $0 < (y_i A, y_i) = \rho_i(y_i, y_i)$, so $\rho_i > 0$.

Similarly, if $\rho_i \geq 0$ for all $i$, then $(xA, x) = \sum \rho_i \xi_i^2 \geq 0$, giving semi-definiteness. Conversely, if $A$ is semi-definite, then $(y_i A, y_i) = \rho_i(y_i, y_i) \geq 0$, so each $\rho_i \geq 0$.

If $A$ is 1-1, then $0$ is not a characteristic root of $A$. Hence if $A$ is semi-definite and 1-1, all of its characteristic roots are positive, and the theorem shows that $A$ is positive definite.
