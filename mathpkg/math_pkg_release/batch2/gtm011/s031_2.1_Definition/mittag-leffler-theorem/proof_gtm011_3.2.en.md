---
role: proof
locale: en
of_concept: mittag-leffler-theorem
source_book: gtm011
source_chapter: "VIII"
source_section: "3.2"
---

**Proof.** Although the details of this proof are somewhat cumbersome, the idea is simple. We use Runge's Theorem to find rational functions \(\{R_k(z)\}\) with poles in \(\mathbb{C}_\infty - G\) such that \(\left\{\sum_{k=1}^n S_k(z) - R_k(z)\right\}\) is a Cauchy sequence in \(M(G)\). The resulting limit is the sought-after meromorphic function. (Actually we must do a little more than this.)

Use Proposition VII.1.2 to find compact subsets of \(G\) such that

\[
G = \bigcup_{n=1}^{\infty} K_n, \quad K_n \subset \operatorname{int} K_{n+1},
\]

and each component of \(\mathbb{C}_\infty - K_n\) contains a component of \(\mathbb{C}_\infty - G\). Since each \(K_n\) is compact and \(\{a_k\}\) has no limit point in \(G\), there are only a finite number of points \(a_k\) in each \(K_n\). Define the sets of integers \(I_n\) as follows:

\[
I_1 = \{k : a_k \in K_1\},
\]
\[
I_n = \{k : a_k \in K_n - K_{n-1}\} \quad (n \geq 2).
\]

Now use Runge's Theorem to choose rational functions \(R_n\) with poles in \(\mathbb{C}_\infty - G\) such that

\[
\left| \sum_{k \in I_n} S_k(z) - R_n(z) \right| < \left( \frac{1}{2} \right)^n
\]

for all \(z\) in \(K_{n-1}\). Define

\[
f(z) = \sum_{n=1}^{\infty} \left[ \sum_{k \in I_n} S_k(z) - R_n(z) \right]. \tag{3.3}
\]

We must show that \(f\) is a meromorphic function and that it has the desired properties. Start by showing that the series in (3.3) converges uniformly on every compact subset of \(G - \{a_k : k \geq 1\}\). This will give that \(f\) is analytic on \(G - \{a_k : k \geq 1\}\) and it will only remain to show that each \(a_k\) is a pole with singular part \(S_k(z)\).

So let \(K\) be a compact subset of \(G - \{a_k : k \geq 1\}\); then \(K\) is a compact subset of \(G\) and, therefore, there is an integer \(N\) such that \(K \subset K_N\). If \(n \geq N\) then

\[
\left| \sum_{k \in I_n} S_k(z) - R_n(z) \right| < \left( \frac{1}{2} \right)^n
\]

for all \(z\) in \(K\). That is, the series (3.3) is dominated on \(K\) by a convergent series of numbers; by the Weierstrass \(M\)-test (II.6.2) the series (3.3) converges uniformly on \(K\). Thus \(f\) is analytic on \(G - \{a_k : k \geq 1\}\).

Now consider a fixed integer \(k \geq 1\); there is a number \(R > 0\) such that \(|a_j - a_k| > R\) for \(j \neq k\). Thus

\[
f(z) = S_k(z) + g(z)
\]

for \(0 < |z - a_k| < R\), where \(g\) is analytic in \(B(a_k; R)\). Hence, \(z = a_k\) is a pole of \(f\) and \(S_k(z)\) is its singular part. This completes the proof of the theorem.
