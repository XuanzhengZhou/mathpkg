---
role: proof
locale: en
of_concept: prop-suppose-that-and-then
source_book: gtm034
source_chapter: "3"
source_section: "008"
---

Proof: An examination of the proof will show that one may assume, without loss of generality, that $\sigma^2 = 1$. Defining

$$F_n(x) = \sum_{t=-\infty}^{[xn^{1/2}]} P_n(0,t) = \mathbf{P}[\mathbf{S}_n \leq \sqrt{nx}],$$

$$F(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{t^2}{2}} dt,$$

we find that the content of the Central Limit Theorem is the convergence of $F_n(x)$ to $F(x)$ at every real $x$. For every $A > 0, k > 0$

$$\left| \int_{0}^{\infty} x dF_k(x) - \int_{0}^{\infty} x dF(x) \right|$$

$$\leq \left| \int_{0}^{A} x dF_k(x) - \int_{0}^{A} x dF(x) \right| + \int_{A}^{\infty} x dF(x) + \int_{A}^{\infty} x dF_k(x).$$

The last integral is less than

$$\frac{1}{A} \int_{A}^{\infty} x^2 dF_k(x) = \frac{1}{A} \mathbf{E}\left[ \frac{\mathbf{S}_k^2}{k}; \mathbf{S}_k^2 > Ak \right] \leq \frac{1}{A} \mathbf{E}\left[ \frac{\mathbf{

which gives (2) by use of the dominated convergence theorem). Combining (1) and (2) we have

$$\left| \int_0^\infty x dF_k(x) - \int_0^\infty x dF(x) \right| < \epsilon$$

for large enough $k$. But

$$\int_0^\infty x dF_k(x) = \frac{1}{\sqrt{k}} \mathbf{E}[\mathbf{S}_k; \mathbf{S}_k \geq 0],$$

$$\int_0^\infty x dF(x) = \frac{1}{\sqrt{2\pi}},$$

and that proves the first part of P3. The second part reduces to showing that if a sequence $c_n$ has a limit as $n \to \infty$, then

$$\lim_{t \to 1} \sqrt{1-t} \sum_{n=1}^{\infty} \frac{c_n t^n}{\sqrt{n}} = \sqrt{\pi} \lim_{n \to \infty} c_n.$$

A typical Abelian argument accomplishes the proof, using the fact (derivable from Stirling's formula) that

$$\binom{-1/2}{n} \sim \frac{1}{\sqrt{n\pi}}, \quad n \to \infty,$$

so that as $t$ tends to one

$$\sqrt{1-t} \sum_{n=1}^{\infty} \frac{c_n t^n}{\sqrt{n}} \sim \sqrt{\pi} \left( \lim_{n \to \infty} c_n \right) \sqrt{1-t} \sum_{n=0}^{\infty} \binom{-1/2}{n} t^n$$

$$= \sqrt{\pi} \lim_{n \to \infty} c_n.$$

In the course of proving that (B) implies (A) in T1 we shall be able to conclude that

$$\lim_{t \to 1} \sum_{k=1}^{\infty} \frac{t^k}{k} \left\{ \frac{1}{2} - \mathbf{P}[\mathbf{S}_k > 0] \right\}$$

exists and is finite. In view of the Central

the "little $o$" meaning that $ka_k \to 0$ as $k \to \infty$. To such power series one can apply Tauber's theorem [39], the simplest and historically the first (1897) of many forms of the converse of Abel's theorem, to conclude that

$$\lim_{t \to 1} \sum_{k=1}^{\infty} \frac{t^k}{k} \left\{ \frac{1}{2} - P[S_k > 0] \right\} = \sum_{k=1}^{\infty} \frac{1}{k} \left\{ \frac{1}{2} - P[S_k > 0] \right\}.$$

Now we are ready to resume the proof of T1, and by following a rather elaborate route we shall obtain
