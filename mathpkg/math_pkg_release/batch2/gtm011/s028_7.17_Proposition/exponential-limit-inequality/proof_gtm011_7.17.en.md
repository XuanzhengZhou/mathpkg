---
role: proof
locale: en
of_concept: exponential-limit-inequality
source_book: gtm011
source_chapter: "7"
source_section: "7.17"
---

(a) Let $K$ be a compact subset of the plane. Then $|z| < n$ for all $z$ in $K$ and $n$ sufficiently large. It suffices to show that

$$\lim_{n \to \infty} n \log \left(1 + \frac{z}{n}\right) = z$$

uniformly for $z$ in $K$ by Lemma 5.7. Recall that

$$\log (1 + w) = \sum_{k=1}^{\infty} (-1)^{k-1} \frac{w^k}{k}$$

for $|w| < 1$. Let $n > |z|$ for all $z$ in $K$; if $z$ is any point in $K$ then

$$n \log \left(1 + \frac{z}{n}\right) = z - \frac{1}{2} \frac{z^2}{n} + \frac{1}{3} \frac{z^3}{n^2} - \dots.$$

So

$$n \log \left(1 + \frac{z}{n}\right) - z = z \left[ -\frac{1}{2} \left(\frac{z}{n}\right) + \frac{1}{3} \left(\frac{z}{n}\right)^2 - \dots \right];$$

taking absolute values gives that

$$\left| n \log \left(1 + \frac{z}{n}\right) - z \right| \leq |z| \sum_{k=2}^{\infty} \frac{1}{k} \left| \frac{z}{n} \right|^{k-1}.$$

Since the series $\sum_{k=2}^{\infty} \frac{1}{k} r^{k-1}$ converges for $0 \leq r < 1$, the right-hand side tends to $0$ uniformly for $z \in K$ as $n \to \infty$, establishing uniform convergence of $n \log(1 + z/n)$ to $z$. By Lemma 5.7 (which relates uniform convergence of logarithms to uniform convergence of the original sequence), this implies $\{(1 + z/n)^n\}$ converges to $e^z$ in $H(\mathbb{C})$.

(b) For $t \geq 0$ and $n \geq t$, using the series expansion of $\log$ gives

$$\log \left(1 - \frac{t}{n}\right) = -\sum_{k=1}^{\infty} \frac{1}{k} \left(\frac{t}{n}\right)^k \leq -\frac{t}{n}.$$

Thus

$$n \log \left( 1 - \frac{t}{n} \right) \leq -t;$$

and since $\exp$ is a monotone function, part (b) is proved:

$$\left(1 - \frac{t}{n}\right)^n \leq e^{-t}.$$
