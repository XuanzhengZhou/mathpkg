---
role: proof
locale: en
of_concept: mercer-theorem
source_book: gtm017
source_chapter: "IX"
source_section: "c"
---
Let $r(t,\tau)$ be continuous, symmetric, positive definite. Define the integral operator $(Rg)(t) = \int_0^T r(t,\tau)g(\tau)d\tau$.

\textbf{Step 1:} $R$ is completely continuous (maps bounded sets to relatively compact sets).

\textbf{Step 2:} By the Hilbert-Schmidt theory, $R$ has countably many positive eigenvalues $\lambda_i^{-1}$ with orthonormal eigenfunctions $\varphi_i$.

\textbf{Step 3:} Define $q(t,\tau) = \sum_{i=1}^\infty \varphi_i(t)\varphi_i(\tau)/\lambda_i$. The residual $s(t,\tau) = r(t,\tau) - q(t,\tau)$ is symmetric positive definite. If $s \neq 0$, the corresponding operator $S$ would have a positive eigenvalue, contradicting that eigenfunctions of $R$ are annihilated by $S$.

\textbf{Step 4:} Uniform convergence: $\sum_{i=n+1}^\infty \varphi_i(t)\varphi_i(\tau)/\lambda_i \leq (\sum_{n+1}^\infty \varphi_i^2(t)/\lambda_i)^{1/2}(\sum_{n+1}^\infty \varphi_i^2(\tau)/\lambda_i)^{1/2} \to 0$ uniformly by Dinis theorem, since $\sum \varphi_i^2(t)/\lambda_i \uparrow r(t,t)$ uniformly.
