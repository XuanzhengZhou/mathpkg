---
role: proof
locale: en
of_concept: thm-is-subject-to-the-truth-of
source_book: gtm034
source_chapter: "3"
source_section: "006"
---

Proof: Restrict $x$ to $B$ in P4 and operate by $K_B$ on the left in P4. This yields

(1) $$K_B(x,y) = K_B(x \cdot) \mu_B(y) + \Pi_B(x,y) - \delta(x,y)$$

for $x, y \in B$. Summing $x$ over $B$ one has, in view of P2,

(2) $$K_B(\cdot y) = K_B(\cdot) \mu_B(y).$$

If we had $K_B(\cdot) = 0$ here, it would follow that $K_B(\cdot y) = 0$ for all $y$ in $B$. But then $K_B$, regarded as a matrix operator, would be singular, which is impossible since $K_B$ has as its inverse the operator $A(x,y)$ restricted to $B$. Therefore $K_B(\cdot) \neq 0$.

Now $K_B(\cdot y) = K_B(\cdot) \mu_B(y)$ shows that either $K_B(\cdot y) \geq 0$ on $B$ or $K_B(\cdot y) \leq 0$ on $B$. Since $\sum_{t \in B} K_B(\cdot t) A(t,x) = 1$ for $x \in B$ and $A(x,y) \ge

Proof: Of course we are interested only in the recurrent case, the truth of P1 in the transient case being not only obvious, but also quite irrelevant to the work in the preceding section. The proof will be Fourier analytical, and we adopt the notation of Chapter II, letting $\phi(\theta)$ denote the characteristic function of the random walk. Using P6.3 we have

(1) $a_n(x) = (2\pi)^{-2} \int \frac{1 - e^{iz \cdot \theta}}{1 - \phi(\theta)} [1 - \phi^{n+1}(\theta)] d\theta$.

(Equation (1) is the result of a straightforward calculation based on

$$\sum_{k=0}^{n} P_k(x,y) = (2\pi)^{-2} \int e^{i\theta \cdot (x-y)} [1 + \phi(\theta) + \cdots + \phi^n(\theta)] d\theta.$$

The integration is over the usual square $C = [\theta | |\theta_i| \leq \pi; i = 1, 2]$ and it is clearest and simplest to use Lebesgue integration for the following reasons. First of all the integrand in (1) is undefined at $\theta = 0$ when $1 - \phi(\theta) = 0$. Secondly, we then have the dominated convergence theorem to work with. It will be useful since $|1 - \phi^n(\theta)| \leq 2$ and $1 - \phi^n(\theta)$ tends to zero, as $n \to \infty$, almost everywhere on $C$ (indeed at all but finitely many points). Hence the existence of the limit in (1) will be assured if we can prove that

(2) $\frac{1 - e^{iz \cdot \theta}}{1 - \phi(\theta)}$ is Lebesgue integrable on the square $C$.

If (2) is true, then we shall know that the limit in P1 exists and has the representation

(3) $a(x) = \lim_{n \to \infty} a_n(x) = (2\pi)^{-2} \int \frac{1 - e^{iz \cdot \theta}}{1 - \phi(\

This last step uses P7.5 which asserts that for aperiodic random walk one can find a constant $\lambda > 0$ such that $\text{Re} [1 - \phi(\theta)] \geq \lambda |\theta|^2$ when $\theta \in C$. Thus

$$\frac{|\theta|}{\text{Re} [1 - \phi(\theta)]} \leq \frac{1}{\lambda |\theta|}, \quad \theta \in C,$$

and $|\theta|^{-1}$ is indeed Lebesgue integrable since we are in dimension $d = 2$, where

$$\int_C \frac{d\theta}{|\theta|} \leq \int_{|\theta| \leq \pi \sqrt{2}} \frac{d\theta}{|\theta|} = 2^{3/2} \pi^2 < \infty.$$

Observe that this completes the proof—but that the same proof would break down at the very last step in one dimension, due to the fact that there

$$\int_C \frac{d\theta}{|\theta|} = \int_{-\pi}^{\pi} \frac{dx}{|x|} = \infty.$$

Much more sophisticated methods are required to show (in Chapter VII) that P1 is true even for one-dimensional random walk.

We proceed to two more results which have a natural proof by Fourier analysis, and which will be useful in continuing the work of section 11. The first proposition (P2) is a general law governing the asymptotic behavior of $A(x,y)$ for two-dimensional aperiodic recurrent random walk. The second result (P3) is a sharp version of P2, valid only for a very restricted class of random walks. Incidentally, for reasons which will appear later, we provide the function $A(x,y)$ with the name of potential kernel.
