---
role: proof
locale: en
of_concept: "with-the-algebraic-operations-71i71iii-and-the-norm"
source_book: gtm025
source_chapter: "Spaces of Continuous Functions"
source_section: "7.9"
---

The only nonobvious point is the completeness of $\mathfrak{C}(X)$ in the uniform metric. Let $(f_n)_{n=1}^{\infty}$ be a sequence of functions in $\mathfrak{C}(X)$ such that

$$\lim_{m,n \to \infty} \|f_n - f_m\|_u = 0.$$

(1)

That is,

$$\lim_{m,n \to \infty} \left[ \sup \left\{ |f_n(x) - f_m(x)| : x \in X \right\} \right] = 0.$$

(2)

For every fixed $x \in X$, (2) implies that

$$\lim_{m,n \to \infty} |f_n(x) - f_m(x)| = 0,$$

and so $(f_n(x))_{n=1}^{\infty}$ is a Cauchy sequence in $K$. Since $K$ is complete [use (6.50) with $n = 1$], the sequence $(f_n(x))$ has a

$$|f_n(x) - f(x)| \leq |f_m(x) - f_n(x)| + |f_m(x) - f(x)|$$
$$< \frac{\varepsilon}{3} + \frac{\varepsilon}{3}$$
$$= \frac{2}{3} \varepsilon$$

(6)

for all $n \geq p$. The integer $p$ is independent of $x$, and as $x$ is arbitrary in (6), we may take the supremum in (6) to write

$$\|f_n - f\|_u = \sup\{|f_n(x) - f(x)| : x \in X\}$$
$$\leq \frac{2}{3} \varepsilon$$
$$< \varepsilon$$

if $n \geq p$. That is, (3) holds.

It remains to prove that $f \in \mathfrak{C}(X)$. Choose $n$ so that $\|f - f_n\|_u < 1$. Then it is evident that $|f(x)| < |f_n(x)| + 1$ for all $x \in X$, and so $\|f\|_u$ exists and does not exceed $\|f_n\|_u + 1$. To prove that $f$ is continuous, let $x$ be any point in $X$, let $\varepsilon$ be a positive number, and let $n$ be so large that $\|f_n - f\|_u < \frac{\varepsilon}{3}$. Let $U$ be a neighborhood of $x$ such that

$$|f_n(y) - f_n(x)| < \frac{\varepsilon}{3} \quad \text{for all} \quad y \in U.$$

For $y \in U$, we thus see that

$$|f(y) - f(x)| \leq |f(y) - f_n(y)| + |f_n(y) - f_n(x)| + |f_n(x) - f(x)|$$
$$\leq \|f - f_n\|_u + |f_n(y) - f_n(x)| + \|f_n - f\|_u$$
$$< \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3}$$

(a) Every noncompact metric space admits an unbounded continuous real-valued function.

(b) Let $P_{\Omega}$ be the well-ordered set defined in (4.49). Let $\mathcal{B}$ be the family of all sets of the form $\{0\}$ or $\{\gamma \in P_{\Omega} : \alpha < \gamma \leq \beta\}$ where $\alpha < \beta < \Omega$. Then $\mathcal{B}$ is a base for the order topology of $P_{\Omega}$ [cf. (6.96) and (6.98)]. The topological space $P_{\Omega}$ is a locally compact Hausdorff space; in fact every subspace $\{\gamma \in P_{\Omega} : \alpha \leq \gamma \leq \beta\}$ is compact. Also $P_{\Omega}$ is noncompact, although it is both sequentially compact and Fréchet compact. [Again see (6.96) and (6.98).]

(c) Every continuous complex-valued function $f$ on $P_{\Omega}$ is ultimately constant: there are an ordinal $\alpha \in P_{\Omega}$ and a complex number $t$ such that $f(\gamma) = t$ for all $\gamma \geq \alpha$. Consequently every continuous complex-valued function on $P_{\Omega}$ is bounded.

(d) Let $X$ be a topological space, and let $\mathfrak{C}_a(X)$ denote the set of all continuous complex-valued functions on $X$, bounded or unbounded. If $\mathfrak{C}_a(X)$ contains unbounded functions, we cannot impose the uniform norm $\| \cdot \|_u$ on $\mathfrak{C}_a(X)$. However, an analogue of (7.9) does hold. If $(f_n)_{n=1}^{\infty}$ is a sequence of functions in $\mathfrak{C}_a(X)$ for which all differences $f_n - f_m$ are bounded, and if

$$\lim_{m,n \to \infty} \| f_n - f_m \|_u = 0,$$

then there is an $f \in \mathfrak{C}_a(X)$ such that

is not in general closed: its closure is $\mathfrak{C}_0(X)$. [A proof of the last statement is indicated in (7.41) below.]

Several concepts closely related to, but not identical with, continuity are needed in our treatment of integration theory. We now take them up.
