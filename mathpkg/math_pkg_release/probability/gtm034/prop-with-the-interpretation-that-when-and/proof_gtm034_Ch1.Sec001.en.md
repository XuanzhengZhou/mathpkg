---
role: proof
locale: en
of_concept: prop-with-the-interpretation-that-when-and
source_book: gtm034
source_chapter: "1"
source_section: "001"
---

Proof: It would perhaps be natural to use the method of generating functions, applied to the convolution equation

(1) $$P_n(0,0) = \sum_{k=0}^{

Summing the convolution equation (1) over $n = 1, 2, \ldots, m$, and adding $P_0(0,0) = 1$ on each side, gives

(2) $G_m = \sum_{k=0}^{m} F_k G_{m-k} + 1, \quad m \geq 1.$

Letting $m \to \infty,$

$$G = 1 + \lim_{m \to \infty} \sum_{k=0}^{m} F_k G_{m-k} \geq 1 + G \sum_{k=0}^{N} F_k,$$

for every integer $N$, and therefore

$$G \geq 1 + GF.$$

This proves, by the way, that $G = +\infty$ when $F = 1$, since the inequality $G \geq 1 + G$ has no finite solutions.

On the other hand, equation (2) gives

(3) $1 = G_m - \sum_{k=0}^{m} G_k F_{m-k} \geq G_m - G_m \sum_{k=0}^{m} F_{m-k} \geq G_m(1 - F),$

so that $1 \geq G(1 - F)$, which shows that $G < \infty$ when $F < 1$. That completes the proof of the identity $G(1 - F) = 1$, and hence of P4.

E2 Consider Bernoulli random walk with $P(0,1) = p, P(0,-1) = q.$ An easy calculation (see E1) gives $P_n(0,0) = 0$ when $n$ is an odd integer, and

(1) $P_{2n}(0,0) = (pq)^n \binom{2n}{n} = (-1)^n (4pq)^n \binom{-1/2}{n}.$

Since $p$ and $q$ are not arbitrary, but $0 \leq p = 1 - q$, it follows that $4pq \leq 1.$ Thus the Binomial Theorem yields the power series (generating function)

(2) $\sum_{n=0}^{\infty} t^n P

It follows from (2), compared to (3), that

$$G = \begin{cases} (1 - 4pq)^{-1/2} < \infty & \text{when } p \neq q \\ +\infty & \text{when } p = q = 1/2. \end{cases}$$

In view of P4, we have shown that Bernoulli random walk in one-dimension is recurrent if and only if $p = q = 1/2$, i.e., simple random walk is the only recurrent Bernoulli random walk.

For the sake of completeness, let us repeat the above argument, working with $F$ instead of with $G$. Setting $x = y = 0$ in part (c) of P2,

$$P_n(0,0) = \sum_{k=0}^{n} P_{n-k}(0,0)F_k(0,0) \text{ for } n \geq 1,$$

or

$$P_n(0,0) = \sum_{k=0}^{n} P_{n-k}(0,0)F_k(0,0) + \delta(n,0) \text{ for } n \geq 0.$$

That gives

$$\sum_{n=0}^{\infty} t^n P_n(0,0) = \sum_{n=0}^{\infty} t^n P_n(0,0) \sum_{n=1}^{\infty} t^n F_n(0,0) + 1, \quad 0 \leq t < 1.$$

Replacing $t$ by $\sqrt{t}$, one concludes from equation (2) that

$$\sum_{n=0}^{\infty} t^n F_{2n}(0,0) = 1 - \sqrt{1 - 4pq}t, \quad 0 \leq t < 1.$$

Again one arrives at the conclusion that

$$F = \lim_{t \to 1} \sum_{n=1}^{\infty} t^n F_{2n}(0,0) = 1 - \sqrt{1 - 4pq} = 1$$

if and only if $4pq = 1$, which happens when $p = q = 1/

where $r_1 = p/q, r_2 = 1$ are the zeros of the polynomial $qt^2 - t + p$. Now we need a "particular" solution $\varphi(x)$ of the nonhomogeneous equation

(8) $\varphi(x) - \delta(x,0) = p\varphi(x - 1) + q\varphi(x + 1)$.

Let us choose $\varphi(0) = \varphi(1) = 0$. Then the function $\varphi(x)$ has a unique extension to $R$ which satisfies (8), and it is simple to calculate, recursively, that

(9) $\varphi(x) = 0$ for $x \geq 0$, $\varphi(x) = (p - q)^{-1}\left[\left(\frac{p}{q}\right)^x - 1\right]$ for $x \leq 0$.

It follows from the elementary theory of difference equations that $G(0,x)$ must be obtainable by superposition of functions in (7) and (9), i.e.,

(10) $G(0,x) = \varphi(x) + A\left(\frac{p}{q}\right)^x + B$.

Observe now that the function $\varphi(x)$ in (9) is bounded (since we are assuming that $p > q$). According to P3 we have $G(0,x) \leq G < \infty$ which implies that $A = 0$. Thus it remains only to evaluate the constant $B$, using equation (4), to the effect that

$$G(0,0) = (1 - 4pq)^{-1/2} = \frac{1}{p - q}$$

From (9) and (10) one therefore obtains the result that $B = (p - q)^{-1}$, and we have proved that for Bernoulli random walk with $p > q$,

(11) $G(0,x) = \begin{cases} (p - q)^{-1} & \text{for } x \geq 0 \\ (p - q)^{-1}\left(\frac{p}{q}\right)^x & \text{for } x \leq 0. \end{cases}$

One last result, easily within reach of the elementary methods of this section

Proof: First we observe that it suffices to prove P5 in the special case when $y = 0$. Thus we may use part (c) of P2 in the form

$$G_n(x,0) = \delta(x,0) + \sum_{k=1}^{n} P_k(x,0)$$

$$= \delta(x,0) + \sum_{j=0}^{n} P_j(0,0) \sum_{k=1}^{n-j} F_k(x,0),$$

so that

$$\frac{G_n(x,0)}{G_n(0,0)} = \frac{\delta(x,0)}{\sum_{j=0}^{n} P_j(0,0)} + \frac{\sum_{j=0}^{n} P_j(0,0) \sum_{k=0}^{n-j} F_k(x,0)}{\sum_{j=0}^{n} P_j(0,0)}, \quad x \in R.$$

In the transient case the denominators have a finite limit, so that one obtains

$$\lim_{n \to \infty} \frac{G_n(x,0)}{G_n(0,0)} = \frac{\delta(x,0)}{G} + F(x,0)$$

for all $x$ in $R$, and in particular the limit $F(x,0)$ when $x \neq 0$.

To obtain a proof when the random walk is recurrent, let

$$a_n = \sum_{k=0}^{n} F_k(x,0), \quad b_n = P_n(0,0), \quad n \geq 0.$$

The problem is then to show that

$$\lim_{n \to \infty} \frac{\sum_{j=0}^{n} b_j a_{n-j}}{\sum_{k=0}^{n} b_k} = \lim_{n \to \infty} a_n = F(x,0).$$

For every positive integer $N$ one can decompose

$$\frac{\sum_{j=0}^{n} b_j a_{n-j}}{\sum_{k=0}^{n} b_k} - \alpha$$

$$= \frac{\sum_{j=0}^{n-N} b_j(a_{n-j}

This decomposition is valid for all $n > N$ and for every real $\alpha$, but we shall of course set $\alpha = F(x,0)$. Since $b_n$ is a bounded sequence such that the series $\sum b_n$ diverges, it is clear that the last two terms tend to zero as $n \to \infty$, for each fixed $N$. We can now choose $N = N(\epsilon)$ so that $|a_n - \alpha| < \epsilon$ when $n > N$. With this choice of $N$ one obtains

$$\lim_{n \to \infty} \left| \frac{\sum_{j=0}^{n} b_j a_{n-j}}{\sum_{k=0}^{n} b_k} - F(x,0) \right| \leq \epsilon$$

and as $\epsilon$ is an arbitrary positive number, the proof of P5 is complete.

E3 Let us now apply P5 to Bernoulli random walk. When $p > q$, P5 tells us that $F(0,x) = 1$ for every $x > 0$, since

$$F(0,x) = \frac{G(0,x)}{G(0,0)}$$

and $G(0,x) = (p - q)^{-1}$, for every $x \geq 0$, according to E2. Inasmuch as $F(0,x)$ represents the probability that the first visit to $x$ occurs at some finite time (i.e., that $x$ is visited at all), it was of course to be expected that $F(0,x) = 1$ for all positive $x$ when $p > q$. In this case one would also expect that $F(0,x) < 1$ when $x < 1$, and E2 together with P5 actually shows that $F(0,x)$ goes to zero geometrically as $x \to -\infty$. One obtains

$$F(0,x) = \left(\frac{p}{q}\right)^x \text{ when } x < 0.$$

Finally, consider the simple random walk, with $p = q = 1/2$. According to P5,

$$\lim_{n \to \infty} \frac{G_n(0,x)}{G_n(0,0

The only trouble is that we used certain intuitively plausible facts about properties of the probability measures induced by the transition function $P(x,y)$, before having described the method by which probability measures are to be assigned. In particular we argued that if $p(x_0)$ is the probability of visiting $x_0$ before the first return to 0, then the probability of visiting $x_0$ before 0, and then 0, is $p(x_0)F(x_0,0)$. This relation of independence is indeed a property of any reasonable assignment of probability measure under which $P_n(x,y)$ retains the obvious interpretation as $n$-step transition probabilities, but the proof must wait until section 3.

It is, however, of some interest to see if one can show analytically that $F(0,x) \equiv 1$ when $p = q$, and we offer the following three alternative methods of proof.

(a) From Stirling's formula

$$n! \sim \sqrt{2\pi n} e^{-n} n^n$$

(here and in the sequel $a_n \sim b_n$ means that the ratio $a_n/b_n \to 1$ as $n \to \infty$), one obtains

$$P_{2n}(0,0) = (-1)^n \binom{-1/2}{n} \sim (\pi n)^{-1/2}.$$

It is equally easy to show that

$$P_{2n}(0,x) \sim (\pi n)^{-1/2} \quad \text{when } x \text{ is an even integer},$$

$$P_{2n+1}(0,x) \sim (\pi n)^{-1/2} \quad \text{when } x \text{ is odd}.$$

Finally, summing on $n$ yields, for every $x$,

$$G_n(0,x) \sim \frac{1}{2} \sum_{k=1}^{n} \left(\frac{\pi k}{2}\right)^{-1/2} \sim \frac{1}{2} \left(\frac{n}{2\pi}\right)^{1/2},$$

so that

$$F(0,x) = \lim_{n \to \infty} \frac{G_n
