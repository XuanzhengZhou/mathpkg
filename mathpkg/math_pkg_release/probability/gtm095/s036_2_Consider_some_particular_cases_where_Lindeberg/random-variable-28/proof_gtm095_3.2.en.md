---
role: proof
locale: en
of_concept: random-variable-28
source_book: gtm095
source_chapter: "3"
source_section: "2"
---

# Proof of Integral Tail Estimate via Characteristic Function

**Lemma.** Let $\xi$ be a random variable with distribution function $F = F(x)$, $E \xi = 0$, $\operatorname{Var} \xi = \gamma > 0$. Then for any $a > 0$

$$\int_{|x| \geq 1/a} x^2 \, dF(x) \leq \frac{1}{a^2} \left[ \operatorname{Re} f(\sqrt{6}a) - 1 + 3\gamma a^2 \right],$$

where $f(t) = E e^{it\xi}$ is the characteristic function of $\xi$.

*Proof.* We have

$$
\begin{aligned}
\operatorname{Re} f(t) - 1 + \frac{1}{2} \gamma t^2
&= \frac{1}{2} \gamma t^2 - \int_{-\infty}^{\infty} [1 - \cos tx] \, dF(x) \\
&= \frac{1}{2} \gamma t^2 - \int_{|x| < 1/a} [1 - \cos tx] \, dF(x)
   - \int_{|x| \geq 1/a} [1 - \cos tx] \, dF(x) \\
&\geq \frac{1}{2} \gamma t^2 - \frac{1}{2} t^2 \int_{|x| < 1/a} x^2 \, dF(x)
   - 2a^2 \int_{|x| \geq 1/a} x^2 \, dF(x) \\
&= \left( \frac{1}{2} t^2 - 2a^2 \right) \int_{|x| \geq 1/a} x^2 \, dF(x).
\end{aligned}
$$

The first inequality uses $1 - \cos tx \leq \frac{1}{2} t^2 x^2$ on $\{|x| < 1/a\}$ and $1 - \cos tx \leq 2$ on the complementary region. The last equality follows from

$$\frac{1}{2}\gamma t^2 - \frac{1}{2}t^2 \int_{|x| < 1/a} x^2 \, dF(x) = \frac{1}{2}t^2 \int_{|x| \geq 1/a} x^2 \, dF(x),$$

since $\gamma = \int_{-\infty}^{\infty} x^2 \, dF(x)$.

Letting $t = \sqrt{6}a$ yields

$$\operatorname{Re} f(\sqrt{6}a) - 1 + 3\gamma a^2 \geq (3a^2 - 2a^2) \int_{|x| \geq 1/a} x^2 \, dF(x) = a^2 \int_{|x| \geq 1/a} x^2 \, dF(x),$$

which is equivalent to (18). $\square$
