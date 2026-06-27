---
role: proof
locale: en
of_concept: area-bound-for-polynomial-hull
source_book: gtm035
source_chapter: "Chapter 21"
source_section: "21.1"
---
# Proof of Area Bound for Polynomial Hulls

**Theorem 21.1.** Let $A$ be a uniform algebra on the compact space $X$ with maximal ideal space $M$. Let $\varphi \in M$ and let $\mu$ be a representing measure supported on $X$ for $\varphi$. Let $f \in A$ and suppose that $\varphi(f) = 0$. Then

$$\pi \int |f|^2 \, d\mu \leq \operatorname{area}(f(M)).$$

**Proof.** Let $\varepsilon > 0$ and put $K = f(M)$. By Lemma 21.3 there is a rational function $r(z)$ with poles off of $K$ such that

$$\|\bar{z} - r(z)\|_K < \left( \frac{\operatorname{area}(K) + \varepsilon}{\pi} \right)^{1/2}.$$

Since $r$ is holomorphic on a neighborhood of the spectrum $K$ of $f$, it follows from the Gelfand theory that $g = r \circ f \in A$ and

$$\|\bar{f} - g\|_M < \left( \frac{\operatorname{area}(K) + \varepsilon}{\pi} \right)^{1/2}.$$

We have $|f|^2 = f(\bar{f} - g) + fg$. Since $g \in A$, we get

$$\int fg \, d\mu = \varphi(f)\varphi(g) = 0,$$

and so

$$\int |f|^2 \, d\mu = \int f(\bar{f} - g) \, d\mu.$$

Thus

$$\int |f|^2 \, d\mu \leq \|\bar{f} - g\|_M \int |f| \, d\mu \leq \left( \frac{\operatorname{area}(K) + \varepsilon}{\pi} \right)^{1/2} \int |f| \, d\mu.$$

Now, letting $\varepsilon \to 0$ yields

$$\int |f|^2 \, d\mu \leq \left( \frac{\operatorname{area}(K)}{\pi} \right)^{1/2} \int |f| \, d\mu.$$

Estimating the last integral by Hölder's inequality,

$$\int |f| \, d\mu \leq \left( \int |f|^2 \, d\mu \right)^{1/2},$$

gives

$$\int |f|^2 \, d\mu \leq \left( \frac{\operatorname{area}(K)}{\pi} \right)^{1/2} \left( \int |f|^2 \, d\mu \right)^{1/2}.$$

Cancelling $\left( \int |f|^2 \, d\mu \right)^{1/2}$ (if it is zero the theorem is trivial) yields

$$\pi \int |f|^2 \, d\mu \leq \operatorname{area}(K) = \operatorname{area}(f(M)).$$

∎
