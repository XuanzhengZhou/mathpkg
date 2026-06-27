---
role: proof
locale: en
of_concept: prop-for-every-aperiodic-transient-random-walk
source_book: gtm034
source_chapter: "2"
source_section: "005"
---

Proof: As in the proof of P8.1 we write, for $0 \leq t < 1$,

(1) $$\sum_{n=0}^{\infty} t^n P_n(0,x) = \sum_{n=0}^{\infty} (2\pi)^{-d} t^n \int e^{-i\theta \cdot x} \phi^n(\theta) d\theta,$$

where $\phi(\theta)$ is the characteristic function of the random walk. The dimension is $d \geq 1$,

For convenience, let us call

$$w_t(\theta) = 2(2\pi)^{-d} \text{ Re} \left[ \frac{1}{1 - t\phi(\theta)} \right], \quad \theta \in C, \quad 0 \leq t < 1.$$

Now we use the aperiodicity of the random walk to conclude, from T7.1, that

$$w(\theta) = \lim_{t \to 1} w_t(\theta) < \infty, \quad \theta \in C - \{0\}$$

exists for every non-zero value of $\theta$ in $C$. For every real $r, 0 < r < \pi$ we define the sphere $S_r = [\theta | |\theta| < r]$. Then, again using T7.1, equation (3) may be written

(4) $$G(0,x) + G(x,0) = \int_{C-S_r} \cos x \cdot \theta w(\theta) d\theta + \lim_{t \to 1} \int_{S_r} \cos x \cdot \theta w_t(\theta) d\theta.$$

Now we call

$$\lim_{t \to 1} \int_{S_r} w_t(\theta) d\theta = L_r,$$

observing that this limit exists, in view of (4). It is crucial to note, at several points in the proof, that $w_t(\theta) \geq 0$ on $C$, and hence also $w(\theta) \geq 0$, $w(\theta)$ being the limit of $w_t(\theta)$. Setting $x = 0$ in (4), it follows from the positivity of $w(\theta)$ that

$$0 \leq L_r \leq 2G(0,0),$$

and that

$$\lim_{r \to 0} L_r = L < \infty$$

exists. Now we shall estimate the second integral in (4) with an arbitrary, fixed, value of $x$. Given any $\epsilon > 0$ we can choose $\rho > 0$ so that $|1 - \cos x \cdot \theta| < \epsilon$ for all $\theta$ in $S_p$. It follows (since $

Now let us set $x = 0$ in (6). Since $w(\theta) \geq 0$ on $C$ we can conclude that

(7) $w(\theta)$ is integrable on $C$.

Hence (6) takes on the simple form

(8) $G(0,x) + G(x,0) = \int_{C} \cos x \cdot \theta w(\theta) d\theta + L, \quad x \in R,$

and the stage is finally set for the application of the Riemann Lebesgue Lemma (P1). The function $\cos x \cdot \theta$ is the sum of two exponentials, and as $w(\theta)$ is integrable we have

$$\lim_{|x| \to \infty} [G(0,x) + G(x,0)] = L < \infty,$$

which completes the proof of P2.

It is not easy to evaluate the limit in P2 explicitly; nor is it clear, perhaps, why this limit should be of any interest. Therefore we shall discuss a special case of obvious interest, namely so called positive one-dimensional random walk with the property that

$$P(0,x) = 0 \text{ for } x \leq 0.$$

Obviously every such random walk is transient so that P2 may be applied. It is more to the point, however, that $G(0,x) = 0$ for $x < 0$, so that P2 reduces to

$$\lim_{x \to +\infty} G(0,x) = L < \infty.$$

The limit $L$ will be evaluated in P3, where it is shown that

$$L = \frac{1}{\mu}, \quad \left(\mu = \sum_{x=1}^{\infty} xP(0,x)\right)$$

when $\mu < \infty$, while $L = 0$ when $\mu = \infty$.

This is the now "classical" renewal theorem in the form in which it was first conjectured and proved by Feller, Erdős, and Pollard (1949). Its name is due to certain of its applications. If $T$ is a positive random variable, whether integer valued or not, it may be thought of

7 Cf. [31],

as a random span of time. Frequently it is a lifetime, of an individual in a large population—or of a mass produced article. Suppose now that identical individuals, or articles, have life times $T_1, T_2, \ldots$, which are identically distributed independent random variables. If each $T_k$ is integer valued we define the transition function $P(x,y)$ so that

$$P(0,x) = P[T_k = x] \text{ for } x > 0, \quad k \geq 1,$$

and $P(0,x) = 0$ for $x \leq 0$. Then, evidently,

$$P_n(0,x) = P[T_1 + T_2 + \cdots + T_n = x], \quad x > 0, \quad n \geq 1,$$

and

$$G(0,x) = \sum_{n=1}^{\infty} P[T_1 + T_2 + \cdots + T_n = x].$$

Thus $G(0,x)$ is a sum of probabilities of disjoint events. We can say that $T_1 + \cdots + T_n = x$ if the $n^{\text{th}}$ lifetime ends at time $x$ (for example, if the $n^{\text{th}}$ individual dies, or if a mass produced article has to be "renewed" for the $n^{\text{th}}$ time at time $x$). Thus $G(0,x)$ is the probability that a renewal takes place at time $x$, and according to P3 it converges to the reciprocal of the expected lifetime

$$\mu = \sum xP(0,x) = E[T].$$

This conclusion is false, when $T$ is integer valued, unless $P(0,x)$ is aperiodic, or equivalently, unless the greatest common divisor

g.c.d. $\{x \mid P[T = x] > 0\}$

has the value one.
