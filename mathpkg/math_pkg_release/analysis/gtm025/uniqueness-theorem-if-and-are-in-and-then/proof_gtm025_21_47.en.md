---
role: proof
locale: en
of_concept: "uniqueness-theorem-if-and-are-in-and-then"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.47"
---

Let $h = f - g$. Then $\hat{h} = 0$, and so (21.43) and (21.45.a) imply that

$$h(x) = \lim

(21.49) Fourier Inversion Theorem. Let $f$ be a function in $\mathfrak{L}_1(R)$. If $f$ is also in $\mathfrak{L}_1(R)$, then

$$\left(2\pi\right)^{-\frac{1}{2}} \int_R f(y) \exp\left(ixy\right) dy = f(x)$$

for every Lebesgue point $x$ of $f$. Hence $f$ is equal a.e. to a function in $\mathfrak{C}_0(R) \cap \mathfrak{L}_1(R)$. If $f$ is continuous, then (i) holds everywhere.

Proof. Suppose that $f \in \mathfrak{L}_1(R)$ and let $x$ be a Lebesgue point of $f$. According to (21.43) and (21.45.a), we have

$$f(x) = \lim_{n \to \infty} \left(2\pi\right)^{-\frac{1}{2}} \int_R f(y) \exp\left(-\frac{|y|}{n}\right) \exp\left(ixy\right) dy. \tag{1}$$

Moreover

$$\left|f(y)\exp\left(-\frac{|y|}{n}\right)\exp\left(ixy\right)\right| \leq |f(y)| \tag{2}$$

for all $n \in N$ and all $y \in R$, and

$$\lim_{n \to \infty} \exp\left(-\frac{|y|}{n}\right) = 1 \tag{3}$$

for all $y \in R$. Since $|f| \in \mathfrak{L}_1(R)$, it follows from (1), (2), (3), and Lebesgue's dominated convergence theorem (12.30) that (i) holds. Theorem (21.39) shows that the left side of (i) is a function in $\mathfrak{C}_0(R)$; and so the second assertion holds. Two continuous functions that are equal a.e. are the same function, and so the last statement holds. $\square$

We propose now to define the Fourier transform for all functions in

for all $n \in N$. Since $f$ is nonnegative, we may apply B. Levi's theorem (12.22) to the left side of (1) to obtain

$$\left(2\pi\right)^{-\frac{1}{2}} \int_{R} f(y) \, dy \leq \|f\|_{\infty} < \infty.$$

Thus $f$ is in $\mathfrak{L}_1(R)$. The rest follows from (21.49).
