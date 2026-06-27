---
role: proof
locale: en
of_concept: "let-and-let-be-as-usual-lebesgue-measure"
source_book: gtm025
source_chapter: "Spaces of Integrable Functions"
source_section: "13.24"
---

Let $\varepsilon$ be an arbitrary positive number. Applying (13.21), choose $\varphi \in \mathfrak{C}_{00}(R)$ such that $\|\varphi - f\|_p < \frac{\varepsilon}{3}$. Then $\varphi$ is uniformly continuous (7.18), and also there is a positive real number $\alpha$ such that $\varphi(t) = 0$ if $|t| \geq \alpha$. Choose $\delta > 0$ so that $\delta <

[Hints. For $0 \leq t < \infty$, prove that

$$1 + t^p \geq (1 + t)^p.$$

This implies that

$$\|f + g\|_p^p \leq \|f\|_p^p + \|g\|_p^p.$$

Next look at the function $\psi(t) = \left(1 + \frac{1}{t^p}\right)(1 + t)^{-\frac{1}{p}}$. The function $\psi$ has exactly one minimum in $[0, \infty[$ at $t = 1$. Computing this minimum, one finds that (i) can be established.]

(b) Prove that $\varrho(f, g) = \|f - g\|_p^p$ is a metric on $\mathfrak{L}_p$ under which $\mathfrak{L}_p$ is a complete metric space. [Hint. Imitate the proof of (13.11).]

(c) Suppose that $X$ contains two disjoint $\mathcal{A}$-measurable sets $A$ and $B$ each of finite positive $\mu$-measure. Prove that $\| \|_p$ is not a norm, i.e., that there are functions $f, g \in \mathfrak{L}_p$ for which $\|f + g\|_p > \|f\|_p + \|g\|_p$.

[Write $q$ for the number $\frac{1}{p}$. Note that $(1 + t)^q > 1 + t^q$ for all positive real numbers $t$. Let $f = \alpha \xi_A$ and $g = \beta \xi_B$, where $\alpha$ and $\beta$ are positive real numbers. Now computing the $\mathfrak{L}_p$-norms of $f, g$, and $f + g$, and using the inequality just noted, one can choose $\alpha$ and $\beta$ so as to solve the present problem.]

(d) In this part, let $p$ be any positive number. Suppose that no two sets in $\mathcal{A}$ of finite positive $\mu$-measure are disjoint. Determine completely the structure of $\mathfrak{L}_p(X, \mathcal

(b) Find a function $f$ on $X$ such that $f \in \mathfrak{L}_{p-\delta}$ for all $\delta > 0$ and $f \notin \mathfrak{L}_p$. [Recall that $\sum_{n=1}^{\infty} n^{-\alpha}$ converges if $\alpha > 1$ and diverges if $0 < \alpha \leq 1$.]

(c) Find a nonnegative real-valued function that is in no $\mathfrak{L}_p$.

(13.29) Exercise. Consider the set $[0, \infty[$ and Lebesgue measure $\lambda$ on it. For every $p > 0$, find a function $f$ on $[0, \infty[$ such that $f \in \mathfrak{L}_p$ and $f \notin \mathfrak{L}_q$ if $p \neq q$. [Hint. Consider the function $g$ such that $g(x) = \frac{1}{x(1 + |\log(x)|)^2}$.]

(13.30) Exercise. Let $(X, \mathcal{A}, \mu)$ be a finite measure space and let $f$ be any bounded measurable function on $X$. Prove that

$$\lim_{p \to \infty} \|f\|_p = \inf \left\{ \alpha \in R : \alpha > 0, \mu \left( \{x \in X : |f(x)| > \alpha \} \right) = 0 \right\}.$$

(13.31) Exercise. Let $p$ be a real number such that $1 \leq p < \infty$, and let $f$ be a function in $\mathfrak{L}_p(R)$ such that $f$ is uniformly continuous. Prove that $f \in \mathfrak{C}_0(R)$. Show by examples that each $\mathfrak{L}_p(R)$ contains an unbounded continuous function.

(13.32) Exercise. Let $(X, \mathcal{A}, \mu)$ be a measure space such that $\mu(X) = 1$ and let $f$ be a function in $\mathfrak{L}_1^

(13.34) Exercise: Convex functions. Let $I$ be an interval of $R$. A real-valued function $\Phi$ defined on $I$ is said to be convex if whenever $a < b$ in $I$ and $0 \leq t \leq 1$ we have

$$\Phi(t a + (1 - t) b) \leq t \Phi(a) + (1 - t) \Phi(b),$$

i.e., on the interval $[a, b]$ the graph of $\Phi$ is never above the chord [line segment] joining the points $(a, \Phi(a))$ and $(b, \Phi(b))$. Let $\Phi$ be a convex function.

(a) Prove that if $t_1, \ldots, t_n$ are positive real numbers and $\{x_1, \ldots, x_n\} \subset I$, then

$$\Phi\left(\frac{t_1 x_1 + \cdots + t_n x_n}{t_1 + \cdots + t_n}\right) \leq \frac{t_1 \Phi(x_1) + \cdots + t_n \Phi(x_n)}{t_1 + \cdots + t_n}.$$

[Use induction.]

(b) Prove that $\Phi$ is continuous on the interior $I^\circ$ of $I$ and show by an example that $\Phi$ may be discontinuous at the endpoints of $I$.

(c) Prove that if $c$ is in $I^\circ$, then there exists a real number $\alpha$ such that $\Phi(u) \geq \alpha(u - c) + \Phi(c)$ for all $u \in I$, i.e., the line through $(c, \Phi(c))$ having slope $\alpha$ is always below or on the graph of $\Phi$.

(d) Prove the following generalization of inequality (i). Let $(X, \mathcal{A}, \mu)$ be a finite measure space. If $f \in \mathfrak{L}_1^r(X, \mathcal{A}, \mu)$, if $f(X) \subset I$, and if $\Phi \circ f \

Let $\mathfrak{L}_{\Phi}$ be the set of all complex-valued $\mathcal{A}$-measurable functions $f$ on $X$ such that

$$\|f\|_{\Phi} = \sup \left\{ \|f g\|_1 : g \in \mathfrak{L}_{\Psi}^{\dagger}, \int_X \Psi \circ |g| d\mu \leq 1 \right\} < \infty.$$

Prove that:

(b) $\mathfrak{L}_{\Phi}^{\dagger} \subset \mathfrak{L}_{\Phi}$ [use (13.2)];
(c) $\mathfrak{L}_{\Phi}$ is a complex linear space;
(d) $\| \|_{\Phi}$ is a norm on $\mathfrak{L}_{\Phi}$, where functions equal a.e. are identified;
(e) with the norm $\| \|_{\Phi}$, $\mathfrak{L}_{\Phi}$ is a Banach space. [First suppose that $\mu(X) < \infty$. Prove that if $\|f_n - f_m\|_{\Phi} \to 0$, then $\|f_n - f_m\|_1 \to 0.$]

The spaces $\mathfrak{L}_{\Phi}$ are called Birnbaum-Orlicz spaces. For further information about these spaces, the reader should consult A. C. Zaanen, Linear Analysis, Vol. I [New York: Interscience Publishers, 1953].

(13.37) Exercise. Define $\Phi$ on $[0, \infty[$ by $\Phi(t) = 0$ if $0 \leq t \leq 1$ and $\Phi(t) = t \cdot \log t$ if $t \geq 1$. The Birnbaum-Orlicz space $\mathfrak{L}_{\Phi}(X, \mathcal{A}, \mu)$ [see (13.36)] is often denoted $\mathfrak{L} \log^+ \mathfrak{L}$. Prove that for the measure space $([0, 1], \mathcal{M}_{\lambda}, \lambda)$

For $\varepsilon > 0$, let $\delta$ be as in (ii). Use Egorov's theorem to find $B \in \mathcal{A}$ such that $\mu(B) < \delta$ and $f_n \rightarrow f$ uniformly on $B'$. Use Fatou's lemma to prove that $\int_B |f|^p d\mu \leq \varepsilon$. Then use Minkowski's inequality to show that $\int_X |f - f_n|^p d\mu < 3^p \varepsilon$ for all large $n$. Thus conclude that $f = (f - f_n) + f_n \in \mathfrak{L}_p$ and $\|f - f_n\|_p \rightarrow 0.$

Vitali's convergence theorem has considerable theoretical importance and can also be frequently applied to prove other useful theorems. The next exercise is also useful for applications [see for example (20.58) infra] and so we provide plentiful hints for its proof.

(13.39) Exercise. Let $(X, \mathcal{A}, \mu), p, (f_n)$, and $f$ be as in (13.38). Suppose that $f_n \rightarrow f \mu$-a.e. For each $(n, k) \in N \times N$ let $B_{n,k} = \{x \in X : |f_n(x)|^p \geq k\}.$

(a) Suppose that condition (13.38.i) holds [as it does, for example, if $\mu(X) < \infty$]. Prove that the following four assertions are equivalent:

(i) $f \in \mathfrak{L}_p$ and $\|f - f_n\|_p \rightarrow 0;$

(ii) if $(E_k)_{k=1}^{\infty} \subset \mathcal{A}, E_1 \supset E_2 \supset \cdots,$ and $\bigcap_{k=1}^{\infty} E_k = \varnothing,$ then $\lim_{k \rightarrow \infty} \int_E |f_n|^p d\mu = 0$ uniformly in $n;$

(iii) $\lim_{k

and for all $n$,

$$\int_{F_k} |f_n|^p d\mu < \varepsilon.$$

For $n \geq k_0$, we have $B_{n,k_0} \subset E_{k_0}$ and so for $n \geq k_0$ and $k \geq k_0$, it follows that

$$\int_{B_{n,k}} |f_n|^p d\mu \leq \int_{B_{n,k_0}} |f_n|^p d\mu \leq \int_{E_{k_0}} |f_n|^p d\mu = \int_{F_{k_0}} |f_n|^p d\mu < \varepsilon.$$

For $n \in \{1, \ldots, k_0 - 1\}$, we have $|f_n|^p \leq \max\{|f_1|^p, \ldots, |f_{k_0-1}|^p\} = g$, and so $\int_{B_{n,k}} |f_n|^p d\mu \leq \int_{B_k} g d\mu$, where $B_k = \bigcup_{n=1}^{k_0-1} B_{n,k} = \{x \in X : g(x) \geq k\}$. Thus dominated convergence applies, and so (iii) holds if (ii) holds.

Finally, suppose that (iii) holds. Choose $k_0$ so large that if $k \geq k_0$ and $n \in N$, we have

$$\int_{B_{n,k}} |f_n|^p d\mu < \varepsilon^p.$$

If $E \in \mathcal{A}$ and $\mu(E) < k_0^{-1} \varepsilon^p$, then

$$\left( \int_{E} |f_n|^p d\mu \right)^{\frac{1}{p}} \leq \left( \int_{E \cap B_{n,k_0}} |f_n|^p d\mu \right)^{\frac{1}{p}} + \left( \int_{E \cap B'_{n,k_0}} |f_n|^p d\

stronger than either [meas.] or [mean-$p$] on finite measure spaces, but for infinite measure spaces there is no implication running either way.

We now introduce a fifth kind of convergence for functions in $\mathfrak{L}_p$ spaces, and will study its relations with the notions studied previously.
