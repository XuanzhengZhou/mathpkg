---
role: proof
locale: en
of_concept: prop-a-0-x
source_book: gtm034
source_chapter: "5"
source_section: "012"
---

Proof: The argument is based on the identities

$$R_N(x,k) = \sum_{y=0}^{N} g_N(x,y)P(y,N+k),$$

$$L_N(x,k) = \sum_{y=0}^{N} g_N(x,y)P(y,-k),$$

valid for $0 \leq x \leq N,$ $k \geq 0$. They are obvious from

$$g_N(x,y)P(y,N+k) = \sum_{j

where $T_N$ is the first exit time from the interval $[0,N]$ defined in D21.2. The identity for $L_N$ is proved in the same way.

The left-hand side in (a) can then be written

$$\sum_{y=0}^{N} g_N(x,y) \left[ 1 - \sum_{s=0}^{N} P(y,s) \right].$$

Keeping in mind that

$$\sum_{y=0}^{N} g_N(x,y) P(y,s) = g_N(x,s) - \delta(x,s)$$

when $x$ and $s$ are both in $[0,N]$, one gets

$$\sum_{k=1}^{N} \left[ R_N(x,k) + L_N(x,k) \right] = \sum_{y=0}^{N} g_N(x,y) - \sum_{s=0}^{N} g_N(x,s) + \sum_{s=0}^{N} \delta(x,s) = 1.$$

The proof of (b) is similar, but it depends in an essential way on the hypothesis that $m < \infty$, $\mu = 0$. The left-hand side in (b) is transformed into

$$\sum_{y=0}^{N} g_N(x,y) \left[ \sum_{k=1}^{\infty} (N+k) P(y,N+k) - \sum_{k=1}^{\infty} kP(y,-k) \right]$$

$$= \sum_{y=0}^{N} g_N(x,y) \left[ \sum_{j=-\infty}^{\infty} jP(y,j) - \sum_{j=0}^{\infty} jP(y,j) \right]$$

$$= \sum_{y=0}^{N} g_N(x,y) \left[ y - \sum_{j=0}^{\infty} jP(y,j) \right]$$

$$= \sum_{y=0}^{N} yg_N(x,y) - \sum_{j=0}^{\infty} jg_N(x,j) + \sum_{j=0}^{\infty} j \delta(x,j) = x.$$

That completes the proof of this intuitively obvious proposition. Part (a) asserts that the random walk leaves $[0,N]$ either on the

The proof is completed by applying P6(b) to the next to last term to get

$$R_N(x) = \frac{x}{N} + \frac{1}{N} \sum_{k=1}^{\infty} kL_N(x,k) - \frac{1}{N} \sum_{k=1}^{\infty} kR_N(x,k).$$

The main theorem of this section (T1 below) concerns the asymptotic behavior of $R_N(x)$ and $L_N(x)$ as $N \to \infty$. The proof will depend on P5 which was proved under the assumption that $\sigma^2 < \infty$. But that is deceptive—P5 can in fact be shown to be true under much more general conditions. However, essential use of the finiteness of the variance will be made in an estimate very much like the ones required to prove P1. In the proof of T1 we shall have occasion to define

(1) $$a(s) = \sum_{k=1}^{\infty} kP(0,s+k), \quad s \geq 0,$$

and we shall need the conclusion that

(2) $$\lim_{n \to \infty} \frac{1}{n} \sum_{s=0}^{n} (1+s)a(s) = 0.$$

This is easily done, for (1) yields

$$\sum_{s=0}^{\infty} a(s) = \sum_{k=0}^{\infty} \sum_{s=0}^{\infty} kP(0,s+k) = \sum_{j=1}^{\infty} (1+2+\cdots+j)P(0,j)$$

$$\leq \sum_{j=1}^{\infty} j^2P(0,j) \leq \sigma^2 < \infty,$$

and by Kronecker's lemma the convergence of the series $\sum a(s)$ implies that

$$\lim_{n \to \infty} \frac{1}{n} \sum_{s=1}^{n} sa(s) = 0,$$

which shows that (2) holds.
