---
role: proof
locale: en
of_concept: prop-m-exists-if-and-only-if
source_book: gtm034
source_chapter: "4"
source_section: "009"
---

Proof: According to theorem T17.1, $T = \infty$ with positive probability if and only if (a) holds. But now it should be intuitively clear that $T = \infty$ with positive probability if and only if $M$ exists: one verifies that $\lim_{n \to \infty} S_n = -\infty$, so that $M < \infty$ with probability one if $T = \infty$ with positive probability, while $\lim_{n \to \infty} S_n = +\infty$ with probability one otherwise. We omit the details because it seems more amusing to give an alternative purely analytic proof of P2, based on the remarks preceding its statement.

First one verifies, using P1 and the relevant definitions, that

(1) $(1 - t) \sum_{n=0}^{\infty} t^n \mathbf{E}[z^M_n] = e^{-\sum_{1}^{\infty} \frac{t^k}{k} \mathbf{E}[1 - z^S_k : S_k > 0]}$

for $0 \leq t < 1, |z| \leq 1$. Now let us assume that $M$ exists. Then

$$\lim_{n \to \infty} \mathbf{E}[z^M_n] = \mathbf{E}[z^M]$$

exists and by Abel's theorem

(2) $\mathbf{E}[z^M] = \lim_{t \nearrow 1} (1 - t) \sum_{n=0}^{\infty} t^n \mathbf{E}[z^M_n].$

Now set $z = 0$ in (1) and then let $t \nearrow 1$. Then one gets from (1) and (2)

(3) $\mathbf{P}[M =

In view of the monotonicity of the sequence $M_n$ this implies that $E[z^{M_n}]$ has a limit, which is given by (b); and, as remarked immediately prior to the statement of P2, we can conclude that $M$ exists (is finite) with probability one.

E1 Consider the left-continuous random walk of E17.2. It is necessary and sufficient for the existence of $M$ that the mean $\mu$ be negative. In equations (2), (3), and (4) of E17.2 we calculated $f_i(t;z), f_e(t;z)$ and $c(t)$. Applying P1 one gets

$$\sum_{n=0}^{\infty} t^n E[z^{M_n}] = [c(t)f_i(t;z)f_e(t,1)]^{-1} = \frac{1}{1-r(t)} \cdot \frac{z-r(t)}{z-tP(z)},$$

where

$$P(z) = \sum_{n=0}^{\infty} P(0,n-1)z^n.$$

Using P2 we have, assuming $\mu < 0$,

$$E[z^{M}] = \lim_{t \to 1} \frac{1-t}{1-r(t)} \cdot \frac{z-r(t)}{z-tP(z)}.$$

When $\mu < 0$ we saw in section 17 that $r(1) = 1$, and that

$$\lim_{t \to 1} \frac{1-t}{1-r(t)} = 1 - \lim_{r \to 1} \frac{1-P(r)}{1-r} = -\mu,$$

so that one obtains

$$E[z^{M}] = -\mu \frac{z-1}{z-P(z)}, \quad \mu < 0.$$

There is one more question of obvious interest. To find the first moment of $M$, we differentiate the generating function of $M$ to get

$$E[M] = -\mu \lim_{z \to 1} \frac{d}{dz} \left( \frac{z-1}{z-P(z)} \right).$$

Because $P'(1) = \mu + 1$,

and only if the random walk has a finite second moment. Indeed it has been shown$^8$ that this phenomenon is quite general:

For every one-dimensional random walk with $m < \infty$ and $\mu < 0$,

$$E[M^k] < \infty \text{ if and only if } m^+_{k+1} = \sum_{n=0}^{\infty} n^{k+1} P(0,n) < \infty.$$

Finally we consider the Green function of the half-line and some of the very simplest applications.
