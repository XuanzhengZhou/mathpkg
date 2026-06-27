---
role: proof
locale: en
of_concept: eigenvalues-in-real-linear-spaces
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§6. The characteristic polynomial"
---

Assume $\dim E = n$ is odd. The characteristic polynomial $f(\lambda) = \det(\varphi - \lambda \iota) = \sum_{p=0}^{n} \alpha_p \lambda^{n-p}$ has degree $n$. The leading term is $(-\lambda)^n = -\lambda^n$ (since $n$ is odd). Therefore
$$\lim_{\lambda \to \infty} f(\lambda) = -\infty, \quad \lim_{\lambda \to -\infty} f(\lambda) = +\infty.$$
By the intermediate value theorem, there exists some $\lambda_0 \in \mathbb{R}$ with $f(\lambda_0) = 0$, hence an eigenvalue exists.

For the determinant relation: evaluating at $\lambda = 0$ gives $f(0) = \alpha_n = \det \varphi$. If $\det \varphi > 0$, then $f(0) > 0$ while $\lim_{\lambda \to \infty} f(\lambda) = -\infty$, so there is a positive root. If $\det \varphi < 0$, then $f(0) < 0$ while $\lim_{\lambda \to -\infty} f(\lambda) = +\infty$, so there is a negative root.

If $n$ is even, then $\lim_{\lambda \to \infty} f(\lambda) = \infty$ and $\lim_{\lambda \to -\infty} f(\lambda) = \infty$. If $\det \varphi < 0$, then $f(0) < 0$, so $f$ must cross the axis both for $\lambda > 0$ and $\lambda < 0$, giving at least one positive and one negative eigenvalue.
