---
role: proof
locale: en
of_concept: prop-if-is-a-monotone-nonincreasing-non
source_book: gtm034
source_chapter: "4"
source_section: "010"
---

Proof: In view of P1 and part (a) of T1,

$$\sqrt{k(n-k)} \mathbf{P}[N_n = k] = \sqrt{k} \mathbf{P}[N_k = k] \sqrt{n-k} \mathbf{P}[N_{n-k} = 0]$$

$$= \left[ \frac{1}{\sqrt{c\pi}} + o_1(k) \right] \left[ \sqrt{\frac{c}{\pi}} + o_2(n-k) \right]$$

$$= \frac{1}{\pi} + o(k,n),$$

where $o(k,n)$ has the required property, given any $\epsilon > o$ there is some $N$ such that $o(k,n) < \epsilon$ when $k > N$ and $n-k > N$. Strictly speaking this was the proof for the symmetric case. In the other case it suffices to replace $\sqrt{c}$ by $e^{-\alpha}$.

Part (b) is the “classical” arc-sine law, which is valid under far weaker conditions than those for (a). (See problems 8 and 9 for a simple necessary and sufficient condition.) To derive (b) from (a) we may write

$$\mathbf{P}[N_n \leq nx] = \mathbf{P}[N_n \leq [nx]] = \frac{1}{n} \sum_{k=0}^{[nz]} \left[ \frac{k}{n} \left(1 - \frac{k}{n}\right) \right]^{-1/2} \left( \frac{1}{\pi} + o(k,n) \right).$$

Interpreting the limit as the approximation to a Riemann integral,

$$\lim_{n \to \infty} \frac{1}{n\pi} \sum_{k=0}^{[nz]} \left

From previous discussions of left-continuous random walk in E17.2, E18.2, and E19.1 we need only the following facts ((1), (2), and (3) below).

(1) $1 - r(t) = e^{-\sum_{k=1}^{\infty} \frac{t_k}{k} P[B_k < 0]}, \quad 0 \leq t < 1,$

where $r(t)$ is the unique positive solution (less than one) of the equation

(2) $r(t) = tP[r(t)]$.

Here $P(z)$ is defined as

$$P(z) = \sum_{n=0}^{\infty} P(0,n-1)z^n,$$

where $P(x,y)$ is the transition function of the random walk. Among the obvious properties of $P(z)$ are

(3) $P(1) = P'(1) = 1, \quad P''(1) = \infty,$

where $P'(1)$ and $P''(1)$ denote the limits of $P'(z)$ and $P''(z)$ as $z$ approaches one through the reals less than one.

Our analysis will make use of a theorem of Hardy and Littlewood, the forerunner of Karamata's theorem (a special case of which was P2). It asserts that when $a_n \geq 0$

(4) $\lim_{t \to 1} (1-t) \sum_{n=0}^{\infty} a_n t^n = 1$ implies $\lim_{n \to \infty} \frac{1}{n} (a_1 + \cdots + a_n) = 1.$

Using (1), (2), and (3) we shall study the behavior of

(5) $A(t) = (1-t) \sum_{0}^{\infty} t^n P[S_n < 0]$

as $t \neq 1$. We shall show that for any constant $a$ in the interval $\frac{1}{2} \leq a \leq 1$ it is possible to find a left-continuous random walk with mean zero and $\sigma^2 = \infty$ such that

(6) $\lim_{t \to 1} A(t

It is also clear, the random variables $N_n/n$ being bounded, that the limit in (7) must exist if the limit of $P[N_n \leq nx]$ is to exist as $n \to \infty$ for every $x$. Thus if we carry out our program it will be clear that there are random walks for which $N_n$ has no nondegenerate limiting distribution. The truth is actually still more spectacular: in problems 8 and 9 at the end of the chapter it will be shown that if there is some $F(x)$, defined on $0 < x < 1$, such that

$$\lim_{n \to \infty} P[N_n \leq nx] = F(x), \quad 0 < x < 1,$$

then (7) must hold with some $a$ between zero and one. If $a = 1$, then $F(x) \equiv 1$; if $a = 0$, then $F(x) \equiv 0$; and if $0 < a < 1$, then

$$F(x) = \lim_{n \to \infty} P[N_n \leq nx] = \frac{\sin \pi a}{\pi} \int_0^x t^{-a}(1-t)^{a-1} dt.$$

The result of (8) with $a = \frac{1}{2}$ was obtained in T2. If we show, as planned, that one can get (8) with $a > \frac{1}{2}$ for suitable left-continuous random walks, then of course one can also get (8) with $a < \frac{1}{2}$. One simply considers the reversed, right-continuous random walk.

It remains, then, to investigate the limit in (6). Differentiating (1) for $0 \leq t < 1$

$$\frac{r'(t)}{1-r(t)} = \sum_1^\infty t^{k-1} P[S_k < 0].$$

By equation (2)

$$r'(t) = P[r(t)] + tr'(t)P'[r(t)].$$

This fact, together with (2) will be used to express $A(t)$ in equation (5) as a function of $r(t) = r

only on the behavior of $P(r)$ and $P'(r)$ near $r = 1$ and that is determined by the behavior of the coefficients $P(0,n)$ for large $n$. Suppose we consider a random walk such that for some integer $N > 0$, and some $c > 0$

(13) $P(0,n) = \frac{c}{n^{\alpha+2}}$ for $n > N$, $0 < \alpha \leq 1$.

The constant $c$ is assumed to be adjusted so that (3) holds, and keeping this in mind, an easy calculation shows that (12) holds, and that the limit is

(14) $\frac{1}{2} \leq a = \frac{1}{\alpha+1} < 1$.

To get (12) with the limit $a = 1$ one can of course take $\alpha = 0$, and get the right result, since the random walk with $\alpha = 0$ will be transient, having infinite first moment, so that $N_n/n \rightarrow +1$ with probability one. If one wants an example where $m < \infty$, so that the random walk remains recurrent, one can take

$$P(0,n) = \frac{c}{(n \ln n)^2}$$

for large enough $n$, but this is now a little tedious to check.

Finally, to produce an example where the limit in (12) fails to exist, there is a procedure familiar to all those whose work requires delicate asymptotic estimates. One simply decomposes the positive integers into blocks or intervals,

$$I_1 = [1,n_1), \quad I_2 = [n_1,n_2), \dots, \quad I_k = [n_{k-1},n_k), \dots.$$

Then one takes two numbers $0 < \alpha_1 < \alpha_2 < 1$, and chooses

$$P(0,n) = \frac{c}{n^{\alpha_1+2}}$$ when $n \in I_1 \bigcup I_3 \bigcup I_5 \bigcup \dots,$

$$= \frac{c}{n^{\alpha_2+2}}$$ when $n \in I_2 \bigcup I

results, called occupation time theorems. Consider arbitrary non-degenerate random walk, and let

(1) $B \subset \bar{R}, |B| < \infty, \quad \varphi(x) = 1$ for $x \in B, 0$ otherwise,

$$N_n = \sum_{k=1}^{n} \varphi(S_k).$$

$N_n$ is then the occupation time of $B$. A typical question concerns the possibility of finding a positive sequence $a_n$ such that

(2) $$\lim_{n \to \infty} P[N_n \leq a_n x] = F(x)$$

exists at all continuity points of $F(x)$, and such that $F(x)$ is a non-degenerate distribution (has more than one point of increase). Typical answers are $^{13}$: If $d = 1, \mu = 0, 0 < \sigma^2 < \infty$, then there is a limit distribution $F(x)$ if one takes $a_n = \sqrt{n}$ (a truncated normal distribution). But if $d = 1, m < \infty, \mu = 0, \sigma^2 = \infty$, the situation is comparable to that concerning the arc-sine law. There is a one-parameter family of distributions (the so-called Mittag-Leffler distributions) which do arise as limits in (2). But there are also random walks which cannot be normalized by any sequence $a_n$ to give a nondegenerate limit distribution.

In two dimensions the situation is similar. When the mean is zero and the second moments exist, one can show that

(3) $$\lim_{n \to \infty} P[N_n > x \ln n] = e^{-cx}, \quad 0 \leq x,$$

where the constant $c$ is a function of the second moments and of the cardinality $|B|$. It is of course inversely proportional to $|B|$.

**Problems**

1. For aperiodic symmetric one-dimensional random walk use P7.6 to prove that $\ln [1 - \phi(\theta)]$ is Lebesgue integrable on the interval $-\pi \leq \theta \leq \pi$.

2. Continuation. Conclude from problem (1) that for $0 \leq r \
