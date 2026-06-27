---
role: proof
locale: en
of_concept: completeness-preservation-uniformly-open
source_book: gtm027
source_chapter: "6"
source_section: "FOR METRIC_SPACES ONLY"
---

# Proof of Completeness Preservation Under Uniformly Open Maps

**Theorem.** Let $(X, d)$ be a complete metric space and $(Y, \rho)$ a Hausdorff space. If $f : X \to Y$ is a continuous, uniformly open surjection, then $Y$ is complete (i.e., there exists a metric on $Y$ compatible with its topology under which $Y$ is complete).

**Proof.** Define the relation $R \subset Y \times X$ by

$$R = \{(f(x), x) : x \in X\}.$$

Since $f$ is continuous and $Y$ is Hausdorff, the graph $\{(x, f(x)) : x \in X\}$ is closed in $X \times Y$; consequently $R$ is closed in $Y \times X$. (If $(y, x) \notin R$, then $y \neq f(x)$. By the Hausdorff property, there are disjoint neighborhoods separating $y$ and $f(x)$, and by continuity of $f$, one obtains a neighborhood of $(y, x)$ disjoint from $R$. Alternatively, if $y \notin R[A]$, then $A \times \{y\}$ is contained in the open set $(X \times Y) \setminus \text{graph}(f)$, and Theorem 5.12 may be applied.)

Because $f$ is uniformly open, for each $\varepsilon > 0$ there exists $\delta > 0$ such that

$$f[U_\varepsilon[x]] \supset V_\delta[f(x)] \quad \text{for all } x \in X,$$

where $U_\varepsilon[x]$ is the open $\varepsilon$-ball in $X$ and $V_\delta[y]$ is the open $\delta$-ball in $Y$. In terms of the relation $R$, this means that for each member $(y, x) \in R$ (so $y = f(x)$),

$$R[V_\delta[y]] \subset U_\varepsilon[x]^{-}.$$

Now let $\{y_n\}$ be a Cauchy sequence in $Y$. For each $k \in \omega$, choose $n_k$ such that $\rho(y_n, y_m) < 2^{-k}$ for all $n, m \geq n_k$. Pick $x_{n_0} \in X$ with $f(x_{n_0}) = y_{n_0}$ (possible since $f$ is surjective). Set $r_0 = 1$.

Applying the closed relation ball lemma (with $R$ closed, $X$ complete), we have

$$R[U_r[x]]^{-} \subset R[U_{r + e}[x]] \quad \text{for all } r, e > 0.$$

Using this, we inductively construct a Cauchy sequence $\{x_{n_k}\}$ in $X$: for each $k$, $x_{n_k}$ is chosen so that $f(x_{n_k}) = y_{n_k}$ and $d(x_{n_k}, x_{n_{k-1}}) < 2^{-(k-1)}$. This is possible by the uniform openness condition: $y_{n_k} \in V_{\delta_k}[y_{n_{k-1}}]$ for suitable $\delta_k$, and $y_{n_k} \in R[U_{\varepsilon_{k-1}}[x_{n_{k-1}}]]^{-}$, so by the lemma there is $x_{n_k}$ with $f(x_{n_k}) = y_{n_k}$ and $d(x_{n_k}, x_{n_{k-1}}) < \varepsilon_{k-1} + 2^{-k}$.

Since $X$ is complete, $\{x_{n_k}\}$ converges to some $x \in X$. By continuity of $f$, $f(x_{n_k}) \to f(x)$, so $y_{n_k} \to f(x)$. Since $\{y_n\}$ is Cauchy and has a convergent subsequence, it converges to $f(x)$. Thus every Cauchy sequence in $Y$ converges, proving that $Y$ is complete.
