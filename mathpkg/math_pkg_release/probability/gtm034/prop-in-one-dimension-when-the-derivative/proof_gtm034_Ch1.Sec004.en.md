---
role: proof
locale: en
of_concept: prop-in-one-dimension-when-the-derivative
source_book: gtm034
source_chapter: "1"
source_section: "004"
---

Proof: If $m_1 < \infty$, then

$$\frac{1}{h} [\phi(\theta + h) - \phi(\theta)] = \frac{1}{h} \sum (e^{ihx} - 1)e^{i\theta x}P(0,x).$$

Note that, according to D3, the sum extends over all of $R$. Now

$$|e^{ihx} - 1| = \left| \int_0^{hx} e^{it} dt \right| \leq \int_0^{|hx|} dt = |hx|,$$

so that

$$\frac{1}{h} \sum

give the continuity of $\phi^{(k)}(\theta)$ when $m_k < \infty$ so that the relation $\phi^{(k)}(0) = (i)^k \mu_k$ holds.

Where the converse is concerned we offer the following well known example, leaving the verification to the reader. Let

$$P(0,x) = c|x|^{-2}(\ln |x|)^{-1}$$ when $|x| \geq 2$, $P(0,x) = 0$ when $|x| \leq 1$, where the constant $c$ is chosen so that $\sum P(0,x) = 1$. Then evidently $m_1 = \infty$, while a somewhat lengthy calculation will show that $\phi^{(1)}(0)$ exists.

Finally, suppose that

$$\phi^{(2)}(0) = \lim_{h \to 0} \frac{\phi^{(1)}(h) - \phi^{(1)}(0)}{h}$$

exists. Then it turns out that

$$\phi^{(2)}(0) = \lim_{\theta \to 0} \frac{1}{\theta^2} [\phi(\theta) + \phi(-\theta) - 2],$$

which is a more convenient representation for the second derivative at the origin. It implies

$$-\phi^{(2)}(0) = \lim_{\theta \to 0} \sum \left(\frac{2}{\theta} \sin \frac{x\theta}{2}\right)^2 P(0,x) = \lim_{\theta \to 0} \sum \left(\frac{\sin \theta x}{\theta x}\right)^2 x^2 P(0,x).$$

Consequently, for each $n \geq 0$,

$$\sum_{z=-n}^{n} x^2 P(0,x) = \lim_{\theta \to 0} \sum_{z=-n}^{n} \left(\frac{\sin \theta x}{\theta x}\right)^2 x^2 P(0,x) \leq -\phi^{(2)}(0).$$

This shows that $m_2 < \infty$ and the proof of P4 is completed by observing that the first part of P4 gives $m_2 = -\phi^{(2)}(0)$.

The extension

Proof: To simplify the notation let $p_n = P(0,x)$ for $x = n \geq 0$. Then

(1) $$\sum_{0}^{\infty} p_k \frac{1 - \cos k\theta}{\theta} \to 0, \quad \sum_{0}^{\infty} p_k \frac{\sin k\theta}{\theta} \to \alpha$$

as $\theta \to 0$. Now the plan of the proof is to use this information to show that $m = \sum_{0}^{\infty} kp_k < \infty$.

The rest of the result will then be an automatic consequence of P4. We start by breaking up the second sum in (1) into two pieces. The choice of pieces is dictated by a convenient estimate of $\sin x$ to the effect that

$$\frac{\sin x}{x} \geq \frac{2}{\pi} \text{ for } |x| \leq \frac{\pi}{2}.$$

Let us use the symbol $\hat{\theta}$ to denote $[\pi/2\theta]$, the greatest integer in $\pi/2\theta$. When $0 \leq k \leq \hat{\theta}$ the above estimate shows that $\sin k\theta \geq 2\theta k/\pi$. Therefore

(2) $$\sum_{0}^{\infty} p_k \frac{\sin k\theta}{\theta} \geq \frac{2}{\pi} \sum_{k=0}^{\dot{\theta}} kp_k + \sum_{k=\dot{\theta}+1}^{\infty} p_k \frac{\sin k\theta}{\theta}.$$

As $\theta \to 0$, $\hat{\theta} \to \infty$, the left-hand side in the above inequality tends to $\alpha$ by (1) and so we can conclude that $\sum_{0}^{\infty} kp_k < \infty$, provided we show that the last sum in (2) stays bounded as $\theta \to 0$. This in turn will be true if we can show that

$$A(\theta) = \frac{1}{\theta} \sum_{k=\dot{\theta}+1}^{\infty} p_k$$

stays bounded as $\theta \to 0$, and we shall in fact show more, namely that $A(\theta) \to

The last term tends to zero in view of the first part of (1), and this shows that $A(\theta) \to 0$ and completes the proof.

The next result concerns a necessary and sufficient condition for the finiteness of the first moment $m$ which is quite different from the condition in P4. One can extend it to moments of arbitrary odd order but this matter is again relegated to the problem section (problem 2).
