---
role: proof
locale: en
of_concept: prop-let-be-a-transient-kernel-on
source_book: gtm034
source_chapter: "6"
source_section: "014"
---

Proof: Suppose that $h(x)$ is $Q$-regular, and not identically zero. We have to show that for some $c > 0$, $h(x) = cf(x)$ on $S$. First observe that $h(x) > 0$ on $S$, in view of

$$\sum_{y \in S} Q_n(x,y)h(y) = h(x), \quad x \in S, \quad n \geq

contradicts our assumption that $g(x,y) > 0$ for all $x,y$ in $S$. Therefore every $Q$-regular function $h(x)$ is strictly positive on all of $S$.

Using the positive $Q$-regular function $h(x)$ we now define $Q^k$ and $g^k(x,y)$ according to D3 and P2. The function $e(x) \equiv 1$ on $S$ is $Q^k$ regular, and will now be approximated from below by the sequence

$$\tau_\pi(x) = \min [e(x), ng^k(x,\eta)].$$

Here the point $\eta$ is an arbitrary fixed point of $S$. It is easy to see that $\tau_\pi(x) \leq e(x)$ and $\tau_\pi(x) \rightarrow e(x)$ as $n \rightarrow \infty$.

Now we use T1 to show that each $\tau_\pi(x)$ is a $Q^k$-potential. Being the minimum of two excessive functions, $\tau_\pi(x)$ is excessive by P1, part (2). Hence, according to T1

$$\tau_\pi(x) = k(x) - u(x),$$

where $k(x)$ is $Q^k$-regular and $u(x)$ is a $Q^k$-potential. But

$$k(x) \leq ng^k(x,\eta), \quad x \in S,$$

which shows, by P1(3), that $k(x) \equiv 0$. Hence we have succeeded in exhibiting a sequence of $Q^k$-potentials $\tau_\pi(x)$ which converge to $e(x)$. All other properties of this sequence will be quite irrelevant from now on.

According to the definition of potentials, there is a sequence of charges $\mu_\pi(x)$, such that

(1) $$\tau_\pi(x) = \sum_{y \in S} g^k(x,y)\mu_\pi(y).$$

With $\xi$ denoting the point in the hypothesis of P3,

(2) $$\tau_\pi(x) = \sum_{y \in S} \frac{g^k(x,y)}{g^k(\xi,y)}\gamma_\pi(y),$$

where $\gamma_\pi(y) = g^k

exists for each $y$ in $S$, and observe, using the hypothesis of P3, that

$$\lim_{|y| \to \infty} \frac{g^h(x,y)}{g^h(\xi,y)} = \lim_{|y| \to \infty} \frac{g(x,y)}{g(\xi,y)} \frac{h(\xi)}{h(x)} = f(x) \frac{h(\xi)}{h(x)}$$

Choosing $M$ so large that

$$\left| \frac{g^h(x,y)}{g^h(\xi,y)} - f(x) \frac{h(\xi)}{h(x)} \right| < \epsilon \quad \text{when} \quad |y| > M,$$

it follows from (4), (5), and (6) that

$$1 = \sum_{|y| \leq M} \frac{g^h(x,y)}{g^h(\xi,y)} \gamma(y) + \lim_{n' \to \infty} \frac{f(x)h(\xi)}{h(x)} \sum_{|y| > M} \gamma_{n'}(y) + R(M),$$

where $R(M)$ is an error term whose magnitude does not exceed $\epsilon$. Now $R(M)$ tends to zero as $M \to \infty$, and if we call

$$\lim_{M \to \infty} \lim_{n' \to \infty} \sum_{|y| > M} \gamma_{n'}(y) = \gamma_\infty,$$

then it follows that

$$1 = \sum_{y \in S} \frac{g^h(x,y)}{g^h(\xi,y)} \gamma(y) + \gamma_\infty f(x) \frac{h(\xi)}{h(x)}, \quad x \in S.$$

In (7), the constant $\gamma_\infty$ has a value between zero and one, and the measure $\gamma(y)$ has total mass at most one. That is all one can conclude from (3). But now we shall show that $\gamma(y)$ is identically zero, by appealing to the Riesz decomposition theorem. In equation (7), the constant on the left is $Q^h$-regular. On the right the function

$$\

Our first application of P3 concerns the transient random walk treated in the last section.

E2 Consider aperiodic random walk in three dimensions, satisfying the hypotheses (a) through (c) of P26.1. Then P26.1 gives

$$\lim_{|\nu| \to \infty} \frac{G(x,y)}{G(0,y)} = 1, \quad x \in R.$$

In order to apply P3 to the problem of finding the $P$-regular functions, we make the obvious identifications,

$$R = S, \quad P(x,y) = Q(x,y), \quad x,y \in S,$$
$$g(x,y) = G(x,y), \quad \xi = 0.$$

One must also note that

$$f(x) = \lim_{|\nu| \to \infty} \frac{g(x,y)}{g(0,y)} = 1, \quad x \in S,$$

is $P$-regular (the constant function is $P$-regular for every random walk) and hence $Q$-regular. Now P3 applies, so that aperiodic three-dimensional random walk with mean zero, and finite second moments has only the constant regular function. The hypotheses are of course much too stringent—see problem 6. Nevertheless there is no "easy" proof, even in the special case of simple random walk. (A short but sophisticated proof for simple random walk is outlined in problem 8.)

E3 Theorem: If $P(x,y)$ is recurrent aperiodic random walk in one dimension, then the Wiener-Hopf equation

$$\sum_{y=0}^{\infty} P(x,y)f(y) = f(x), \quad x = 0, 1, 2, \ldots,$$

has a unique non-negative solution. It is

$$f(x) = u(0) + u(1) + \cdots + u(x), \quad x \geq 0,$$

$u(x)$ being the function defined in D18.2.

Proof: The problem is merely one of verifying the hypotheses in P3. According to the discussion of this problem preceding P3, we have

(1) $g(x,y) = u(x)v(y) + u(x-1)v(y-1)

Here $c$ may be any positive constant, $\xi$ has been taken to be the origin, and $|y| \to \infty$ in this problem clearly means $y \to +\infty$. In view of (1), equation (2) is equivalent to

$$\lim_{y \to +\infty} \frac{1}{u(0)v(y)} [u(x)v(y) + u(x - 1)v(y - 1) + \cdots + u(0)v(y - x)]$$
$$= c[u(0) + u(1) + \cdots + u(x)], \quad x \geq 0,$$

and (3) will be valid if we prove

$$\lim_{y \to +\infty} \frac{v(y + 1)}{v(y)} = 1.$$

In fact, if (4) holds, then $f(x)$ in P3 will be a constant multiple of $u(0) + \cdots + u(x)$, and this function was shown to be regular in P19.5. Hence it remains only to prove (4).

In P18.8 a much stronger result than (4) was proved under the additional restriction that the random walk has finite variance. It was shown that $v(y)$ tends to a positive constant as $y \to +\infty$. Equation (4), being far weaker, can be proved by a simple probabilistic argument (suggested by H. Kesten) for any recurrent random walk. (Note, however, that the proof of (4) we are about to give runs into difficulties if the random walk is transient. See problem 11.)

For $x \geq 0$ and $y \geq 0$, we denote by $J(x,y)$ the probability that the random walk, starting at $x_0 = x$, will visit $y$ before entering the set $R - S = [x \mid x < 0]$. Also let $J(x,x) = 1$. Then

$$g(0,x) = u(0)v(x) = J(0,x)g(x,x),$$

$$\frac{v(x + 1)}{v(x)} = \frac{J(0,x + 1)}{J(0,x

speaking. The inequalities in (8) should also be intuitively obvious: the first one says that in going from 0 to $x + 1$, and then from $x + 1$ to $x$, without meeting $R - S$, the random walk goes from 0 to $x$ without meeting $R - S$. Finally (9) is true for exactly the same reason as (7).

Combining (6), (7), (8), and (9) in the obvious manner, one observes that the right-hand side in (5) tends to one as $x \to +\infty$. But that is the statement in (4) which has been shown to guarantee the truth of E3.

In problem 12 it will be shown that the unique solution of E3 is no longer unique if one admits solutions which may oscillate in sign.

E4 Let $A(x,y) = A(0,y - x)$, $a(x) = A(x,0)$ be the potential kernel of recurrent aperiodic random walk in the plane. Then $a(x)$ is the only non-negative solution of

$$\sum_{y \neq 0} P(x,y)a(y) - a(x) = 0, \quad x \neq 0.$$

To prove this we take $Q(x,y) = P(x,y)$ ($P$ is the transition function of the random walk) for $x$ and $y$ in $S = R - \{0\}$. According to the results of Chapter III,

$$g_{(0)}(x,y) = g(x,y) > 0, \quad x,y \in S,$$

$a(x)$ is a $Q$-regular function, and for arbitrary $\xi$ in $S$,

$$\frac{g(x,y)}{g(\xi,y)} = \frac{a(x) + a(-y) - a(x - y)}{a(\xi) + a(-y) - a(\xi - y)}$$

The limiting process $|y| \to \infty$ of D3 is equivalent to letting $|y| \to \infty$ in the metric (Euclidean distance) of $R$. And, finally,

$$\lim_{|y| \to \infty} \frac{g(x,y)}{g(\xi,y)} =

Let $P(x,y)$ be the transition function of the following simple unsymmetric two-dimensional random walk. If $x = (m,n)$, $m$ and $n$ being the coordinates of the lattice points of $R$, then

$$P(0,x) = \frac{1}{2} \text{ if } x = (0,1) \text{ and if } x = (1,0).$$

Let

(1) $$f_i(x) = 2^{m+n} t^m (1-t)^n, \quad x = (m,n), \quad 0 < t < 1.$$

Thus $f_i(x)$ is a one parameter family of functions on $R$. For each value of the parameter $t$ between 0 and 1, $f_i(x)$ happens to be a regular function. This is simple to verify; it suffices to check

$$\sum_{x \in R} P(0,x) f_i(x) = \frac{1}{2} \cdot 2t + \frac{1}{2} \cdot 2(1-t) = 1 = f(0).$$

Note that the functions in (1) are also regular if $t = 0$ or 1, provided we restrict them to the first quadrant

$$R^+ = [x \mid x = (m,n), m \geq 0, n \geq 0].$$

This is very natural as $R^+$ is the semigroup associated with the support $\sum$ of $P(0,x)$. From now on we shall confine our attention to those regular functions which are non-negative solutions of

(2) $$f(x) = \sum_{y \in R^+} P(x,y) f(y), \quad x \in R^+.$$

Then we can assert, by linearity, that

(3) $$f(x) = \int_0^1 f_i(x) d\mu(t) = 2^{m+n} \int_0^1 t^m (1-t)^n d\mu(t), \quad x \in R^+.$$

is a regular function, in the sense of equation (2), for every finite measure $\mu$ on the unit interval. (The integral in (3) is the Leb

Here $x = (m,n)$ and $y = (r,s)$ are confined to $R^+$ (the first quadrant) and the proof of (5) depends on Stirling's formula

$$n! \sim n^n e^{-n} \sqrt{2\pi n} \text{ as } n \to \infty.$$

The tedious but straightforward details are omitted.

Just as in the proof of P3 we pick an arbitrary regular function (non-negative solution of (2)) with the intention of showing that it has an integral representation of the type in (3). We must now distinguish between two possibilities.

I: $h(x) = 0$ for all $x = (m,n)$ such that $m > 0, n > 0.$

In this case $h(x) = 2^n a$ when $m = 0, n \geq 1, h(x) = 2^m b$ when $m \geq 1, n = 0$, and $h(0) = a + b$; here $a$ and $b$ are non-negative constants. It follows that $h(x)$ is represented by (3) with a measure $\mu$ which assigns masses of $a$ and $b$ to the points $t = 0$ and $t = 1$. In this case, then, there is nothing to prove.

II: $h(x) > 0$ for some $x = (m,n)$ such that $m > 0, n > 0.$

In this case it follows from a careful scrutiny of equation (2) that $h(x) > 0$ for every $x \in R^+$. (To see this, assume the contrary. The set of zeros of $h$ must then be of the form $[x \mid x = (m,n); m \geq m_0, n \geq n_0]$ where either $m_0 > 1$ or $n_0 > 1$ or both, since we are not in case I. Suppose therefore that $m_0 > 1$. On the vertical half-line defined by $x = (m_0 - 1,n), n \geq n_0, h(x)$ must then be of the form $h(x) =

where

(8) $\gamma_n(y) \geq 0, \quad \sum_{y \in R^+} \gamma_n(y) \leq 1$.

Of course we choose a subsequence $k'$ such that

(9) $\lim_{k' \to \infty} \gamma_{k'}(y) = \gamma(y), \quad y \in R^+$,

and a number $M$ such that the error in (5) is less than $\epsilon$ when $|y| > M$. Then (7) implies

(10) $\lim_{k' \to \infty} v_{k'}(x) = 1 = \sum_{|y| \leq M} \frac{g^h(x,y)}{g^h(0,y)} \gamma(y)$
$+ \lim_{k' \to \infty} \frac{h(0)}{h(x)} 2^{n+m} \sum_{|y| > M} \left(\frac{r}{r+s}\right)^m \left(\frac{s}{r+s}\right)^n \gamma_{k'}(y) + R(M)$,

where $x = (m,n), y = (r,s)$, and $R(M)$ does not exceed $(h(0)/h(x))\epsilon$. If we let $M \to \infty$, then $R(M) \to 0$, and (10) becomes

(11) $1 = v^h(x) + \lim_{M \to \infty} \lim_{k' \to \infty} \frac{h(0)}{h(x)} 2^{n+m} \sum_{|y| > M} \left(\frac{r}{r+s}\right)^m \left(\frac{s}{r+s}\right)^n \gamma_{k'}(y)$,

where $v^h$ is the $Q^h$-potential

$v^h(x) = \sum_{y \in R^+} \frac{g^h(x,y)}{g^h(0,y)} \gamma(y)$.

Observe now that the sums in (11) can be interpreted as integrals over the unit interval, with respect to measures whose masses are concentrated on the rational numbers. Equation (

This result yields (in fact is equivalent to) the solution of a problem in classical analysis—the Hausdorff moment problem. A sequence $c(n)$, $n \geq 0$, is called a (Hausdorff) moment sequence if

$$c(n) = \int_0^1 t^n d\mu(t), \quad n \geq 0,$$

for some measure $\mu$ on $[0,1]$.

To present Hausdorff's [41], 1921, characterization of moment sequences, we define the difference operator $\Delta$ acting on functions defined on the non-negative integers by

$$\Delta f(n) = f(n) - f(n + 1), \quad n \geq 0.$$

Its iterates are defined by $\Delta^0 f = f$, $\Delta^1 f = \Delta f$, $\Delta^2 f = \Delta(\Delta f)$, $\Delta^{n+1} f = \Delta(\Delta^n f)$.

Theorem: The sequence $c(n)$ is a moment sequence if and only if $\Delta^k c(n) \geq 0$ whenever $k \geq 0$ and $n \geq 0$.

Proof: Given any sequence $c(n)$, $n \geq 0$, we define a function $h(m,0)$ by

$$h(m,0) = 2^m c(m), \quad m \geq 0.$$

Next define

$$h(m,1) = 2^{m+1} \Delta c(m), \quad m \geq 0,$$

$$h(m,n) = 2^{m+n} \Delta^n c(m), \quad m \geq 0, \quad n \geq 0.$$

Let

$$f(x) = h(m,n), \quad x = (m,n) \in R^+.$$

Now one verifies, using the definition of $\Delta$ and of its iterates, that $f(x)$ satisfies the equation

$$\sum_{y \in R^+} P(x,y)f(y) = f(x), \quad x \in R^+.$$

Note that $f$ is not necessarily regular, since it is not necessarily non-neg

Problems

1. Prove P13.1 by using T24.1. (Hint: Show that recurrent random walk has no excessive functions, i.e., functions $f \geq 0$ such that $f \geq Pf$ on $R$, other than the regular functions. Then show that, given any constant $c \geq 0$, the function $u(x) = \min [f(x), c]$ is excessive, provided that $f(x)$ is regular.)

2. Prove, using D25.2, that every transient random walk has infinite recurrent sets as well as infinite transient sets.

3. For aperiodic transient random walk in one dimension which has $\mu^+ < \infty, \mu^- = \infty$, exhibit a transient set which is unbounded on the left (or prove that there is one!).

4. Given an aperiodic transient random walk with state space $R$, let $B \subseteq R$ be any additive subgroup of $R$. Prove that the set $B$ is recurrent (i.e., visited infinitely often with probability one) if and only if

$$\sum_{x \in B} G(0, x) = \infty$$

Hint: The above sum is the total expected time the random walk spends in the set $B$.

5. Following R. Bucy [S3], prove the following strengthened form of T25.1: A set $B$ is transient if and only if there exists a function $u \geq 0$ on $B$ such that

$$\sum_{y \in B} G(x, y)u(y) = 1, \quad x \in B.$$

Hint: Suppose there is such a function $u$ and that $B$ is recurrent. Let $T_n$ be the time of the first visit to $B$ after time $n$. Then, for $x \in B$,

$$1 = E_z \sum_{k=0}^{\infty} u(x_k) = E_z \sum_{k=0}^{n} u(x_k) + E_z \sum_{k=T_n}^{\infty} u(x_k).$$

Now let $n \to \infty$ to arrive at the contradiction that $1 = 2$

Let $C_0 = C$,

$$C_1 = \left[ \varphi \mid \varphi \in C; \varphi(x_1) = \max_{f \in C} f(x_1) \right],$$

$$C_{n+1} = \left[ \varphi \mid \varphi \in C_n; \varphi(x_{n+1}) = \max_{f \in C_n} f(x_{n+1}) \right],$$

and show that $\bigcap_{n=0}^{\infty} C_n$ consists of a single regular function $f(x)$. Show that this is a minimal regular function, i.e., that $f \in C$ and $f \leq f$ on $R$ implies that $f = f'$. But

$$f(x) = \sum_{y \in R} P(x,y)f(y) = \sum_{z \in R} P(0,z)f(z) \frac{f(z+x)}{f(z)}$$

exhibits $f$ as a convex combination of the functions

$$\varphi_z(x) = \frac{f(z+x)}{f(z)}$$

which are in $C$. Since $f$ is minimal one can conclude that $\varphi_z = f$ whenever $P(0,z) > 0$. Consequently $f(z+x) = f(z)f(x)$ for all $x,z \in R$, which shows that $f$ is an exponential. Prove that $f$ is constant and conclude that simple random walk has only constant regular functions.

9. Problem 8 strongly suggests that every regular function for a transient random walk should be a convex combination of minimal regular functions. As in problem 8 one can show that the minimal regular functions are exponentials of the form

$$f(x) = e^{a \cdot x}$$

where $a$ is a vector whose dimension is that of $R$ (see [25]). In view of problem 6, random walk with zero mean is not of interest. Therefore we shall consider strongly aperiodic random walk with mean vector $\mu \neq 0$, assuming also that $P_n(0,x) > 0$ for some $n$ which may depend on $x$, and that

$$\sum P(0,x)e^{a \cdot x} < \infty$$

10. Continuation. If $x \to \infty$ in the direction of the mean vector $\mu$, use the Local Central Limit Theorems P7.9 and P7.10 to show that

$$\lim_{x \to \infty} \frac{G(x,y)}{G(x,0)} = 1, \quad y \in R.$$

If $x \to \infty$ in the direction $p$, choose $a = a(p) \in A$ as in problem 9, and observe that the random walk with transition function

$$Q(x,y) = P(x,y)e^{a \cdot (y-x)}$$

has its mean vector along $p$. Using this idea, P. Ney and the author [S21] proved

$$\lim_{|x| \to \infty} \left| \frac{G(y,x)}{G(0,x)} - e^{a(x)\cdot y} \right| = 0$$

for every $y \in R$. Now one can imitate the method of E27.5 to conclude that the regular functions of a random walk subject to the conditions in problem 9 have the representation

$$f(x) = \int_A e^{a \cdot x} d\mu(a), \quad x \in R,$$

where $\mu$ is a Lebesgue-Stieltjes measure on $A$.

11. It is not known whether the Wiener-Hopf equation

$$\sum_{y=0}^{\infty} P(x,y)f(y) = f(x), \quad x \geq 0,$$

has a solution for every transient random walk (excluding of course the trivial case with $P(0,x) = 0$ for $x \geq 0$ and $P(0,0) < 1$, when there is obviously no solution). Demonstrate, however, that example E27.3 does not extend to transient random walk, for the following reason. Take a random walk with negative mean, satisfying in addition the hypotheses in P19.6. Show that the unique non-negative solution of the above Wiener-Hopf equation is then of the form

$$f(x) = \sum_{k=0}^{\infty} r^k u(x-k), \quad x \geq 0,$$

13. Show that the Green function $G(x,y)$ determines the random walk (i.e., two transient random walks with the same Green function must have the same transition function). (Hint: Show that $G(x,y)$ determines $\Pi_A(x,y)$, and then let the set $A$ "grow very large" so that $\Pi_A(x,y) \rightarrow P(x,y)$.)

14. One more definition of capacity. Given an arbitrary aperiodic transient random walk, and a finite subset $A \subset R$, consider the (random) set $A_n$ which is "swept out" by the random walk in time $n$: formally

$$A_n = [x \mid x \in x_k + A \text{ for some } k, 0 \leq k \leq n]$$

Finally let $C_n(A) = |A_n|$ denote the cardinality of $A_n$. Prove that the capacity $C(A)$ of the set $A$ is given by

$$\lim_{n \to \infty} \frac{C_n(A)}{n} = C(A)$$

with probability one.

Hint: Observe that if $A = \{0\}$, then $C_n(A) = R_n$, the range of the random walk, as defined in D4.1. According to E4.1 the above limit then exists and is $1 - F = G^{-1}$, the capacity of a single point. Observe further that the proof in E4.1 applies, with obvious modifications, in the present case.

15. For simple random walk in three-space or, more generally, for any random walk satisfying the hypotheses (a) through (d) in P26.1, let $A$ be a finite subset of $R$ and prove that

(1) $P_z[T_A < \infty] - P_z[T_A \leq n] = P_z[n < T_A < \infty]$
$$\sim P_z[T_A = \infty] \frac{2C(A)}{(2\pi\sigma^2)^{3/2}} n^{-1/2}, \text{ as } n \to \infty,$$

for all $x \in R$. (This is the transient analogue of the results in section 16 concerning the rate of approach
