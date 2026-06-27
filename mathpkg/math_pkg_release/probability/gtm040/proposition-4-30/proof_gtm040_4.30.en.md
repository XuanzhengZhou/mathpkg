---
role: proof
locale: en
of_concept: proposition-4-30
source_book: gtm040
source_chapter: "4"
source_section: "30"
---

**Proof:** Let the states be the first $n$ positive integers, and suppose the class is transient. Then $N_{ij}$ is finite for every $i$ and $j$ in the class. Therefore

$$c = M_i \left[ \sum_{j=1}^{n} n_j \right] = \sum_{j=1}^{n} N_{ij}$$

is finite. But $c$ is the mean total number of steps taken in the class, and $c$ is infinite because the class is closed. This contradiction establishes the proposition.

To see that infinite closed equivalence classes need not be recurrent, we consider the basic example, whose states form a single equivalence class. Let $\bar{H}_{00}^{(n)}$ be the probability that the chain, started

since a single step other than away from zero returns the process to zero at once. Now in order for the process to be recurrent it is necessary and sufficient that $\bar{H}_{00} = 1$ or that

$$\lim_{n} \beta_n = \lim_{n} (1 - \bar{H}_{00}^{(n)}) = 0.$$

The reader should be able to construct examples where $\lim_{n} \beta_n = 0$ and where $\lim_{n} \beta_n \neq 0$. Thus the basic example may be either transient or recurrent.

8. Problems

1. Find an expression analogous to that in Proposition 4-3 for $\Pr_i[x_n = j]$ in a Markov process.

2. Let $p_m$ be the Poisson distribution with mean $m$ on the non-negative integers. A game is played as follows: A random integer $n_1$ is selected with probabilities determined by $p_1$. A second random integer $n_2$ is selected with probabilities determined by $p_{n_1}$. The $i$th random integer is selected with probabilities determined by $p_{n_i-1}$. Prove that with probability one the integer 0 is eventually selected.

3. Show that if $h \geq 0$ is a column vector for which $P^n h$ converges, then the limit function is non-negative superregular.

4. Let $j$ be an absorbing state. Prove that the probability starting at $i$ of ever reaching $j$ is a regular function.

5. Show that an independent trials process is a Markov chain in which $P_{ij}$ is independent of $i$. Let 0 be any fixed state and let $t$ be any stopping time. Show that $\Pr_n[x_{t+1} = j] = P_{0j}$, and give an example to show that $\Pr_n[x_t = j]$ does not have to equal $P_{0j}$.

6. If the symmetric random walk in 3 dimensions is started at the origin, the probability of being at the origin after $n$ steps is 0 if $n$ is odd and is of the order of magnitude of $n^{-3/2}$ for $n$ even. Prove that the probability of

12. Let
$$\beta_i = p_0 p_1 \ldots p_{i-1}, \quad \gamma_i = q_1 q_2 \ldots q_i, \quad \alpha_i = c \beta_i / \gamma_i.$$
Show that, for any choice of the constant $c$, $\alpha$ is a regular measure.

13. Show that all regular measures are of the form given in the previous problem.

14. Show that $\alpha_j P_{ji} / \alpha_i = P_{ij}$ for all $i$ and $j$.

Problems 15 to 18 refer to a branching process and use the notation of Sections 2 and 3 of the text.

15. Show that the roots of the equation $\varphi(r) = r$ satisfy the following conditions:
(a) There is an $r < 1$ if $m > 1$.
(b) There is an $r > 1$ if $m < 1$.
(c) $r = 1$ is the only root if $m = 1$.

16. Show that $\{r^{x_n}\}$ is a martingale if and only if $\varphi(r) = r$.

17. Show that $\{x_n\}$ is a martingale if and only if $m = 1$.

18. What condition on $m$ will assure that the branching process has positive probability of survival (of not dying out)?

Problems 19 to 24 concern space-time processes and martingales. If $P$ is a Markov chain with state space $S$, we define the space-time process to be a Markov chain whose states are pairs $(i, n)$, where $i$ is in $S$ and $n$ is a non-negative integer, and which moves from $(i, n)$ to $(j, n + 1)$ with probability $P_{ij}$.

19. Prove that any space-time process is transient. What can be said about classification of states?

20. Prove that if $f(i, n)$ is a finite-valued non-negative regular function for the space-time process, then $f(x_n, n)$ is a martingale for the process $P$ started at a given state 0.

21. Special

1. Properties of transient chains

Recall that a transient Markov chain is a Markov chain all of whose recurrent states are absorbing. Its transition matrix satisfies $P_1 \leq 1$. For any transient state $j$ in the chain, we have seen that $\bar{H}_{jj} < 1$ and $N_{ij} < +\infty$ for every $i$. If $E$ is any set of states, we can put the transition matrix in the canonical form

$$P = \begin{pmatrix} E & \tilde{E} \\ E & \tilde{E} \end{pmatrix} \begin{pmatrix} T & U \\ R & Q \end{pmatrix}.$$

In the special case in which $P$ is a transient chain and $E$ is the set of absorbing states, we find that $T = I$ and $U = 0$. (If there are no absorbing states, we agree to write $P = Q$. We shall assume that not all states are absorbing, however.) Thus, for a transient chain,

$$P = \begin{pmatrix} I & 0 \\ R & Q \end{pmatrix}.$$

The matrices $R$ and $Q$ for a transient chain will always be associated with this standard decomposition. We observe that $Q$ itself is the transition matrix for a transient chain and that this chain has only transient states. Some authors actually define a transient chain to be one with all states transient. However, in the study of these chains, it is often convenient to add absorbing states to ensure $P_1 = 1$. And as we saw in Chapter 4, the decomposition of general Markov chains into transient and recurrent chains depends on allowing absorbing states in transient chains. For these reasons we have adopted the slightly more general definition of transient chain which permits absorbing states.

Let $P$ be the transition matrix of a transient chain, and consider the quantity $N_{ij}$, the mean number of times in state $j$ when the process is

started in state $i$. If $j$ is an absorbing state, then this quantity is infinite if $j$ can be reached from $i$ with positive probability and 0 otherwise. If $i$ is absorbing, it is 0 unless $i = j$, and then it is infinite. Hence $N_{ij}$ is of interest only when $i$ and $j$ are transient. Thus we shall agree to restrict $N$ to these entries: The matrix so restricted is called the fundamental matrix for the chain. We shall show that the restricted matrix is the matrix $\{N_{ij}\}$ for the chain determined by $Q$. In what follows, $N$ always denotes the restricted matrix associated with $P$.
