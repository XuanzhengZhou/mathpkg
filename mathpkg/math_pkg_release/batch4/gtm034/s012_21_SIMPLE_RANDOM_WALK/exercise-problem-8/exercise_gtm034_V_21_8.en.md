---
role: exercise
locale: en
chapter: "V"
section: "21-23"
exercise_number: 8
---

For symmetric one-dimensional random walk \(x_n\), let \(Q_n\) be the \((n+1) \times (n+1)\) matrix defined in D21.1, and let \(\lambda_0(n) \leq \lambda_1(n) \leq \cdots \leq \lambda_n(n)\) be its (real) eigenvalues. Define \(M_k = \max_{0 \leq j \leq k} x_j - \min_{0 \leq j \leq k} x_j\). Prove that
\[
(n+1)P_k(0,0) - \operatorname{Tr}(Q_n^k) = (n+1)P_0[x_k = 0; M_k > n] + E_0[M_k; x_k = 0, M_k \leq n].
\]
Without any assumptions on the moments of the random walk, prove that
\[
\lim_{n \to \infty} \frac{1}{n+1} \sum_{j=0}^{n} \lambda_j^k(n) = P_k(0,0), \quad n \geq 0.
\]
