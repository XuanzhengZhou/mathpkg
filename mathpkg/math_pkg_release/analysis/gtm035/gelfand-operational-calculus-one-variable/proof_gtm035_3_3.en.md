---
role: proof
locale: en
of_concept: gelfand-operational-calculus-one-variable
source_book: gtm035
source_chapter: "3"
source_section: "3.3"
---
# Proof of Gelfand Operational Calculus in One Variable

Let $\mathfrak{A}$ be a Banach algebra, $x \in \mathfrak{A}$, and $\Omega$ an open set in $\mathbb{C}$ containing $\sigma(x)$.

## 1. Construction on rational functions

Choose an open set $\Omega_1$ with

$$\sigma(x) \subset \Omega_1 \subset \overline{\Omega}_1 \subset \Omega$$

whose boundary $\gamma$ consists of finitely many simple closed polygonal curves. For any rational function $R$ with poles off $\overline{\Omega}_1$, define

$$R(x) := \frac{1}{2\pi i} \int_\gamma R(t) (t - x)^{-1} \, dt. \tag{6}$$

This is well-defined because $t \mapsto (t-x)^{-1}$ is continuous on $\gamma$ (since $\gamma \cap \sigma(x) = \varnothing$) and the integral converges in the Banach space $\mathfrak{A}$.

The map $R \mapsto R(x)$ defined by (6) is clearly a homomorphism on the algebra of rational functions with poles off $\overline{\Omega}_1$. Moreover, if $R(z) = z$ (the identity function), then by the resolvent equation and Cauchy's integral formula one checks that $R(x) = x$, so condition (c) holds for rational functions.

For the Gelfand transform, if $h \in \mathcal{M}$ (the maximal ideal space of $\mathfrak{A}$), then applying $h$ to (6) yields

$$\widehat{R(x)}(h) = \frac{1}{2\pi i} \int_\gamma R(t) (t - \hat{x}(h))^{-1} \, dt = R(\hat{x}(h)),$$

since the Cauchy integral formula recovers the value of the rational function $R$ at the point $\hat{x}(h) \in \sigma(x) \subset \Omega_1$. Thus condition (d) holds for rational functions.

The Spectral Mapping Theorem for rational functions gives

$$\sigma(R(x)) = R(\sigma(x)),$$

which is condition (e); this follows from the fact that for any $\lambda \in \mathbb{C}$, the rational function $R(z) - \lambda$ factors as $c \prod (z - z_j) / \prod (z - p_k)$, and invertibility of $R(x) - \lambda$ is equivalent to all $x - z_j$ being invertible, i.e., $z_j \notin \sigma(x)$.

## 2. Extension to $H(\Omega)$

Let $F \in H(\Omega)$. By Runge's theorem, there exists a sequence of rational functions $\{F_n\}$ with poles off $\overline{\Omega}$ such that $F_n \to F$ uniformly on compact subsets of $\Omega$, hence in particular on $\overline{\Omega}_1$. We write

$$F_n \to F \quad \text{in } H(\Omega).$$

We claim that $\{F_n(x)\}$ is a Cauchy sequence in $\mathfrak{A}$. For any $n, m$, using the integral representation (6) applied to $F_n - F_m$,

$$\|F_n(x) - F_m(x)\| = \left\| \frac{1}{2\pi i} \int_\gamma (F_n(t) - F_m(t)) (t - x)^{-1} \, dt \right\|$$

$$\leq \frac{1}{2\pi} \cdot \operatorname{length}(\gamma) \cdot \max_{t \in \gamma} |F_n(t) - F_m(t)| \cdot \max_{t \in \gamma} \|(t-x)^{-1}\|.$$

Since $F_n \to F$ uniformly on $\gamma$ and $\|(t-x)^{-1}\|$ is bounded on $\gamma$ (as a continuous function on a compact set disjoint from $\sigma(x)$), the right-hand side tends to $0$ as $n, m \to \infty$. Thus $\{F_n(x)\}$ converges in $\mathfrak{A}$. We define

$$F(x) := \lim_{n \to \infty} F_n(x)$$

and $\tau : H(\Omega) \to \mathfrak{A}$ by $\tau(F) = F(x)$. A standard argument shows that the limit is independent of the choice of approximating sequence $\{F_n\}$.

## 3. Verification of properties

**(a) $\tau$ is an algebra homomorphism.** For $F, G \in H(\Omega)$, approximate by rational functions $F_n \to F$, $G_n \to G$. Then $F_n + G_n \to F + G$ and $F_n G_n \to FG$ in $H(\Omega)$. Since the map is a homomorphism on rational functions and the algebraic operations are continuous in $\mathfrak{A}$,

$$(F+G)(x) = \lim (F_n + G_n)(x) = \lim (F_n(x) + G_n(x)) = F(x) + G(x),$$

$$(FG)(x) = \lim (F_n G_n)(x) = \lim (F_n(x) G_n(x)) = F(x) G(x).$$

**(b) Continuity.** If $F_n \to F$ in $H(\Omega)$ (uniformly on compact sets), then the same estimate as above shows $F_n(x) \to F(x)$ in $\mathfrak{A}$.

**(c) Identity.** Since the identity function $z \mapsto z$ is a rational function, and condition (c) was verified for rational functions, it holds in general by the definition of the extension.

**(d) Gelfand transform.** For any $h \in \mathcal{M}$, $\widehat{F(x)}(h) = \lim \widehat{F_n(x)}(h) = \lim F_n(\hat{x}(h)) = F(\hat{x}(h))$, where the first equality uses continuity of $h \in \mathfrak{A}^*$, the second uses (d) for rational functions, and the third uses uniform convergence of $F_n$ to $F$ on $\sigma(x)$.

**(e) Spectral Mapping Theorem.** $\sigma(F(x)) = F(\sigma(x))$. This follows by the same reasoning as for rational functions, using the homomorphism property and the fact that $F(x) - \lambda 1$ is invertible iff $F(z) - \lambda$ does not vanish on $\sigma(x)$.

## 4. Uniqueness

Suppose $\tau' : H(\Omega) \to \mathfrak{A}$ is another map satisfying (a), (b), and (d) of the theorem. For any rational function $R$ with poles off $\Omega$, conditions (a) and (d) uniquely determine $R(x)$: by (a) and (d),

$$\widehat{\tau'(R)}(h) = R(\hat{x}(h)) = \widehat{R(x)}(h) \quad \text{for all } h \in \mathcal{M},$$

so by the semisimplicity of the Gelfand transform (or by direct computation), $\tau'(R) = R(x)$. Thus $\tau'$ and $\tau$ agree on rational functions. For general $F \in H(\Omega)$, approximate $F$ by rational functions $F_n \to F$ in $H(\Omega)$. By condition (b) applied to both $\tau$ and $\tau'$,

$$\tau'(F) = \lim_{n \to \infty} \tau'(F_n) = \lim_{n \to \infty} \tau(F_n) = \tau(F).$$

Hence $\tau' = \tau$, proving uniqueness. $\square$
