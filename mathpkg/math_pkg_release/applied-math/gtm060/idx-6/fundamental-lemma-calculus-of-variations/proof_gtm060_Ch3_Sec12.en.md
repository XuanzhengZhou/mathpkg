---
role: proof
locale: en
of_concept: fundamental-lemma-calculus-of-variations
source_book: gtm060
source_chapter: "3"
source_section: "12"
---
Suppose, for contradiction, that $f(t^*) \neq 0$ for some $t^* \in (t_0, t_1)$. Without loss of generality, assume $f(t^*) > 0$. By continuity of $f$, there exists a neighborhood $[t^* - \delta, t^* + \delta] \subset (t_0, t_1)$ on which $f(t) > f(t^*)/2 > 0$.

Construct a continuous function $h(t)$ that is positive on $(t^* - \delta, t^* + \delta)$, zero outside this interval, and satisfies $h(t_0) = h(t_1) = 0$ and $h(t) \geq 0$ everywhere. For instance, take

$$h(t) = \begin{cases} \delta^2 - (t - t^*)^2, & |t - t^*| \leq \delta, \\ 0, & \text{otherwise}. \end{cases}$$

Then $h(t)$ is continuous, $h(t_0) = h(t_1) = 0$, and

$$\int_{t_0}^{t_1} f(t) h(t)\, dt = \int_{t^* - \delta}^{t^* + \delta} f(t) h(t)\, dt > \frac{f(t^*)}{2} \int_{t^* - \delta}^{t^* + \delta} h(t)\, dt > 0,$$

contradicting the hypothesis. Hence $f(t) \equiv 0$ on $[t_0, t_1]$.
