---
role: proof
locale: en
of_concept: prop-if-is-integrable-on-then
source_book: gtm034
source_chapter: "2"
source_section: "005"
---

Proof: First we derive Bessel's inequality: if a function $g(\theta)$ on $C$ is square integrable and has Fourier coefficients

$$a(x) = (2\pi)^{-d} \int e^{ix \cdot \theta} g(\theta) d\theta, \quad x \in R,$$

then

(1) $$\sum_{x \in R} |a(x)|^2 \leq (2\pi)^{-d} \int |g(\theta)|^2 d\theta.$$

The proof of (1) is elementary, unlike that of Parseval's identity which was mentioned in section 6; for if

$$g_M(\theta) = \sum_{|x| \leq M} a(x) e^{ix \cdot \theta}, \quad \theta \in E,$$

then P6.1 gives

$$0 \leq (2\pi)^{-d} \int |g(\theta) - g_M(\theta)|^2 d\theta = (2\pi)^{-d} \int |g(\theta)|^2 d\theta - \sum_{|x| \leq M} |a(x)|^2$$

for every $M > 0$, which implies (1).

To prove P1 we now decompose $f(\theta)$. For every $A > 0$,

$$f(\theta) = g_A(\theta) + h_A(\theta), \quad \theta \in E$$

where

$$g_A(\theta) = f(\theta) \text{ when } |f(\

Since $g_A(\theta)$ is bounded, it is square integrable, so that (1) implies that $a_A(x) \to 0$ as $|x| \to \infty$. Also

(3) $b_A(x) \leq (2\pi)^{-d} \int |h_A(\theta)| d\theta = (2\pi)^{-d} \int_{[\theta] |f(\theta)| > A} f(|\theta|) d\theta = \beta_A$

where $\beta_A$ tends to zero as $A \to \infty$. It follows from (2) that

$$\lim_{|x| \to \infty} (2\pi)^{-d} \int e^{ix \cdot \theta} f(\theta) d\theta \leq \lim_{|x| \to \infty} a_A(x) + \lim_{|x| \to \infty} b_A(x) \leq \beta_A$$

or every $A > 0$. By letting $A \to \infty$ we are therefore able to complete the proof of P1.

Now we shall apply the Riemann Lebesgue Lemma to the discussion of certain aspects of aperiodic transient random walk. According to T2.1

$$G(0,x) = \sum_{n=0}^{\infty} P_n(0,x) < \infty$$

for all $x$ in $R$, if $P(x,y)$ is the transition function of an arbitrary transient random walk. We shall prove (a brief discussion of this result precedes the proof of P3)
