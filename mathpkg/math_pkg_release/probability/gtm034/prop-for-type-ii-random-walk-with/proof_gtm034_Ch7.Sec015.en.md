---
role: proof
locale: en
of_concept: prop-for-type-ii-random-walk-with
source_book: gtm034
source_chapter: "7"
source_section: "015"
---

Proof: We need

(1) $$\lim_{n \to \infty} P_n(x,y) = 0, \quad x,y \in R,$$

which is P7.6, and

(2) $$\lim_{n \to \infty} \sum_{t=a}^{\infty} P_n(x,t) = 1/2$$

for every $x \in R$ and every $a$ in $R$. This is a very weak form of the rarely used one-dimensional Central Limit Theorem (P6.8). Combined with P6, equations (1) and (2) evidently yield P7 by a simple truncation argument: Choosing $N > 0$ large enough so that

$$|H_B(t,y) - H_B(-\infty,y)| < \epsilon \text{ for } t \leq -N,$$

$$|H_B(t,y) - H_B(+\infty,y)| < \epsilon \text{ for } t \geq N,$$

$$\lim_{n \to \infty} \sum_{t \in R} P_n(x,t)H_B(t,y) \leq \lim_{n \to \infty} \sum_{t=-N+1}^{N-1} P_n(x,t)$$

$$+ [H_B(-\infty,y) + \epsilon] \lim_{n \to \infty} \sum_{t=-\infty}^{-N} P_n(x,t)$$

$$+ [H_B(+\infty,y) + \epsilon] \lim_{n \to \infty} \sum_{t=N}^{\infty} P_n(x,t)$$

$$= \frac{1}{2}[H_B(-\infty,y) + H_B(+\infty,y)] + \epsilon.$$

An entirely similar under-estimate completes the proof of P7.

Finally we apply P7 to P2, where we

One may summarize P5 and P8 and even P12.1 of Chapter III in the single statement that the potential kernel exists for every aperiodic recurrent random walk, regardless of dimension (remember, however, that $d = 1$ or 2 in view of T8.1!). We might as well also include in this summary the equation

$$\sum_{y \in R} P(x,y)a(y) - a(x) = \delta(x,0), \quad x \in R,$$

which will later, in section 31, be used to characterize the potential kernel. Observe that the proof of this equation, given in P13.3, is available, without any modification whatever, for the one-dimensional case, now that we have P5 and P8.

Therefore we claim to have proved the following theorem.
