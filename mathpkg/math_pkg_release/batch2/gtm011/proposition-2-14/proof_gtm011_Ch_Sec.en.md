---
role: proof
locale: en
of_concept: proposition-2-14
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Let $n = n(r) =$ the number of zeros of $f$ in $B(0; r)$; according to the Poisson-Jensen formula

$$\log |f(z)| = -\sum_{k=1}^{n} \log \left| \frac{r^2 - \bar{a}_k z}{r(z - a_k)} \right| + \frac{1}{2\pi} \int_{0}^{2\pi} \text{Re} \left( \frac{re^{i\theta} + z}{re^{i\theta} - z} \right) \log |f(re^{i\theta})| d\theta$$

for $|z| < r$. Using Exercise 1 and Leibniz's rule for differentiating under an integral sign this gives

$$\frac{f'(z)}{f(z)} = \sum_{k=1}^{n} (z - a_k)^{-1} + \sum_{k=1}^{n} \bar{a}_k (r^2 - \bar{a}_k z)^{-1}$$

$$+ \frac{1}{2\pi} \int_{0}^{2\pi} 2re^{i\theta} (re^{i\theta} - z)^{-2} \log |f(re^{i\theta})| d\theta$$

for $|z| < r$ and $z \neq a_1, \ldots, a_n$. Differentiating $p$ times yields:

$$\frac{d^p}{dz^p} \left[ \frac{f'(z)}{f(z)} \right] = -p! \sum_{k=1}^{n} (a_k - z)^{-p-1} + p! \sum_{k=1}^{n} \bar{a}_k^{p+1} (r^2 - \bar{a}_k z)^{-p-1}$$

$$+ (p+1)! \frac{1}{2\pi} \int_{0}^{2\pi} 2re^{i\theta} (re^{i\theta} - z)^{-p-2} \log |f(re^{i\theta})| d\theta.$$

Now as $r \to \infty$, $n(r

So for $2|z| < r$, the absolute value of the integral in (3.2) is dominated by

$$2(p+1)! 2^{p+3} r^{-(p+1)} \frac{1}{2\pi} \int_{0}^{2\pi} [\log M(r) - \log |f(re^{i\theta})|] d\theta.$$

But according to Jensen's Formula,

$$\frac{1}{2\pi} \int_{0}^{2\pi} \log |f(re^{i\theta})| d\theta \geq 0$$

since $f(0) = 1$. Also $\log M(r) \leq r^{\lambda+\epsilon}$ for sufficiently large $r$ so that (3.3) is dominated by

$$2(p+1)! 2^{p+3} r^{\lambda+\epsilon-(p+1)}$$

As before, $\epsilon$ can be chosen so that $r^{\lambda+\epsilon-(p+1)} \to 0$ as $r \to \infty$.

Note that the preceding lemma implicitly assumes that $f$ has infinitely many zeros. However, if $f$ has only a finite number of zeros then the sum in Lemma 3.1 becomes a finite sum and the lemma remains valid.

3.4 Hadamard's Factorization Theorem. If $f$ is an entire function of finite order $\lambda$ then $f$ has finite genus $\mu \leq \lambda$.

Proof. Let $p$ be the largest integer less than or equal to $\lambda$; so $p \leq \lambda < p+1$. The first step in the proof is to show that $f$ has finite rank and that the rank is not larger than $p$. So let $\{a_1, a_2, \ldots\}$ be the zeros of $f$ counted according to multiplicity and arranged such that $|a_1| \leq |a_2| \leq \ldots$. It must be shown that

$$\sum_{n=1}^{\infty} |a_n|^{-(p+1)} < \infty.$$

There is no loss in generality in assuming that $f(0) = 1$. Indeed, if $f$ has a

for $k > k_0$. So if $\epsilon$ is chosen with $\lambda + \epsilon < p + 1$ (recall that $\lambda < p + 1$) then $\sum |a_k|^{-(p+1)}$ is dominated by a convergent series; (3.5) now follows.

Let $f(z) = P(z) \exp (g(z))$ where $P$ is a canonical product in standard form. Hence for $z \neq a_k$

$$\frac{f'(z)}{f(z)} = g'(z) + \frac{P'(z)}{P(z)}$$

Using Lemma 3.1 gives that

$$-p! \sum_{n=1}^{\infty} (a_n - z)^{-(p+1)} = g^{(p+1)}(z) + \frac{d^p}{dz^p} \left[ \frac{P'(z)}{P(z)} \right]$$

However it is easy to show that

$$\frac{d^p}{dz^p} \left[ \frac{P'(z)}{P(z)} \right] = -p! \sum_{n=1}^{\infty} (a_n - z)^{-(p+1)}$$

for $z \neq a_1, a_2, \ldots$. Hence $g^{(p+1)} \equiv 0$ and $g$ must be a polynomial of degree $\leq p$. So the genus of $f \leq p \leq \lambda$.

As an application of Hadamard’s Theorem a special case of Picard’s Theorem can be proved. This theorem is proved in full generality in the next chapter.
