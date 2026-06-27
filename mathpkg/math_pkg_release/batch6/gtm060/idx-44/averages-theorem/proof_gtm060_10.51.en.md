---
role: proof
locale: en
of_concept: averages-theorem
source_book: gtm060
source_chapter: "10"
source_section: "51"
---

The proof consists of three lemmas.

**Lemma 1.** The theorem holds for exponential functions $f = e^{i(k, \varphi)}$ with $k \in \mathbb{Z}^n$.

If $k = 0$, then $f \equiv 1$, the space average is $1$, and the time average is also $1$ since $\frac{1}{T}\int_0^T 1 dt = 1$.

If $k \neq 0$, the space average is $\bar{f} = (2\pi)^{-n} \int_{T^n} e^{i(k, \varphi)} d\varphi = 0$ by orthogonality. For the time average, compute

$$\frac{1}{T} \int_0^T e^{i(k, \varphi_0 + \omega t)} dt = \frac{e^{i(k, \varphi_0)}}{T} \int_0^T e^{i(k, \omega)t} dt = \frac{e^{i(k, \varphi_0)}}{i(k, \omega)} \frac{e^{i(k, \omega)T} - 1}{T}.$$

Since the frequencies are independent, $(k, \omega) \neq 0$ for $k \neq 0$. As $T \to \infty$, the fraction $(e^{i(k, \omega)T} - 1)/T$ is bounded, so the time average tends to $0$, agreeing with the space average.

**Lemma 2.** The theorem holds for trigonometric polynomials

$$f = \sum_{|k| < N} f_k e^{i(k, \varphi)}.$$

Both the time and space averages depend linearly on $f$, so the equality follows immediately from Lemma 1 applied to each term.

**Lemma 3.** Let $f$ be a real Riemann integrable function on $T^n$. For any $\varepsilon > 0$, there exist two trigonometric polynomials $P_1$ and $P_2$ such that $P_1 < f < P_2$ and

$$\frac{1}{(2\pi)^n} \int_{T^n} (P_2 - P_1) d\varphi \leq \varepsilon.$$

*Proof of Lemma 3:* If $f$ is continuous, by the Weierstrass approximation theorem we can approximate $f$ by a trigonometric polynomial $P$ with $|f - P| < \varepsilon/2$. Set $P_1 = P - \varepsilon/2$ and $P_2 = P + \varepsilon/2$.

If $f$ is only Riemann integrable, there exist continuous functions $f_1, f_2$ with $f_1 < f < f_2$ and $(2\pi)^{-n} \int (f_2 - f_1) d\varphi < \varepsilon/3$. Approximating $f_1$ and $f_2$ by polynomials $P_1 < f_1 < f_2 < P_2$ with $(2\pi)^{-n} \int (P_2 - f_2) d\varphi < \varepsilon/3$ and $(2\pi)^{-n} \int (f_1 - P_1) d\varphi < \varepsilon/3$ yields the desired inequality.

Now, applying Lemmas 2 and 3: for any $\varepsilon > 0$, choose $P_1, P_2$ as in Lemma 3. Then for all $T$,

$$\frac{1}{T} \int_0^T P_1(\varphi(t)) dt \leq \frac{1}{T} \int_0^T f(\varphi(t)) dt \leq \frac{1}{T} \int_0^T P_2(\varphi(t)) dt.$$

Taking $T \to \infty$ and using Lemma 2 for $P_1$ and $P_2$, we obtain

$$\bar{P_1} \leq \liminf_{T \to \infty} \frac{1}{T} \int_0^T f dt \leq \limsup_{T \to \infty} \frac{1}{T} \int_0^T f dt \leq \bar{P_2}.$$

Since $\bar{P_2} - \bar{P_1} \leq \varepsilon$ and $\varepsilon$ is arbitrary, the limit exists and equals $\bar{f}$. This completes the proof of the theorem.
