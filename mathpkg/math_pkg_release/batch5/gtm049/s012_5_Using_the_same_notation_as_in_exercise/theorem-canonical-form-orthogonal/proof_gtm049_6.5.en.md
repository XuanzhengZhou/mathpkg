---
role: proof
locale: en
of_concept: theorem-canonical-form-orthogonal
source_book: gtm049
source_chapter: "6"
source_section: "6.5"
---

Let $c$ be an eigenvector of $f$ (acting on $V_{(C)}$) with eigenvalue $e^{i\theta}$. If $e^{i\theta}$ is real then $\theta = 0$ or $\theta = \pi$, i.e., $e^{i\theta} = \pm 1$, and we set $M = [c]$. If $e^{i\theta}$ is not real then we set $M = T$ as in Lemma 5 (the two-dimensional real invariant subspace). In either case, $V = M \oplus M^\perp$ (by Proposition 5 of Chapter V, p. 96, since $M$ is non-degenerate under $\sigma$) and $Mf = M$, $M^\perp f = M^\perp$ (by Lemma 6). The existence of a cartesian basis as required for our theorem now follows by induction on $\dim V$.

For the special case $\dim V = 2$, we have two possibilities:
(i) the matrix of $f$ is $\begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$ where $-\pi < \theta \leq \pi$; or
(ii) the matrix of $f$ is $\begin{pmatrix} x & 0 \\ 0 & y \end{pmatrix}$ where $x = +1, y = -1$ or $x = -1, y = +1$.
