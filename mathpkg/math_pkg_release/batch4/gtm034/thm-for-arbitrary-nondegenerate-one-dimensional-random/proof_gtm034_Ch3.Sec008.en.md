---
role: proof
locale: en
of_concept: thm-for-arbitrary-nondegenerate-one-dimensional-random
source_book: gtm034
source_chapter: "3"
source_section: "008"
---

Proof: It is fairly easy to show that (A) implies (B). After doing so we shall pause and prove several lemmas, namely P3 through P5, and the proof of P5 will complete the proof of the theorem.$^6$

Using P17.4, P17.5 of section 17 and the notation in D1

$$1 - t\phi(\theta) = \{1 - E[t^T e^{i\theta Z}]\}\{1 - E[t^T^* e^{i\theta Z}]\}$$

for $0 \leq t < 1$, $\theta$ real. Now we let $t \nearrow 1$ (this causes no concern) and just as in E1 we divide by $\theta^2$ when $\theta \neq 0$. As we are assuming (A) it follows from P6.4 that

$$\lim_{\theta \to 0} \frac{1 - E[e^{i\theta Z}]}{i\theta} = E[Z]$$

and that a similar result holds for $\bar{Z}$. This gives us

$$\lim_{\theta \to 0} \frac{1 - \phi(\theta)}{\theta^2} = E[Z]E[-\bar{Z}] < \infty.$$

Hence

$$\text{Re} \frac{1 - \phi(\theta)}{\theta^2} = \sum P(0,x) \frac{1 - \cos x\theta}{\theta^2}$$

is a bounded function of $\theta$. Therefore

$$\sum_{x=-M}^{M} x^2P(0,x) = 2 \lim_{\theta \to 0} \sum_{x=-M}^{M} P(0,x) \frac{1 - \cos x\theta}{\theta^2} \leq 2E[Z]E
