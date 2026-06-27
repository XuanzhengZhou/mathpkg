---
role: proof
locale: en
of_concept: proposition-3-7
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. From the hypothesis

$$\left| \frac{f(z)}{

|f+g| < |g| on $\gamma$. This weaker version often suffices in the applications as can be seen in the next paragraph.

Rouché's Theorem can be used to give another proof of the Fundamental Theorem of Algebra. If $p(z) = z^n + a_1 z^{n-1} + \cdots + a_n$ then

$$\frac{p(z)}{z^n} = 1 + \frac{a_1}{z} + \cdots + \frac{a_n}{z^n}$$

and this approaches 1 as $z$ goes to infinity. So there is a sufficiently large number $R$ with

$$\left| \frac{p(z)}{z^n} - 1 \right| < 1$$

for $|z| = R$; that is, $|p(z) - z^n| < |z|^n$ for $|z| = R$. Rouché's Theorem says that $p(z)$ must have $n$ zeros inside $|z| = R$.

We also mention that the use of a circle in Rouché's Theorem was a convenience and not a necessity. Any closed rectifiable curve $\gamma$ with $\gamma \sim 0$ in $G$ could have been used, although the conclusion would have been modified by the introduction of winding numbers.

Exercises

1. Prove Theorem 3.6.

2. Suppose $f$ is analytic on $\bar{B}(0; 1)$ and satisfies $|f(z)| < 1$ for $|z| = 1$. Find the number of solutions (counting multiplicities) of the equation $f(z) = z^n$ where $n$ is an integer larger than or equal to 1.

3. Let $f$ be analytic in $B(0; R)$ with $f(0) = 0$, $f'(0) \neq 0$ and $f(z) \neq 0$ for $0 < |z| \leq R$. Put $\rho = \min\{|f(z)|: |z| = R\} > 0$. Define $g: B(0; \rho) \to \mathbb{C}$ by

$$g(\omega)

arises, is every meromorphic function on $G$ the quotient of two analytic functions on $G$? Alternately, is $M(G)$ the quotient field of $H(G)$? The answer is yes but some additional theory will be required before this answer can be proved.

7. State and prove a more general version of Rouché’s Theorem for curves other than circles in $G$.

8. Is a non-constant meromorphic function on a region $G$ an open mapping of $G$ into $\mathbb{C}$? Is it an open mapping of $G$ into $\mathbb{C}_{\infty}$?

9. Let $\lambda > 1$ and show that the equation $\lambda - z - e^{-z} = 0$ has exactly one solution in the half plane $\{z: \text{Re } z > 0\}$. Show that this solution must be real. What happens to the solution as $\lambda \to 1$?

10. Let $f$ be analytic in a neighborhood of $D = \bar{B}(0; 1)$. If $|f(z)| < 1$ for $|z| = 1$, show that there is a unique $z$ with $|z| < 1$ and $f(z) = z$. If $|f(z)| \leq 1$ for $|z| = 1$, what can you say?
