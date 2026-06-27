---
role: proof
locale: en
of_concept: proposition-9-131
source_book: gtm040
source_chapter: "9"
source_section: "131"
---

**Proof:** The first assertion follows directly from Lemmas 9-129 and 9-130. The second assertion follows from the fact that $P$ is ergodic if and only if $\alpha_1 < \infty$, where $\alpha_i = \sum_j c_{ij}$.

**11. A nonnormal chain and other examples**

We shall show by examples in this section that all three of the following conjectures are false:

(1) Small sets and ergodic sets are identical concepts, or at least one of the notions includes the other.

(2) All null chains are normal.

(3) The existence of either $C$ or $G$ implies the existence of both.

First, we settle the independence of the notions of small sets and ergodic sets. We saw in Section 6 an example of an ergodic set which is not small, and we shall now produce a small set which is not ergodic.

Let $P$ be a chain with states the non-negative integers and with transition probabilities

$$P_{0i} = p_i = P_{i0} \quad \text{for } i > 0$$

$$P_{ii} = q_i = 1 - p_i.$$

All other entries of $P$ are 0. We impose no requirements on the $p_i$ yet except that $p_i > 0$ and $\sum p_i = 1$. It is clear that $\bar{H}_{00} = 1$ and hence $P$ is recurrent. Since $P = P^T$, $\alpha = 1^T$ is regular and $

whereas

$$\lambda_0^E = \lim_n \sum_k P_{0k}^{(n)} B_{k0}^E$$

$$= \lim_n P_{00}^{(n)} + \lim_n \sum_{k \in E} P_{0k}^{(n)}$$

$$= 1 - \lim_n P_{0E}^{(n)}$$

Thus any set containing 0 such that $P_{0E}^{(n)} \to 0$ satisfies $\lambda_0^E = 1$ and is therefore a small set. Let

$$p_i = 4^{-k} \text{ for } 2^k - 1 \leq i \leq 2^{k+1} - 2.$$

The $p_i$ assume the constant value $4^{-k}$ on a block of length $2^k$. Thus

$$\sum p_i = \sum_{k=1}^{\infty} 2^k \cdot 4^{-k} = 1.$$

Let $E$ consist of 0 and one state, such as $2^k$, from each block, and label the representative of the $k$th block in $E$ as $e_k$. Then

$$P_{0E}^{(n)} = P_{00}^{(n)} + \sum_{k=1}^{N-1} P_{0e_k}^{(n)} + P_{0T_N}^{(n)},$$

where $T_N = \{e_N, e_{N+1}, e_{N+2}, \ldots\}$. We can form $2^N$ disjoint sets like $T_N$ each differing from it in every representative selected from the $N$th block on. By symmetry $P_{0T_N}' = P_{0T_N}^{(n)}$ for all such sets $T_N'$. Hence $P_{0T_N}^{(n)} \leq 1/2^N$ for all $n$. Since $P_{0j}^{(n)} \to 0$ in a null chain,

$$\limsup_n P_{0E}^{(n)} \leq \frac{1}{2^N},$$

and we must have $P_{0E}^{(n)} \to 0.$

Second, we shall construct a non

Abel summable. Let $E = \{0, 1\}$ and define generating functions as follows:

$$A_{00}(t) = \sum_{n} {}^1 \bar{F}_{00}^{(n)} t^n, \quad A_{01}(t) = \sum_{n} {}^0 \bar{F}_{01}^{(n)} t^n$$

$$A_{10}(t) = \sum_{n} {}^1 \bar{F}_{10}^{(n)} t^n, \quad A_{11}(t) = \sum_{n} {}^0 \bar{F}_{11}^{(n)} t^n$$

$$P_{ij}(t) = \sum_{n} P_{ij}^{(n)} t^n$$

$$H_0(t) = A_{00}(t) + A_{01}(t) = \sum_{n} \bar{F}_{0E}^{(n)} t^n$$

$$H_1(t) = A_{10}(t) + A_{11}(t) = \sum_{n} \bar{F}_{1E}^{(n)} t^n$$

$$Q(t) = \sum_{n} \left( P_{11}^{(n)} - P_{01}^{(n)} \right) t^n = P_{11}(t) - P_{01}(t)$$

$$R(t) = \frac{1 - H_1(t)}{1 - H_0(t)}$$

We note that the series defining $C_{01}$ is Abel summable if and only if $\lim_{t \to 1^-} Q(t)$ exists. We shall prove that this limit exists if and only if $\lim_{t \to 1^-} R(t)$ exists. We have

$$P_{01}^{(n)} = \sum_{k} \left( {}^1 \bar{F}_{00}^{(k)} P_{01}^{(n-k)} + {}^0 \bar{F}_{01}^{(k)} P_{11}^{(n-k)} \right)$$

or

$$P_{01}(t) = A_{00}(t) P_{01}(t) + A

and if $p_i > 0$, $p_i' > 0$, $\sum p_i = 1$, and $\sum p_i' = 1$, then the transition probabilities are

$$P_{0a_i} = p_i = P_{a_i1}$$
$$P_{a_i a_i} = q_i = 1 - p_i$$
$$P_{1b_i} = p_i' = P_{b_i0}$$
$$P_{b_i b_i} = q_i' = 1 - p_i'.$$

All other entries are 0. We see easily that $\bar{H}_{00} = 1$ and that $\alpha = 1^T$ is regular, hence the chain is recurrent and null. For $E = \{0, 1\}$,

$$\bar{F}_{0E}^{(n)} = F_{01}^{(n)} = \sum_i p_i q_i^{n-2} p_i \text{ for } n \geq 2.$$

Therefore

$$H_0(t) = \sum_i p_i^2 \sum_{n=2}^{\infty} q_i^{n-2} t^n = \sum_i \frac{p_i^2 t^2}{1 - q_i t}.$$

Similarly,

$$H_1(t) = \sum_i \frac{(p_i')^2 t^2}{1 - q_i't},$$

and we have defined $R(t)$ by

$$R(t) = \frac{1 - H_1(t)}{1 - H_0(t)}.$$

We again choose the $p_i$'s in blocks as follows. Let $\{n_k\}$ and $\{n_k'\}$ be two rapidly increasing sequences (with magnitude specified later) such that $n_k < n_k' < n_{k+1}$. Let there be $n_k$ consecutive $p_i$'s equal to $\epsilon_k = 1/(2^k n_k)$, and let there be $n_k'$ consecutive $(p_i')$'s equal to $\epsilon_k' = 1/(2^k n_k')$. The remainder of the proof consists in showing that for suitably chosen $\{n_k\}$ and $\{n_k'\}$

$$\lim_{n \to

which differs from $H_0(1 - \epsilon_n)$ if $\epsilon_n$ is chosen to be negligible compared with $\epsilon'_n$ but much bigger than $\epsilon'_{n-1}$.

$$R(1 - \epsilon_n) \sim \frac{2^{-n+1}}{2^{-n+1} - 2^{-n-1}} = \frac{4}{3}.$$

If $t = 1 - \epsilon'_n$ and $n$ is large we obtain, similarly,

$$H_0(1 - \epsilon'_n) \sim \sum_{k=1}^{\infty} 2^{-k} \frac{\epsilon_k}{\epsilon_k + \epsilon'_n} \sim \sum_{k=1}^{n} 2^{-k} = 1 - 2^{-n}$$

and

$$H_1(1 - \epsilon'_n) \sim \sum_{k=1}^{\infty} 2^{-k} \frac{\epsilon'_k}{\epsilon'_k + \epsilon'_n} \sim \sum_{k=1}^{n-1} 2^{-k} + 2^{-n} \cdot 2^{-1}$$

$$= 1 - 2^{-n+1} + 2^{-n-1}.$$

The asymmetry in $H_0(1 - \epsilon'_n)$ and $H_1(1 - \epsilon_n)$ arises because the condition $n_k < n'_k < n_{k+1}$ is not symmetric. We thus find

$$R(1 - \epsilon'_n) \sim \frac{2^{-n+1} - 2^{-n-1}}{2^{-n}} = \frac{3}{2}.$$

Therefore, $\lim_{t \to 1^{-}} R(t)$ does not exist and $C_{01}$ cannot exist. In particular, $P$ is not normal.

This example has the property that neither $C$ nor $G$ exists. The reverse process has transition probabilities $\hat{P}_{0b_i} = P_{b_i0} = p'_i = \hat{P}_{b_i1}$ and $\hat{P}_{1a_i} = p_i = \hat{P}_{a_i0}$. Thus $\hat

Third, we show that the existence of one of $C$ and $G$ does not imply the existence of the other. Again we modify the first example of a nonnormal chain. Let

$$P_{0a_i} = p_i, \quad P_{a_i a_i} = q_i, \quad P_{1b_i} = p_i', \quad \text{and} \quad P_{b_i b_i} = q_i'$$

as before, and use the same $p$'s. But set

$$P_{a_i 0} = P_{a_i 1} = \frac{1}{2} p_i \quad \text{and} \quad P_{b_i 0} = P_{b_i 1} = \frac{1}{2} p_i'.$$

It is clear that $\bar{F}_{0, (0, 1)}^{(n)}$ and $\bar{F}_{1, (0, 1)}^{(n)}$ are the same as before, so that $\lim_{t \to 1^-} R(t)$ does not exist and $C_{01}$ does not exist. On the other hand, the reverse chain is no longer of the same type and the argument for the nonexistence of $G$ fails. In fact,

$$0 \lambda_1 = \lim_n \left[ P_{01}^{(n)} + \sum_i P_{0a_i}^{(n)} 0 H_{a_i 1} + \sum_i P_{0b_i}^{(n)} 0 H_{b_i 1} \right]$$

$$= \lim_n \left[ P_{01}^{(n)} + \frac{1}{2} \sum_i \left(P_{0a_i}^{(n)} + P_{0b_i}^{(n)}\right) \right]$$

$$= \frac{1}{2}.$$

Hence $G_{01} = \frac{1}{2} 0 N_{11}$ exists. Moreover, if $x$ and $y$ are any two states other than 0 and 1,

$$x \lambda_y = \frac{1}{2} x H_{0y} + \frac{1}{2} x H_{1y}.$$

Therefore all of $G

In particular, the values at the four points neighboring the origin must be the same. Since their average is one, $k(0, 1) = 1$.

We shall need one more result. It can be shown (see Spitzer [1964]) that

$$k(x, x) = \frac{4}{\pi} \left( \frac{1}{1} + \frac{1}{3} + \cdots + \frac{1}{2x - 1} \right) \text{ for } x > 0.$$

This identity, together with the properties above, determines the function $k$.

In fact, it suffices to restrict attention to $0 \leq x \leq y$. We know that $k(0, 0) = 0, k(0, 1) = 1$, and $k(1, 1) = 4/\pi$. If we know the values of $k(x, y)$ up to a given $y_0$ for all $x$ such that $0 \leq x \leq y$, then we can find the values of $k(x, y_0 + 1)$ for $0 \leq x \leq y_0 + 1$. The averaging and symmetry properties give

$$k(0, y_0 + 1) = 4k(0, y_0) - 2k(1, y_0) - k(0, y_0 - 1)$$

$$k(x, y_0 + 1) = 4k(x, y_0) - k(x + 1, y_0) - k(x - 1, y_0) - k(x, y_0 - 1)$$

for $0 < x < y_0$

$$k(y_0, y_0 + 1) = 2k(y_0, y_0) - k(y_0 - 1, y_0).$$

And $k(y_0 + 1, y_0 + 1)$ is given by the identity for $k(x, x)$.

The equations above thus are recursion equations for $k(x, y)$. Actually these equations are so simple that we apparently have a very rapid method of computing $K_E$ for large finite sets $E$. Unfortunately the recursion is

If we wish to find $k(E), \lambda^E$, and $P^E$ for a finite set of points $E$, we first construct $K_E$ and then compute the inverse $K_E^{-1}$. Let $z = K_E^{-1}1$. Since $\alpha = 1^T$ and since $K$ is symmetric, the results in the statement and proof of Corollary 9-92 simplify to

$$k(E) = 1/(1^Tz)$$
$$\lambda^E = k(E)z^T$$
$$P^E = I + K_E^{-1} - k(E)zz^T.$$

Calculations for various sets $E$ appear in Tables 9-2, 9-3, and 9-4.

**Table 9-2.** $k(E), \lambda^E$, and $P^E$ when $E$ consists of three points on a line; $E = \{(0, 0), (a, 0), (2a, 0)\}$

| $a = 1$ | $a = 2$ |
| :--- | :--- |
| $k(E) = 0.785$ | $k(E) = 1.082$ |
| $\lambda^E = 0.393$ $0.215$ $0.393$ | $\lambda^E = 0.372$ $0.256$ $0.372$ |
| $P^E = 0.460$ $0.393$ $0.148$ | $P^E = 0.610$ $0.256$ $0.134$ |
| $\alpha = 0.393$ $0.215$ $0.393$ | $\alpha = 0.256$ $0.488$ $0.256$ |
| $\alpha = 0.148$ $0.393$ $0.460$ | $\alpha = 0.134$ $0.256$ $0.610$ |

| $a = 3$ | $a = 4$ |

21 points arranged in an isosceles right triangle of base 6

$$k(E) = 1.611$$
$$\lambda^E$$
0.162
0.046 0.059
0.041 0 0.051
0.041 0 0 0.051
0.044 0 0 0 0.059
0.109 0.044 0.041 0.041 0.046 0.162

13 points arranged in a figure $\times$

$$k(E) = 1.778$$
$$\lambda^E$$
0.153
0.064
0.030 0.015
0.030
0.064
0.153

30 points in a 5-by-6 rectangle

$$k(E) = 1.670$$
$$\lambda^E$$
0.105 0.042 0.038 0.038 0.042 0.105
0.044 0 0 0 0 0 0.044
0.041 0 0 0 0 0 0.041
0.044 0 0 0 0 0 0.044
0.105 0.042 0.038 0.038 0.042 0.105

It is hard to acquire an intuition for the capacities of sets aside from their monotonicity. However, the values of $P^E$ and $\lambda^E$ are quite intuitive. The latter, in this random walk, may be thought of as the entrance probabilities to $E$ if the chain is started near $\infty$. For example, in the case of the 5-by-6 rectangle in Table 9-4, it is clear that the corner positions should be considerably more probable than the points on the side. Points on the short sides are more probable than points on the long ones,

13. Problems

1. Prove that $iN_{jj} = jN_{ii}$ for recurrent sums of independent random variables.

2. Prove that for any null chain and for any states $i$ and $j$ there is a finite set $E$ such that

$$\limsup_{n} \frac{N_{ij}^{(n)}}{N_{iE}^{(n)}} < \epsilon.$$

3. Let a recurrent chain $P$ be started in state 0. Let $\alpha_{i}^{E}$ be the mean number of times in state $i$ in the time required to reach the set $E$ and then return to 0. Thus, for example, if $E$ is the set of all states, then $\alpha_{i}^{E} = (1/\alpha_{0})\alpha$.

(a) Prove that for any set $E$ there is a constant $k_{E}$ such that $\alpha_{i}^{E} = k_{E}\alpha$.

(b) Let $Q$ be the transition matrix for the transient states when 0 is made absorbing and let $\bar{\alpha}$ be the restriction of $\alpha$ to the transient states. Show that if $E$ is a set which does not contain 0, then

$$1 - E\bar{H}_{00} = \frac{1}{\alpha_{0}}\bar{\alpha}[(I - Q)B^{E}1],$$

where $B^{E}$ is restricted to the transient states.

(c) Conclude that if $E$ is a set which does not contain 0, then $1/k_{E}$ is the transient capacity of the set $E$ in the chain $Q$, provided the distinguished superregular measure is taken as $\bar{\alpha}$.

4. Prove that for a recurrent chain

$$jN_{ik} + iN_{jk} = jN_{ii}\frac{\alpha_{k}}{\alpha_{i}}.$$

5. For the symmetric random walk in two dimensions, verify that the function whose $(x, y)$th entry is $(|x| + |y| + 1)^{-1}$ is a potential, using only Corollary 9-16. Show that its charge $f$ satisfies $\alpha f = 0$.

6

9. In Problem 8 show that

$$kH_{ij} = \sum_{m \in E} B_{im}^F kH_{mj} \quad \text{for all } j \in E.$$

Use the identity of Problem 8 to eliminate the factors $B_{im}^F$, and solve the resulting identity for $B_{ik}^F$. Prove from this result that $\lambda_k^F$ exists, provided $P$ is normal.

10. Use the results of the two previous problems to prove that the union of a small set and a finite set is small in a normal chain.

Problems 11 to 22 develop a new null example and use it to illustrate results in the chapter. The state space consists of all points $z = (x, y)$ in the plane with integer coordinates $\geq 1$. It will be convenient to let $n = x + y$. We let $(1, 1)$ be our state 0. Define

$$P_{(x, y), (x + 1, y)} = \frac{x}{x + y + 1}, \quad P_{(x, y), (x, y + 1)} = \frac{y}{x + y + 1},$$

and

$$P_{(x, y), 0} = \frac{1}{x + y + 1}.$$

11. Verify that $P$ is null recurrent and that $\alpha_z = 2/[(n - 1)n].$

12. Compute $\hat{P}.$

13. Prove that $P_{0z}^{(m)}$ is the same for all $z$ with $n = x + y$ fixed. Do the same for $\hat{P}_{0z}^{(m)}$.

14. Let $E = \{z \mid x + y \leq n_0\}$. Find $\lambda^E$ and $\hat{\lambda}^E.$

15. Show that

$$0N_{zz'} = \begin{cases} \left( \begin{array}{cc} x' - 1 \\ x - 1 \end{array} \right) \left( \begin{array}{cc} y' - 1 \\ y - 1 \end{array} \right) / \left( \begin{array}{c

Problems 23 to 26 develop some theoretical results for an ergodic chain in terms of the operator $K$.

23. Express $K$ in terms of $M$ and $\hat{M}$.

24. Prove that $M_{ij} = (K_{ij} - K_{jj})/\alpha_j$.

25. Show that $\hat{M}_{ij} - M_{ji} = k(\{i\}) - k(\{j\})$.

26. What happens to the formulas in Problems 24 and 25 if the reference point 0 is changed?

Problems 27 to 32 carry this development further for finite recurrent chains.

27. Show that $k(S) = M_{\alpha 0} = \hat{M}_{\alpha 0}$.

28. Prove that $K1 = k(S)1$ and $\alpha K = k(S)\alpha$.

29. Prove that $M\alpha^T = c1$, where $c = k(S) - \sum_i k(\{i\})\alpha_i$.

30. Prove that

$$K = \left( \frac{1}{k(S)} 1\alpha + P - I \right)^{-1}.$$

31. Prove that the set of charges is the same as the set of potentials.

32. To what extent do the results of Problems 27 to 31 generalize to strong ergodic chains?

Problems 33 to 39 are intended to illustrate Problems 23 to 32 for the Land of Oz example, which was defined in Chapter 4. [See also Chapter 6, Problem 1.] We choose the middle state (nice weather) to be the distinguished state 0.

33. Show that $P = \hat{P}$ (the chain is reversible).

34. Find $M$.

35. Find $K$, using the result of Problem 23.

36. Find $k(S)$, using the result of Problem 27.

37. Find $K$, using the result of Problem 30, and compare with the value of $K$ found in Problem 35.

38. Check the results given in Problems 24, 25, 28,

42. Let $P^*$ be the transition matrix of the modified chain watched in $B$. Prove that this is an ergodic chain.

43. Show that the requirement that $h$ have the specified normal derivatives can be written as $(I - P^*)h_B = d$, where $d$ has the given values $d_k$ as components.

44. Prove that $\alpha^*d = 0$ is a necessary condition for a solution to exist.

45. Show that $\alpha^*d = 0$ is also sufficient by showing that $d$ is a charge, that its potential will serve as $h_B$, and that the $h$ supplied by Problem 40 is a solution.

46. Prove that the most general solution differs from the given one only by a constant.

47. Prove that if the modified chain (indexed on all states) is a normal chain, then the most general solution is

$$h = -K \binom{d}{0} + c1.$$

48. Show that if the transient states are the lattice points in a bounded convex set in $n$-dimensional Euclidean space and if the process moves as a symmetric random walk which is stopped when it moves out of the convex set, then we can apply the previous results.

Problems 49 to 53 give a complete characterization of degenerate chains.

49. Prove that if $P$ is degenerate, so is $\hat{P}$.

50. Show that if $P$ is degenerate and if we let $i < j$ stand for $j\lambda_i = 1$, then $<$ is a simple ordering.

51. Prove that if $k < i < j$, then $jH_{ki} = 1$. Deduce from this fact that, in moving to the right, the process can move at most one step at a time. [Hint: Consider $\lambda^E$ for $E = \{k, i, j\}.$]

52. Prove that the ordering of states must be that of the integers, the positive integers, or the negative integers.

53. Show that the basic example and its reverse illustrate two of the possible orderings, and construct an example of the third.

1. Motivation for Martin boundary theory

For purposes of motivation it is convenient to think of the state space of a Markov chain $P$ with only transient states as being similar to the open unit disk of two-dimensional Euclidean space. In two-space the boundary of the disk—namely the circle $S^1$—has the property that there is a one-one correspondence between the non-negative harmonic functions $h(re^{i\theta})$ in the disk and the non-negative Borel measures $\mu^h$ on the circle. The correspondence is

$$h(re^{i\theta}) = \int_{S^1} P(re^{i\theta}, t) d\mu^h(t),$$

(*)

where $P(re^{i\theta}, t)$ is the Poisson kernel

$$\frac{1 - r^2}{1 - 2r \cos(\theta - t) + r^2}.$$

Transient boundary theory seeks an analogous representation theorem for all non-negative $P$-regular functions defined on the state space.

The first problem that arises is to find what the analogs of the circle (the boundary) and the kernel should be. We would like a representation

$$h(i) = \int K(i, x) d\mu^h(x).$$

In the case of the disk, a calculation with Green's identities shows that any kernel $P(re^{i\theta}, t)$ giving rise to the correspondence (*) and satisfying

$$\frac{1}{2\pi} \int_0^{2\pi} P(re^{i\theta}, t) dt = 1$$

must be the normal derivative at $t$ of the Green's function for the disk relative to the point $re^{i\theta}$. That is,

$$P(re^{i\theta}, t) = \left[ \frac{\partial}{\partial n} G(\cdot, re^{i\theta}) \right]_t.$$

Application of l'Hospital's rule shows that

$$\lim_{z \to t \text{ radially}} \frac{G(z, re^{i\theta})}{G(z, p)} = \left[ \frac{\partial}{\partial n} G(\cdot, re^{i\theta}) \right]_t = P(re^{i\theta}, t) / P(p, t),$$

where $p$ is any fixed reference point in the disk. Hence, except for the positive factor $P(p, t)$ which depends on $t$ but not on $re^{i\theta}$, the Poisson kernel is equal to

$$\lim_{z \to t \text{ radially}} \frac{G(z, re^{i\theta})}{G(z, p)}.$$

Therefore this last function may be used in the representation (*) in place of the Poisson kernel; the distinction between the kernels is just a normalizing factor (depending on $t$) which can be absorbed by changing the measures.

Two comments are in order. First, the limit in (**) need not be taken radially. Any method of approach of $z$ to $t$, as long as $z$ stays in the interior of the disk, will give the same value. Second, the considerations above apply equally well to any domain in $n$-dimensional space with a sufficiently smooth boundary. Although the explicit form of the kernel will vary from region to region, it will always be connected to the Green's function in the way we have just described.

R. S. Martin [1941] made use of these observations to define an ideal boundary for an arbitrary domain in Euclidean space. If the Green's function for the region is denoted $G(z, y)$, he noted that points $t$ on the ordinary topological boundary of the region did not necessarily have the property that

$$\lim_{z \to t} \frac{G(z, y)}{G(z, p)}$$

exists. He suggested that distinct ideal boundary points $

Doob [1959], taking advantage of the fact that the $N$-matrix for a transient Markov chain is the analog of the Green’s function (see Proposition 7-4), showed that Martin’s approach could be used to obtain a boundary for Markov chains. (We remark that $N_{ij}$ corresponds to $G(j, i)$ with the indices in the reversed order.) As the analog of Martin’s kernel he used limits on $j$ of expressions of the form $N_{ij}/N_{0j}$.

There is a minor restriction imposed by the Doob approach, namely that $N_{0j}$ is assumed non-zero for all $j$. For a more general chain in which it is not possible to get from state 0 to every other state, what Doob did was to consider only those states that could be reached from 0. We shall not follow him in this respect. We simply use limits of $N_{ij}/(\pi N)_j$ instead, where $\pi$ is a probability vector such that $\pi N$ is strictly positive. In terms of this kernel there is a natural space to try as the one corresponding to the closed unit disk. The space should consist of one point for each possible limit of $N_{ij}/N_{\pi j}$. Actually we shall find that this space is too large—that the space has to be cut down a bit for the representation to be unique. The price of uniqueness is that the cut-down space is not compact.

The introduction of $\pi$ in place of 0 itself leads to a problem. The representation will have to be restricted to $\pi$-integrable regular functions $h$, those for which $\pi h$ is finite. This requirement evaporated in Martin’s or Doob’s treatment because for them $\pi$ assigned unit mass to a point 0 and $h(0)$ was automatically finite.

Hunt [1960] gave a new approach to Martin boundary theory for Markov chains which was more probabilistic in nature than Doob’s. We follow Hunt’s probabilistic approach, except that we use a different metric and get a boundary which is more like Doob’s.

2. Extended chains

We begin by introducing the machinery which we shall use in later sections to develop Martin boundary theory for Markov chains. We are going to use a broader notion of Markov chain than we have been considering so far

First we must extend the concept of a stochastic process. The state space will be a denumerable set $S$ (with at least two elements) and two distinguished other states $a$ and $b$. The underlying set $\Omega$ of the measure space will consist of all doubly infinite sequences

$$\omega = (\ldots, c_{-2}, c_{-1}, c_0, c_1, c_2, \ldots)$$

such that

(1) $c_n \in S$ or $c_n = a$ or $c_n = b$.
(2) If $c_n = a$, then $c_m = a$ for all $m < n$.
(3) If $c_n = b$, then $c_m = b$ for all $m > n$.
(4) $c_n \in S$ for at least one $n$.

The interpretation of (2) and (3) is that state $a$ stands for “not yet started” and state $b$ stands for “stopped.” Thus (4) has the meaning that each path in $\Omega$ represents some nontrivial possibility for the process. We shall refer to $\Omega$ as a double sequence space.

We define the outcome functions $x_n$ as usual except that $n$ may be any integer. A basic cylinder set is any truth set in $\Omega$ of a statement of the form

$$x_m = c_m \wedge x_{m+1} = c_{m+1} \wedge \cdots \wedge x_n = c_n,$$

where at least one $c_i$ is an element of $S$. The field generated by the basic cylinder sets is denoted $\mathcal{F}$, and the smallest Borel field containing $\mathcal{F}$ is $\mathcal{G}$.
