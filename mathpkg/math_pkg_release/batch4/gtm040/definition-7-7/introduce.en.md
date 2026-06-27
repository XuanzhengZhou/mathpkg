---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Any column vector $f$ with $\alpha f$ well defined and finite for which the limit

$$g = \lim_{n \to \infty} [(I + P + \cdots + P^n)f]$$

exists and is finite-valued is called a right charge with potential function $g$.

From our knowledge of what happens with Brownian motion, we should expect that the Markov chain potential operators will arise in different ways in the transient and recurrent cases. Consequently, we shall treat the different kinds of processes separately, handling the transient case in Chapter 8 and the recurrent case in Chapter 9.

In the transient case of Brownian motion the operator was formally

$$\lim_{t \to 0} P^t dt = \int_{0}^{\infty} P^t dt,

Proposition 7-5, is that for any charge of total charge zero on which the potential operator is defined the potential operator should agree with the operator which is formally

$$\lim \int_0^T P^t dt.$$

It will turn out that there are many possible potential operators for left charges and many others for right charges. Of these the matrices $-C$ and $-G$, respectively, will be representative (see Definition 9-24). But if we ask that the same matrix work for both left and right charges, then we shall see that there is a matrix $K$ such that all such potential operators are of the form $-K + c1\alpha$, where $c$ is a constant (see Theorem 9-84). With $-K$ as our operator, we have some hope of imitating classical potential theory if we redefine charge and potential in terms of $K$: The column vector $f$ is a charge, for instance, with potential $g$ if

$$g = -Kf.$$

From this new definition of charges and potentials, we shall be able, just as in the transient case, to prove theorems which are analogs of some of the main results of classical potential theory.

In discussing the relation of Brownian motion to potential theory in Section 3, we mentioned that the operator inverse to $-A$, where

$$Af = \lim_{t \to 0} \frac{1}{t} (Q^t f - f),$$

was of the same form as the potential operator. It is thus quite believable that $-A$ should be essentially the inverse operator that transforms potentials into charges. Now the definition of $A$ involves a derivative, and when concepts in Brownian motion are translated into concepts in Markov chains, derivatives transform into differences. Therefore, the proper analog of $Af$ for Markov chains is $Pf - f = (P - I)f$. That is, $I - P$ plays the role of $-A$. In Theorems 8-4 and 9-15 we shall see that $I - P$ is indeed the operator that transforms potentials in the sense of Definitions 7-6 and 7-7 into charges.

With Brownian motion the operator $A$ is a constant multiple of the Laplacian operator $\Delta$

behavior for Markov chains that harmonic functions have classically. As an example, a function harmonic on a connected open set in $R^n$ cannot assume its maximum value inside that open set unless the function is constant. We shall see in Corollary 8-44 that an analogous result holds for Markov chains.

A twice continuously differentiable function $f$ is said to be superharmonic if $\Delta f \leq 0$. The analog of this property is the condition that $(P - I)f \leq 0$ or $f \geq Pf$. Thus the analog of a superharmonic function is a superregular function.

Table 7-2. Markov Chain Analogs of Potential Theory Concepts

| Classical Notion | Markov Chain Analog |
| :--- | :--- |
| $R^n$ | State space $S$ |
| $P^t$ and $Q^t$ | $P^n$ |
| Lebesgue measure | $\alpha$ |
| Potential | $\lim \mu(I + P + \cdots + P^n)$ or $\lim (I + P + \cdots + P^n)f$ |
| Total charge | $\mu1$ or $\alpha f$ |
| Potential operator | Transient: $N$ |
| Inverse operator | Recurrent: $-K$ |
| Harmonic function | $I - P$ |
| Superharmonic function | Regular function |
| Connected set | Superregular function |
| Communicating set |

6. Brownian motion as a limit of the symmetric random walk

The symmetric random walk in $n$ dimensions was defined in Chapter 4 as a Markov chain obtained from sums of independent random variables on the integer lattice in $R^n$ with the probability of going from any state to any of the $2n$ neighboring states equal to $1/(2n)$. In potential theory for Markov chains this process assumes the role of the “classical case,” exhibiting in its potential theory much of the special behavior of the theory in Section 2. For instance, the matrix of the potential operator for this process has the same asymptotic behavior at infinity as the potential kernel has classically: $\log |x|$ in two dimensions, $1/|x|$ in three dimensions, and so on.

The reason

that ball after time $t$. We shall prove this result only in the one-dimensional case, and we make use of the Central Limit Theorem (Theorem 1-68).

Consider for fixed $k$ the random walk on the line having as states the points of the form $j2^{-k}$, for $j$ any integer, and having transition probabilities $\frac{1}{2}$ from any state to each of its two neighbors. This process is the symmetric random walk with a change in scale. Let $x_n^{(k)}$ be the $n$th outcome function, and let $x_0^{(k)} = 0$. As in Section 1, we let $x_t$ denote the position in Brownian motion.
