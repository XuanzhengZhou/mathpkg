---
role: proof
locale: en
of_concept: thm-aperiodic-dimensional-random-walk-is-transient
source_book: gtm034
source_chapter: "2"
source_section: "005"
---

Proof: As shown by the argument involving Fatou's lemma we need only prove that $G < \infty$ when $\text{Re}[1 - \phi(\theta)]^{-1}$ is integrable. Let us therefore assume that $G = \infty$, and work toward a contradiction. The random walk is then recurrent and aperiodic, and in this case it is known that the series

$$a(x) = \sum_{n=0}^{\infty} [P_n(0,0) - P_n(x,0)]$$

converges for all $x \in R$. (That is shown in T28.1 of Chapter VII.) It is further known that

(2) $a(x) + a(-x) = 2(2\pi)^{-d} \int_C \frac{1 - \cos x \cdot \theta}{1 - \phi(\theta)} d\theta$

$$= 2(2\pi)^{-d} \int_C [1 - \cos x \cdot \theta] \text{Re} \frac{1}{1 - \phi(\theta)} d\theta, \quad x \in R.$$

(That follows from P28.4 when $d = 1$; when $d = 2$ it is proved earlier, in P12.1.) Finally it will be shown, in P29.4, that the function $a(x) + a(-x)$ has an interesting probability interpretation: it represents the expected number of visits of the random walk $x_n$, $n \geq 0$, starting at $x_0 = x$, to the point $x$, before the first visit to the origin. Thus, in the notation of P29.4,

$$a(x) + a(-x) = g_{(0)}(x,x) = \sum_{k=0}^{\infty} P_x[x_k = x; T > k],$$

where $T = \min[k \mid k \geq 0; x

To achieve this select a positive integer $N$, and observe that $T < \infty$ with probability one for recurrent random walk. It follows that

$$a(x) + a(-x) \geq \sum_{k=0}^{N} P_z[x_k = x; T > k] = \sum_{k=0}^{N} P_z[x_k = x]$$

$$- \sum_{k=0}^{N} P_z[x_k = x; T \leq k] = \sum_{k=0}^{N} P_k(0,0) - \sum_{k=0}^{N} P_z[x_k = x; T \leq k].$$

For each fixed integer $k$

$$P_z[x_k = x; T \leq k] \leq P_z[T \leq k]$$

$$= \sum_{j=0}^{k} P_z[T = j] \leq \sum_{j=0}^{k} P_z[x_j = 0] = \sum_{j=0}^{k} P_j(x,0),$$

which tends to zero as $|x| \to \infty$. Therefore

$$\lim_{|x| \to \infty} [a(x) + a(-x)] \geq \sum_{k=0}^{N} P_k(0,0)$$

for arbitrary $N$. As the random walk was assumed recurrent it follows that (5) holds. The contradiction between (4) and (5) shows that aperiodic random walk cannot be recurrent when $\text{Re}[1 - \phi(\theta)]^{-1}$ is integrable, and hence the proof of T2 is complete.

E1 To prove part (a) of T1 by use of P1, observe that

(1) $$\int_{-\pi}^{\pi} \text{Re} \left[ \frac{1}{1 - t\phi(\theta)} \right] d\theta \geq \int_{-\alpha}^{\alpha} \text{Re} \left[ \frac{1}{1 - t\phi(\theta)} \right] d\theta$$

when $0 \leq t < 1$ and $0 < \alpha < \pi$, since the real part of $[1 - t\phi(\theta)]^{-1}$ is non-negative. Now

(2

It follows from (1) that

$$\lim_{t \to 1} \int_{-\pi}^{\pi} \text{Re} \left[ \frac{1}{1 - t \phi(\theta)} \right] d\theta \geq \frac{1}{3} \int_{-\infty}^{\infty} \frac{dx}{1 + \epsilon^2 x^2} = \frac{\pi}{3\epsilon}.$$

By letting $\epsilon$ tend to zero we see that the limit in (5) is infinite, and by P1 the random walk in question is recurrent.

The Fourier analytical proof of part (b) of T1 is so similar to that of part (a) that we go on to a different problem. We shall prove (without using the strong law of large numbers that was used in T3.1) that one-dimensional random walk is transient if $m < \infty, \mu \neq 0$. Curiously it seems to be impossible to give a proof using only P1 and P6.4. But if in addition we use P6.6, to the effect that the function $\theta^{-2} \text{Re} [1 - \phi(\theta)]$ is Lebesgue integrable on the interval $[-\pi, \pi]$, then the proof is easy. As we may as well assume the random walk to be aperiodic, we have to show that

$$\lim_{t \to 1} \int_{-\alpha}^{\alpha} \text{Re} \left[ \frac{1}{1 - t \phi(\theta)} \right] d\theta < \infty$$

for some $\alpha > 0$. We use the decomposition

$$\text{Re} \left[ \frac{1}{1 - t \phi} \right] = \frac{\text{Re} (1 - \phi) + (1 - t) \text{Re} \phi}{[\text{Re} (1 - t \phi)]^2 + t^2 (\text{Im} \phi)^2}$$

$$\leq \frac{\text{Re} (1 - \phi)}{t^2 (\text{Im} \phi)^2} + \frac{1 - t}{|1 - t|^2}.$$

Choosing $\alpha$ sufficiently small

It is known from T1 that such a random walk is recurrent when $\alpha > 1$ (for then the first moment $m$ will be finite). We shall now prove that the random walk in question is in fact recurrent when $\alpha \geq 1$ and transient when $\alpha < 1$. This will be accomplished by investigating the asymptotic behavior of $1 - \phi(\theta)$ as $\theta \rightarrow 0$. When $\alpha > 2$, the second moment exists and we know from P6.4 that $1 - \phi(\theta) \sim c_2 \theta^2$ for some positive $c_2$ as $\theta \rightarrow 0$. Thus we may confine the discussion to the case when $0 < \alpha \leq 2$. We shall prove that

(1) $$\lim_{\theta \rightarrow 0} \frac{1 - \phi(\theta)}{|\theta|^\alpha} = c_1 \int_{-\infty}^{\infty} \frac{1 - \cos x}{|x|^{\alpha+1}} dx < \infty$$

when $0 < \alpha < 2$, and once this is done it is trivial to conclude from P1 that the random walk is transient if and only if $0 < \alpha < 1$. To prove (1) we write

$$1 - \phi(\theta) = \sum_{n=-\infty}^{\infty} [1 - \cos n\theta] P(0,n),$$

(2) $$\frac{1 - \phi(\theta)}{|\theta|^\alpha} = \sum_{n=-\infty}^{\infty} |n|^{1+\alpha} P(0,n) \left| \frac{1}{n\theta} \right|^{\alpha+1} |\theta| [1 - \cos n\theta].$$

Letting

$$f(x) = |x|^{-(1+\alpha)} (1 - \cos x), \quad -\infty < x < \infty,$$

observe that (2) becomes

(3) $$\frac{1 - \phi(\theta)}{|\theta|^\alpha} = c_1 \sum_{n=-\infty}^{\infty} |\theta| f(n\theta) + \sum_{n=-\infty}^{\infty} f(n\theta

E3 Consider simple random walk $x_n$ in the plane, starting at $x_0 = 0$. We write $x_n$ in complex form (i.e., for each $n \geq 0$, $x_n = a_n + ib_n$, so that the random variable $a_n$ is the real part of $x_n$, and $b_n$ the imaginary part). Let us now define the stopping time

(1) $T = \min [k \mid 1 \leq k \leq \infty; a_k = b_k]$.

Thus $T$ is the first time the simple random walk in the plane visits the diagonal $\text{Re}(x) = \text{Im}(x)$. According to T1 the simple random walk is recurrent and by P3.3 this means that $T < \infty$ with probability one.

We shall be interested in the hitting place $x_T$ rather than in the hitting time $T$ of the diagonal and define

(2) $Q(0,n) = P_0[x_T = n(1 + i)], \quad n = 0, \pm 1, \pm 2, \ldots$.

The foregoing remarks concerning recurrence show that

$$\sum_{n=-\infty}^{\infty} Q(0,n) = 1,$$

or, expressing it differently, $Q(m,n) = Q(0,n - m), m,n = 0, \pm 1, \ldots$, is the transition function of a one-dimensional random walk. In fact, we can even deduce from T1 that $Q(m,n)$ is the transition function of a recurrent one-dimensional random walk (which is just the original simple random walk in the plane, observed only at those times when it visits the diagonal $\text{Re}(x) = \text{Im}(x)$).

It is of interest to determine $Q(m,n)$ explicitly, and we do so, showing that its characteristic function $\psi(\theta)$ is given by

(3) $\psi(\theta) = \sum_{n=-\infty}^{\infty} Q(0,n)e^{i n \theta} = 1 - \sin \left| \frac{\theta}{2} \right|, \quad -\pi \leq \theta \leq \pi$.

Using (3) a simple calculation

The trick we mentioned consists in observing that the sequence of random variables $u_n$ is independent of the sequence $v_n$. One simply checks that for every pair of positive integers $m$ and $n$

(7) $P_0[u_m - u_{m-1} = r; v_n - v_{n-1} = s]$
$= P_0[u_m - u_{m-1} = r]P_0[v_n - v_{n-1} = s]$.

Moreover, in so doing, one makes the pleasant discovery that the probability in (7) is zero unless $|r| = 1$ and $|s| = 1$, in which case it is one fourth. Thus we have observed that $u_n$ and $v_n$ are a pair of independent simple one-dimensional random walks.

The rest is easy. Since $T$ depends only on the sequence $v_n$, but not on the random walk $u_n$, we may apply P3.1 to (6), to obtain

$$\psi(\theta) = \sum_{k=1}^{\infty} E_0\left[e^{i\theta u_k}\right] P_0[T = k],$$

and the observation that $u_n$ is a simple random walk gives

(8) $$\psi(\theta) = \sum_{k=1}^{\infty} \left(\cos \frac{\theta}{2}\right)^k P_0[T = k] = E_0\left[\left(\cos \frac{\theta}{2}\right)^T\right].$$

It remains only to evaluate $E_0(s^T)$ for arbitrary $s$ in $[-1,1]$. $T$ is the first time of return to zero for the simple random walk $v_n$, and as shown in equation (5) of E1.2,

(9) $$E_0(s^T) = \sum_{n=1}^{\infty} s^n F_n(0,0) = 1 - \sqrt{1-s^2}, \quad |s| \leq 1.$$

We conclude from (8) and (9) that

(10) $$\psi(\theta) = 1 - \sqrt{1 - \left(\cos \frac{\theta}{2}\right)^2} = 1 - \sin \left

Whereas E1, E2, and E3 were designed to establish or to disprove recurrence for specific random walks, the last example is intended to illuminate general principles. We shall take a brief look at abstract harmonic analysis on Abelian groups $G$ and exhibit a class of functions $\chi_{\lambda}(g), g \in G$, called the characters of $G$, which exhibit exactly the same behavior as the exponential functions $e^{i\lambda x}$ on $R$. Actually we shall discuss only one specific group $G$, but one whose structure differs considerably from that of the group of lattice points $R$.

E4 We take for $G$ the following countably infinite Abelian group. The elements of $G$ are infinite sequences

$$g = (\epsilon_1, \epsilon_2, \epsilon_3, \ldots)$$

where each $\epsilon_k = \epsilon_k(g)$ is either 0 or 1, and only a finite number of 1's occur in each $g$. Addition is defined modulo 2; when $g \in G$ and $h \in G$, $g + h$ is defined by

$$\epsilon_k(g + h) = \begin{cases} 0 & \text{if } \epsilon_k(g) = \epsilon_k(h), \\ 1 & \text{otherwise.} \end{cases}$$

Each $g$ in $G$ can be expressed in a unique way as a finite sum of generators $g_k \in G$, $g_k$ being defined by

$$\epsilon_n(g_k) = \delta(n,k), \quad k \geq 1, \quad n \geq 1.$$

The identity element of $G$ will be

$$e = (0,0, \ldots).$$

A complex valued function $\chi(g)$ on $G$ will be called a character of $G$, if

(1) $$|\chi(g)| = 1, \quad \chi(g + h) = \chi(g)\chi(h) \text{ for } g, h \in G.$$

It follows from (1) that $\chi(e) = 1$ (using none of the special properties of $G$) and that $\chi(g)$ is either +1 or -1 for each $g$ in $G

for every $g = g_{i_1} + g_{i_2} + \cdots + g_{i_n} \in G$. Clearly (3) implies that $\chi_\lambda(g)$ is a character.

Classical harmonic analysis is based on the orthogonality of the exponential functions in P6.1. The analogue of this proposition in the present setting is the orthogonality relation

$$\frac{1}{2} \int_{-1}^{1} \chi_\lambda(g) \chi_\lambda(h) d\lambda = \begin{cases} 1 & \text{if } g = h \\ 0 & \text{if } g \neq h, \end{cases}$$

where $d\lambda$ is ordinary Lebesgue measure on $I$. Although the proof of (4), based on (1), (2), and (3) is not at all difficult, the observation that such orthogonality relations hold in a very general setting is profound enough to have played a major role in the modern development of probability and parts of analysis. Continuing to imitate the development in section 6, our next step is the definition of a "transition function"

$$P(g,h) = P(e,h - g),$$

satisfying

$$P(e,g) \geq 0, \quad \sum_{g \in G} P(e,g) = 1$$

and of its "characteristic function"

$$\phi(\lambda) = \sum_{g \in G} P(e,g) \chi_\lambda(g), \quad \lambda \in I.$$

Now we can generalize parts (a) and (b) of P6.3. If we define the iterates of $P(g,h)$ by

$$P_0(g,h) = \delta(g,h), \quad P_1(g,h) = P(g,h),$$

$$P_{n+1}(g,h) = \sum_{f \in G} P(g,f) P_n(f,h), \quad n \geq 0,$$

then P6.3(a) becomes

$$\phi^n(\lambda) = \sum_{g \in G} P_n(e,g) \chi_\lambda(g), \quad \lambda \in I, \quad n \geq 0,$$

and part (b

any difficulty. Given a transition function, we may therefore call the corresponding random walk recurrent, if

(9) $$\sum_{n=0}^{\infty} P_n(e,e) = \infty,$$

and ask for criteria for (9) to hold, just as was done in this section, in terms of the characteristic function $\phi(\lambda)$. This is easy, as equation (8) implies that (9) holds if and only if

(10) $$\sum_{n=0}^{\infty} \int_{-1}^{1} \phi^n(\lambda) d\lambda = \infty.$$

Let us "test our theory" in terms of a very down-to-earth example. We consider an infinite sequence of light bulbs, and an infinite sequence of numbers $p_k$ such that

$$p_k \geq 0, \quad \sum_{k=1}^{\infty} p_k = 1.$$

At time 0 all the light bulbs are "off." At each unit time $(t = 1, 2, 3, \ldots)$ thereafter one of the light bulbs is selected (the $k^{\text{th}}$ one with probability $p_k$), and its switch is turned. Thus it goes on if it was off, and off if it was on. What is the probability that all the light bulbs are off at time $t = n$? A moment of thought will show that this is a problem concerning a random walk on the particular group $G$ under discussion, and that the desired probability is $P_n(e,e)$, provided we define the transition function $P(g,h)$ by

(11) $$P(e,g) = p_k \text{ if } g = g_k, \quad 0 \text{ otherwise.}$$

(More specifically, the probability that exactly bulbs number 3, 5, 7, and 11 are burning at time $n$, and no others, is $P_n(e,g)$ where $g = g_3 + g_5 + g_7 + g_{11}$, and so forth.)

In this "applied" setting the recurrence question of equations (9) and (10) has some intuitive interest. Equation (10) is equivalent to the statement that with probability one the system of light bulbs will infinitely often be in the state

Just as in the proof of P1 we can write

$$\sum_{0}^{\infty} P_n(e, e) = \lim_{t \to 1} \sum_{0}^{\infty} t^n P_n(e, e) = \lim_{t \to 1} \frac{1}{2} \sum_{0}^{\infty} t^n \int_{-1}^{1} \phi^n(\lambda) d\lambda$$

$$= \lim_{t \to 1} \frac{1}{2} \int_{-1}^{1} \frac{d\lambda}{1 - t\phi(\lambda)}$$

Here it is possible to interchange limits and integration, since

$$\int_{-1}^{1} \frac{d\lambda}{1 - t\phi(\lambda)} = \int_{[\lambda | \phi(\lambda) \leq 0]} \frac{d\lambda}{1 - t\phi(\lambda)} + \int_{[\lambda | \phi(\lambda) > 0]} \frac{d\lambda}{1 - t\phi(\lambda)}$$

The first of these tends to the integral of $[1 - \phi(\lambda)]^{-1}$ by dominated convergence, and to the second integral one can apply the monotone convergence theorem. Thus (13) and (14) give

$$\sum_{0}^{\infty} P_n(e, e) = \frac{1}{2} \int_{-1}^{1} \frac{d\lambda}{1 - \phi(\lambda)} \leq \infty.$$

Let us now partition the interval $[-1, 1]$ into the sets

$$A_k = [\lambda | \lambda_1 = \lambda_2 = \cdots = \lambda_{k-1} = +1, \lambda_k = -1], k \geq 1,$$

noting that $\lambda \in A_k$ implies that

$$1 - 2f_k \leq \phi(\lambda) = \sum p_k \lambda_k \leq 1 - 2p_k,$$

where $f_k = p_k + p_{k+1} + \cdots$. Hence (15) yields

$$\sum \frac{\mu(A_k)}{2f_k} \leq \int_{-1}^{1} \frac{d\

Remark: By direct probabilistic methods Darling and Erdős [S5] have shown that condition (16) is in fact necessary and sufficient for recurrence. For a generalization to random walk on more general Abelian groups see [S10].

Remark: The most interesting general result, so far, concerning random walk on groups is a generalization of T1 due to Dudley [26]. He considers countable Abelian additive groups $G$, and asks what groups admit an aperiodic recurrent random walk. In other words, on what groups $G$ can one define a transition function $P(x,y), x,y \in G$, such that $P(x,y) = P(e,y-x)$, and

(a) no proper subgroup of $G$ contains $[x \mid P(e,x) > 0]$,

(b) $\sum_{n=0}^{\infty} P_n(e,e) = \infty$,

where $e$ is the identity element and $P_n(x,y)$ is defined as in E4? The answer is that $G$ admits an aperiodic recurrent random walk if and only if it contains no subgroup which is isomorphic to $R_3$ (the triple direct product of the group of integers). Note that, consequently, it is possible to define an aperiodic recurrent random walk on the additive group of rational numbers!

9. THE RENEWAL THEOREM

In the study of random walk, as in any other area of mathematics, there are some quite indispensable propositions, intimately related to the subject but not actual goals of the theory. Two such propositions will be proved here, the Riemann Lebesgue Lemma (P1) and the renewal theorem (P3). The former belongs in this chapter, being a basic result in Fourier analysis. The latter does not; it properly belongs in Chapter VI where its most general form appears as T24.2. But we shall wish to use P3 long before that and since there is a simple proof of P3 due to Feller ([31], Vol. 2) which is based on P1, we chose to put the renewal theorem in this section.

The Riemann Lebesgue Lemma concerns the Fourier coefficients of functions $f(\theta)$, integrable on the cube

$$

All integrals will be over $C$, as in D6.3, and $d\theta$ is Lebesgue measure (volume). The space $R$ of lattice points is of the same dimension $d$ as $E$, and for a function $g(x)$ on $R$

$$\lim_{|x| \to \infty} g(x) = c$$

has the obvious meaning, i.e., $g$ is arbitrarily close to $c$ outside sufficiently large spheres in $R$.
