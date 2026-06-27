---
role: proof
locale: en
of_concept: great-picard-theorem
source_book: gtm011
source_chapter: "XII"
source_section: "§4. The Great Picard Theorem"
---

Suppose $f$ has an essential singularity at $z = 0$ and there exist two distinct complex numbers $\alpha$ and $\beta$ and a sequence $\{z_n\}$ with $z_n \to 0$ such that $f(z_n) \notin \{\alpha, \beta\}$ for all $n$. By considering $\frac{f(z) - \alpha}{\beta - \alpha}$, we may assume $\alpha = 0$ and $\beta = 1$.

Define $f_n(z) = f(z/n)$. Then each $f_n$ is analytic on $\{z : 0 < |z| < R\}$ for sufficiently large $n$, and does not assume the values $0$ and $1$ there. Let $\{f_{n_k}\}$ be a subsequence of $\{f_n\}$ such that $f_{n_k} \to \varphi$ uniformly on $\{z : |z| = \frac{1}{2}R\}$, where $\varphi$ is either analytic on $G$ or $\varphi \equiv \infty$.

If $\varphi$ is analytic, let $M = \max\{|\varphi(z)| : |z| = \frac{1}{2}R\}$. Then

$$|f(z/n_k)| = |f_{n_k}(z)| \leq |f_{n_k}(z) - \varphi(z)| + |\varphi(z)| \leq 2M$$

for $n_k$ sufficiently large and $|z| = \frac{1}{2}R$. Thus $|f(z)| \leq 2M$ for $|z| = R/(2n_k)$ and for sufficiently large $n_k$. By the Maximum Modulus Principle, $f$ is uniformly bounded on concentric annuli about zero. This gives that $f$ is bounded by $2M$ on a deleted neighborhood of zero, so $z = 0$ must be a removable singularity. Therefore $\varphi$ cannot be analytic and must be identically infinite.

If $\varphi \equiv \infty$, then $f$ must have a pole at zero.

Hence at most one complex number is never assumed. If there is a complex number $w$ which is assumed only a finite number of times, then by taking a sufficiently small disk, we again arrive at a punctured disk in which $f$ fails to assume two values.
