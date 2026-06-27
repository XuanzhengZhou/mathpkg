---
role: proof
locale: en
of_concept: finitely-generated-uniform-algebra-is-full
source_book: gtm035
source_chapter: "15"
source_section: "15.6"
---
# Proof that a Finitely Generated Uniform Algebra is Full

**Lemma 15.6.** Let $\mathcal{L}$ be a finitely generated uniform algebra on a compact space $X$ with $X = \mathcal{M}(\mathcal{L})$. Then $\mathcal{L}$ is a full subalgebra of $C(X)$.

## Proof

By Exercise 7.3, it suffices to consider the case where $\mathcal{L} = P(X)$ (the polynomial algebra) and $X$ is a compact polynomially convex set in $\mathbb{C}^n$. The reduction works because any finitely generated uniform algebra can be realized as $P(X)$ for some polynomially convex $X \subset \mathbb{C}^n$ via the joint spectrum of its generators.

**Step 1: Surjectivity of $\eta$ on $(P(X))^{-1}$.**

By the Oka–Weil theorem, $\mathcal{H}(X) \subset P(X)$ (holomorphic functions near $X$ are uniformly approximable by polynomials on $X$). Fix $\gamma \in H^1(X, \mathbb{Z})$. By Lemma 15.5, $\mathcal{H}(X)$ is full, so there exists $f \in (\mathcal{H}(X))^{-1}$ with $\eta(f) = \gamma$. Since $\mathcal{H}(X) \subset P(X)$, we have $f \in (P(X))^{-1}$ as well. Thus $\eta$ maps $(P(X))^{-1}$ onto $H^1(X, \mathbb{Z})$.

**Step 2: The kernel argument.**

Now fix $f \in (P(X))^{-1}$ with $\eta(f) = 0$. Choose $\varepsilon > 0$ with $\varepsilon < \inf_X |f|$. By the Oka–Weil theorem, choose a polynomial $g$ such that

$$\|g - f\|_{P(X)} < \varepsilon < \inf_X |f|.$$

Define $h = (f - g)/f$. Then $\|h\|_{P(X)} < 1$ and

$$g = f(1 - h).$$

Since $\|h\| < 1$, the element $1 - h$ is in $\exp C(X)$ (its spectrum lies in a disk of radius $< 1$ centered at $1$, hence does not contain $0$). Consequently $\eta(1 - h) = 0$, and

$$\eta(g) = \eta(f(1 - h)) = \eta(f) + \eta(1 - h) = 0 + 0 = 0.$$

**Step 3: Lifting to an exponential.**

By the Oka–Weil theorem, $g$ is a polynomial, hence $g \in (\mathcal{H}(X))^{-1}$. Applying Lemma 15.5 (the fullness of $\mathcal{H}(X)$) to $g$ with $\eta(g) = 0$, we obtain $g^\circ \in \mathcal{H}(X)$ such that

$$g = e^{g^\circ}.$$

**Step 4: Exponential representation of $f$.**

Since $\|h\| < 1$ in $P(X)$, the element $1 - h$ has a logarithm in $P(X)$. Indeed, the series

$$-\sum_{n=1}^{\infty} \frac{1}{n} h^n$$

converges in $P(X)$ to some $k$ satisfying $1 - h = e^k$. To see this: $h = (f-g)/f$ implies $h \in P(X)$, and $\|h\| < 1$ guarantees spectral radius less than $1$, so the logarithm series converges.

Therefore

$$f = g \cdot (1 - h)^{-1} = e^{g^\circ} \cdot e^{-k} = e^{g^\circ - k} \in \exp(P(X)).$$

**Conclusion.** We have shown that $\eta$ maps $(P(X))^{-1}$ onto $H^1(X, \mathbb{Z})$ (step 1) and that $\ker(\eta|_{(P(X))^{-1}}) = \exp(P(X))$ (steps 2–4). Hence $P(X)$ is a full subalgebra. By the reduction via Exercise 7.3, the same holds for any finitely generated uniform algebra $\mathcal{L}$.
