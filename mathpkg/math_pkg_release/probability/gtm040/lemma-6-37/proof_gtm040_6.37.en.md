---
role: proof
locale: en
of_concept: lemma-6-37
source_book: gtm040
source_chapter: "6"
source_section: "37"
---

**Proof:** Let $E = \{n \mid (\beta P^n)_s \leq (\gamma P^n)_s\}$ and $F = \{n \mid (\beta P^n)_s \geq (\gamma P^n)_s\}$. By Lemma 6-36, either

$$\Pr_{\beta}[x_n = s \text{ for infinitely many } n \in E] = 1$$

or

$$\Pr_{\gamma}[x_n = s \text{ for infinitely many } n \in F] = 1,$$

and by symmetry we may assume that the former alternative holds.

Let $h^{(n)}$ be the statement that $x_m = s$ for some $m \in E$ with $m < n$, and let

$$\beta_k^{(n)} = \Pr_{\beta}[x_n = k \land \sim h^{(n)}].$$

Then

$$\|\beta^{(n)}\| = \beta^{(n)}1 = \Pr_{\beta}[\sim h^{(n)}] \to 0$$

by the above assumption. Also

$$\beta^{(0)} = \beta$$

and

$$\beta_k^{(n+1)} = \begin{cases} \sum_j \beta_j^{(n)}P_{jk} & \text{if } n \notin E \\ \sum_{j \neq s} \beta_j

Next, we define

$$\gamma^{(n)} = \beta^{(n)} + (\gamma - \beta)P^n.$$

From this relation,

$$\gamma^{(n-1)}P = \beta^{(n-1)}P + (\gamma - \beta)P^n$$

and

$$\gamma^{(0)} = \gamma$$

and hence

$$\gamma^{(n+1)} = \gamma^{(n)}P + \beta^{(n+1)} - \beta^{(n)}P = (\gamma^{(n)} - \delta^{(n)})P.$$

We shall show by induction that $\gamma^{(n)} \geq \delta^{(n)}$. First, $\gamma^{(0)} = \gamma \geq 0$. If $0 \notin E$, then $\delta^{(0)} = 0 \leq \gamma^{(0)}$. If $0 \in E$, then $\gamma_s^{(0)} = \gamma_s \geq \beta_s = \beta_s^{(0)}$ by the definition of $E$, and $\beta_s^{(0)} = \delta_s^{(0)}$. Thus $\gamma^{(0)} \geq \delta^{(0)}$ in either case. Suppose $\gamma^{(n-1)} \geq \delta^{(n-1)}$. Then

$$\gamma^{(n)} = (\gamma^{(n-1)} - \delta^{(n-1)})P \geq 0.$$

If $n \notin E$, then $\delta^{(n)} = 0$ and $\gamma^{(n)} \geq \delta^{(n)}$. If $n \in E$, then $[(\gamma - \beta)P^n]_s \geq 0$ by the definition of $E$, and hence

$$\gamma_s^{(n)} \geq \beta_s^{(n)} = \delta_s^{(n)}$$

by the definition of $\gamma^{(n)}$. Thus $\gamma^{(n)} \geq \delta^{(n)}$ for every $n$.

In particular, we have $\gamma^{(n)} \geq 0$. Thus

$$\|\gamma^{(n)}\| = \gamma^{(n)}1$$

$$= \beta^{(n)}1 + [(\gamma - \beta)P^n]1$$

$$= \beta

Proof: Every recurrent chain is either ergodic or null; taking $\pi$ to be a vector with 1 in the $i$th entry and zeros elsewhere, we see that the existence of $\lim P^n$ follows from the other assertions of the theorem.

Let $P$ be ergodic and let $A = 1\alpha$ be the Cesaro limit of the powers of $P$. We have $\alpha P^n = \alpha$ for every $n$. Letting $\beta = \pi$ and $\gamma = \alpha$ in Lemma 6-37, we obtain the desired result.

Let $P$ be null and suppose the assertion of the theorem is false. Then by Corollary 1-64, for some probability vector $\pi$, there is an increasing sequence $\{n_k\}$ of positive integers and there is a row vector $\rho \neq 0$ such that

$$\lim_k (\pi P^{n_k})_i = \rho_i \text{ for every state } i.$$

Certainly $\rho_i \geq 0$. Summing on $i$, we obtain

$$\rho_1 = \sum_i \rho_i = \sum_i \lim_k (\pi P^{n_k})_i \leq \lim_k \sum_i (\pi P^{n_k})_i = 1,$$

the inequality following from Fatou's Theorem. Applying Lemma 6-37 with $\beta = \pi$ and $\gamma = \pi P$, we see that

$$\lim_k (\pi P^{n_k+1})_i = \rho_i \text{ for each } i.$$

By Fatou's Theorem,

$$\rho P = (\lim \pi P^{n_k})_P \leq \lim \pi P^{n_k+1} = \rho.$$

Hence $\rho$ is non-negative superregular and satisfies $\rho_1 < \infty$; $\rho$ must be regular by Proposition 6-4, and the fact that $P$ is null then contradicts Theorem 6-9.

Corollary 6-39: If $P$ is a null chain (not necessarily noncyclic), then $\lim P^n = 0.$

Proof: Let $P$ have

SECOND PROOF OF THEOREM 6-38: We first prove the theorem for the $i$th diagonal entry. Set $f_n = \bar{F}_{ii}^{(n)}$, $u_n = (P^n)_{ii}$, and

$$\mu = \sum_n nf_n = \sum_n n\bar{F}_{ii}^{(n)} = \sum_n n\Pr_i[\bar{t}_i = n] = M_i[\bar{t}_i] = \bar{M}_{ii}.$$

Lemmas 6-34 and 6-35 establish all the hypotheses of Theorem 1-67 except for the fact that $\sum_n f_n = 1$:

$$\sum_n f_n = \sum_n \bar{F}_{ii}^{(n)} = \bar{H}_{ii} = 1.$$

Therefore $u_n \to 1/\mu$ or 0 according as $\mu$ is finite or infinite, and the value of the limit for the diagonal entries follows from Proposition 6-25. For the off-diagonal entries, let $i$ and $j$ be any two distinct states. Define a row vector $\beta$ and a sequence of column vectors $\{g^{(n)}\}$ by

$$\beta_m = \bar{F}_{ij}^{(m)}$$

$$g^{(n)}_m = \begin{cases} (P^{n-m})_{jj} & \text{if } n \geq m \\ 0 & \text{if } n < m. \end{cases}$$

Then $\lim_n g^{(n)}_m = L_{jj}$ exists since we have proved the theorem for diagonal entries. Furthermore, by Lemma 6-34,

$$(P^n)_{ij} = \sum_{m=1}^n \beta_m(P^{n-m})_{jj}$$

$$= \sum_{m=1}^{\infty} \beta_m g^{(n)}_m$$

$$= \beta g^{(n)}.$$

Since $\beta 1 = 1$ and $g^{(n)} \leq 1$, the Dominated Convergence Theorem applies and

$$\lim_n (P^n)_{ij} = \lim_n \beta g

Proposition 6-40: If every noncyclic recurrent chain converges to a limiting matrix, then the Renewal Theorem holds.

Proof: Let the sequence $\{f_n\}$ be given. Define $r_i = \sum_{k>i} f_k$; the $r_i$ tend to 0 because $\sum_k f_k = 1$. As long as $r_i > 0$, define

$$p_{i+1} = \frac{r_{i+1}}{r_i} \quad \text{for } i = 0, 1, 2, \dots.$$

If $r_i = 0$ for some $i$, then $p_i = 0$ and the $p_k$ for $k > i$ are irrelevant. Set $q_i = 1 - p_i$ and let the $p_i$ and the $q_i$ represent the transition probabilities associated with the basic example. We have

$$\beta_i = p_1 p_2 \dots p_i = \frac{r_1}{r_0} \frac{r_2}{r_1} \dots \frac{r_i}{r_{i-1}} = r_i.$$

That is, $\beta_i = r_i$. Since $r_i \to 0$, $\beta_i \to 0$ and the chain is recurrent. Now

$$\bar{F}_{00}^{(n)} = \beta_{n-1}(1 - p_n)$$

$$= \beta_{n-1} - \beta_n$$

$$= \sum_{k>n-1} f_k - \sum_{k>n} f_k$$

$$= f_n.$$

Thus $\mu = \sum_n nf_n = \bar{M}_{00}$. By Lemma 6-34 we see that $u_n = P_{00}^{(n)}$. The Markov chain is noncyclic by Lemma 6-35 because the greatest common divisor of the $k$'s for which $f_k > 0$ is 1. Therefore $u_n = \lim P_{00}^{(n)}$ exists. On the other hand, by Proposition 6-25 the Cesaro limit of $P_{00}^{

Proof: Apply Theorem 4-11 with the random time equal to one. Then

$$M_i[\bar{t}_j] = \sum_k P_{ik} M_k[\bar{t}_j + 1]$$
$$= \sum_k P_{ik}(M_{kj} + 1)$$
$$= \sum_k P_{ik} M_{kj} + \sum_k P_{ik}$$
$$= (PM)_{ij} + 1.$$

For an ergodic chain $P$ we define $D$ to be the diagonal matrix whose diagonal entries are $1/\alpha_i$, where $\alpha_1 = 1$. From Proposition 6-25 we see that

$$\bar{M} = D + M.$$

Proposition 6-42: If $P$ is an ergodic chain, the mean first passage time matrix $M$ satisfies these properties:

(1) $M_{dg} = 0$ and $M \geq 0$.
(2) $M$ is finite-valued.
(3) $(I - P)M = E - D.$

Proof: The first statement is obvious, and the third follows immediately from Proposition 6-41 and the identity $\bar{M} = D + M$ if we can show that $M$ is finite-valued. The problem thus reduces to proving (2). We know that $M_{ii} = 0$; therefore let $i$ and $j$ be distinct states. We shall show that $M_{ij}$ is finite. Let $t = \min(\bar{t}_i, \bar{t}_j)$. Then

$$\frac{1}{\alpha_j} = \bar{M}_{jj} = M_j[\bar{t}_j]$$
$$\geq \Pr_j[x_t = i] M_j[\bar{t}_j \mid x_t = i]$$
$$\geq \Pr_j[x_t = i] M_{ij} \text{ by Theorem 4-11}$$
$$= {}^j\bar{H}_{ji} M_{ij}.$$

If we can show that ${}^j\bar{H}_{ji} > 0$, we will have

$$M_{ij}

Theorem 6-43—is also true. Thus once a candidate for $M$ has been found, even by guessing, we need check only that it satisfies (1), (2), and (3).

Theorem 6-43: If $P$ is an ergodic chain, the mean first passage time matrix $M$ is characterized by these properties:

(1) $M_{dg} = 0$ and $M \geq 0$.
(2) $M$ is finite valued.
(3) $(I - P)M = E - D$.

Proof: Proposition 6-42 shows that $M$ satisfies these properties. Let $Y$ be any matrix for which (1), (2), and (3) hold. Let 0 be an arbitrary fixed state of the chain. It is sufficient to show that $y$, the zeroth column of $Y$, is equal to $m$, the zeroth column of $M$. Forming the chain $^0P$, in which state 0 has been made absorbing, and writing

$$^0P = \begin{pmatrix} 1 & 0 & 0 & \ldots \\ \vdots & & Q & \end{pmatrix} \text{ and } y = \begin{pmatrix} y_0 \\ \bar{y} \end{pmatrix} \text{ and } m = \begin{pmatrix} m_0 \\ \bar{m} \end{pmatrix},$$

we see that $m = \{M_i[a]\}$ and by Corollary 5-17 that $\bar{m}$ is the minimum finite-valued non-negative solution of the equation $(I - Q)\bar{x} = 1$. We first show that $\bar{y}$ is another finite-valued non-negative solution. We know that $\bar{y}$ is finite-valued and non-negative by hypothesis. The identity $(I - P)Y = E - D$ yields in the zeroth column

$$\begin{pmatrix} 1 - P_{00} & \ldots \\ \vdots & I - Q \end{pmatrix} \begin{pmatrix} y_0 \\ \bar{y} \end{pmatrix} = \begin{pmatrix

A random walk on the non-negative integers is defined by the transition probabilities

$$P_{00} = q, \quad \text{where } q \neq 0 \text{ and } q \neq 1,$$

$$P_{i,i+1} = p = 1 - q \quad \text{for } i \geq 0$$

$$P_{i,i-1} = q \quad \text{for } i > 0.$$

We note that the process $P$ with 0 made absorbing is the infinite drunkard's walk $P'$. For the present chain we have

$$\bar{H}_{00} = pH_{10} + qH_{00} = pH_{10} + q.$$

But $H_{10}$ is the absorption probability $B_{10}$ for the infinite drunkard's walk. And $B_{10} = 1$ if $p \leq q$, and $B_{10} < 1$ if $p > q$. Therefore

$$\bar{H}_{00} \begin{cases} = 1 & \text{if } p \leq q \\ < 1 & \text{if } p > q, \end{cases}$$

and $P$ is recurrent if and only if $p \leq q$.

A similar relation holds for $\bar{M}_{00}$; we have

$$\bar{M}_{00} = 1 + pM_{10} + qM_{00} = 1 + pM_{10}.$$

Since $M_{10}$ is the mean time to absorption $M_1[\mathbf{a}]$ in the $P'$ chain, we see that $\bar{M}_{00}$ is finite if and only if $p < q$. That is,

$$P \text{ is } \begin{cases} \text{transient} & \text{if } p > q \\ \text{null} & \text{if } p = q \\ \text{ergodic} & \text{if } p < q. \end{cases}$$

The chain is never cyclic, since $P_{00} > 0$.

We shall compute $M$ for the ergod

The entries $M_{i0}$ of the mean first passage time matrix are easily found once the value of $\alpha_0$ is known. Letting $m$ be the zeroth column of the $M$ matrix, we see from Proposition 6-42 that

$$ (I - P)m = 1 - \{\delta_{i0} / \alpha_0 \} $$

or that

$$ m_0 - qm_0 - pm_1 = 1 - 1 / \alpha_0 $$

and

$$ m_i - qm_{i-1} - pm_{i+1} = 1 \quad \text{for } i > 0. $$

Since $\alpha_0 = 1 - p / q$, we have $1 - 1 / \alpha_0 = -p / (q - p)$. The fact that $m_0 = 0$ then reduces the first relation to

$$ -pm_1 = -p / (q - p), $$

so that

$$ m_1 = 1 / (q - p). $$

The difference equation for $m_i$ has as a general solution

$$ m_i = A + B(q / p)^i + i / (q - p) \quad \text{for } i \geq 0. $$

The boundary conditions on $m_0$ and $m_1$ imply that $A = B = 0$ and that

$$ M_{i0} = i / (q - p). $$

The computation of $M_{0i}$ uses the same general methods. First, we note that if $i < j$, then the process must pass through $i$ from 0 to get to $j$. Hence

$$ M_{0i} + M_{ij} = M_{0j} $$

or

$$ M_{ij} = M_{0j} - M_{0i}. $$

Now

$$ M_{01} = p + q(1 + M_{01}) $$

so that

$$ M_{01} = 1 / p. $$

For $0 < i < j$,

$$ M_{ij} = p(1 + M_{i+1,j}) + q(1 + M_{i-1,j}) $$

or

$$ M_{0j} - M_{0

Solving this equation and using the relations $M_{00} = 0$ and $M_{01} = 1/p$, we find

$$M_{0i} = \frac{q}{(q - p)^2} (r^i - 1) - \frac{i}{q - p}.$$

Algebraic manipulation yields the alternate formula

$$M_{0i} = \frac{1}{p} \sum_{k=0}^{i-1} r^k (i - k).$$

Since $M_{i0} = M_{ij} + M_{j0}$ when $i > j$ and since $M_{0i} + M_{ij} = M_{0j}$ when $i < j$, we may summarize our results as follows:

$$M_{ij} = \begin{cases} \frac{i - j}{q - p} & \text{if } i \geq j \\ \frac{q}{(q - p)^2} (r^j - r^i) - \frac{j - i}{q - p} & \text{if } i \leq j. \end{cases}$$

**EXAMPLE 2: Basic Example.**

The vector $\beta$ defined for the basic example has the property that $\beta P = \beta$ if and only if $\lim_{i \to \infty} \beta_i = 0$. Furthermore, $P$ is recurrent if and only if $\lim_{i \to \infty} \beta_i = 0$. When $P$ is recurrent, it is null if $\sum_i \beta_i$ is infinite and ergodic if $\sum_i \beta_i$ is finite. In the ergodic case the regular measure $\alpha$ for which $\alpha = 1$ has entries

$$\alpha_i = \frac{\beta_i}{\sum_i \beta_i}.$$

Entries $M_{ij}$ of the mean first passage time matrix for the basic example satisfy the equations

$$M_{0i} + M_{ij} = M_{0j} \quad \text{for } i < j$$

and

$$M_{ij} = M_{i0} + M_{0j} \quad \text{for } i > j.$$

Since

$$M_{i0} + M_{0i

Solving this equation with the aid of the relation $\beta_k q_{k+1} = \beta_k - \beta_{k+1}$, we obtain

$$M_{0i} = \frac{1}{\beta_i} \sum_{k < i} \beta_k.$$

Therefore, for $i > 0$,

$$M_{i0} = \frac{1}{\beta_i} \sum_{k \ge i} \beta_k.$$

The general entries may be computed from

$$M_{ij} = M_{0j} - M_{0i} \quad \text{if } i < j$$

$$M_{ij} = M_{i0} + M_{0j} \quad \text{if } i > j.$$

8. Reverse Markov chains

Let $\{x_n\}$ be the outcome functions for a denumerable Markov process defined on a space $\Omega$ and with range in $S$. The outcome functions appear in a certain order and represent the forward passage of time. One may well wonder, however, if, when the functions are looked at in reverse order, the process is in any sense still Markovian. It is the purpose of this section to discuss this question; as a by-product of the discussion, we shall gain an interpretation for the dual of an ergodic Markov chain.

The sense in which a Markov process reversed in time is still a Markov process is the following.
