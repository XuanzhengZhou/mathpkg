---
role: proof
locale: en
of_concept: "let-be-a-lebesgue-measurable-function-on-let"
source_book: gtm025
source_chapter: "The Lebesgue Integral"
source_section: "12.44"
---

For $f \geq 0$, the translation and inversion invariance of the Riemann integral makes it clear that

$$\bar{S}(f_t) = \bar{S}(f^\star) = \bar{S}(f).$$

(1)

[Use (8.15.iv), (8.15.v), (9.8), and (9.15).] Now call on (12.35); and refer to (12.2) and (12.26) for conditions under which the integrals in (i) are defined. $\square$

(12.45) Continuous images of measures. This construction requires some preliminary explanation, although the basic idea is simple enough. Let $X$ and $Y$ be locally compact Hausdorff spaces, and let $\varphi$ be a continuous mapping of $X$ onto $Y$. Suppose that we are given a measure $\mu$ on $X$ in the sense of §9, and make the hypothesis that

(i) $\varphi^{-1}(F)$ is compact in $X$ for every compact subset $F$ of $Y$ or that

(ii) $\mu(X)$ is finite.

Consider an arbitrary function $f \in \mathfrak{C}_{00}(Y)$. It is easy to see that the composite function $f \circ \varphi$ is in $\mathfrak{L}_1(X, \mathfrak{M}_\mu, \mu)$, since it is in $\mathfrak{C}_{00}(X)$ if (i) holds and is a bounded continuous function in any case and so is in $\mathfrak{L}_1(X, \mathfrak{M}_\mu, \mu)$ if $\mu(X)$ is finite. Therefore the mapping

(iii) $$f \

and it is obvious that $\mathfrak{R}$ is directed upward in the sense of (9.11). Taking note of (12.35) and applying (9.11) twice, we find that

$$\nu(U) = \int_Y \xi_U(y) d\nu(y) = \sup \left\{ \int_Y f(y) d\nu(y) : f \in \mathfrak{R} \right\}$$

$$= \sup \left\{ \int_X f \circ \varphi(x) d\mu(x) : f \in \mathfrak{R} \right\}$$

$$= \int_X \sup \left\{ f \circ \varphi(x) : f \in \mathfrak{R} \right\} d\mu(x) = \int_X \xi_U \circ \varphi(x) d\mu(x)$$

$$= \mu(\varphi^{-1}(U)).$$

(1)

Next suppose that $B$ is an arbitrary subset of $Y$. Theorem (9.24) and (1) show that

$$\nu(B) = \inf \{ \nu(U) : U \text{ is open in } Y \text{ and } U \supset B \}$$

$$= \inf \{ \mu(\varphi^{-1}(U)) : U \text{ is open in } Y \text{ and } U \supset B \}$$

$$\geq \mu(\varphi^{-1}(B)).$$

(2)

In particular, if $\nu(B) = 0$, then (i) holds for $B$. If $F$ is a compact subset of $Y$, then $F$ is contained in an open set $U$ such that $U^{-}$ is compact (6.79). Thus $\nu(U)$ is finite (9.27), and so

$$\nu(U) - \nu(U \cap F') = \nu(F).$$

(3)

Apply (1) to (3) and note that $U \cap F'$ is open:

$$\nu(F) = \mu(\varphi^{-1}(U)) - \mu(\varphi^{-1}(U \cap F'))$$

$$= \mu(\varphi^{-1}(U) \cap (\varphi^{-1}(U \cap F'))

because of (2). If $B$ is not $\sigma$-finite, let $E$ be any compact subset of $X$. We have

$$E \cap \varphi^{-1}(B) = E \cap \varphi^{-1}(\varphi(E) \cap B)$$

since $\varphi$ is single-valued. The set $\varphi(E) \cap B$ is plainly $\nu$-measurable and finite for $\nu$, so that $\varphi^{-1}(\varphi(E) \cap B)$ is $\mu$-measurable, as was just proved. Thus $E \cap \varphi^{-1}(B)$ is in $M_\mu$, and (10.31) implies that $\varphi^{-1}(B)$ is in $M_\mu$.

It is now obvious that for every $\nu$-measurable complex function $f$ on $Y$, the function $f \circ \varphi$ on $X$ is $\mu$-measurable. Using (i), it is easy to establish (ii). Consider $f \in \mathfrak{L}_1(Y, M_\nu, \nu)$; we may suppose that $f \geq 0$. By (11.35) there is a nondecreasing sequence $(s_n)_{n=1}^{\infty}$ of simple, $\nu$-measurable functions such that $\lim_{n \to \infty} s_n(y) = f(y)$ everywhere on $Y$. Plainly

$$\int_Y s_n(y) d\nu(y) \leq \int_Y f(y) d\nu(y) < \infty. \tag{7}$$

Write $s_n = \sum_{k=1}^{m} \alpha_k \xi_{B_k}$, where $0 < \alpha_1 < \cdots < \alpha_m$. Then $\nu(B_k)$ is finite for all $k$, as (7) proves, and (12.4) and (i) imply that

$$\int_Y s_n(y) d\nu(y) = \sum_{k=1}^{m} \alpha_k \nu(B_k) = \sum_{k=1}^{m} \alpha_k \mu(\varphi^{-1}(B_k))$$

$$= \int_X \left( \sum_{k=1}^{m} \alpha_k \xi

That is, identifying functions equal a.e., we have defined a complete metric space $\mathfrak{F}$.

(e) For $f \in \mathfrak{F}$ and $(f_n) \subset \mathfrak{F}$ we have $\varrho(f_n, f) \to 0$ if and only if $f_n \to f$ in measure. For this reason we call $\varrho$ the metric of convergence in measure.

(12.48) Exercise. Let $(X, \mathcal{A}, \mu)$ be any measure space and let $f$ be a nonnegative, real-valued, bounded, $\mathcal{A}$-measurable function on $X$. Let $\alpha = \inf\{f(x) : x \in X\}$ and $\beta = \sup\{f(x) : x \in X\}$. For $n \in N$ and $j = 1, 2, \ldots, n - 1$, let

$$A_j = \left\{x \in X : \alpha + \frac{(j - 1)(\beta - \alpha)}{n} \leq f(x) < \alpha + \frac{j(\beta - \alpha)}{n}\right\}$$

and let

$$A_n = \left\{x \in X : \alpha + \frac{(n - 1)(\beta - \alpha)}{n} \leq f(x) \leq \beta\right\}.$$

The Lebesgue sums for $f$ are defined as the numbers

$$s_n = \sum_{j=1}^{n} \left(\alpha + \frac{(j - 1)(\beta - \alpha)}{n}\right) \mu(A_j).$$

Prove that $\lim_{n \to \infty} s_n = \int_X f d\mu$.

Next suppose that $\mu(X) < \infty$. Let $f$ be any bounded, real-valued, $\mathcal{A}$-measurable function on $X$. Define $s_n$ as above. Prove that $\lim_{n \to \infty} s_n = \int_X f d\mu$.

(12.49) Exercise. Let $(X, \mathcal{A}, \mu)$ be

Let $(\Delta_j)_{j=1}^{\infty}$ be a sequence of subdivisions of $[a, b]$, say

$$\Delta_j = \{a = x_0^{(j)} < x_1^{(j)} < \cdots < x_{n_j}^{(j)} = b\},$$

such that

$$\lim_{j \to \infty} \max \{x_k^{(j)} - x_{k-1}^{(j)} : 1 \leq k \leq n_j\} = 0.$$

Let

$$m_k^{(j)} = \inf \{f(t) : x_{k-1}^{(j)} \leq t \leq x_k^{(j)}\}, \quad M_k^{(j)} = \sup \{f(t) : x_{k-1}^{(j)} \leq t \leq x_k^{(j)}\},$$

$$\varphi_j = \sum_{k=1}^{n_j} m_k^{(j)} \xi_{x_{k-1}^{(j)}, x_k^{(j)}}$$

and

$$\psi_j = \sum_{k=1}^{n_j} M_k^{(j)} \xi_{x_{k-1}^{(j)}, x_k^{(j)}}.$$

Prove that:

(b) if $x \in [a, b]$ and $x$ is distinct from all $x_k^{(j)}$, then $\lim_{j \to \infty} \varphi_j(x) = m(x)$ and $\lim_{j \to \infty} \psi_j(x) = M(x)$;

(c) $m$ and $M$ are Lebesgue measurable on $[a, b]$;

(d) if $L(f, \Delta_j)$ and $U(f, \Delta_j)$ are the lower and upper Darboux sums respectively [defined with $\alpha(x) = x$] for the function $f$ corresponding to the subdivision $\Delta_j$, then

$$\lim_{j \to \infty} L(f, \Delta_j) = \int_a^b m(x) \, dx$$

and

$$\lim_{j \to \infty} U(f, \Delta_j) = \int_a^b M(x) \, dx;$$

(e) $f$ is Riemann integra

(16.34) infra. Hints are as follows. Since $\int_{a}^{b} f(t) dt$ exists and is finite, $|f|$ is in $\mathcal{L}_1([a, b], \mathcal{M}_1, \lambda)$. It is evident from (6.59), (12.32), and our hypothesis that $\int_{U} f d\lambda = 0$ for all open subsets $U$ of $[a, b]$. Use (9.24) to infer that $\int_{A} f d\lambda = 0$ for all $\lambda$-measurable sets $A \subset [a, b]$. From this the identity $f = 0$ $\lambda$-a.e. is immediate.]

(12.55) Exercise. Let $X$ be a locally compact Hausdorff space such that every open subset of $X$ is $\sigma$-compact. Suppose that $\mu$ is a measure defined on $\mathcal{B}(X)$ such that $\mu(F) < \infty$ for all compact sets $F \subset X$. Prove that $\mu$ is a regular measure. [First consider the case that $X$ is compact. Consider the family $\mathcal{R} = \{E \in \mathcal{B}(X) : \mu(E) = \inf \{\mu(U) : U \text{ is open}, U \supset E\}\}$ and $\mu(E) = \sup \{\mu(F) : F \text{ is compact}, F \subset E\}\}.]

(12.56) Exercise. Let $\mu$ be a measure defined on $\mathcal{B}(R)$ such that $\mu([0, 1]) = 1$ and $\mu(E + x) = \mu(E)$ for every $E \in \mathcal{B}(R)$ and $x \in R$. Prove that $\mu(E) = \lambda(E)$ for all $E \in \mathcal{B}(R)$. [First prove that $\mu(\{x\}) = 0$ for all $x \in R$. Next show that $\mu([a, b]) = b - a$ for all $a < b$ in $R$. Use (12.55)].

(

stant on each $E_k$ except for a set of $\mu$-measure zero, and accordingly write the integral $\int_X f d\mu$ as a certain finite sum.

(12.61) Exercise. Let $(X, \mathcal{A}, \mu)$ be a measure space that is degenerate in the sense of (10.3): $\mu(A) = 0$ or $\mu(A) = \infty$ for all $A \in \mathcal{A}$. Show that every function $f \in \mathcal{L}_1(X, \mathcal{A}, \mu)$ vanishes except on a set of $\mu$-measure zero and that $\int_X |f| d\mu = 0$. [This unpleasant property justifies the term "degenerate" for the measure spaces under consideration.]

(12.62) Exercise. Let $X$ be a locally compact, $\sigma$-compact Hausdorff space and let $\mu$ be a regular measure defined on a $\sigma$-algebra $\mathcal{A}$ of subsets of $X$ [$\mathcal{A} \supset \mathcal{B}(X)$]. Let $f$ be an $\mathcal{A}$-measurable function on $X$ such that $f(X) \subset [0, \infty]$ and such that $f\xi_F \in \mathcal{L}_1(X, \mathcal{A}, \mu)$ for all compact subsets $F$ of $X$. [Such an $f$ is called locally $\mu$-integrable.] Define the set-function $\nu$ on $\mathcal{A}$ by

$$\nu(A) = \int_A f(x) d\mu(x).$$

Prove that $\nu$ is a regular measure on $\mathcal{A}$.

(12.63) Exercise: Integrals on the completion of a measure space. Let $(X, \mathcal{A}, \mu)$ be a measure space and $(X, \bar{\mathcal{A}}, \bar{\mu})$ its completion (11.21).

(a) Let $\bar{f}$ be a complex- or extended real-valued $\bar{\mathcal{A}}$-measurable function defined on $X$. Prove that there is an $\mathcal{A}$-measurable function $f$

denote the Borel sets of $X$. Prove that $(X, \mathcal{M}_i, \iota)$ is the completion of $(X, \mathcal{B}(X), \iota)$. What does this tell you about Borel measurable functions and arbitrary $\mathcal{M}_i$-measurable functions? [Use part (a).]

(d) Drop the hypothesis in part (c) that $X$ be $\sigma$-finite. Let $f$ be an arbitrary function in $\mathfrak{L}_1(X, \mathcal{M}_i, \iota)$. Prove that there is a Borel measurable function $f_1$ on $X$ such that $f_1 = f \iota$-almost everywhere and such that $|f_1| \leq |f|$. [Consider a subset $Y$ of $X \sigma$-finite with respect to $\iota$ such that $f$ vanishes on $Y'$ [$Y$ can be chosen to be open if you like], and then argue as in part (c).]

(12.64) Exercise. Let $(X, \mathcal{A}, \mu)$ be a measure space and let $f$ be a complex-valued $\mathcal{A}$-measurable function on $X$. Prove that $f \in \mathfrak{L}_1(X, \mathcal{A}, \mu)$ if and only if there exists a sequence $(s_n)$ of simple functions such that $(s_n) \subset \mathfrak{L}_1, s_n \rightarrow f$ in measure, and

$$\lim_{m, n \rightarrow \infty} \int_X |s_m - s_n| d\mu = 0.$$

In this case we have

$$\int_X f d\mu = \lim_{n \rightarrow \infty} \int_X s_n d\mu.$$

[If one first defines $\int_X s d\mu$ for complex-valued, $\mathcal{A}$-measurable, simple functions, then the above facts can be used to define $\mathfrak{L}_1$ and the integral on $\mathfrak{L}_1$. This approach is useful when dealing with functions with values in a Banach space. It does not depend

CHAPTER FOUR

Function Spaces and Banach Spaces

The theory of integration developed in Chapter Three enables us to define certain spaces of functions that have remarkable properties and are of enormous importance in analysis as well as in its applications. We have already, in §7, considered spaces whose points are functions. In §7, we considered only the uniform norm $\| \|_u$ [see (7.3)] to define the distance between two functions. The present chapter is concerned with norms that are defined in one way or another from integrals. The most important such norms are defined and studied in §13. These special norms lead us very naturally to study abstract Banach spaces, to which §14 is devoted. While we are not concerned with Banach spaces per se, it is an inescapable fact that many results can be proved as easily for all Banach spaces [perhaps with some additional property] as for the special Banach spaces defined in §§7 and 13. Our desires both for economy of effort and for clarity of exposition dictate that we treat these results in general Banach spaces. In §15, we give a strictly computational construction of the conjugate spaces of the function spaces $\mathfrak{L}_p(1 < p < \infty)$. We have chosen this construction because of its elementary nature and also because we think that manipulation of inequalities is something that every student of analysis should learn. In §16, we consider Hilbert spaces, which are $\mathfrak{L}_2$ spaces looked at abstractly, and also give some concrete examples and illustrations.

All of the sections of this chapter are important, and the reader is advised to study them all.

§13. The spaces $\mathfrak{L}_p(1 \leq p < \infty)$

As usual, we begin with a definition.
