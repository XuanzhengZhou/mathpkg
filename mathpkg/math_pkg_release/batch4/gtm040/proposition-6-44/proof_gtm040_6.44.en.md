---
role: proof
locale: en
of_concept: proposition-6-44
source_book: gtm040
source_chapter: "6"
source_section: "44"
---

**Proof:** We shall show that the functions $y_n$ satisfy the Markov property. Clearly, this needs to be checked only for $n \leq N$. If $\Pr[y_0 = c_0 \land \cdots \land y_{n-1} = c_{n-1}] > 0$, then

$$\Pr[y_n = c_n \mid y_0 = c_0 \land \cdots

which by the Markov property is

$$\Pr[x_{N-n} = c_n \wedge x_{N-n+1} = c_{n-1}] \cdot P_{c_{n-1}c_{n-2}} \cdot \dots \cdot P_{c_1c_0}.$$

The denominator similarly reduces to

$$\Pr[x_{N-n+1} = c_{n-1}] \cdot P_{c_{n-1}c_{n-2}} \cdot \dots \cdot P_{c_1c_0}.$$

Dividing, we obtain

$$\Pr[y_n = c_n \mid y_0 = c_0 \wedge \dots \wedge y_{n-1} = c_{n-1}]$$

$$= \frac{\Pr[x_{N-n} = c_n \wedge x_{N-n+1} = c_{n-1}]}{\Pr[x_{N-n+1} = c_{n-1}]}$$

$$= \Pr[x_{N-n} = c_n \mid x_{N-n+1} = c_{n-1}]$$

$$= \Pr[y_n = c_n \mid y_{n-1} = c_{n-1}].$$

It is not true in general that, if the original process is a Markov chain $P$, then the new process is also a Markov chain. Let $P$ be started with distribution $\pi$. We then have, if $\Pr[y_{n-1} = i] > 0,$

$$\Pr[y_n = j \mid y_{n-1} = i] = \Pr_\pi[x_{N-n} = j \mid x_{N-n+1} = i]$$

$$= \frac{\Pr_\pi[x_{N-n} = j \wedge x_{N-n+1} = i]}{\Pr_\pi[x_{N-n+1} = i]}$$

$$= \frac{(\pi P^{N-n})_j \cdot P_{ji}}{(\pi P^{N-n+1})_i}.$$

The last quantity on the right need not be independent of $n$. Nevertheless, if $P$ is ergodic, there is a case where we can state a positive result—a

9. Problems

1. Compute for the Land of Oz example $P^2$, $P^4$, and $P^8$. What is $A = \lim P^n$? Show that each row of $A$ is a regular measure and that each column is a regular function.

2. Let

$$P = \begin{pmatrix}
1 & 2 & 3 & 4 & 5 & 6 \\
\frac{1}{2} & 0 & 0 & \frac{1}{4} & \frac{1}{4} & 0 \\
0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & \frac{3}{5} & 0 & \frac{2}{5} & 0 \\
\frac{1}{2} & 0 & 0 & 0 & 0 & \frac{1}{2} \\
0 & 0 & \frac{3}{5} & 0 & \frac{2}{5} & 0 \\
0 & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} & \frac{1}{4} & 0
\end{pmatrix}.$$

The process is started in state 1. Find the probability of being in the various states in the long run.

3. In the basic example, let

$$p_i = \left( \frac{i}{i+1} \right)^2.$$

Is the chain transient, null, or ergodic?

4. Prove that $\alpha = 1^T$ is regular for any sums of independent random variables process. Give a careful statement as to the existence of transient, null, and ergodic examples.

5. Establish the following relationships between a chain with transition matrix $P$ and one with matrix $P^E$:

(a) If $P$ is transient, then $P^E$ is transient.

(b) If $P$ is recurrent, then $P^E$ is recurrent and $\alpha^E = c\alpha_E$.

(c) If $P$ is ergodic, then $P^E$ is ergodic, but the converse is not always true.

6. Prove that if a recurrent $P$ has column-s

If transient: Put into standard form, and find $N, B,$ and $a$.
If recurrent: Is it cyclic? Find $\alpha, M, \hat{P}, \hat{M}$.

12. Do the same for

$$P = \begin{pmatrix} 1 - c & c \\ 1 & 0 \end{pmatrix}, \quad 0 < c \leq 1.$$

13. Find $\alpha$ and $M$ for an independent trials process by the methods of this chapter, and check your answers by a direct computation. [See Problem 5 in Chapter 4.]

14. (a) Complete the work of finding $M$ for the basic example.
(b) Find the reverse of the basic example (when recurrent), and compute $M$ for this chain.

15. A light bulb in a fixture lasts $j$ time units with probability $f_j$. It is replaced with a similar bulb when it burns out. Assume that $\sum f_j = 1,$ $f_0 = 0,$ and $f_1 > 0$. Let $x_n$ be the length of time that the bulb in use at time $n$ has lasted (taken to be 0 if there is a replacement at time $n$). Show that $\{x_n\}$ is the set of outcome functions for a Markov chain and discuss the connection with the basic example. Show that the probability that a bulb is replaced at time $n$ tends to a limit as $n \to \infty$.

Problems 16 to 26 refer to sums of independent random variables on the circle. Mark $n$ ($n \geq 3$) points on a circle, labeled $i = 0, 1, \ldots, n - 1$ clockwise. The process either moves one step clockwise with probability $\frac{2}{3}$, or it moves one step counterclockwise with probability $\frac{1}{3}$.

16. Prove that the chain is ergodic. Is it cyclic?

17. Find a positive regular measure $\alpha$ with $\alpha = 1$. Interpret it.

18. Construct the reverse chain.

19. Compute $M$ by means of Theorem 6-43. [It is sufficient to find $

CHAPTER 7

INTRODUCTION TO POTENTIAL THEORY

1. Brownian motion

One of the fruitful achievements of probability theory in recent years has been the recognition that two seemingly unrelated theories in physics—one for Brownian motion and one for potentials—are mathematically equivalent. That is, the results of the two theories are in one-to-one correspondence and any proof of a result in one theory can be translated directly into a proof of the corresponding result in the other theory. In this chapter we shall sketch how this equivalence comes about, and we shall see that Brownian motion is a process which is like a Markov chain except that it does not have a denumerable state space and time does not proceed in discrete steps. The details of this equivalence can be found in Knapp [1965]. The important thing to notice will be that the definitions of potential-theoretic concepts in terms of Brownian motion do not depend on isolated specific properties of the process but depend only on the Markovian character of Brownian motion. In other words, there is reasonable hope of defining for an arbitrary Markov chain a potential theory in which analogs of the classical theorems hold.

We begin by describing Brownian motion. In 1826 the botanist Robert Brown observed that microscopic particles, when left alone in a liquid, are seen to move constantly in the fluid along erratic paths. Much later Albert Einstein investigated this movement of particles from a theoretical point of view. Einstein was able to derive statistical laws which estimate how a large number of particles spread over a period of time, and his predictions were verified.

In setting up a probabilistic model for this so-called Brownian motion, we simply replace Einstein’s estimate of what happens to a large number of particles by a probability for what happens to one particle. We are then to require that

$$\Pr[\text{particle started at } u \text{ is in } E \text{ at time } t] = \int_E \frac{1}{(2\pi t)^{3/2}} e^{-|u-y|^2/2t} dy,$$

where $E$ is a Borel set in three-dimensional (Euclidean) space $R^3$ and $|u - y|$ denotes the Euclidean distance from $u$ to $y$. If we use the notation $\Pr_u[x_t \in E]$ for the left side and the notation $p^t(u, E)$ for the right side, we have

$$\Pr_u[x_t \in E] = p^t(u, E).$$

By Theorem 1-41, $p^t(u, F)$ is a measure depending on $t$ and $u$ and defined on the smallest Borel field containing the open sets of $R^3$. Therefore, we may write

$$\Pr_u[x_t \in E] = \int_E p^t(u, dy).$$

The physical theory also makes us require that if $t_1 < t_2 < \cdots < t_n$, then $\{x_{t_1}, x_{t_2} - x_{t_1}, \ldots, x_{t_n} - x_{t_{n-1}}\}$ should behave like a set of independent random variables with $x_{t+s} - x_t$ having the same distribution as $x_s$. That is, we require that

$$\Pr_u[x_{t_1} \in E_1 \wedge \cdots \wedge (x_{t_n} - x_{t_{n-1}}) \in E_n]$$

$$= \Pr_u[x_{t_1} \in E_1] \cdot \cdots \cdot \Pr_u[x_{t_n} - x_{t_{n-1}} \in E_n]$$

$$= \Pr_u[x_{t_1} \in E_1] \cdot \cdots \cdot \Pr_u[x_{(t_n - t_{n-1})} \in E_n].$$

This identity implies that we must have

$$\Pr_u[x_q \in E \wedge x_r \in F \wedge \cdots \wedge x_s \in G \wedge x_t \in H]$$

$$= \int_E p^q(u, dw) \int_F p^{r-q}(w, dx) \int_H p^{t

The last equality (3a) implies and is implied by

(3b) $$\Pr_i[x_1 \in E \land x_2 \in F \land \cdots \land x_{n-1} \in G \land x_n \in H]$$
$$= \sum_{j \in E} P_{ij} \sum_{k \in F} P_{jk} \cdots \sum_{s \in H} P_{rs}.$$

It is easy to prove both the Markov property and the Markov chain property from (3a), and hence (1), (2), and (3b) give an equivalent definition of Markov chain. The analogous statements for Brownian motion are

(1') $$0 \leq \int_E p^t(u, dy) = \Pr_u[x_t \in E],$$

(2') $$\Pr_u[x_t \in R^3] = \int_{R^3} p^t(u, dy) = 1,$$

and

(3') $$\Pr_u[x_q \in E \land x_r \in F \land \cdots \land x_t \in H]$$
$$= \int_E p^q(u, dw) \int_F p^{r-q}(w, dx) \int \cdots \int_H p^{t-s}(y, dz).$$

As expected, these statements imply that the position of a particle at time $t + s$ depends only on $s$ and the particle's position at time $t$, and not on the value of $t$ or what happened to the particle before time $t$. (This assertion can be formulated precisely in terms of means of functions given a Borel field, which are a technical generalization of conditional means of functions given a partition.)

As with denumerable Markov chains we need not require that a Brownian motion particle be started deterministically at a state $u$. If we start the particle according to probabilities assigned by a measure $\mu$ on $R^3$, then we have

$$\Pr_\mu[x_t \in E] = \int_{R^3} \int_E \frac{1}{(2\pi t)^{3/2}} e^{-|u-y|^2/2t} dyd\mu(u)$$
