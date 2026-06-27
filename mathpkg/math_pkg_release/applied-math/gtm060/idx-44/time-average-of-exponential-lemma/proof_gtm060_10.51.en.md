---
role: proof
locale: en
of_concept: time-average-of-exponential-lemma
source_book: gtm060
source_chapter: "10"
source_section: "51"
---

If $k = 0$, then $f \equiv 1$. The space average is $\bar{f} = (2\pi)^{-n} \int_{T^n} 1 \, d\varphi = 1$, and the time average is $f^*(\varphi_0) = \lim_{T \to \infty} \frac{1}{T} \int_0^T 1 \, dt = 1$. Both are equal.

If $k \neq 0$, the space average is $\bar{f} = (2\pi)^{-n} \int_{T^n} e^{i(k, \varphi)} d\varphi = 0$ by orthogonality of exponentials.

For the time average, compute:

$$\frac{1}{T} \int_0^T e^{i(k, \varphi_0 + \omega t)} dt = \frac{e^{i(k, \varphi_0)}}{T} \int_0^T e^{i(k, \omega)t} dt = \frac{e^{i(k, \varphi_0)}}{i(k, \omega)} \cdot \frac{e^{i(k, \omega)T} - 1}{T}.$$

Since the frequencies are independent, $(k, \omega) \neq 0$ for $k \neq 0$. The numerator $e^{i(k, \omega)T} - 1$ is bounded in absolute value by $2$, so the fraction $\frac{e^{i(k, \omega)T} - 1}{T}$ tends to $0$ as $T \to \infty$. Therefore the time average is $0$, agreeing with the space average.
