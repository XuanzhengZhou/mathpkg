---
role: proof
locale: en
of_concept: thm-a-and-for-0
source_book: gtm034
source_chapter: "4"
source_section: "010"
---

Proof: Equations (b) and (c) follow immediately from earlier results. To get (b) observe that

$$P[N_j = 0] = P[T > j]$$

so that

$$\sum_{j=0}^{\infty} P[N_j = 0]t^j = \sum_{j=0}^{\infty} t^jP[T > j] = \frac{1 - E[t^T]}{1 - t},$$

and from P17.5(a) with $x = 1$

$$\

of functions $\mathcal{A}, \mathcal{A}_e, \mathcal{A}_i$. Note also that each of these three function spaces is closed under multiplication. For example if $\phi$ and $\psi$ are in $\mathcal{A}_i$, then for real $\theta$,

$$\phi(\theta) = \sum_{0}^{\infty} a_k e^{ik\theta}, \quad \sum_{0}^{\infty} |a_k| < \infty,$$

$$\psi(\theta) = \sum_{0}^{\infty} b_k e^{ik\theta}, \quad \sum_{0}^{\infty} |b_k| < \infty.$$

But then the product is

$$\phi(\theta)\psi(\theta) = \sum_{-\infty}^{\infty} c_k e^{ik\theta}$$

where $c_k = 0$ for $k \leq -1$,

$$c_n = \sum_{k=0}^{n} a_k b_{n-k}$$ for $n \geq 0, \quad \sum_{0}^{\infty} |c_n| < \infty,$

so that the product $\phi\psi$ is again in $\mathcal{A}_i$.

Following Baxter's treatment [2] of fluctuation theory, we introduce the "+" operator and the "−" operator." For arbitrary

$$\phi(\theta) = \sum_{-\infty}^{\infty} a_k e^{ik\theta}$$ in $\mathcal{A}$

we define

$$\phi^+(\theta) = \sum_{k=1}^{\infty} a_k e^{ik\theta},$$

$$\phi^-(\theta) = \sum_{k=-\infty}^{0} a_k e^{ik\theta}.$$

Thus $\phi^+$ is in $\mathcal{A}_i$ and $\phi^-$ in $\mathcal{A}_e$ whenever $\phi$ is in $\mathcal{A}$. In other words, the "+" and "−" operators are projections of $\mathcal{A}$ into the subspaces $\mathcal{A}_i$ and $\mathcal{A}_e$ of $\mathcal{A}$. We list the obvious algebraic properties of the "+" operator. It is linear, i.e., for arbitrary $\phi,\psi$ in $\mathcal{A}$,

$$(a\

and $\mathcal{A}^-$ are disjoint, so that an arbitrary $\phi$ in $\mathcal{A}$ can be decomposed uniquely into $\phi = \phi_1 + \phi_2$ with $\phi_1$ in $\mathcal{A}^+$ and $\phi_2$ in $\mathcal{A}^-$. Of course $\phi_1 = \phi^+$, $\phi_2 = \phi^-$.

Now we are ready to define certain useful Fourier series, and leave to the reader the slightly tedious but easy task of checking that they are all in $\mathcal{A}$. They depend on the parameters $s, t$ which will be real with $0 \leq s < 1, 0 \leq t < 1$. Let

$$\phi_n(s; \theta) = \sum_{k=0}^{n} s^k \mathbf{E}[e^{i\theta S_n}; \mathbf{N}_n = k], \quad n \geq 0,$$

$$\psi(s, t; \theta) = \sum_{n=0}^{\infty} t^n \phi_n(s; \theta),$$

and

$$\phi(\theta) = \sum_{n=-\infty}^{\infty} P(0, n) e^{i n \theta},$$

as usual.

We require the important identity

(1) $$s(\phi \phi_n)^+ + (\phi \phi_n)^- = \phi_{n+1}, \quad n \geq 0.$$

The variables $s, t$, and $\theta$ have been suppressed, but (1) is understood to be an identity for each $\theta$ (real), $0 \leq s < 1, 0 \leq t < 1$. To prove it we write

$$\phi \phi_n = \sum_{k=0}^{n} s^k \mathbf{E}[e^{i\theta S_{n+1}}; \mathbf{N}_n = k] = \sum_{k=0}^{n} s^k \mathbf{E}[e^{i\theta S_{n+1}}; \mathbf{N}_{n+1}$$

$$= k + 1; \mathbf{S}_{n+1} > 0] + \sum_{k=0}^{n} s

and upon adding the last two identities one has (1). Multiplying (1) by $t^{n+1}$ and summing over $n \geq 0$,

$$1 + st(\phi \psi)^+ + t(\phi \psi)^- = \psi,$$

or equivalently

$$[\psi(1 - st\phi)]^+ = [\psi(1 - t\phi) - 1]^- = 0.$$

This says that $\psi(1 - st\phi) \in \mathcal{A}_e$, $\psi(1 - t\phi) \in \mathcal{A}_i$, and, by P17.2, these functions can be extended uniquely, $\psi(1 - st\phi)$ to an outer function $g_e$, and $\psi(1 - t\phi)$ to an inner function $g_i$. Thus

$$\psi(1 - st\phi) = g_e(z), \psi(1 - t\phi) = g_i(z), \quad \text{for } |z| = 1.$$

Using the factorization

$$1 - t\phi = c(t)f_i(t;z)f_e(t;z), \quad |z| = 1$$

of P17.4,

$$g_e(z) = g_i(z) \frac{1 - st\phi}{1 - t\phi} = g_i(z) \frac{c(st)}{c(t)} \frac{f_i(st;z)f_e(st;z)}{f_i(t;z)f_e(t;z)},$$

and

$$\frac{c(st)}{c(t)} \frac{f_i(st;z)}{f_i(t;z)} g_i(z) = g_e(z) \frac{f_e(t;z)}{f_e(st;z)} = \text{constant},$$

since both sides together determine a bounded analytic function. The constant (which may depend on $s$ and $t$) is determined by checking that

$$g_i(0) = f_i(st;0) = f_i(t;0) = 1.$$

This yields

$$g_i(z) = \frac{f_i(t;z)}{f_i(st;z)}$$

and from $g_i = \psi

To complete the proof of T1 one has to show that (a) holds. Now equations (b) and (c), which have already been proved, may be written

(4) $\sum_{j=0}^{\infty} \mathbf{P}[\mathbf{N}_j = 0]t^j = [c(t)f_e(t;1)]^{-1},$

(5) $\sum_{j=0}^{\infty} \mathbf{P}[\mathbf{N}_j = j](st)^j = [f_i(st;1)]^{-1}$.

Combining (3), (4), and (5)

$$\sum_{n=0}^{\infty} t^n \mathbf{E}[s^{N_n}] = \sum_{j=0}^{\infty} \mathbf{P}[\mathbf{N}_j = 0]t^j \cdot \sum_{j=0}^{\infty} s^j \mathbf{P}[\mathbf{N}_j = j]t^j$$

$$= \sum_{n=0}^{\infty} t^n \sum_{k=0}^{n} \mathbf{P}[\mathbf{N}_{n-k} = 0]s^k \mathbf{P}[\mathbf{N}_k = k].$$

Identifying coefficients of $t^n s^k$ completes the proof of (a) and thus of T1.

E1 Symmetric random walk. As shown in Example E17.1, equation (7),

$$1 - \mathbf{E}[t^T] = \sqrt{\frac{1-t}{c(t)}},$$

so that

(1) $\sum_{j=0}^{\infty} \mathbf{P}[\mathbf{N}_j = 0]t^j = \frac{1 - \mathbf{E}[t^T]}{1-t} = \frac{(1-t)^{-1/2}}{\sqrt{c(t)}}.$$

It is equally easy to get

(2) $\sum_{j=0}^{\infty} \mathbf{P}[\mathbf{N}_j = j]t^j = \sqrt{c(t)} (1-t)^{-1/2},$

for example, by setting $z = 1$ in P17.4, which gives

$$(1-t) = c(t)

Therefore one can express $P[N_n = k]$ in terms of binomial coefficients. With $c_n$ defined by

$$\sum_{0}^{\infty} c_n t^n = \sqrt{\frac{1+t}{1-t}},$$

one finds

$$P[N_n = 0] = c_{n+1}, \quad P[N_n = n] = \frac{1}{2}c_n + \frac{1}{2}\delta(n,0), \quad n \geq 0.$$

There is no doubt what causes the slight but ugly asymmetry in the distribution of $N_n$. It is the slight but unpleasant difference between positive and non-negative partial sums. As indicated in problems 13 and 14, the corresponding result for random variables with a continuous symmetric distribution function is therefore much more elegant. However even in the case of simple random walk one can obtain formally elegant results by a slight alteration in the definition of $N_n = \theta(S_0) + \cdots + \theta(S_n)$. One takes $\theta(S_k) = 1$ if $S_k > 0$, $\theta(S_k) = 0$ if $S_k < 0$, but when $S_k = 0$, $\theta(S_k)$ is given the same value as $\theta(S_{k-1})$. In other words, a zero partial sum $S_k$ is counted as positive or negative according as $S_{k-1}$ is positive or negative. With this definition it turns out that

$$P[N_{2n} = 2k + 1] = 0, \quad P[N_{2n} = 2k] = 2^{-2n} \binom{2k}{k} \binom{2n-2k}{n-k}.$$

Now we turn to the asymptotic study of $N_n$ and show that even in the limit theorems the symmetric random walk continues to exhibit a certain amount of asymmetry due to our definition of $N_n$. We shall go to some trouble to exhibit the same kind of almost symmetric behavior also for random walk with mean zero and finite variance.
