---
role: proof
locale: en
of_concept: rapid-decay-function-on-lightcone
source_book: gtm048
source_chapter: "5"
source_section: "5.6"
---

Let $(x, X)$ be an instantaneous observer. For any $Y \in \mathcal{L}_x^+$, write $Y = e(X - U)$ where $e \in (0, \infty)$ and $U \in \mathcal{S}_x \subset X^\perp$, with $|U| = 1$.

Let $\omega \in M_x^*$ be causal and decompose $\omega = a\chi + \alpha$, where $a \in \mathbb{R}$, $\chi \in M_x^*$ is physically equivalent to $X$ (so $\chi(X) = 1$), and $\alpha \in M_x^*$ satisfies $\alpha(X) = 0$.

For any $Y = e(X - U) \in \mathcal{L}_x^+$, we compute:
$$\tilde{\omega}(Y) = \omega(Y) = a\chi(e(X - U)) + \alpha(e(X - U)) = ae\chi(X) - ae\chi(U) + e\alpha(X) - e\alpha(U).$$

Since $\chi(X) = 1$, $\chi(U) = 0$ (because $\chi$ is physically equivalent to $X$ and $U \in X^\perp$), and $\alpha(X) = 0$, we obtain:
$$\tilde{\omega}(Y) = -e(a + \alpha(U)).$$

Now apply the Schwarz inequality on the inner product space $X^\perp$ (which is a Euclidean space). Since $\alpha$ is a linear functional on $X^\perp$ and $U \in X^\perp$ with $|U| = 1$:
$$|\alpha(U)| \leq |\alpha| \cdot |U| = |\alpha|.$$

Setting $b = |a| + |\alpha|$, we have $|a + \alpha(U)| \leq |a| + |\alpha| = b$, hence:
$$|\tilde{\omega}(Y)| = e|a + \alpha(U)| \leq eb \quad \forall Y \in \mathcal{L}_x^+.$$

Now, $f \circ \pi_x = e^{-1} \exp(-e)$. Using the diffeomorphism $\pi_x: P_x \to \mathcal{L}_x^+$ and the relation $\pi_x \Lambda_x = \zeta \otimes e^2 de$ (where $\zeta$ is the standard volume element on $\mathcal{S}_x$), we estimate:
\begin{align*}
b^{-N} \left| \int_{\mathcal{L}_x^+} \tilde{\omega}^N f \Lambda_x \right|
&= \left| \int_{P_x} (\tilde{\omega} \circ \pi_x)^N (f \circ \pi_x) \pi_x^* \Lambda_x \right| b^{-N} \\
&\leq \int_{\mathcal{S}_x} \zeta \int_0^\infty (eb)^N \cdot \frac{\exp(-e)}{e} \cdot e^2 \, de \cdot b^{-N} \\
&= \int_{\mathcal{S}_x} \zeta \int_0^\infty e^{N+1} \exp(-e) \, de.
\end{align*}

The $e$-integral $\int_0^\infty e^{N+1} \exp(-e) \, de = (N+1)!$ converges for all nonnegative integers $N$, and $\int_{\mathcal{S}_x} \zeta = 4\pi$ (the area of the unit 2-sphere). Thus the original integral is absolutely convergent, proving that $f$ is of rapid decay.
