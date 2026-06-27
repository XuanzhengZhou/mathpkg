---
role: proof
locale: en
of_concept: kronecker-first-form
source_book: gtm041
source_chapter: "7"
source_section: "7.5"
---

Choosing $F(t)$ as in Lemma 2 we have

$$F(t) = 1 + \sum_{r=1}^{n} e^{2\pi i(t\theta_r - \alpha_r)}.$$

By Lemma 2, to prove Kronecker's theorem it suffices to prove that $L = n + 1$ where $L = \sup |F(t)|$.

Now $|F(t)| \leq L$ so $|F^p(t)| \leq L^p$ for all $t$, hence

$$\left| \frac{1}{T} \int_0^T F^p(t) e^{-it\lambda_r} dt \right| \leq \frac{1}{T} \int_0^T L^p dt = L^p.$$

Hence $|c_r| \leq L^p$ for each $r$, and

$$(1 + n)^p \leq (N + 1)L^p \leq (p + 1)^nL^p$$

by Lemma 3. Therefore

$$\frac{n + 1}{L} \leq (p + 1)^{n/p}$$

from which we find

$$\log \left( \frac{n + 1}{L} \right) \leq \frac{n}{p} \log (p + 1).$$

Now let $p \to \infty$. The last inequality becomes $\log[(n + 1)/L] \leq 0$, so $L \geq n + 1$. But $L \leq n + 1$ hence $L = n + 1$, and this proves Kronecker's theorem.
