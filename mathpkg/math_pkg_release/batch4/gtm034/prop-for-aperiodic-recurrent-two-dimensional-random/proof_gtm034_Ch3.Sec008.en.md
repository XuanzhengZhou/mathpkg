---
role: proof
locale: en
of_concept: prop-for-aperiodic-recurrent-two-dimensional-random
source_book: gtm034
source_chapter: "3"
source_section: "008"
---

Proof: We have

$$U_{2n+1} = 0, \quad U_{2n} = 4^{-2n} \binom{2n}{n}^2,$$

and Stirling's formula provides the estimate

$$U_{2n} \sim \frac{1}{n\pi}, \quad n \to \infty.$$

Hence

$$U_0 + U_2 + \cdots + U_{2n} \sim \frac{1}{\pi} \ln n, \quad n \to \infty.$$

Using the identity

$$\sum_{k=0}^{2n} U_k R_{2n-k} = 1, \quad n \geq 0,$$

as in the proof of P1, one obtains

$$R_{2n-2k} [U_0 + \cdots + U_{2k}] + U_{2k+2} + \cdots + U_{2n} \geq 1.$$

Here we let $k$ depend on $n$, choosing

$$k = k(n) = n - \left[ \frac{n}{\ln n} \right].$$

Then

$$U_0 + \cdots + U_{2k

as $n \to \infty$. Hence, for each $\epsilon > 0$,

$$\frac{\ln (n - k)}{\pi} R_{2n-2k} \geq 1 - \epsilon$$

for all large enough values of $n$, so that

$$\lim_{n \to \infty} \frac{\ln n}{\pi} R_n \geq 1.$$

On the other hand,

$$1 = \sum_{k=0}^{n} R_k U_{n-k} \geq R_n(U_0 + \cdots + U_n),$$

giving

$$\lim_{n \to \infty} \frac{\ln n}{\pi} R_n \leq 1.$$

That completes the proof of E1. The important thing for our purpose is that

$$\lim_{n \to \infty} \frac{R_n}{R_{2n}} = \lim_{n \to \infty} \frac{\ln 2n}{\ln n} = 1.$$

Hence equation (7) holds and, in view of the discussion following the proof of T1, various extensions of T1 are valid for simple random walk. The next two examples are devoted to two of these. E2 concerns equation (1) which in view of E1 may be written as

$$\lim_{n \to \infty} \frac{\ln n}{\pi} P_z[T_B > n] = g_B(x, \infty), \quad x \in R - B.$$

E2 For simple random walk we shall use the above result to obtain a novel version of the famous double point problem. Let $A_n$ denote the event that $x_0, x_1, \ldots, x_n$, the positions of the random walk at times 0, 1, \ldots, up to $n$, are all distinct. It is known that

$$2 < \gamma = \lim_{n \to \infty} \{P[A_n]\}^{1/n} < 3$$

exists. As pointed out in section 10, it requires no great art to calculate $\gamma$ quite accurately, but the difficulty of the problem is indicated by the fact that it is not even known whether

$$\lim_{n \to \infty} \frac{P[A_{n+1}]}{P[A

that the random walk at time $n$ finds itself at a new point, i.e., one which was not visited before. We shall show that

$$\lim_{n \to \infty} P[B_{n+1} \mid B_n] = 1/2.$$

Proof:

$$P[B_{n+1} \mid B_n] = \frac{P_0[B_nB_{n+1}]}{P_0[B_n]}.$$

By reversing the random walk it is seen that

$$P_0[B_n] = P_0[T > n] = R_n,$$

and similarly, that

$$P_0[B_nB_{n+1}] = \sum_{z \in R} P(0,x)P_z[T > n, T_z > n],$$

where

$$T = \min[k \mid 1 \leq k, x_k = 0], \quad T_z = \min[k \mid 1 \leq k, x_k = x].$$

Now it is quite clear, from the symmetry of the simple random walk, that $P_z[T > n, T_z > n]$ has the same value for each of the four points $x$ where $P(0,x) > 0$. But we prefer to spurn this opportunity to make an apparent simplification, in order to prove the result for an arbitrary random walk in the plane which is aperiodic, symmetric $(P(x,y) = P(y,x))$, has the property that $P(0,0) = 0$ and finally is such that T1 holds for sets of cardinality two. (This is always true but we have proved it only for simple random walk.)

For each fixed $x \neq 0$ we let $B = \{0,x\}$. Then

$$P_z[T > n; T_z > n] = P_0[T > n; T_z > n]$$

$$= \sum_{y \in R-B} P(0,y)P_y[T_B > n - 1].$$

Hence

$$\lim_{n \to \infty} \frac{P_z[T > n; T_z > n]}{R_n} = \sum_{y \in R-B} P(0,y)g_B(y,\infty).$$

That gives

$$\lim_{n \to \infty} \frac{P_0[B_n B_{n+1}]}{R_n} = \frac{1}{2}$$

which is the desired result, since $R_n = P_0[B_n]$.

E3 Let

$$N_n = \sum_{k=1}^{n} \delta(0, x_k)$$

denote the number of visits of the random walk to the origin in time $n$. We propose to show, for every recurrent aperiodic random walk in the plane which satisfies equation (7) in the discussion following T1, that

$$\lim_{n \to \infty} \frac{P_z[N_n = m]}{R_n} = 1$$

for all $x$ in $R$ and for every integer $m \geq 1$. When $m = 1$, observe that

$$\frac{P_z[N_n = 1]}{R_n} = \frac{1}{R_n} \sum_{k=1}^{n} P_z[T = k]R_{n-k}.$$

Hence the desired result was proved in the course of deriving (8) and (9) from condition (7) in the discussion following the proof of T1. Nor is it difficult to extend the argument to the case $m > 1$. One has

$$P_z[N_n = m] = \sum_{k=1}^{n} P_z[T = k]P_0[N_{n-k} = m - 1],$$

which leads to a simple proof by induction; for if

$$f_n = \frac{P_0[N_n = m - 1]}{R_n} \rightarrow 1$$

as $n \to \infty$, then we truncate

$$\frac{P_z[N_n = m]}{R_n} = \frac{1}{R_n} \sum_{k=1}^{n-M} P_z[T = k]R_{n-k}f_{n-k} + \frac{1}{R_n} \sum_{k=n-M+1}^{n} P_z[T = k]R_{n-k}f_{n-k}.$$

In view of (11) the last term tends to 0 for each fixed $M >

Problems

1. For an entirely arbitrary random walk (recurrent or transient) prove that
$$\Pi_A(x,x) = \Pi_A(y,y),$$
if the set $A$ consists of the two distinct points $x$ and $y$.

2. For transient random walk show that
$$g_{(0)}(x,y) = G(x,y) - \frac{G(x,0)G(0,y)}{G(0,0)}.$$

3. In this and the next two problems we develop the theory of recurrent aperiodic symmetric random walk in the plane by following a different route from that in sections 11, 12, and 13. The proof of P12.1 is taken as the basis of further developments. It yields
$$a(x) = (2\pi)^{-2} \int \frac{1 - \cos x \cdot \theta}{1 - \phi(\theta)} d\theta.$$
Now use the monotone convergence theorem (this is not possible if the random walk is unsymmetric!) to conclude that for every $x \in R$
$$\sum_{t \in R} P(x,t)a(t) = (2\pi)^{-2} \int \frac{1 - \phi(\theta) \cos x \cdot \theta}{1 - \phi(\theta)} d\theta = a(x) + \delta(x,0).$$

4. Prove that the operator $A = A(x,y)$, restricted to a finite set $B$, $|B| > 1$, has one simple positive eigenvalue, that its other eigenvalues are negative, and that its inverse $K$ has the property
$$K(\cdot \cdot) = \sum_{x \in B} \sum_{y \in B} K(x,y) \neq 0.$$
Hint: Following the author [93], who imitated Kac [50], suppose that $\lambda_1$ and $\lambda_2$ are two distinct positive eigenvalues of $A$, with eigenfunctions $u_1(x)$ and $u_2(x)$, $x \in B$. Since $A$ is symmetric, $u_1$ and $u_2$ may be taken real and such that $(u_1,u_1) = (u_

5. According to P13.2 the hitting probability function $H_B(x,y)$ is uniquely determined by its properties

(a) $\sum_{t \in R} P(x,t)H_B(t,y) - H_B(x,y) = 0, \quad x \in R - B$

(b) $H_B(x,y) = \delta(x,y), \quad x \in B$

(c) $|H_B(x,y)| \leq M$ for some $M < \infty$.

Show that the function

$$\frac{K_B(\cdot y)}{K_B(\cdot)} + \sum_{t \in B} A(x,t)\left[K_B(t,y) - \frac{K_B(t \cdot)K_B(\cdot)}{K_B(\cdot)}\right]$$

has these three properties. This may be done by using only the results of problems 3, 4 and of P12.2 and P13.2. Thus T11.1 may be proved for symmetric random walk without the manipulations in P11.1 through P11.8.

6. How must the conclusion of P12.3 be modified if one drops the "isotropy" assumption (c) to the effect that $Q(\theta) = \sigma^2|\theta|^2$?

7. Verify the properties of capacity, stated without proof at the end of section 14.

8. Let $x_1, x_2, \ldots, x_n$ denote $n$ fixed distinct points of the plane $R$, and let $B$ denote the set $B = \{x_1, x_2, \ldots, x_n,y\}$. For two-dimensional aperiodic recurrent symmetric random walk prove that

$$\lim_{|y| \to \infty} H_B(\infty,y) = 1/2.$$

9. Simple random walk in the plane. The random walk, starting at $x_0 = x \neq 0$ must visit either one, two, three, or all four of the four neighbors $i, -i, 1, -1$ of the origin before its first visit to 0. Calling $N$ the exact number of neighbors visited, calculate

$$p_n = \lim_{|z| \to \infty}

in the first quadrant, with boundary values 1 and 0 on the positive real and imaginary axes, respectively. (The solution is the actual hitting probability of the positive real axis for two-dimensional Brownian motion—see Itô and McKean [47], Ch. VII, or Lévy [72], Ch. VII.)

12. For simple random walk in the plane let $A_n$ denote the event that $x_n \neq x_k$ for $k = 0, 1, \ldots, n-1$, i.e., that a new point is visited at time $n$. The point $x_n + (x_n - x_{n-1})$ is the point which the random walk would visit at time $n+1$ if it continued in the same direction as that from $x_{n-1}$ to $x_n$. If $B_n$ is the event that $x_n + (x_n - x_{n-1}) \neq x_k$ for $k = 0, 1, \ldots, n$, show that

$$\lim_{n \to \infty} P_0[B_n \mid A_n] = 2 - \frac{4}{\pi}.$$

13. For simple random walk in the plane, let $T$ denote the time of the first double point (the time of the first visit of $x_n$ to a point which was occupied for some $n \geq 0$). Let

$$f(x) = P_0[x_T = x], \quad h(x) = P_0[T_x < T],$$

where $T = \min[k \mid k \geq 0, x_k = x]$, and prove that

$$h(x) - \sum_{y \in R} h(y)P(y,x) = \delta(x,0) - f(x), \quad x \in R,$$

$$h(x) = \sum_{y \in R} a(x-y)f(y) - a(x), \quad x \in R,$$

and finally observe that

$$E_0[a(x_T)] = 1, \quad E_0[|x_T|^2] = E_0[T]E_0[|x_1|^2].$$

14. Generalize

Chapter IV

RANDOM WALK ON A HALF-LINE

17. THE HITTING PROBABILITY OF THE RIGHT HALF-LINE

For one-dimensional random walk there is an extensive theory concerning a very special class of infinite sets. These sets are half-lines, i.e., semi-infinite intervals of the form $a \leq x < \infty$ or $-\infty < x \leq a$, where $a$ is a point (integer) in $R$. When $B \subset R$ is such a set it goes without saying that one can define the functions

$$Q_n(x,y), \quad H_B(x,y), \quad g_B(x,y), \quad x,y \text{ in } R,$$

just as in section 10, Chapter III. Of course the identities discovered there remain valid—their proof having required no assumptions whatever concerning the dimension of $R$, the periodicity or recurrence of the random walk, or the cardinality of the set $B$.

In this chapter, then, the random walk will be assumed to be genuinely one dimensional, i.e., according to D7.1 the zero-dimensional random walk with $P(0,0) = 1$ is excluded but no other assumptions

1 A large literature is devoted to the results of this chapter, usually dealing with the more general situation of arbitrary, i.e., not integer valued, sums of random variables. In 1930 Pollaczek [82] solved a difficult problem in the theory of queues (mass service systems) which was only much later recognized to be a special case of the one-sided absorption problem (in section 17) and of the problem of finding the maximum of successive partial sums (in section 19). The basic theorems in this chapter were first proved by elementary combinatorial methods devised in [91] and [92]. For the sake of a brief unified treatment we shall instead employ the same Fourier analytical approach as Baxter in [2] and Kemperman in [57]. Kemperman's book contains a bibliography of important theoretical papers up to 1960. The vast applied literature is less accessible since identical probability problems often arise in the context of queueing, inventory or storage problems, particle counters, traffic congestion, and even in actuarial

are made concerning periodicity, which plays a very secondary role; only occasionally in results like P18.8, P19.4 which involve application of the renewal theorem will it be essential that the random walk be aperiodic. Similarly, the recurrence of the random walk will not be so important here as in Chapter III. When $B \subset R$ is a finite set it is clear that

(1) $$\sum_{y \in B} H_B(x,y) = 1, \quad x \in R,$$

at least in the aperiodic case, if and only if the random walk is recurrent. But when $B$ is a half-line it will turn out that the criterion for whether (1) holds or not is quite a different one. Let $B$ be a right half-line, i.e., $B = [x \mid a \leq x < \infty]$, and consider Bernoulli random walk with $P(0,1) = p, P(0,-1) = q = 1 - p$. When $p = q$ the random walk is recurrent so that (1) holds since every point is then visited with probability one, and therefore also every subset $B$ of $R$. When $p > q$ the random walk is transient, but (1) is still true since every point to the right of the starting point is visited with probability one. Hence (1) can hold for transient as well as recurrent random walk. For a case when (1) fails one has of course to resort to a transient random walk, and indeed Bernoulli random walk with $p < q$ provides an example. These examples indicate that it is not quite trivial to determine when (1) holds. We shall see, and this is not surprising, that (1) is equivalent to the statement that the random walk visits the half-line $B$ infinitely often with probability one, regardless of the starting point, and an extremely simple necessary and sufficient condition for (1) to hold will be given in Theorem T1 of this section.

The object of our study is to gain as much information as possible about the hitting probabilities $H_B(x,y)$ and the Green function $g_B(x,y)$ of a half-line. To start with the hitting probabilities, one might approach the problem by trying to solve the exterior Dirichlet problem

(2)

Another possibility would be to utilize part (c) of the same proposition, namely

(3) $H_B(x,y) = \sum_{t \in R-B} g_B(x,t)P(t,y), \quad x \in R-B, \quad y \in B.$

The methods we will actually use will be based on an identity very much like (3). In the process we shall require simple but quite powerful methods of Fourier analysis, or alternatively of complex variable theory. To avoid convergence difficulties, which one might encounter if one tried to form Fourier series like

$$\sum_{y \in R} g_B(x,y)e^{iy\theta}$$

(a series which need not converge, as later developments will show) one is tempted to introduce generating functions. In other words,

$$g_B(x,y) = \sum_{n=0}^{\infty} Q_n(x,y)$$

is replaced by the series

$$\sum_{n=0}^{\infty} t^n Q_n(x,y),$$

with $0 \leq t < 1$. It will be unnecessary to give this series a name, however, since far more drastic changes in notation are both convenient, and in accord with tradition in this particular subject. We shall, in short, switch back to the notation and terminology in D3.1, describing the random walk $x_n$ with $x_0 = 0$, as

$$x_n = X_1 + \cdots + X_n = S_n,$$

the $X_i$ being independent identically distributed integer valued random variables with $P[X_i = x] = P(0,x)$. Thus we shall arrange matters so that $x_0 = 0$ as a general rule, and exceptions from this general rule will be carefully noted. The principal new definition we need for now is
