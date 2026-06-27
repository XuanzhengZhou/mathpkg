---
role: proof
locale: en
of_concept: gram-schmidt-orthogonalization-random-variables
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Gram-Schmidt Orthogonalization for Random Variables

Let $\eta_1, \eta_2, \ldots$ be a sequence of linearly independent random variables in $L^2$. We construct an orthonormal sequence $\varepsilon_1, \varepsilon_2, \ldots$ inductively.

Set $\varepsilon_1 = \eta_1 / \|\eta_1\|$. Since $\eta_1 \neq 0$ (P-a.s.) by linear independence, $\|\eta_1\| > 0$, so $\varepsilon_1$ is well-defined and $\|\varepsilon_1\| = 1$.

Now suppose $\varepsilon_1, \ldots, \varepsilon_{n-1}$ have been constructed and are orthonormal. Define

$$\hat{\eta}_n = \sum_{k=1}^{n-1} (\eta_n, \varepsilon_k) \varepsilon_k,$$

which is the projection of $\eta_n$ onto the linear manifold $\mathcal{L}(\varepsilon_1, \ldots, \varepsilon_{n-1})$. Then set

$$\varepsilon_n = \frac{\eta_n - \hat{\eta}_n}{\|\eta_n - \hat{\eta}_n\|}.$$

Since $\eta_1, \ldots, \eta_n$ are linearly independent and $\mathcal{L}\{\eta_1, \ldots, \eta_{n-1}\} = \mathcal{L}\{\varepsilon_1, \ldots, \varepsilon_{n-1}\}$, we have $\|\eta_n - \hat{\eta}_n\| > 0$. Hence $\varepsilon_n$ is well-defined and $\|\varepsilon_n\| = 1$.

Moreover, for any $j < n$, we have

$$(\varepsilon_n, \varepsilon_j) = \frac{(\eta_n - \hat{\eta}_n, \varepsilon_j)}{\|\eta_n - \hat{\eta}_n\|} = \frac{(\eta_n, \varepsilon_j) - \sum_{k=1}^{n-1} (\eta_n, \varepsilon_k)(\varepsilon_k, \varepsilon_j)}{\|\eta_n - \hat{\eta}_n\|} = \frac{(\eta_n, \varepsilon_j) - (\eta_n, \varepsilon_j)}{\|\eta_n - \hat{\eta}_n\|} = 0,$$

since $(\varepsilon_k, \varepsilon_j) = \delta_{kj}$ by the induction hypothesis. Thus $\varepsilon_n$ is orthogonal to all previously constructed $\varepsilon_j$, and the sequence $\varepsilon_1, \varepsilon_2, \ldots$ is orthonormal.

By construction, each $\varepsilon_n$ is a linear combination of $\eta_1, \ldots, \eta_n$, and conversely each $\eta_n$ can be recovered as a linear combination of $\varepsilon_1, \ldots, \varepsilon_n$. Therefore $\mathcal{L}\{\eta_1, \ldots, \eta_n\} = \mathcal{L}\{\varepsilon_1, \ldots, \varepsilon_n\}$ for all $n$.
