---
role: proof
locale: en
of_concept: proposition-8-78
source_book: gtm040
source_chapter: "8"
source_section: "78"
---

**Proof:** Existence and uniqueness of the representation follows immediately from Theorem 5-10 and Propositions 8-75 and 8-77. Then $r_n = \lim_k M\left[h_{n+k} \mid \mathcal{R}_n\right]$ by Lemma 8-74. For the last part, let $(f_n, \mathcal{R}_n)$ be the charge of $(g_n, \mathcal{R}_n)$. Set

$$s_n = f_0 + \cdots + f_{n-1}$$

and

$$s = \lim s_n.$$

Then $s_n$ increases monotonically to $s$, and

$$M[s] \leq \sum_n M\left[f_n \mid \mathcal{R}_n\right] < \infty$$

by monotone convergence. Since $f_n \geq 0$,

$$g_n = \sum_k M\left[f_{n+k} \mid \mathcal{R}_n\right] = M\left[\sum_k f_{n+k} \mid \mathcal{R}_n\right]$$

Proof: Let $f \sim (\mathbf{f}_k, \mathcal{R}_n)$; $f$ is non-negative superregular. Let $E$ and $F$ be the sets of states in the space-time chain defined by

$$E = \{ \langle U, m \rangle \mid m \leq n \text{ and } \mathbf{f}_m(U) \leq r \}$$
$$F = \{ \langle U, m \rangle \mid m \leq n \text{ and } \mathbf{f}_m(U) \geq s \}.$$

Hence $f_i \leq r$ for $i \in E$ and $f_j \geq s$ for $j \in F$. For any other state, $i = \langle U, m \rangle$ with $m \leq n$, $r < f_i < s$. Now $h_0^F = (B^F 1)_0$ is the probability that the random variables $\mathbf{f}_0, \ldots, \mathbf{f}_n$ ever take on a value greater than or equal to $s$. Similarly, $(B^E B^F 1)_0$ is the probability of at least one upcrossing, and in general $[(B^E B^F)^k 1]_0$ is the probability of at least $k$ upcrossings by $\mathbf{f}_0, \mathbf{f}_1, \ldots, \mathbf{f}_n$. Hence

$$\mathrm{M}[\beta] = \sum_{k=1}^{\infty} \Pr[\beta \geq k] = \sum_{k=1}^{\infty} [(B^E B^F)^k 1]_0.$$

Since the chain cannot be in $F$ after time $n$, $F$ is an equilibrium set, and $h^F = B^F 1$ is a potential. For $i \in F$

$$(B^F 1)_i = 1 \leq \frac{1}{s} f_i.$$

By the Principle of Domination (Theorem 8-45),

$$(B^F 1) \leq \frac{1}{s} f$$

everywhere. Hence $B^E B^

10. Problems

1. If $P$ is a transient chain whose states communicate and if $\alpha > 0$ is superregular, show that
   (a) $\hat{P}$ stops (disappears) a.e. if and only if $\alpha$ is a potential measure.
   (b) The mean stopping time is finite if and only if $\alpha$ is a charge. [Hint: Adjoin an absorbing state to $\hat{P}$.]

2. Let $P$ be a recurrent chain, and let $E$ be a finite set. Show that for any specified values of $h_E$ there is a unique bounded function $h$ with the specified values which is regular on $\tilde{E}$. Show that $h$ takes on its maximum on $E$.

3. Illustrate the result of the previous problem for the symmetric random walk on the integers with the specified values $h_0 = 0$ and $h_1 = 1$.

4. Let $P$ have only transient states, let $\pi$ be a specified probability vector, and let $\alpha = \pi N$. Let $f \geq 0$ be a charge, and define the random variable

$$s = \sum_{n=0}^{\infty} f(x_n).$$

Show that $s$ is finite a.e. and that $M_\pi[s] = \alpha f$. What is the value of $M_i[s]$? Give a game-interpretation.

5. In the framework of Problem 4, introduce a second charge $\bar{f}$, its potential $\bar{g}$, and $\bar{s}$. Prove that if $\mu = \text{dual } f$, then

$$(g, \bar{g}) = \frac{1}{2} M_\pi[s s] + \frac{1}{2} \mu \bar{f}.$$

Find the corresponding expression for $I(g)$.

6. If $P$ is a chain with only transient states, let $\text{Var}_{ij}$ be the variance of $n_j$ for the process started at $i$. Show that

$$\text{Var}_{ij} = N_{ij} (2N_{jj} - N_{ij} - 1).$$

7. In the framework of Problem 6, if $P

13. Use Problems 9 and 11 to construct a counterexample to Theorem 8-45 if the assumption $h \geq 0$ is omitted.

14. If $\alpha_j = N_{0j}$, form $\hat{P}$ and compute $\hat{N}$.

15. For $E = \{0, 1, 2\}$, find $\bar{h}^E$. [See the end of Section 8.] Show that $v^E = N\bar{h}^E$ has the desired interpretation. [Remember that the chain starts at time 0, not at time 1.]

16. Show that $C(E) = 1$ for all equilibrium sets. Show that both the hypothesis and the conclusion of Proposition 8-39 are false for $P$.

17. Show that $\hat{C}(E) = 1$ for all sets $E$. Show that both the hypothesis and the conclusion of Proposition 8-39 hold for $\hat{P}$.

18. Let $E = \{0, 1, \ldots, n\}$. Find $B^E$. If $g$ is a potential, what is the form of its balayage potential on $E$? Show that Theorem 8-46 is satisfied.

19. Show that if $\mu = \text{dual } f$, then

$$I(g) = \frac{1}{2} \left( \sum_i \mu_i \right)^2 + \frac{1}{2} \sum_i \mu_i^2.$$

Problems 20 to 30 refer to sums of independent random variables on the integers with $p_{-1} = \frac{1}{3}$ and $p_1 = \frac{2}{3}$. Use the results of Problems 12 to 19 in Chapter 5.

20. Show that there are two essentially different positive regular measures and that all regular measures are linear combinations of the two basic measures.

21. Show that if $f \geq 0$ and $\alpha f < +\infty$ for either $\alpha$, then $g = Nf$ is finite-valued. Show also that $\lim P^n g = 0$.

22. Let $E = \{0,

CHAPTER 9

RECURRENT POTENTIAL THEORY

1. Potentials

Throughout this chapter $P$ is a recurrent chain which is either null or noncyclic ergodic. For such a chain, $\lim_n P^n$ always exists; we let $L = \lim P^n$.

In a recurrent chain the non-negative finite-valued superregular measures are uniquely determined up to multiplication by a constant, and the non-zero ones are positive and regular. We choose one such non-zero regular measure and call it $\alpha$.

If $P$ is noncyclic ergodic, then $L_{ij} = \alpha_j / \sum_k \alpha_k$; whereas if $P$ is null, then $L_{ij} = 0$. In either case, $L_{ik} - L_{ij}\alpha_k / \alpha_j = 0$.

Duality for $P$ is defined with respect to the regular measure $\alpha$. The dual $\hat{P}$ of a null chain is null, and the dual of a noncyclic ergodic chain is noncyclic ergodic. In general, if two results are duals, we shall prove only one of the pair. As usual, the key to the proof by duality of the second result is that $\hat{P}$ is the most general chain of the type we consider in this chapter.

As Definition 9-1 suggests, we define charges and potentials in the same way as in transient potential theory.

Definition 9-1: If $\mu$ is a signed measure with $\mu 1$ finite and if

$$\nu = \lim_n [\mu(I + P + \cdots + P^{n-1})]$$

exists and is finite-valued, then $\mu$ is called a left charge with potential measure $\nu$ and total charge $\mu 1$. If $f$ is a function with $\alpha f$ finite and if $g = \lim_n [(I + P + \cdots + P^{n-1})f]$ exists and is finite-valued, then $f$ is called a right charge with potential function $g$ and total charge $\alpha f$. The support of a charge is the set on which the charge is not zero; the support of a potential is the support of its charge.

The definition of the support of a potential is not justified until we prove a uniqueness theorem for the charge of a potential, but such a result will follow directly from conclusion (2) of Theorem 9-15.

We note that the dual of a left (right) charge for $P$ is a right (left) charge for $\hat{P}$ and that their total charges are the same (since the dual of a number is the same number).

Although we adopt the same definitions as with transient chains, the results are sometimes significantly different. For example, the only pure potential is the zero potential: If $f \geq 0$, then by monotone convergence $\lim_n [(I + P + \cdots + P^{n-1})f]_j = \sum_i N_{ij}f_j$, where $N_{ij} = +\infty$ for every $i$ and $j$. Thus the limit is finite-valued only if $f = 0$.

On the other hand, every row (or column) of $I - P$ is a charge, and the potential of the $i$th row (column) of $I - P$ is the $i$th row (column) of $I - L$. For if $\mu$ is the $i$th row of $I - P$, then $|\mu|1 \leq 2 < \infty$ and

$$\nu_j = \lim_n [\mu(I + P + \cdots + P^{n-1})]_j = \lim_n (I - P^n)_{ij}$$

$$= (I - L)_{ij};$$

the assertion for columns is dual.

Our first potential theory result will be that every charge has total charge zero. To prove this fact, we require the Doeblin Ratio Limit Theorem, Theorem 9-4. We recall that $H_{ij}^{(n)}$ is the probability starting in $i$ of reaching $j$ before or at time $n$ and that $N_{ij}^{(n)}$ is the mean number of times the process started at $i$ is in $j$ up to and including time $n$. Hence $H_{ij}^{(n)} = \sum_{k=0}^{n} F_{ij}^{(k)}$ and $N_{ij}^{(n)} = \sum_{

PROOF: If $i$ and $j$ communicate, then $i^2\bar{H}_{jj} < 1$, so that $i^2N_{jj} = 1/(1 - i^2\bar{H}_{jj}) < \infty$. It is clear that

$$N_{jj}^{(n)} - N_{ij}^{(n)} \geq 0$$

and that

$$N_{jj}^{(n)} \leq i^2N_{jj} + N_{ij}^{(n)},$$

and hence the first expression is non-negative and bounded by $i^2N_{jj} < \infty$. By duality, $N_{jj}^{(n)} - N_{ji}^{(n)}(\alpha_j/\alpha_i)$ is non-negative and bounded; if we multiply by $\alpha_i/\alpha_j$ and interchange $j$ and $i$, we obtain the second result.

Lemma 9-3: Let $P$ be any Markov chain with a positive superregular measure $\alpha$. If $i$ and $j$ communicate, then for all $n$

$$\frac{N_{ij}^{(n)}}{N_{jj}^{(n)}} \leq 1 \quad \text{and} \quad \frac{N_{ij}^{(n)}}{N_{it}^{(n)}} \leq \frac{\alpha_j}{\alpha_i},$$

and

$$\lim_n \frac{N_{ij}^{(n)}}{N_{jj}^{(n)}} = H_{ij} \quad \text{and} \quad \lim_n \frac{N_{ij}^{(n)}}{N_{ii}^{(n)}} = \frac{\alpha_j}{\alpha_i} \hat{H}_{ji} = i^2\bar{N}_{ij}.$$

PROOF: By Lemma 9-2,

$$0 \leq N_{jj}^{(n)} - N_{ij}^{(n)} \leq c \quad \text{for all } n.$$

Hence

$$0 \leq 1 - \frac{N_{ij}^{(n)}}{N_{jj}^{(n)}} \leq \frac{c}{N_{jj}^{(n)}}.$$

exists. If all four states are recurrent, the limit is $\alpha_j / \alpha_{j'}$. If the states are transient, the limit is

$$\frac{H_{ij} \hat{H}_{jj'} \alpha_j}{H_{i'j'} H_{j'j'} \alpha_{j'}}.$$

Remark: Since the states in question communicate, they must be either all recurrent or all transient.

Proof: Write

$$\frac{N_{ij}^{(n)}}{N_{i'j'}^{(n)}} = \left[ \frac{N_{i'j'}^{(n)}}{N_{j'j'}^{(n)}} \right]^{-1} \left[ \frac{N_{j'j'}^{(n)}}{N_{jj'}^{(n)}} \right]^{-1} \left[ \frac{N_{ij}^{(n)}}{N_{ij'}^{(n)}} \right],$$

and apply Lemma 9-3 to each factor.

Proposition 9-5: Every charge has total charge zero.

Proof: If $\mu$ is a left charge, then $\sum |\mu_k| < \infty$ and

$$\nu_j = \lim_n \sum_k \mu_k N_{kj}^{(n)}$$

is finite. Therefore

$$\sum_k \mu_k \left( \frac{N_{kj}^{(n)}}{N_{jj}^{(n)}} \right) \rightarrow 0.$$

Since by Lemma 9-3, $N_{kj}^{(n)}/N_{jj}^{(n)} \leq 1$, dominated convergence gives

$$0 = \lim \sum_k \mu_k \left( \frac{N_{kj}^{(n)}}{N_{jj}^{(n)}} \right) = \sum_k \mu_k \lim \left( \frac{N_{kj}^{(n)}}{N_{jj}^{(n)}} \right) = \sum \mu_k = \mu_1.$$

The result for functions is dual.

The condition that a function $f$ satisfy $\alpha f = 0$ is a strong necessary condition for it to be a charge, but it is by no means sufficient

PROOF: Let $\epsilon > 0$ be given. Choose $N$ sufficiently large that $\sum_{k>N} a_k < \epsilon/(4B)$ and pick $N'$ large enough so that for all $n \geq N'$

$$|b_n - b_{n-1}| \leq \frac{\epsilon}{2aN}.$$

Then for $n \geq N + N'$, we have

$$\left| \sum_{k=0}^{n} a_k (b_n - b_{n-k}) \right| \leq \sum_{k=0}^{N} a_k |b_n - b_{n-k}| + \sum_{k=N+1}^{n} a_k (|b_n| + |b_{n-k}|)$$

$$\leq \sum_{k=0}^{N} a_k \sum_{j=0}^{k-1} |b_{n-j} - b_{n-j-1}| + 2B \sum_{k=N+1}^{n} a_k$$

$$\leq \sum_{k=0}^{N} a_k \sum_{j=0}^{k-1} \frac{\epsilon}{2aN} + \frac{\epsilon}{4B} \cdot 2B,$$ since $n-j \geq N'$

$$\leq \frac{\epsilon}{2a} \sum_{k=0}^{N} a_k + \frac{\epsilon}{2}$$

$$\leq \epsilon.$$

Theorem 9-7: Let $i, j$, and $k$ be arbitrary states in a recurrent Markov chain which is either null or noncyclic ergodic. Then

$$\lim_{n \to \infty} \left[ (N_{kk}^{(n)} - N_{ik}^{(n)}) \alpha_j / \alpha_k + N_{ij}^{(n)} - N_{kj}^{(n)} \right] = k N_{ij}.$$

PROOF: We may assume that neither $i$ nor $j$ equals $k$, since otherwise both sides are clearly zero. We begin by establishing four equations:

(1) $$N_{kk}^{(n)} = \sum_{v=0}^{\infty} F_{ik}^{(v)} N_{kk}^{(n)}$$

(

Multiply (1) by $\alpha_j/\alpha_k$, (2) by $-\alpha_j/\alpha_k$, (3) by $-1$, and (4) by 1, and add. We obtain

$$\left(N_{kk}^{(n)} - N_{ik}^{(n)}\right)\alpha_j/\alpha_k + \left(N_{ij}^{(n)} - N_{kj}^{(n)}\right)$$

$$= kN_{ij}^{(n)} + \sum_{v=0}^{n} F_{ik}^{(v)} \left(b_n - b_{n-v}\right) + \sum_{v=n+1}^{\infty} F_{ik}^{(v)} b_n,$$

where $b_n = N_{kk}^{(n)}\alpha_j/\alpha_k - N_{kj}^{(n)}$, and $\{b_n\}$ is a bounded sequence by Lemma 9-2. The first term $kN_{ij}^{(n)}$ on the right side tends to $kN_{ij}$, and the third term tends to zero since $\{b_n\}$ is bounded and $\sum F_{ik}^{(v)}$ is finite. It is thus sufficient to show that

$$\lim_{n \to \infty} \sum_{v=0}^{n} a_v \left(b_n - b_{n-v}\right) = 0,$$

where $a_v = F_{ik}^{(v)}$. Since $a_n \geq 0$, $\sum a_n = 1$, and $\{b_n\}$ is bounded, we need show only that $(b_n - b_{n-1}) \to 0$ to apply Lemma 9-6. But

$$b_n - b_{n-1} = \left(N_{kk}^{(n)} - N_{kk}^{(n-1)}\right)\frac{\alpha_j}{\alpha_k} - \left(N_{kj}^{(n)} - N_{kj}^{(n-1)}\right)$$

$$= P_{kk}^{(n)}\frac{\alpha_j}{\alpha_k} - P_{kj}^{(n)}$$

$$\rightarrow L_{kk}\frac{\alpha_j}{\alpha_k} - L_{kj}$$

$$= 0.$$

Hence

$$iN_{jj} = 1 / (1 - i\bar{H}_{jj}) = 1 / j\bar{H}_{ji}.$$

Therefore, by Proposition 5-4 and Corollary 6-21,

$$\frac{jN_{ii}}{iN_{jj}} = j\bar{H}_{ji} jN_{ii} = j\bar{N}_{ji} = \frac{\alpha_i}{\alpha_j}.$$

Proof 2: Set $i = j$ in Theorem 9-7. Then

$$\lim \left[ (N_{kk}^{(n)} - N_{ik}^{(n)})\alpha_i + (N_{ii}^{(n)} - N_{ki}^{(n)})\alpha_k \right] = \alpha_k k N_{ii}.$$

Interchange $i$ and $k$, and the left side stays the same. The right side becomes $\alpha_i i N_{kk}$.

Lemma 9-9: For any states $i, j, k$ with $i \neq j$,

$$jN_{ki} + iN_{kj} \frac{\alpha_i}{\alpha_j} = jN_{ii}.$$

Proof:

$$jN_{ki} + iN_{kj} \frac{\alpha_i}{\alpha_j} = jH_{ki} jN_{ii} + iH_{kj} iN_{jj} \frac{\alpha_i}{\alpha_j}$$

$$= (jH_{ki} + iH_{kj}) jN_{ii} \text{ by Lemma 9-8}$$

$$= jN_{ii}.$$

Lemma 9-10:

$$\left| N_{ki}^{(n)} - N_{k0}^{(n)} \frac{\alpha_i}{\alpha_0} \right| \leq 0 N_{ii}.$$

Proof: If $i = 0$, both sides are zero. Otherwise we have

$$\hat{N}_{ik}^{(n)} \leq 0 \hat{N}_{ik} + \hat{N}_{0k}^{(n)}.$$

If we multiply through by $\alpha_i/\alpha_k$, we obtain

$$N_{ki

Therefore,

$$\left| N_{ki}^{(n)} - \frac{\alpha_i}{\alpha_0} N_{k0}^{(n)} \right| \leq 0 N_{ki} + i N_{k0} \frac{\alpha_i}{\alpha_0} = 0 N_{ii} \text{ by Lemma 9-9.}$$

As usual, we agree that $E N$, and in particular $0 N$, is a square matrix indexed by the set of all states; the entries of $E N$ on the rows or columns indexed by $E$ are all zeros.
