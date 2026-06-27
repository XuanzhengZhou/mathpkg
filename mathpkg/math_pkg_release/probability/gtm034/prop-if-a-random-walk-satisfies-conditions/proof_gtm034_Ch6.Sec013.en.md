---
role: proof
locale: en
of_concept: prop-if-a-random-walk-satisfies-conditions
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: The proof depends on rather delicate Fourier analysis as we shall have to utilize the full strength of the Local Central Limit Theorems P7.9 and P7.10. They apply only to strongly aperiodic random walk, a restriction which will be removed at the last step of the proof. Under this restriction

(1) $|x|P_n(0,x) = |x|(2\pi n)^{-\frac{d}{2}}|Q|^{-\frac{1}{2}}e^{-\frac{1}{2n}(x \cdot Q^{-1}x)} + |x|n^{-\frac{d}{2}}E_1(n,x),$

(2) $|x|P_n(0,x) = |x|(2\pi n)^{-\frac{d}{2}}|Q|^{-\frac{

When $x \neq 0$ and $d = 3$ they yield the series

$$S(x) = (2\pi)^{-3/2}|Q|^{-1/2}|x| \sum_{n=1}^{\infty} n^{-3/2}e^{-\frac{1}{2n}(z \cdot Q^{-1}z)}.$$

As $|x| \to \infty$ it will now be easy to replace this sum by an asymptotically equal Riemann integral. Let us call $(x \cdot Q^{-1}x)^{-1} = \Delta$, observing that $\Delta \to 0$ as $|x| \to \infty$ (the quadratic form $Q^{-1}$ is positive definite!). Then

$$S(x) = \frac{(2\pi)^{-3/2}|Q|^{-1/2}|x|}{(x \cdot Q^{-1}x)^{1/2}} \sum_{n=1}^{\infty} (n\Delta)^{-3/2}e^{-(2n\Delta)^{-1}}\Delta,$$

and as $\Delta \to 0$ the sum on the right tends to the convergent improper Riemann integral

$$\int_{0}^{\infty} t^{-3/2}e^{-1/2t} dt = \sqrt{2\pi}.$$

Therefore

(3) $$S(x) \sim (2\pi)^{-1}|Q|^{-1/2}(x \cdot Q^{-1}x)^{-1/2}|x| \text{ as } |x| \to \infty.$$

This is the desired result, so that we now only have to explain why the error terms do not contribute. It is here that the need for the two different types of error terms in (1) and (2) becomes manifest. We shall use (1) for the range $[|x|^2] < n < \infty$, and (2) for the range $1 \leq n \leq [|x|^2]$. Here $[y]$ denotes the greatest integer in $y$. Since the contribution of the principal terms in (3) is positive, we have to show that

(4) $$\lim_{|x| \to \infty} |x|^{-1} \sum_{

for some positive $k_1$ which is independent of $\epsilon$ and $x$. Since $\epsilon$ is arbitrary, the first limit in (4) is zero. The second limit is also zero since

$$|x| \sum_{n=|z|^2+1}^{\infty} n^{-3/2} |E_1(n,x)| \leq |x| \sup_{n>|z|^2} |E_1(n,x)| \sum_{n=|z|^2}^{\infty} n^{-3/2} \leq k_2 \sup_{n>|z|^2} |E_1(n,x)|,$$

which tends to zero as $|x| \to \infty$ ($k_2$ is a positive constant, independent of $x$).

The proof of P1 is now complete for strongly aperiodic random walk, but this requirement is superfluous and may be removed by a trick of remarkable simplicity (a version of which was used in the proof of P5.4). If $P(x,y)$ is aperiodic, but not strongly aperiodic, define the transition function

$$P'(x,y) = (1 - \alpha) \delta(x,y) + \alpha P(x,y),$$

with $0 < \alpha < 1$. $P'$ will now be strongly aperiodic, and of course if $P$ satisfies conditions (a), (b), (c) in P1, then so does $P'$. The Green function $G'$ of $P'$, as a trivial calculation shows, is given by

$$G'(x,y) = \frac{1}{\alpha} G(x,y).$$

In particular,

(5) $$|x| G(0,x) = \alpha|x| G'(0,x), \quad x \in R.$$

As we have proved P1 for strongly aperiodic random walk, the asymptotic behavior of $|x| G'(0,x)$ is known, and that of $|x| G(0,x)$ may be inferred from it. It remains only to check that we obtain the right constant. The asymptotic behavior of $|x| G'(0,x)$ is governed by the second moments of the $P'$ random walk. These are continuous functions of $\alpha$. Since equation (

It follows that the semigroup $R^+$ must be all of $\bar{R}$. By the assumption of aperiodicity $R^+ = \bar{R} = R$; hence every point has positive probability of being visited at some time. This implies the almost obvious but exceedingly useful corollary to P1 that for every aperiodic three-dimensional random walk with mean 0 and finite second moments the Green function $G(x,y)$ is everywhere positive.

As the first application of P1 we consider the hitting probabilities of a finite set $A$. For any three-dimensional random walk

$$\lim_{|z| \to \infty} H_A(x,y) = 0.$$

This was P25.3. But one can refine the question and expect a more interesting conclusion by imposing the condition that $A$ is visited in a finite time. Let

$$T_A = \min [n \mid 0 \leq n \leq \infty, x_n \in A].$$

Then the conditional probability of hitting $A$ at $y$, given that $T_A < \infty$, is

$$\frac{P_z[x_{T_A} = y; T_A < \infty]}{P_z[T_A < \infty]} = \frac{H_A(x,y)}{H_A(x)}.$$

To calculate the limit as $|x| \to \infty$, for a random walk which satisfies the conditions for P1, observe that by P25.1

$$H_A(x,y) = \sum_{t \in A} G(x,t)[\delta(t,y) - \Pi_A(t,y)],$$

so that

$$\lim_{|z| \to \infty} |x|H_A(x,y) = \lim_{|z| \to \infty} |x|G(x,0) \sum_{t \in A} [\delta(t,y) - \Pi_A(t,y)].$$

Let $E_A^*$ be the equilibrium charge of the reversed random walk. Then, using P1 and D25.1

$$\lim_{|z| \to \infty} |x|H_A(x,y) = \frac{1}{2\pi\sigma^2} E_A^*(y).$$

Since $|A| < \infty$,

$$\lim_{|z|

because $C^*(A)$, the capacity of the set $A$ with respect to the reversed random walk, is easily shown to be the same as $C(A)$. Therefore we have proved
