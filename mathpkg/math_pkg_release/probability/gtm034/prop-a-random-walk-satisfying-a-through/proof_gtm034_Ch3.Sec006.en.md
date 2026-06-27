---
role: proof
locale: en
of_concept: prop-a-random-walk-satisfying-a-through
source_book: gtm034
source_chapter: "3"
source_section: "006"
---

Proof: We begin by checking that

$$\psi(\theta) = \frac{1}{1 - \phi(\theta)} - \frac{2}{Q(\theta)}$$

is Lebesgue integrable on the square $C$. Let us write, as we may in view of (c),

$$\psi(\theta) = \frac{2}{\sigma^2} \cdot \frac{|\theta|^2}{1 - \phi(\theta)} \chi(\theta),$$

$$\chi(\theta) = |\theta|^{-4} \left[ \sigma^2 \frac{|\theta|^2}{2} - 1 + \phi(\theta) \right].$$

By P6.7

$$\lim_{|\theta| \to 0} \frac{|\theta|^2}{1 - \phi(\theta)} = \frac{2}{\sigma^2} > 0,$$

and according to T7.1, $1 - \phi(\theta) = 0$ only at $\theta = 0$ in the square $C$. Therefore it suffices to prove that $\chi(\theta)$ is integrable on $C$.

Now

$$\sigma^2 \frac{|\theta|^2}{2} - 1 + \phi(\theta) = \mathbf{E} \left[ e^{iX \cdot \theta} - 1 - iX \cdot \theta - \frac{1}{2}(iX \cdot \theta)^2 \right],$$

if $\mathbf{X}$ is a random variable with values in $R$ such that

$$\mathbf{P}[\mathbf{X} = x] = P(0,x), \quad x \in R.$$

Here we used condition (b) in inserting the useful term $iX \cdot \theta$. Now we use the positive number $\delta$ in condition (d) by making the obvious assertion that there is some $h > 0$ such that

for some $M < \infty$. Thus $\chi(\theta)$, and hence $\psi(\theta)$, is integrable, for

$$\int_c |\theta|^{\delta-2} d\theta \leq \int_{|\theta| \leq \pi\sqrt{2}} |\theta|^{\delta-2} d\theta = 2\pi \int_0^{\pi\sqrt{2}} \frac{dt}{t^{1-\delta}} < \infty.$$

The next step is to decompose

$$a(x) = (2\pi)^{-2} \int \frac{1-e^{ix\cdot\theta}}{1-\phi(\theta)} d\theta$$

$$= \frac{2}{\sigma^2} (2\pi)^{-2} \int \frac{1-\cos x \cdot\theta}{|\theta|^2} d\theta + (2\pi)^{-2} \int (1-e^{ix\cdot\theta})\psi(\theta) d\theta.$$

The last integral tends to the constant $c$ in P3, by the Riemann Lebesgue Lemma in P9.1. Therefore the proof of P3, apart from the calculations for simple random walk, will be complete if we show that

$$\lim_{|x| \to \infty} \left[ \frac{1}{2\pi} \int \frac{1-\cos x \cdot\theta}{|\theta|^2} d\theta - \ln |x| \right] = \gamma - \frac{2}{\pi} \lambda + \ln \pi.$$

To accomplish this we decompose

$$\frac{1}{2\pi} \int \frac{1-\cos x \cdot\theta}{|\theta|^2} d\theta = I_1(x) + I_2(x).$$

Here $I_1(x)$ is the integral over the circular disc $|\theta| \leq \pi$ and $I_2(x)$ is the contribution from the rest of the square. The proof will be completed by showing that

$$\lim_{|x| \to \infty} \left[ I_1(x) - \ln |x| \right] = \gamma + \ln \frac{\pi}{2}$$

and

$$\lim

Now we shall use as our definition of Euler's constant

$$\gamma = \int_{0}^{1} \frac{1 - \cos u}{u} du - \int_{1}^{\infty} \frac{\cos u}{u} du.$$

Substitution into the formula for $I_1(x)$ yields

$$I_1(x) = \frac{2}{\pi} \int_{0}^{\pi/2} \left[ \gamma + \ln |x| + \ln (\sin t) + \ln \pi + \int_{\pi|x| \sin t}^{\infty} \frac{\cos u}{u} du \right] dt.$$

Taking account of

$$\frac{2}{\pi} \int_{0}^{\pi/2} \ln (\sin t) dt = -\ln 2,$$

and of

$$\lim_{|x| \to \infty} \frac{2}{\pi} \int_{0}^{\pi/2} dt \int_{\pi|x| \sin t}^{\infty} \frac{\cos u}{u} du = 0,$$

one has

$$\lim_{|x| \to \infty} \left[ I_1(x) - \ln |x| \right] = \gamma - \ln 2 + \ln \pi,$$

as was to be shown.

By use of the Riemann Lebesgue Lemma

$$\lim_{|x| \to \infty} I_2(x) = \lim_{|x| \to \infty} \frac{1}{2\pi} \int_{\begin{subarray}{c} |\theta_1| \leq \pi, |\theta_2| \leq \pi \\ |\theta| \geq \pi \end{subarray}} \frac{1 - \cos x \cdot \theta}{|\theta|^2} d\theta$$

$$= \frac{1}{2\pi} \int_{\begin{subarray}{c} |\theta_1| \leq \pi, |\theta_2| \leq \pi \\ |\theta| \geq \pi \end{subarray}} \frac{d\theta}{|\theta|^2}.$$

Again introducing polar coordinates, one obtains

$$\lim_{|x| \to
