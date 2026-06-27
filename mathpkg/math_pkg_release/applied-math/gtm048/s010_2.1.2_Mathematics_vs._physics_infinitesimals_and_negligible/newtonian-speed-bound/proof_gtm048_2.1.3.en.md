---
role: proof
locale: en
of_concept: newtonian-speed-bound
source_book: gtm048
source_chapter: "2"
source_section: "2.1.3"
---

Let $Z$ be a future-pointing unit timelike vector, so $g(Z, Z) = -1$. Let $p \in Z^\perp$, so $g(Z, p) = 0$. Since $g|_{Z^\perp}$ is positive definite (as established in Section 1.2), we have $g(p, p) = |p|^2 \ge 0$.

Compute $g(X, X)$ using the decomposition $X = eZ + p$:
$$
g(X, X) = g(eZ + p, eZ + p) = e^2 g(Z, Z) + 2e g(Z, p) + g(p, p) = -e^2 + |p|^2.
$$

\textbf{(1)} Since $X$ is causal (future-pointing), by definition $g(X, X) \le 0$. Therefore
$$
-e^2 + |p|^2 \le 0 \quad \Longrightarrow \quad |p|^2 \le e^2.
$$
Since $e > 0$ (as $X$ is future-pointing and $Z$ is future-pointing timelike, $e = -g(X, Z) > 0$ by Section 1.2), we obtain
$$
\frac{|p|}{e} \le 1.
$$

\textbf{(2)} $X$ is timelike if and only if $g(X, X) < 0$. Using the same computation:
$$
g(X, X) < 0 \;\Longleftrightarrow\; -e^2 + |p|^2 < 0 \;\Longleftrightarrow\; |p|^2 < e^2 \;\Longleftrightarrow\; \frac{|p|}{e} < 1.
$$
Thus $X$ is timelike exactly when the Newtonian speed is strictly less than $1$.
