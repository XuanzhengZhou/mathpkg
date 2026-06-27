---
role: proof
locale: en
of_concept: theorem-2-6
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Since $f$ is an

Hence,

$$\lim_{z \to \infty} \frac{\log |E_\mu(z)|}{|z|^{\mu+1}} = 0$$

So if $A > 0$ then there is a number $R > 0$ such that

2.8 $$\log |E_\mu(z)| \leq A |z|^{\mu+1}, |z| > R.$$

But on $\{z: \frac{1}{2} \leq |z| \leq R\}$ the function $|z|^{-(\mu+1)} \log |E_\mu(z)|$ is continuous except at $z = +1$, where it tends to $-\infty$. Hence there is a constant $B > 0$ such that

2.9 $$\log |E_\mu(z)| \leq B |z|^{\mu+1}, \frac{1}{2} \leq |z| \leq R.$$

Combining (2.7), (2.8), and (2.9) gives that

2.10 $$\log |E_\mu(z)| \leq M |z|^{\mu+1}$$

for all $z$ in $\mathbb{C}$, where $M = \max \{2, A, B\}$.

Since $\sum |a_n|^{-(\mu+1)} < \infty$, an integer $N$ can be chosen so that

$$\sum_{n=N+1}^{\infty} |a_n|^{-(\mu+1)} < \frac{\alpha}{4M}.$$

But, using (2.10),

2.11 $$\sum_{n=N+1}^{\infty} \log |E_\mu(z/a_n)| \leq M \sum_{n=N+1}^{\infty} \left| \frac{z}{a_n} \right|^{\mu+1} \leq \frac{\alpha}{4} |z|^{\mu+1}.$$

Now notice that in the derivation of (2.8), $A$ could be chosen as small as desired by taking $R$ sufficiently large. So choose $r_1 > 0$ such that

$$\log |E_\mu(z)| \leq \frac{\alpha}{4N} |z|^{\mu+1}, \text{ for } |z| > r_1.$$

for $|z| > r_0 = \max \{r_2, r_3\}$. By taking the exponential of both sides, the desired inequality is obtained.

The preceding theorem says that by restricting the rate of growth of the zeros of the entire function $f(z) = z^m \exp g(z)P(z)$ and by requiring that $g$ be a polynomial, then the growth of $M(r) = \max \{|f(re^{i\theta})| : 0 \leq \theta \leq 2\pi\}$ is dominated by $\exp (\alpha |z|^{\mu+1})$ for some $\mu$ and any $\alpha > 0$.

We wish to prove the converse to this result.
