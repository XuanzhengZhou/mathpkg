---
role: proof
locale: en
of_concept: "f-riesz-let-be-a-bounded-linear-functional"
source_book: gtm025
source_chapter: "Lp Spaces"
source_section: "15.11"
---

The result is trivial for $L = 0$, so we suppose that $L \neq 0$. Using (15.9), select a function $g \in \mathfrak{L}_p$ such that $L(g) = \|L\|$ and $\|g\|_p = 1$. We want to apply (15.10), and to do this we must show that the function

$$t \rightarrow \|tf + g\|_p = \psi_f(t)$$

is differentiable at $t = 0$ for every $f \in \mathfrak{L}_p$. Let $\omega(t) = \psi_f^p(t) = \int_X |tf + g|^p d\mu$.

Writing $f = f_1 + if_2$ and $g = g_1 + ig_2$, we have

$$|tf + g|^p = \left[ (tf_1 + g_1)^2 + (tf_2 + g_2)^2 \right]^{\frac{p}{2}},$$

and so almost everywhere on $X$ we have

$$\frac{d}{dt} |tf + g|^p = p |tf + g|^{p-2} \left[ (tf_1 + g_1) f_1 + (tf_2 + g_2) f_2 \right]$$

for all $t$. [If $1 < p < 2$ and the points $x \in X$ and $t \in R$ are such

on dominated convergence (12.24) implies that

$$\lim_{t \to 0} \int_X \frac{|g + tf|^p - |g|^p}{t} d\mu = \int_X p |g|^{p-2}[g_1 f_1 + g_2 f_2] d\mu.$$

[If $1 < p < 2$ and $g(x) = 0$, then the integrand in (4) and in the following integrals is zero.] Combining (2) and (4), we see that $\omega'(0)$ exists and that

$$\omega'(0) = \int_X p |g|^{p-2}[g_1 f_1 + g_2 f_2] d\mu.$$

Consequently $\psi'_f(0)$ also exists. Using (5), we write

$$\psi'_f(0) = \frac{1}{p} \left( \int_X |g|^p d\mu \right)^{\frac{1}{p}-1} \cdot \omega'(0) = \frac{1}{p} \|g\|_p^{1-p} \omega'(0)$$

$$= \int_X |g|^{p-2}[g_1 f_1 + g_2 f_2] d\mu.$$

Lemma (15.10) and (6) imply that

$$L(f) = \|L\| (\psi'_f(0) + i \psi'_{-if}(0))$$

$$= \|L\| \int_X |g|^{p-2} \left( (g_1 f_1 + g_2 f_2) + i (g_1 f_2 - g_2 f_1) \right) d\mu = \|L\| \cdot \int_X |g|^{p-2} \bar{g} f d\mu.$$

The theorem follows when we set $h = \|L\| \cdot |g|^{p-1} \text{sgn}(g)$; i.e.,

$$L(f) = \int_X f \bar{h} d\mu.$$

(15.1

(15.14) Exercise. (a) Let $(X, \mathcal{A}, \mu)$ be a measure space, let $p$ be a real number such that $p > 1$, and let $f$ be an $\mathcal{A}$-measurable function on $X$ such that:

(i) $\{x \in X : f(x) \neq 0\}$ is the union of a countable number of sets in $\mathcal{A}$ having finite measure;

(ii) $f g \in \mathfrak{L}_1(X, \mathcal{A}, \mu)$ for all $g \in \mathfrak{L}_p(X, \mathcal{A}, \mu)$. Then $f$ is in $\mathfrak{L}_p'(X, \mathcal{A}, \mu)$. [Hints. Construct a sequence of functions $(f_n)_{n=1}^{\infty}$ such that $(|f_n|)_{n=1}^{\infty}$ is nondecreasing, $|f_n| \rightarrow |f|$ everywhere, and each $f_n$ vanishes except on a set of finite measure. Then use (12.22), (15.1), and (14.23) to infer that $f \in \mathfrak{L}_p'$.]

(b) [E. B. LEACH]. Let $(X, \mathcal{A}, \mu)$ be a measure space and suppose that every set $A$ in $\mathcal{A}$ such that $\mu(A) = \infty$ contains a set $B \in \mathcal{A}$ for which $0 < \mu(B) < \infty$. Let $f$ be any $\mathcal{A}$-measurable function on $X$ for which (ii) above holds. Then $f$ is in $\mathfrak{L}_p'(X, \mathcal{A}, \mu)$. [Hints. Let $A_n = \{x \in X : |f(x)| \geq \frac{1}{n}\}$. If $\mu(A_m) = \infty$, use (10.56.d) to find a subset $C$ of $A_m$ such that $C \in \mathcal{A}, \mu(C) = \infty$, and $

be any element of $E \cap S'$. Show that there is one and only one element $y_0 \in S$ such that

$$\|y_0 - x\| = \inf\{\|y - x\| : y \in S\}.$$

(15.17) Exercise: Weak convergence and the RADON-RIESZ theorem. In (13.41), we defined weak convergence for sequences of functions in $\mathfrak{L}_p$ and thereafter studied relations between weak convergence and other sorts of convergence. Weak convergence can be defined for sequences $(x_n)$ in any normed linear space $E$, as follows. The sequence $(x_n)$ converges weakly to $x \in E$ if $f(x_n) \rightarrow f(x)$ for all $f$ in the conjugate space $E^*$ of $E$. Theorem (15.11) shows that the present definition is consistent with the definition offered in (13.41) for $E = \mathfrak{L}_p$ ($1 < p < \infty$): for $E = \mathfrak{L}_1$, see (20.19) infra.

(a) Let $E$ be a normed linear space [over $R$ or $K$] with the property that if $(x_n)$ is a sequence in $E$, $x \in E$, $\|x_n\| = 1$, and $\|x\| = 1$, then the relation

$$\left\| \frac{x_n + x}{2} \right\| \rightarrow 1$$

implies

$$\|x_n - x\| \rightarrow 0.$$

[Such spaces are called locally uniformly convex.] Let $(y_n)$ be a sequence in $E$ and $y$ an element of $E$ such that:

(i) $\|y_n\| \rightarrow \|y\|$;
(ii) $y_n \rightarrow y$ weakly.

Prove that $\|y_n - y\| \rightarrow 0$. [If $\|y\| = 0$, the assertion is trivial. Otherwise, write $x_n = \|y_n\|^{-1}y_n$ and $x

(15.18) Exercise. Define $f$ and $f_n$, $n = 1, 2, \ldots$, on $[0, 2\pi]$ by the rules: $f(x) = 1$, $f_n(x) = 1 + \sin(nx)$. Notice that $f, f_n \in \mathcal{L}_1([0, 2\pi], \mathcal{M}_\lambda, \lambda)$ for all $n \in N$. Prove that:

(a) $f_n \rightarrow f$ weakly in $\mathcal{L}_1$ [use (16.35)];
(b) $\|f\|_1 = \|f_n\|_1 = 2\pi$ for all $n \in N$;
(c) $f_n \rightarrow f$ in measure;
(d) $\|f_n - f\|_1 \rightarrow 0$;
(e) $f_n \rightarrow f$ a.e.;
(f) $\mathcal{L}_1([0, 2\pi], \mathcal{M}_\lambda, \lambda)$ is not locally uniformly convex.

§ 16. Abstract Hilbert spaces

(16.1) Inner product spaces. Recall (13.16) that an inner product space is a linear space $H$ over $K$ together with a mapping $(x, y) \rightarrow \langle x, y \rangle$ of $H \times H$ into $K$ such that:

$$\langle x + y, z \rangle = \langle x, z \rangle + \langle y, z \rangle;$$
$$\langle \alpha x, y \rangle = \alpha \langle x, y \rangle;$$
$$\langle y, x \rangle = \overline{\langle x, y \rangle};$$
$$\langle x, x \rangle > 0 \quad \text{if} \quad x \neq 0;$$

[for all $x, y, z \in H$ and $\alpha \in K$]. The above relations imply trivially that:

$$\langle 0, y \rangle = \langle y, 0 \rangle =

It is clear that strict inequality holds throughout this computation unless $x - \gamma y = 0$.

If $\alpha x = \beta y$, where $|\alpha| + |\beta| \neq 0$, it is easy to see that the two sides of (i) are equal. $\square$
