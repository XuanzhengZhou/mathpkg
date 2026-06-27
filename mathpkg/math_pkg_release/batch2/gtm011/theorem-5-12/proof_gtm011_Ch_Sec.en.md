---
role: proof
locale: en
of_concept: theorem-5-12
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Suppose there are integers $p_n$ such that (5.13) is satisfied. Then, according to Lemma 5.11,

matter. For any $r$ there is an integer $N$ such that $|a_n| > 2r$ for all $n \geq N$. This gives that $\left(\frac{r}{|a_n|}\right) < \frac{1}{2}$ for all $n \geq N$; so if $p_n = n-1$ for all $n$, the tail end of the series (5.13) is dominated by $\sum \left(\frac{1}{2}\right)^n$. Thus, (5.13) converges.

There is, of course, a great latitude in picking the integers $p_n$. If $p_n$ were bigger than $n-1$ we would have the same conclusion. However, there is an advantage in choosing the $p_n$ as small as possible. After all, the smaller the integer $p_n$ the more elementary the elementary factor $E_{p_n}(z/a_n)$. As is evident in considering the series (5.13), the size of the integers $p_n$ depends on the rate at which $\{|a_n|\}$ converges to infinity. This will be explored later in Chapter XI.

5.14 The Weierstrass Factorization Theorem. Let $f$ be an entire function and let $\{a_n\}$ be the non-zero zeros of $f$ repeated according to multiplicity; suppose $f$ has a zero at $z=0$ of order $m \geq 0$ (a zero of order $m=0$ at $z=0$ means $f(0) \neq 0$). Then there is an entire function $g$ and a sequence of integers $\{p_n\}$ such that

$$f(z) = z^m e^{g(z)} \prod_{n=1}^{\infty} E_{p_n}\left(\frac{z}{a_n}\right).$$

Proof. According to the preceding theorem integers $\{p_n\}$ can be chosen such that

$$h(z) = z^m \prod_{n=1}^{\infty} E_{p_n}\left(\frac{z}{a_n}\right)$$

has the same zeros as $f$ with the same multiplicities. It follows that $f(z)/h(z)$

and with the further property that

5.17 $$\lim_{z \to \infty} f(z) = 1.$$

In fact, if such an $f$ can always be found for a set satisfying (5.16), let $G_1$ be an arbitrary open set in $\mathbb{C}$ with $\{\alpha_j\}$ a sequence of distinct points in $G_1$ with no limit point, and let $\{m_j\}$ be a sequence of integers. Now if $\bar{B}(a; r)$ is a disk in $G_1$ such that $\alpha_j \notin B(a; r)$ for all $j \geq 1$, consider the Möbius transformation $Tz = (z - a)^{-1}$. Put $G = T(G_1) \setminus \{\infty\}$; it is easy to see that $G$ satisfies condition (5.16) where $a_j = T\alpha_j = (\alpha_j - a)^{-1}$. If there is a function $f$ in $H(G)$ with a zero at each $a_j$ of multiplicity $m_j$, with no other zeros, and such that $f$ satisfies (5.17); then $g(z) = f(Tz)$ is analytic in $G_1 - \{a\}$ with a removable singularity at $z = a$. Furthermore, $g$ has the prescribed zero at each $\alpha_j$ of multiplicity $m_j$.

So assume that $G$ satisfies (5.16). Define a second sequence $\{z_n\}$ consisting of the points in $\{a_j\}$, but such that each $a_j$ is repeated according to its multiplicity $m_j$. Now, for each $n \geq 1$ there is a point $w_n$ in $\mathbb{C} - G$ such that

$$|w_n - z_n| = d(z_n, \mathbb{C} - G).$$

Notice that the hypothesis (5.16) excludes the possibility that $G = \mathbb{C}$ unless the sequence $\{a_j\}$ were finite. In fact, if $\{a_j\}$ were finite the theorem could be easily proved so it suffices to assume that $\{a_j\}$ is infinite

for all $z$ in $K$ and $n \geq N$. But this gives that the series

$$\sum_{n=1}^{\infty} \left[ E_n \left( \frac{z_n - w_n}{z - w_n} \right) - 1 \right]$$

converges uniformly and absolutely on $K$. According to Theorem 5.9

$$f(z) = \prod_{n=1}^{\infty} E_n \left( \frac{z_n - w_n}{z - w_n} \right)$$

converges in $H(G)$, so that $f$ is an analytic function on $G$. Also, Theorem 5.9 implies that the points $\{a_j\}$ are the only zeros of $f$ and $m_j$ is the order of the zero at $z = a_j$ (because $a_j$ occurs $m_j$ times in the sequence $\{z_n\}$). To show that $\lim f(z) = 1$, let $\epsilon > 0$ be an arbitrary number and let $R_1 > R$ ($R_1$ will be further specified shortly). If $|z| \geq R_1$ then, because $|z_n| \leq R$ and $w_n \in \mathbb{C} - G \subset B(0; R)$,

$$\left| \frac{z_n - w_n}{z - w_n} \right| \leq \frac{2R}{R_1 - R}.$$

So, if we choose $R_1 > R$ so that $2R < \delta(R_1 - R)$ for some $\delta, 0 < \delta < 1$, (5.18) holds for $|z| \geq R_1$ and for all $n \geq 1$. In particular, $\text{Re} E_n \left( \frac{z_n - w_n}{z - w_n} \right) > 0$ for all $n$ and $|z| \geq R_1$; so that

$$|f(z) - 1| = \left| \exp \left( \sum_{n=1}^{\infty} \log E_n \left( \frac{z_n - w_n}{z

then equation (5.19) gives that $|f(z) - 1| < \epsilon$ whenever $|z| \geq R_1$. That is, $\lim_{z \to \infty} f(z) = 1$.

One of the more interesting results that follows from the above theorem says (in algebraic terms) that $M(G)$ is the quotient field of the integral domain $H(G)$. Avoiding this language the result is as follows.
