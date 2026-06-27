---
role: proof
locale: en
of_concept: prop-strongly-aperiodic-random-walk-of-arbitrary
source_book: gtm034
source_chapter: "1"
source_section: "004"
---

Proof: For the direct part suppose that $|\phi(\theta_0)| = 1$, so that $\phi(\theta_0) = e^{it}$ for some real $t$. It follows that $x \cdot \theta_0 = t + 2n\pi$ for all $x$ such that $P(0,x) > 0$, where of course the integer $n$ may depend on $x$. Continuing to work with this fixed value of $\theta_0$, we select a point $z_0$ in $R$ such that $z_0 \cdot \theta_0 = t + 2m\pi$, where $m$ is an integer. Now consider the transition function defined by $Q(0,x) = P(0,x + z_0)$, where $P(0,x)$ is the transition function of the given, strongly aperiodic random walk. We know from D5.1 that $Q(0,x)$ is the transition function of an aperiodic random walk. Its characteristic function is

$$\psi(\theta) = \sum_{x \in R} Q(0,x)e^{iz \cdot \theta} = \sum_{x \in R} P(0,x + z_0)e^{iz \cdot \theta} = e^{-iz_0 \cdot \theta}\phi(\theta).$$

Hence

$$\psi(\theta_0) = e^{-iz_0 \cdot \theta}\phi(\theta_0) = e^{-iz_0 \cdot \theta}e^{it} = 1,$$

but since $\psi(\theta)$ is the characteristic function of an aperiodic random walk we conclude from T1 that $\theta_0$ is a point all of whose coordinates are integer multiples of $

Proof: According to P6.3,

$$\left(2\pi n\right)^{d/2} P_n(0,x) = n^{d/2}\left(2\pi\right)^{-d/2} \int_C \phi^n(\theta) e^{-i x \cdot \theta} d\theta.$$

We perform the change of variables $\theta \sqrt{n} = \alpha$, so that

$$\left(2\pi n\right)^{\frac{d}{2}} P_n(0,x) = \left(2\pi\right)^{-\frac{d}{2}} \int_{\alpha \in \sqrt{n} C} \phi^n\left(\frac{\alpha}{\sqrt{n}}\right) e^{-\frac{i x \cdot \alpha}{\sqrt{n}}} d\alpha.$$

With $A > 0$, and $0 < r < \pi$, one decomposes this integral to obtain

(1) $$\left(2\pi n\right)^{\frac{d}{2}} P_n(0,x) = \left(2\pi\right)^{-\frac{d}{2}} \int_E e^{-\frac{1}{2} Q(\alpha)} e^{-\frac{i x \cdot \alpha}{\sqrt{n}}} d\alpha$$
$$+ I_1(n,A) + I_2(n,A) + I_3(n,A,r) + I_4(n,r).$$

The last four integrals, which will play the role of error terms, are

$$I_1(n,A) = \left(2\pi\right)^{-\frac{d}{2}} \int_{|\alpha| \leq A} \left[ \phi^n\left(\frac{\alpha}{\sqrt{n}}\right) - e^{-\frac{1}{2} Q(\alpha)} \right] e^{-\frac{i x \cdot \alpha}{\sqrt{n}}} d\alpha,$$

$$I_2(n,A) = -\left(2\pi\right)^{-\frac{d}{2}} \int_{|\alpha| > A} e^{-\frac{1}{2} Q(\alpha)} e^{-\frac{i x \cdot \alpha}{\sqrt{n}}} d\alpha,$$

$$I_3(n,A,r) = \left(2\pi

But the product of the eigenvalues of $Q$ is the determinant $|Q|$ so that $I_0 = |Q|^{-1/2}$. Since this integral is finite, it is clear that

$$\lim_{n \to \infty} (2\pi)^{-\frac{d}{2}} \int_E e^{-\frac{1}{2}Q(\alpha)} e^{-\frac{12\alpha}{\sqrt{n}}} d\alpha = |Q|^{-\frac{1}{2}},$$

and therefore the proof of P9 will be complete as soon as we show that the sum of the four error terms tends to zero as $n \to \infty$.

To estimate $I_1(n,A)$ we use P7 which implies that

$$\lim_{n \to \infty} \phi^n \left( \frac{\alpha}{\sqrt{n}} \right) = e^{-\frac{1}{2}Q(\alpha)}$$

for each $\alpha$ in $E$. Thus $I_1(n,A)$ tends to zero as $n \to \infty$, for every $A > 0$. Next we estimate $I_4(n,r)$ by remarking that

$$|I_4(n,r)| \leq n^{d/2}(2\pi)^{-d/2} \int_{[\theta|\theta \in C; |\theta| > r]} |\phi(\theta)|^n d\theta.$$

We know from P8 that $|\phi(\theta)| < 1 - \delta$ for some $\delta = \delta(r)$ on the set of integration. Therefore $I_4(n,r)$ tends to zero as $n \to \infty$, whenever $0 < r < \pi$. Now we have to worry only about $I_2$ and $I_3$. Using P7 again we can choose $r$ small enough so that

$$\left| \phi^n \left( \frac{\alpha}{\sqrt{n}} \right) \right| \leq e^{-\frac{1}{2}Q(\alpha)}$$

when $|\alpha| \leq r\sqrt{n}$. Then

$$|I_3(n,A,r)| \leq (2\pi)^{-d/2} \int_{|\alpha| > A} e^{-\frac{

This is really an immediate corollary of the method of proof of P9. It follows from the way the four error terms $I_1, I_2, I_3,$ and $I_4$ were estimated in the proof of P9 that their sum tends to zero uniformly in $x$. Comparing equations (1) and (2), it therefore suffices to show that

$$\left(2\pi\right)^{-\frac{d}{2}} \int_E e^{-\frac{1}{2}Q(\alpha)} e^{-\frac{12\alpha}{n}} d\alpha = |Q|^{-\frac{1}{2}} e^{-\frac{1}{2n}(z \cdot Q^{-1} z)}.$$

In (3) as well as (2), $x \cdot Q^{-1} x$ denotes the inverse quadratic form of $Q(\alpha) = \alpha \cdot Q\alpha$. It is easy to verify (3) by making an orthogonal transformation from the $\alpha$-coordinate system to one where the quadratic form $Q(\alpha)$ is of the diagonal type. Due to the presence of the exponential involving $x$ on the left in (3), this calculation is slightly more complicated than the evaluation of $I_0$ in the proof of P9, but no new ideas are involved.

E2 Simple random walk of dimension $d \geq 1$ is not strongly aperiodic. Nevertheless it is quite easy to modify the proof of P9 appropriately. The characteristic function, for dimension $d$, is

$$\phi(\theta) = \sum P(0,x) e^{i z \cdot \theta} = \frac{1}{d} \left[ \cos \theta_1 + \cdots + \cos \theta_d \right].$$

Although $P_n(0,0) = 0$ when $n$ is odd, we get

$$P_{2n}(0,0) = (2\pi)^{-d} \int_C \left[ \frac{1}{d} \sum_{k=1}^{d} \cos \theta_k \right]^{2n} d\theta.$$

Since the integrand in (1) is periodic in each coordinate $\theta_k$ with period $2\pi$, we may translate the cube $C$

Applying the estimate (3) to (2), one obtains for large $n$

$$P_{2n}(0,0) \sim 2(2\pi)^{-d} \int_{S} e^{-|\theta|^2} \frac{d\theta}{d n} d\theta$$

$$\sim 2(2\pi)^{-d} \int_{E} e^{-|\theta|^2} \frac{d\theta}{d n} d\theta = 2 \left[ \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\frac{x^2}{2}} dx \right]^d \left( \frac{d}{4n\pi} \right)^{\frac{d}{2}}.$$

The integral of the Gaussian density is one, so that we have shown, for $d$-dimensional simple random walk, that

$$P_{2n}(0,0) \sim 2 \left( \frac{d}{4n\pi} \right)^{d/2}, \quad \text{as } n \to \infty.$$

The strong form of P9 given in the remark following its proof is known as the Local Central Limit Theorem. Although it is an extremely useful tool, in many applications of probability theory, there are occasions when one needs even better error estimates (P9 is really quite poor for large values of $|x|$, say when $|x|$ is of the order of $\sqrt{n}$ or larger). There is a variant of P9 (due to Smith [89], 1953, in the one-dimensional case) which provides sharper estimates for large $|x|$. For us it will be indispensable in section 26, where it will be combined with P9 to shed light on the asymptotic behavior of the Green function $G(x,y)$ for three-dimensional random walk.
