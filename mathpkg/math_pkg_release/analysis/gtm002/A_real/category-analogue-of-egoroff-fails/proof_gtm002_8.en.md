---
role: proof
locale: en
of_concept: category-analogue-of-egoroff-fails
source_book: gtm002
source_chapter: "8"
source_section: "The Theorems of Lusin and Egoroff"
---

Let $\phi(x)$ be the piecewise linear continuous function defined by
$$\phi(x) = \begin{cases}
2x & \text{on } [0, 1/2], \\
2 - 2x & \text{on } [1/2, 1], \\
0 & \text{on } \mathbb{R} - [0, 1].
\end{cases}$$

Then $\phi \geq 0$ and $\lim_{n \to \infty} \phi(2^n x) = 0$ for every $x \in \mathbb{R}$ (since for each fixed $x \neq 0$, $\phi(2^n x) = 0$ for all sufficiently large $n$, and for $x = 0$, $\phi(0) = 0$).

Let $\{r_i\}_{i=1}^{\infty}$ be a dense sequence in $\mathbb{R}$ (for example, an enumeration of the rationals), and define
$$f_n(x) = \sum_{i=1}^{\infty} 2^{-i} \phi\bigl( 2^n (x - r_i) \bigr).$$

The series converges uniformly in $x$ for each fixed $n$, since $|\phi| \leq 1$ and $\sum 2^{-i} = 1$. As a uniform limit of continuous functions, each $f_n$ is continuous on $\mathbb{R}$. Moreover,
$$\lim_{n \to \infty} f_n(x) = \sum_{i=1}^{\infty} 2^{-i} \lim_{n \to \infty} \phi\bigl( 2^n (x - r_i) \bigr) = 0$$
for each $x \in \mathbb{R}$ (the interchange of limit and sum is justified by the uniform bound $|\phi| \leq 1$).

Now let $(a, b)$ be any nonempty open interval. Since $\{r_i\}$ is dense, there exists some index $i$ such that $r_i \in (a, b)$. For this $i$, consider $x = r_i + 2^{-n-1}$. For all sufficiently large $n$, we have $x \in (a, b)$, and
$$\phi\bigl( 2^n (x - r_i) \bigr) = \phi(1/2) = 1.$$
Hence
$$f_n(x) \geq 2^{-i} \cdot 1 = 2^{-i}.$$
Since there are points in $(a, b)$ where $f_n(x) \geq 2^{-i}$ for arbitrarily large $n$, the convergence $f_n \to 0$ is not uniform on $(a, b)$.

Moreover, for any first-category set $P \subset \mathbb{R}$, the complement $\mathbb{R} - P$ is dense (by the Baire category theorem). Hence $(a, b) - P$ is nonempty, and the same argument shows that $\sup_{x \in (a,b) - P} f_n(x) \geq 2^{-i}$ for all sufficiently large $n$. Therefore $f_n$ does **not** converge uniformly to $0$ on $(a, b) - P$ for any first-category set $P$ and any nonempty open interval $(a, b)$.

This demonstrates that the direct category analogue of Egoroff's theorem — namely, "if $f_n \to f$ pointwise on $\mathbb{R}$ and each $f_n$ has the Baire property, then there exists a first-category set $P$ such that $f_n \to f$ uniformly on $\mathbb{R} - P$" — is false.
