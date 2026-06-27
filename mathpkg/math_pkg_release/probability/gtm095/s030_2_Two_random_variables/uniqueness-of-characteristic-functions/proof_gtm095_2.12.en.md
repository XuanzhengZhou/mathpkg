---
role: proof
locale: en
of_concept: uniqueness-of-characteristic-functions
source_book: gtm095
source_chapter: "2"
source_section: "12"
---

# Proof of Uniqueness Theorem for Characteristic Functions

Let $F$ and $G$ be distribution functions such that

$$\int_{-\infty}^{\infty} e^{itx} dF(x) = \int_{-\infty}^{\infty} e^{itx} dG(x)$$

for all $t \in R$. We show that $F(x) \equiv G(x)$.

Choose $a, b \in R$ and $\varepsilon > 0$, and consider the piecewise linear function $f^\varepsilon = f^\varepsilon(x)$ that equals $1$ on $[a, b]$, $0$ outside $[a-\varepsilon, b+\varepsilon]$, and is linear on the intermediate intervals. We show that

$$\int_{-\infty}^{\infty} f^\varepsilon(x) dF(x) = \int_{-\infty}^{\infty} f^\varepsilon(x) dG(x).$$

Let $n \geq 0$ be large enough so that $[a, b+\varepsilon] \subseteq [-n, n]$, and let $\{\delta_n\}$ be a sequence with $1 \geq \delta_n \downarrow 0$ as $n \to \infty$. By the Weierstrass-Stone theorem, every continuous function on $[-n, n]$ that takes equal values at the endpoints can be uniformly approximated by trigonometric polynomials. Hence there exists a finite sum

$$f_n^\varepsilon(x) = \sum_k a_k \exp\left( i\pi x \frac{k}{n} \right)$$

such that

$$\sup_{-n \leq x \leq n} |f^\varepsilon(x) - f_n^\varepsilon(x)| \leq \delta_n.$$

Extend the periodic function $f_n^\varepsilon(x)$ to all of $R$, and observe that $\sup_x |f_n^\varepsilon(x)| \leq 2$.

Since $F$ and $G$ have the same characteristic function, and $f_n^\varepsilon$ is a trigonometric polynomial, we have

$$\int_{-\infty}^{\infty} f_n^\varepsilon(x) dF(x) = \int_{-\infty}^{\infty} f_n^\varepsilon(x) dG(x).$$

Consequently,

$$\begin{aligned}
&\left| \int_{-\infty}^{\infty} f^\varepsilon(x) dF(x) - \int_{-\infty}^{\infty} f^\varepsilon(x) dG(x) \right| \\
&\quad \leq \left| \int_{-\infty}^{\infty} f^\varepsilon(x) dF(x) - \int_{-\infty}^{\infty} f_n^\varepsilon(x) dF(x) \right|
+ \left| \int_{-\infty}^{\infty} f_n^\varepsilon(x) dG(x) - \int_{-\infty}^{\infty} f^\varepsilon(x) dG(x) \right| \\
&\quad \leq 2\delta_n (F(n) - F(-n)) + 2\delta_n (G(n) - G(-n)) + 2(F(-n) + 1 - F(n) + G(-n) + 1 - G(n)).
\end{aligned}$$

Letting first $n \to \infty$ and then $\varepsilon \downarrow 0$, we obtain $F(b) - F(a-) = G(b) - G(a-)$ for all continuity points $a, b$. Hence $F \equiv G$ everywhere.
