---
role: proof
locale: en
of_concept: eigenvalues-of-restricted-transition
source_book: gtm034
source_chapter: "V"
source_section: "21"
---

Let $\Delta_N = \Delta_N(\lambda)$ denote the determinant of $Q_N - \lambda I_N$. Expanding the determinant in terms of its minors yields the difference equation
$$\Delta_n = -\lambda \Delta_{n-1} - \frac{1}{4} \Delta_{n-2}, \quad n = 2, 3, \ldots.$$

Direct computation of the two lowest-order determinants gives the initial conditions
$$\Delta_0 = -\lambda, \quad \Delta_1 = \lambda^2 - \frac{1}{4}.$$

By standard methods one obtains
$$\Delta_n(\lambda) = A r_1^n + B r_2^n$$
where $r_1$ and $r_2$ are the roots of the quadratic equation $x^2 + \lambda x + \frac{1}{4} = 0$.

Making the substitution $\lambda = -\cos t$, one finds that
$$x^2 - x \cos t + \frac{1}{4} = \left(x - \frac{e^{it}}{2}\right)\left(x - \frac{e^{-it}}{2}\right) = 0,$$
so that $2x = e^{\pm it}$. Hence $\Delta_n(\lambda) = 0$ when $(n + 2)t$ is a multiple of $\pi$ but not zero, leading to $(n + 2)t = (k + 1)\pi$, $k = 0, 1, \ldots, n$. This yields the eigenvalues
$$\lambda_k = -\cos\frac{k+1}{N+2}\pi.$$
Since $\cos\frac{k+1}{N+2}\pi = -\cos\frac{(N-k)+1}{N+2}\pi$, the sign reversal yields an equivalent set. As $N+1$ distinct eigenvalues have been found for an $(N+1) \times (N+1)$ matrix, part (a) is proved.

The verification that $v_k(x)$ are eigenfunctions is straightforward using trigonometric identities. One checks that $Q_N v_k = \lambda_k v_k$ and $(v_k, v_k) = 1$. The orthogonality $(v_k, v_m) = 0$ for $k \neq m$ follows from the general fact that eigenvectors belonging to distinct eigenvalues of a symmetric matrix are orthogonal. The normalization is verified by
$$(v_k, v_k) = \frac{2}{N+2} \sum_{x=0}^{N} \sin^2 \left[ \frac{k+1}{N+2} (x+1)\pi \right] = 1 - \frac{1}{N+2} \sum_{x=-1}^{N+1} \cos \left[ 2 \frac{k+1}{N+2} (x+1)\pi \right] = 1.$$
