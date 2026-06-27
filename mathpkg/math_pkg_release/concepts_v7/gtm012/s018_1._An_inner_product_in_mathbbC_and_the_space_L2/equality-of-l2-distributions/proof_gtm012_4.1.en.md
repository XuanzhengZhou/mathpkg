---
role: proof
locale: en
of_concept: equality-of-l2-distributions
source_book: gtm012
source_chapter: "4. Hilbert Spaces and Fourier Series"
source_section: "§1. An inner product in ℂ, and the space L²"
---

# Proof of equality criterion for $L^2$ distributions

**Lemma 1.2.** Suppose $(u_n)_{1}^{\infty}, (v_n)_{1}^{\infty} \subset \mathcal{C}$ are Cauchy sequences with respect to $\|\cdot\|$, and let $F = \lim F_{u_n}$, $G = \lim F_{v_n}$ in $\mathcal{P}'$. Then $F = G$ if and only if

$$\|u_n - v_n\| \to 0 \quad \text{as } n \to \infty.$$

*Proof.* Let $w_n = u_n - v_n$ and let $H_n = F_n - G_n = F_{w_n}$. We want to show

$$H_n \to 0 \quad \text{in } \mathcal{P}' \quad \text{if and only if} \quad \|w_n\| \to 0.$$

**($\Leftarrow$)** Suppose $\|w_n\| \to 0$. Then for any $u \in \mathcal{P}$,

$$|H_n(u)| = |F_{w_n}(u)| = |(u, w_n^*)| \leq \|u\| \|w_n\| \to 0.$$

Thus $H_n \to 0$ in $\mathcal{P}'$.

**($\Rightarrow$)** Conversely, suppose $H_n \to 0$ in $\mathcal{P}'$. Given $\varepsilon > 0$, since $(u_n)$ and $(v_n)$ are both $\|\cdot\|$-Cauchy, take $N$ so large that $n, m \geq N$ implies

$$\|u_n - u_m\| \leq \frac{\varepsilon}{3}, \quad \|v_n - v_m\| \leq \frac{\varepsilon}{3}.$$

Then for $n, m \geq N$,

$$\|w_n - w_m\| = \|(u_n - u_m) - (v_n - v_m)\| \leq \|u_n - u_m\| + \|v_n - v_m\| \leq \frac{2\varepsilon}{3} < \varepsilon.$$

So $(w_n)$ is also $\|\cdot\|$-Cauchy.

Fix $m \geq N$. Then for any $n \geq N$,

$$\|w_m\|^2 = (w_m, w_m) = (w_m, w_m - w_n) + (w_m, w_n)$$

$$= (w_m, w_m - w_n) + H_n(w_m)$$

$$\leq \|w_m\| \|w_m - w_n\| + |H_n(w_m)| \quad \text{(by Schwarz inequality)}$$

$$\leq \varepsilon \|w_m\| + |H_n(w_m)|.$$

Letting $n \to \infty$, since $H_n \to 0$ in $\mathcal{P}'$, we have $H_n(w_m) \to 0$. Hence

$$\|w_m\|^2 \leq \varepsilon \|w_m\|,$$

and if $\|w_m\| > 0$, division gives $\|w_m\| \leq \varepsilon$. If $\|w_m\| = 0$, the same inequality holds trivially. Thus $\|w_m\| \leq \varepsilon$ for all $m \geq N$, proving $\|w_n\| \to 0$. ∎
