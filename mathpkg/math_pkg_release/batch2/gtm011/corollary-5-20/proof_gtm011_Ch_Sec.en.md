---
role: proof
locale: en
of_concept: corollary-5-20
source_book: gtm011
source_chapter: "Entire Functions"
source_section: ""
---

Proof. Let $\{a_j\}$ be the poles of $f$ and let $m_j$ be the order of the pole at $a_j$. According to the preceding theorem there is an analytic function $h$ with a zero of multiplicity $m_j$ at each $z = a_j$ and with no other zeros. Thus $hf$ has removable singularities at each point $a_j$. It follows that $g = hf$ is analytic in $G$.

Exercises

1. Show that $\prod (1 + z_n)$ converges absolutely iff $\prod (1 + |z_n|)$ converges.

2. Prove that $\lim_{z \to 0} \frac{\log(1 + z)}{z} = 1$.

3. Let $f$ and $g$ be analytic functions on a region $G$ and show that there are analytic functions $f_1, g_1$, and $h$ on $G$ such that $f(z) = h(z)f_1(z)$ and $g(z) = h(z)g_1(z)$ for all $z$ in $G$; and $f_1$ and $g_1$ have no common zeros.

4. (a) Let $0 < |a| < 1$ and $|z| \leq r < 1$; show that

$$\left| \frac{a + |a| z}{(1 - \bar{a} z) a} \right| \leq \frac{1 + r}{1 - r}$$

(b) Let $\{a_n

9. Use Theorem 5.15 to show there is an analytic function $f$ on $D = \{z : |z| < 1\}$ which is not analytic on any region $G$ which properly contains $D$.

10. Suppose $G$ is an open set and $\{f_n\}$ is a sequence in $H(G)$ such that $f(z) = \prod f_n(z)$ converges in $H(G)$. (a) Show that

$$\sum_{k=1}^{\infty} \left[ f'_k(z) \prod_{n \neq k} f_n(z) \right]$$

converges in $H(G)$ and equals $f'(z)$. (b) Assume that $f$ is not the identically zero function and let $K$ be a compact subset of $G$ such that $f(z) \neq 0$ for all $z$ in $K$. Show that

$$\frac{f'(z)}{f(z)} = \sum_{n=1}^{\infty} \frac{f'_n(z)}{f_n(z)}$$

and the convergence is uniform over $K$.

11. A subset $\mathcal{I}$ of $H(G)$, $G$ a region, is an ideal iff: (i) $f$ and $g$ in $\mathcal{I}$ implies $af + bg$ is in $\mathcal{I}$ for all complex numbers $a$ and $b$; (ii) $f$ in $\mathcal{I}$ and $g$ any function in $H(G)$ implies $fg$ is in $\mathcal{I}$. $\mathcal{I}$ is called a proper ideal if $\mathcal{I} \neq (0)$ and $\mathcal{I} \neq H(G)$; $\mathcal{I}$ is a maximal ideal if $\mathcal{I}$ is a proper ideal and whenever $\mathcal{J}$ is an ideal with $\mathcal{I} \subset \mathcal{J}$ then either $\mathcal{J} = \mathcal{I}$ or $\mathcal{J} = H(G)$; $\mathcal{I}$ is a prime ideal if whenever $f$ and $g \in H(G)$ and $fg \in \mathcal{I}$ then either $f \in \

Factorization of the sine function

(apostrophe) (i.e., $\sum'$ or $\prod'$), then the sum or product is to be taken over all the indicated indices $n$ except $n = 0$. For example,

$$\sum_{n=-\infty}^{\infty} a_n = \sum_{n=1}^{\infty} a_{-n} + \sum_{n=1}^{\infty} a_n.$$

The zeros of $\sin \pi z = \frac{1}{2i} \left(e^{i\pi z} - e^{-i\pi z}\right)$ are precisely the integers; moreover, each zero is simple. Since

$$\sum_{n=-\infty}^{\infty} \left(\frac{r}{n}\right)^2 < \infty$$

for all $r > 0$, one can (5.13) choose $p_n = 1$ for all $n$ in the Weierstrass Factorization Theorem. Thus

$$\sin \pi z = \left[ \exp g(z) \right] z \prod_{n=-\infty}^{\infty} \left(1 - \frac{z}{n}\right) e^{z/n};$$

or, because the terms of the infinite product can be rearranged,

6.1 $$\sin \pi z = \left[ \exp g(z) \right] z \prod_{n=1}^{\infty} \left(1 - \frac{z^2}{n^2}\right)$$

for some entire function $g(z)$. If $f(z) = \sin \pi z$ then, according to Theorem 2.1,

$$\pi \cot \pi z = \frac{f'(z)}{f(z)}$$

$$= g'(z) + \frac{1}{z} + \sum_{n=1}^{\infty} \frac{2z}{z^2 - n^2}$$

and the convergence is uniform over compact subsets of the plane that contain no integers (actually, a small additional argument is necessary to justify this—see Exercise 5.10). But according to Exercise V. 2.8,

$$\pi \cot \pi z = \frac{1}{z} + \sum_{n=1}^{\infty} \frac{

Exercises

1. Show that $\cos \pi z = \prod_{n=1}^{\infty} \left[ 1 - \frac{4z^2}{(2n-1)^2} \right]$.

2. Find a factorization for $\sinh z$ and $\cosh z$.

3. Find a factorization of the function $\cos \left( \frac{\pi z}{4} \right) - \sin \left( \frac{\pi z}{4} \right)$.

4. Prove Wallis's formula: $\frac{\pi}{2} = \prod_{n=1}^{\infty} \frac{(2n)^2}{(2n-1)(2n+1)}$.

§7. The gamma function

Let $G$ be an open set in the plane and let $\{f_n\}$ be a sequence of analytic functions on $G$. If $\{f_n\}$ converges in $H(G)$ to $f$ and $f$ is not identically zero, then it easily follows that $\{f_n\}$ converges to $f$ in $M(G)$. Since $d(z_1, z_2) = d\left(\frac{1}{z_1}, \frac{1}{z_2}\right)$, where $d$ is the spherical metric on $\mathbb{C}_\infty$ (see (3.1)), it follows that $\left\{\frac{1}{f_n}\right\}$ converges to $\frac{1}{f}$ in $M(G)$. It is an easy exercise to show that $\left\{\frac{1}{f_n}\right\}$ converges uniformly to $\frac{1}{f}$ on any compact set $K$ on which no $f_n$ vanishes. (What does Hurwitz's Theorem have to say about this situation?) Since, according to Theorem 5.12, the infinite product

$$\prod_{n=1}^{\infty} \left( 1 + \frac{z}{n} \right) e^{-z/n}$$

converges in $H(\mathbb{C})$ to an entire function which only has simple zeros at $z = -1, -2, \ldots$, the above discussion yields that

7.1 $$\prod_{n=1}^{\infty} \left(

The first thing that must be done is to show that the constant $\gamma$ exists; this is an easy matter. Substituting $z = 1$ in (7.1) yields a finite number

$$c = \prod_{n=1}^{\infty} \left( 1 + \frac{1}{n} \right)^{-1} e^{1/n}$$

which is clearly positive. Let $\gamma = \log c$; it follows that with this choice of $\gamma$, equation (7.3) for $z = 1$ gives $\Gamma(1) = 1$. This constant $\gamma$ is called Euler's constant and it satisfies

$$e^{\gamma} = \prod_{n=1}^{\infty} \left( 1 + \frac{1}{n} \right)^{-1} e^{1/n}$$

Since both sides of (7.4) involve only real positive numbers and the real logarithm is continuous, we may apply the logarithm function to both sides of (7.4) and obtain

$$\gamma = \sum_{k=1}^{\infty} \log \left[ \left( 1 + \frac{1}{k} \right)^{-1} e^{1/k} \right]$$

$$= \sum_{k=1}^{\infty} \left[ \frac{1}{k} - \log (k+1) + \log k \right]$$

$$= \lim_{n \to \infty} \sum_{k=1}^{n} \left[ \frac{1}{k} - \log (k+1) + \log k \right]$$

$$= \lim_{n \to \infty} \left[ \left( 1 + \frac{1}{2} + \ldots + \frac{1}{n} \right) - \log (n+1) \right]$$

Adding and subtracting $\log n$ to each term of this sequence and using the fact that $\lim \log \left( \frac{n+1}{n} \right) = 0$ yields

$$\gamma = \lim_{n \to \infty} \left[ \left( 1 + \frac{1}{2} + \ldots + \frac{1}{n} \right) - \log n \

However

$$e^{-\gamma z} \exp \left[ \left( 1 + \frac{1}{2} + \ldots + \frac{1}{n} \right) z \right] = n^z \exp \left[ z \left( -\gamma + 1 + \frac{1}{2} + \ldots + \frac{1}{n} - \log n \right) \right]$$

So that the following is obtained

7.6 Gauss’s Formula. For $z \neq 0, -1, \ldots$

$$\Gamma(z) = \lim_{n \to \infty} \frac{n! n^z}{z(z+1) \ldots (z+n)}$$

The formula of Gauss yields a simple derivation of the functional equation satisfied by the gamma function.

7.7 Functional Equation. For $z \neq 0, -1, \ldots$

$$\Gamma(z+1) = z \Gamma(z)$$

To obtain this important equation substitute $z+1$ for $z$ in (7.6); this gives

$$\Gamma(z+1) = \lim_{n \to \infty} \frac{n! n^{z+1}}{(z+1) \ldots (z+n+1)}$$

$$= z \lim_{n \to \infty} \left[ \frac{n! n^z}{z(z+1) \ldots (z+n)} \right] \left[ \frac{n}{z+n+1} \right]$$

$$= z \Gamma(z)$$

since $\lim \left( \frac{n}{z+n+1} \right) = 1$.

Now consider $\Gamma(z+2)$; we have $\Gamma(z+2) = \Gamma((z+1)+1) = (z+1) \Gamma(z+1)$ by the functional equation. A second application of (7.7) gives $\Gamma(z+2) = z(z+1) \Gamma(z)$. In fact, by reiterating this procedure

7.8 $$\Gamma(z+n) = z(z+1) \ldots (z+n-1) \Gamma(z)$$

for $n$ a non negative integer and

for each non-negative integer $n$. But from (7.8)

$$(z+n)\Gamma(z) = \frac{\Gamma(z+n+1)}{z(z+1) \ldots (z+n-1)}$$

So letting $z$ approach $-n$ gives that

7.10 Res $(\Gamma; -n) = \frac{(-1)^n}{n!}, n \geq 0.$

According to Exercise 5.10 we can calculate $\Gamma'/\Gamma$ by

7.11 $$\frac{\Gamma'(z)}{\Gamma(z)} = -\gamma - \frac{1}{z} + \sum_{n=1}^{\infty} \frac{z}{n(n+z)}$$

for $z \neq 0, -1, \ldots$ and convergence is uniform on every compact subset of $\mathbb{C} - \{0, -1, \ldots\}$. It follows from Theorem 2.1 that to calculate the derivative of $\Gamma'/\Gamma$ we may differentiate the series (7.11) term by term. Thus when $z$ is not a negative integer

7.12 $$\left( \frac{\Gamma'(z)}{\Gamma(z)} \right)' = \frac{1}{z^2} + \sum_{n=1}^{\infty} \frac{1}{(n+z)^2}.$$

At this time the reader may well be asking when this process will stop. Will we calculate the second derivative of $\Gamma'/\Gamma$? The answer to this question is no. The answer to the implied question of why anyone would want to derive formulas (7.11) and (7.12) is that they allow us to characterize the gamma function in a particularly beautiful way.

Notice that the definition of $\Gamma(z)$ gives that $\Gamma(x) > 0$ if $x > 0$. Thus, $\log \Gamma(x)$ is well defined for $x > 0$ and, according to formula (7.12), the second derivative of $\log \Gamma(x)$ is always positive. According to Proposition VI. 3.4 this implies that the gamma function is logarithmically convex on $(0, \infty)$; that is, $\log \Gamma(x)$ is conve

equation will give that $f$ and $\Gamma$ are everywhere identical. Let $0 < x \leq 1$ and let $n$ be an integer larger than 2. From Exercise VI. 3.3

$$\frac{\log f(n-1) - \log f(n)}{(n-1) - n} \leq \frac{\log f(x+n) - \log f(n)}{(x+n) - n} \leq \frac{\log f(n+1) - \log f(n)}{(n+1) - n}$$

Since (7.14) holds we have that $f(m) = (m-1)!$ for every integer $m \geq 1$. Thus the above inequalities become

$$-\log (n-2)! + \log (n-1)! \leq \frac{\log f(x+n) - \log (n-1)!}{x} \leq \log n! - \log (n-1)!;$$

or

$$x \log (n-1) \leq \log f(x+n) - \log (n-1)! \leq x \log n.$$

Adding $\log (n-1)!$ to each side of this inequality and applying the exponential (exp is a monotone increasing function and therefore preserves inequalities) gives

$$(n-1)^x (n-1)! \leq f(x+n) \leq n^x (n-1)!$$

Applying (7.14) to calculate $f(x+n)$ yields

$$\frac{(n-1)^x (n-1)!}{x(x+1) \ldots (x+n-1)} \leq f(x) \leq \frac{n^x (n-1)!}{x(x+1) \ldots (x+n-1)}$$

$$= \frac{n^x n!}{x(x+1) \ldots (x+n)} \left[ \frac{x+n}{n} \right].$$

Since the term in the middle of this sandwich, $f(x)$, does not involve the integer $n$ and since the inequality holds for all integers $n \geq 2$, we may vary the
