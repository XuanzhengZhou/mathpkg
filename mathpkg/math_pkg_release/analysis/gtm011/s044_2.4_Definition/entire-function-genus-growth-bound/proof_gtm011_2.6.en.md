---
role: proof
locale: en
of_concept: entire-function-genus-growth-bound
source_book: gtm011
source_chapter: "2"
source_section: "2.6"
---

Since $f$ is an entire function of genus $\mu$, we have the factorization $f(z) = z^m e^{g(z)} P(z)$ with $P$ in standard form and $\deg g = q \leq \mu$. The growth is dominated by the canonical product $P(z) = \prod E_\mu(z/a_n)$.

First, observe that
$$\lim_{z \to \infty} \frac{\log |E_\mu(z)|}{|z|^{\mu+1}} = 0.$$

So if $A > 0$ then there is a number $R > 0$ such that
$$\log |E_\mu(z)| \leq A |z|^{\mu+1}, \quad |z| > R. \tag{2.8}$$

But on $\{z: \tfrac{1}{2} \leq |z| \leq R\}$ the function $|z|^{-(\mu+1)} \log |E_\mu(z)|$ is continuous except at $z = +1$, where it tends to $-\infty$. Hence there is a constant $B > 0$ such that
$$\log |E_\mu(z)| \leq B |z|^{\mu+1}, \quad \tfrac{1}{2} \leq |z| \leq R. \tag{2.9}$$

Combining (2.7), (2.8), and (2.9) gives that
$$\log |E_\mu(z)| \leq M |z|^{\mu+1} \tag{2.10}$$
for all $z$ in $\mathbb{C}$, where $M = \max\{2, A, B\}$.

Since $\sum |a_n|^{-(\mu+1)} < \infty$, an integer $N$ can be chosen so that
$$\sum_{n=N+1}^{\infty} |a_n|^{-(\mu+1)} < \frac{\alpha}{4M}.$$

But, using (2.10),
$$\sum_{n=N+1}^{\infty} \log |E_\mu(z/a_n)| \leq M \sum_{n=N+1}^{\infty} \left| \frac{z}{a_n} \right|^{\mu+1} \leq \frac{\alpha}{4} |z|^{\mu+1}. \tag{2.11}$$

Now notice that in the derivation of (2.8), $A$ could be chosen as small as desired by taking $R$ sufficiently large. So choose $r_1 > 0$ such that
$$\log |E_\mu(z)| \leq \frac{\alpha}{4N} |z|^{\mu+1}, \quad \text{for } |z| > r_1.$$

Applying this to the first $N$ factors and combining with (2.11) yields
$$\log |P(z)| \leq \frac{\alpha}{2} |z|^{\mu+1}$$
for $|z| > r_0 = \max\{r_1, r_2\}$. The exponential factor $e^{g(z)}$ contributes at most a polynomial growth, which is absorbed by the $\exp(\alpha |z|^{\mu+1})$ bound for large $|z|$. Taking the exponential of both sides, the desired inequality is obtained.
