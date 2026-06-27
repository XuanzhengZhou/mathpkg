---
role: proof
locale: en
of_concept: gauss-lemma-for-spacetimes
source_book: gtm048
source_chapter: "2"
source_section: "2.0.1"
---

Suppose $e \in \mathcal{E}$. Since $X$ is geodesic, $X$ is nowhere zero (Section 0.0.8), so we can take an open neighborhood $U$ of $\gamma e$ and a subinterval $F \subset \mathcal{E}$ containing $e$ such that on $U$, there exists a coordinate system with $X|_U = \partial_1$. Define $\tilde{\gamma} = \gamma|_F$. Let $\tilde{W}$ be a vector field on $U$ such that $\tilde{W} \circ \tilde{\gamma} = W|_F$ and $L_X \tilde{W} = 0$.

Since the Levi-Civita connection $D$ is symmetric (Section 0.0.8a),
$$D_X \tilde{W} - D_{\tilde{W}} X = L_X \tilde{W} = 0.$$

Now compute:
$$X g(X, \tilde{W}) = g(D_X X, \tilde{W}) + g(X, D_X \tilde{W}).$$
Since $X$ is geodesic, $D_X X = 0$, so the first term vanishes. Thus
$$X g(X, \tilde{W}) = g(X, D_X \tilde{W}) = g(X, D_{\tilde{W}} X) = \frac{1}{2} \tilde{W} g(X, X) = 0,$$
where the last equality holds because $g(X, X)$ is constant on $M$ by assumption.

Restricting this equation to $\tilde{\gamma}$, we obtain
$$\frac{d}{du} g(\tilde{\gamma}_*, W|_F) = 0.$$
Since $e \in \mathcal{E}$ was arbitrary and $\mathcal{E}$ is connected, $g(\gamma_*, W)$ is constant on all of $\mathcal{E}$.

The orthogonality relations $g(D_{\gamma_*} W, \gamma_*) = 0$ and $g(D_{\gamma_*} D_{\gamma_*} W, \gamma_*) = 0$ follow from differentiating the constancy result and using that $D_{\gamma_*} \gamma_* = 0$ (since $\gamma$ is an integral curve of a geodesic vector field).
