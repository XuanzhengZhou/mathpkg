---
role: proof
locale: en
of_concept: proposition-2-3
source_book: gtm011
source_chapter: "Harmonic Functions"
source_section: "2. Harmonic functions on a disk"
---

Proof. (a) For a fixed value of $r$, $0 \leq r < 1$, the series (2.1) converges uniformly in $\theta$. So

$$\frac{1}{2\pi} \int_{-\pi}^{\pi} P_r(\theta) d\theta = \sum_{n=-\infty}^{\infty} r^{|n|} \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{in\theta} d\theta = 1$$

(b) From equation (2.2), $P_r(\theta) = (1-r^2)|1-re^{i\theta}|^{-2} > 0$ since $r < 1$. The rest of (b) is an equally trivial consequence of (2.2).

(c) Let $0 < \delta < \theta \leq \pi$ and define $f: [\delta, \theta] \to \mathbb{R}$ by $f(t) = P_r(t

Moreover $u$ is unique and is defined by the formula

$$u(re^{i\theta}) = \frac{1}{2\pi} \int_{-\pi}^{\pi} P_r(\theta - t) f(e^{it}) dt$$

for $0 \leq r < 1$, $0 \leq \theta \leq 2\pi$.

Proof. Define $u: \bar{D} \to \mathbb{R}$ by letting $u(re^{i\theta})$ be as in (2.5) if $0 \leq r < 1$ and letting $u(e^{i\theta}) = f(e^{i\theta})$. Clearly $u$ satisfies part (a); it remains to show that $u$ is continuous on $D^-$ and harmonic in $D$.

(i) $u$ is harmonic in $D$. If $0 \leq r < 1$ then

$$u(re^{i\theta}) = \frac{1}{2\pi} \int_{-\pi}^{\pi} \text{Re} \left[ \frac{1 + re^{i(\theta - t)}}{1 - re^{i(\theta - t)}} \right] f(e^{it}) dt$$

$$= \text{Re} \left\{ \frac{1}{2\pi} \int_{-\pi}^{\pi} f(e^{it}) \left[ \frac{1 + re^{i(\theta - t)}}{1 - re^{i(\theta - t)}} \right] dt \right\}$$

$$= \text{Re} \left\{ \frac{1}{2\pi} \int_{-\pi}^{\pi} f(e^{it}) \left[ \frac{e^{it} + re^{i\theta}}{e^{it} - re^{i\theta}} \right] dt \right\}$$

So define $g: D \to \mathbb{C}$ by

$$g(z) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(e^{it}) \left[ \frac{e^{it} + z}{e^{it} - z} \right] dt.$$

Since $u = \text{Re} g$ we need only show that $g$ is analytic. But this is an easy consequence of

if $|\theta| < \delta$. Let $M = \max \{|f(e^{i\theta})| : |\theta| \leq \pi\}$; from Proposition 2.3 (d) there is a number $\rho$, $0 < \rho < 1$, such that

2.8 $P_r(\theta) < \frac{\epsilon}{3M}$

for $\rho < r < 1$ and $|\theta| \geq \frac{1}{2}\delta$. Let $A$ be the arc $\{e^{i\theta} : |\theta| < \frac{1}{2}\delta\}$. Then if $e^{i\theta} \in A$ and $\rho < r < 1$,

$$u(re^{i\theta}) - f(1) = \frac{1}{2\pi} \int_{-\pi}^{\pi} P_r(\theta - t)f(e^{it}) dt - f(1)$$

$$= \frac{1}{2\pi} \int_{|t| < \delta} P_r(\theta - t)[f(e^{it}) - f(1)] dt + \frac{1}{2\pi} \int_{|t| \geq \delta} P_r(\theta - t)[f(e^{it}) - f(1)] dt.$$

If $|t| \geq \delta$ and $|\theta| \leq \frac{1}{2}\delta$ then $|t - \theta| \geq \frac{1}{2}\delta$; so from (2.7) and (2.8) it follows that

$$|u(re^{i\theta}) - f(1)| \leq \frac{1}{3}\epsilon + 2M\left(\frac{\epsilon}{3M}\right) = \epsilon.$$

This proves Claim 2.6.

Finally, to show that $u$ is unique, suppose that $v$ is a continuous function on $D^-$ which is harmonic on $D$ and $v(e^{i\theta}) = f(e^{i\theta})$ for all $\theta$. Then $u - v$ is harmonic in $D$ and $(u - v)(z) = 0$ for all $z$ in $\partial D$. It

it is an easy matter to show that $w(z) = u\left(\frac{z-a}{\rho}\right)$ is the desired function on $\bar{B}(a; \rho)$.

It is now possible to give the promised converse to the Mean Value Theorem.
