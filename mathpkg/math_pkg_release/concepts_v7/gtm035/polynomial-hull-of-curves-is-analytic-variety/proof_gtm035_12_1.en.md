---
role: proof
locale: en
of_concept: polynomial-hull-of-curves-is-analytic-variety
source_book: gtm035
source_chapter: "12"
source_section: "12.1"
---
# Proof of Polynomial Hull of Curves is a One-Dimensional Analytic Variety

Let $\gamma_1, \gamma_2, \ldots, \gamma_p$ be a finite collection of compact smooth curves in $\mathbb{C}^N$ and let $\gamma$ be their union. Write $\hat{\gamma}$ for the polynomial hull $h(\gamma)$. We use $z_j$, $1 \leq j \leq N$, for the complex coordinates in $\mathbb{C}^N$.

We proceed in four steps.

**Step 1.** Fix a point $x^0 \in \hat{\gamma} \setminus \gamma$. Construct a polynomial $f$ in $z_1, \ldots, z_N$ such that $f(x^0) = 0$ and $0 \notin f(\gamma)$.

Notation: For $S \subseteq \mathbb{C}$,

$$f^{-1}(S) = \{(z_1, \ldots, z_N) \in \hat{\gamma} : f(z_1, \ldots, z_N) \in S\}.$$

We say $f^{-1}(S)$ lies at most $k$-sheeted over $S$ if $\# f^{-1}(\lambda) \leq k$ for each $\lambda \in S$, and finite-sheeted if this holds for some $k$.

**Step 2.** Let $U$ and $V$ be components of $\mathbb{C} \setminus f(\gamma)$ that share a common boundary arc $\alpha$ such that $f|\gamma$ is $s$ to $1$ over $\alpha$ for some positive integer $s$. Assume $f^{-1}(U)$ is at most $k$-sheeted over $U$. Then $f^{-1}(V)$ lies at most $(k+s)$-sheeted over $V$.

This step relies on Lemma 12.3 (which bounds the fiber cardinality at the edge arc) and Theorem 11.12 (which extends the bound from the edge to the interior).

**Step 3.** Recall from the proof of Theorem 11.9 that either $f(\hat{\gamma})$ contains $U_0$ or $f(\hat{\gamma})$ is disjoint from $U_0$. Since $\hat{\gamma}$ is the maximal ideal space of $\mathbf{P}(\gamma)$ (by Exercise 7.4) and $|f(z)| \leq \|f\|_\gamma < \infty$ for all $z \in \hat{\gamma}$, $f(\hat{\gamma})$ does not contain $U_0$. Hence $f(\hat{\gamma})$ is disjoint from $U_0$, and $f^{-1}(U_0)$ lies at most $0$-sheeted over $U_0$.

**Step 4.** Let $U^*$ denote the component of $\mathbb{C} \setminus f(\gamma)$ that contains $0$. We parametrize $\gamma$ by a finite set of $\mathcal{C}^1$ maps $\phi_j : J_j \to \gamma$, and construct a sequence of components

$$U_1, U_2, \ldots, U_\ell$$

of $\mathbb{C} \setminus f(\gamma)$ such that:
1. $U_0$ and $U_1$ share a boundary arc $\alpha_0$ where $f|\gamma$ is $s_0$ to $1$ for some $s_0 > 0$.
2. $U_j$ and $U_{j+1}$ share a boundary arc $\alpha_j$ where $f|\gamma$ is $s_j$ to $1$ for some $s_j > 0$, $j = 1, \ldots, \ell-1$.
3. $U_\ell = U^*$.

This is achieved by considering a subregion $W$ of $\mathbb{C} \setminus f(\gamma)$ consisting of $\ell+1$ components $W_0, W_1, \ldots, W_\ell$, where $W_0$ is unbounded and $W_\ell$ contains $0$. Since $f(\gamma) \cap W = E$, each $W_s$ is contained in a component $U_s$ of $\mathbb{C} \setminus f(\gamma)$ for $1 \leq s \leq \ell$. Condition (3) holds since $0 \in W_\ell \subseteq U_\ell$, and conditions (1) and (2) hold by the construction of the parametrization arcs $\{\sigma_s\}$.

**Conclusion of the proof.** From Step 4 we obtain the sequence $U_1, U_2, \ldots, U_\ell = U^*$. By Step 3, $f^{-1}(U_0)$ lies at most $0$-sheeted over $U_0$. Using Step 2 at each of the edges $\alpha_0, \alpha_1, \ldots, \alpha_{\ell-1}$, we deduce after $\ell$ applications that $f^{-1}(U^*)$ lies finite-sheeted over $U^*$. By Corollary 11.11, $f^{-1}(U^*)$ is a finite-sheeted analytic cover of $U^*$. Since $x^0 \in f^{-1}(U^*)$, the set $f^{-1}(U^*)$ provides a neighborhood of $x^0$ in $\hat{\gamma}$. Thus $\hat{\gamma}$ is locally an analytic variety at $x^0$. Since this holds for each $x^0 \in \hat{\gamma} \setminus \gamma$, the set $\hat{\gamma} \setminus \gamma$ is a one-dimensional analytic subvariety of $\mathbb{C}^N \setminus \gamma$. $\square$
