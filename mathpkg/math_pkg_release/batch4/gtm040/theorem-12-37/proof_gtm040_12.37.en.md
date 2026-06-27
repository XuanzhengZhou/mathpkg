---
role: proof
locale: en
of_concept: theorem-12-37
source_book: gtm040
source_chapter: "12"
source_section: "37"
---

Proof: Suppose $\mu \in \mathcal{E}_Q$, and let $k_n, n \in \mathbb{Z}$, be the states in the ratio limit representation of Theorem 12-37 for the functions $g_{(m,i)}$ and $h_{(m,i)}$. Since $S$ is finite, there is some state $j'' \in S$ and an infinite sequence $n'' \to \infty$ such that $k_{n''} \equiv j''$. Hence

$$h_{(m,i_m)} = c'' \frac{\lim_{n'' \to \infty} (Q^{n''} - m)_{i_m j''}}{\lim_{n'' \to \infty} (Q^{n''})_{0 j''}} = c'' \frac{\alpha_{j''}}{\alpha_{j''}} = c'',

by the convergence theorem for noncyclic ergodic chains. Thus $h$ is constant. Similarly, there is some $j'$ and sequence $n' \to -\infty$ with $k_{n'} \equiv j'$, whereby

$$g_{(m,i_m)} = c' \frac{\lim_{n' \to -\infty} (Q^{m-n'} )_{j' i_m}}{\lim_{n' \to -\infty} (Q^{-n'} )_{j' 0}} = c' \frac{\alpha_{i_m}}{\alpha_0} = c_0 \alpha_{i_m}.

It follows that $\pi_{n,j} \equiv \alpha_j$ and $P_{n,jk} \equiv Q

that $Q_1 = 1$. We remark next that $Q$ is ergodic, with regular measure $\alpha_i = e^{-1}/i!$, $i \in S$. In fact, $Q$ is $\alpha$-reversible;

$$\alpha_i Q_{ij} = e^{-3/2} \sum_{k=0}^{i \wedge j} \left[ \frac{\binom{i}{k}}{i!(j-k)!} \right] \left(\frac{1}{2}\right)^{i+j-k}$$

$$= e^{-3/2} \sum_{k=0}^{i \wedge j} \left[ \frac{\binom{j}{k}}{j!(i-k)!} \right] \left(\frac{1}{2}\right)^{i+j-k} = \alpha_j Q_{ji},$$

since the terms in square brackets agree for every $i, j$ and $k$. Thus $\mathcal{G}_Q$ contains the stationary Markov chain with $\pi_{n,i} = \alpha_i$ and $P_{n,ij} = Q_{ij}$ for every $n \in \mathbb{Z}$. In order to determine the other elements of $\mathcal{G}_Q$, we first compute the powers of $Q$. For this purpose it is convenient to introduce the generating functions $\gamma_i^n(s) = \sum_{j=0}^{\infty} (Q^n)_{ij} s^j (|s| \leq 1), i \in \mathbb{Z}$. We claim:

$$\gamma_i^n(s) = [1 - \left(\frac{1}{2}\right)^n (1-s)]^i \exp \left\{-[1 - \left(\frac{1}{2}\right)^n (1-s)]\right\}.$$

When $n = 0$ both sides are $s^i$; the result follows by induction from the following considerations. If we start with $i$ particles at time 0, and $S_n$ denotes the number at time $n + 1$, then $S_{n+1} = X + \sum_{i=1}^{S_n} Y_i$, where $X$ and the $Y_i$ are independent, $X$ Poisson with

and

$$\binom{k-n}{l}((\frac{1}{2})^{n+m})^l \rightarrow \frac{\theta^l(1/2)^{ml}}{l!}, l \geq 0.$$

Hence

$$\lim_{n \to \infty} (Q^{n+m})_{k-ni} = \sum_{l=0}^{i} \left[ \frac{\theta^l(1/2)^{lm}}{l!} e^{-\theta(1/2)m} \right] [e^{-1}/(i-l)!]$$

$$= e^{-(\theta(1/2)m+1)} \sum_{l=0}^{i} \binom{i}{l} [\theta(1/2)m]^l/i!$$

$$= e^{-(\theta(1/2)m+1)} (\theta(1/2)m+1)^i/i!.$$

We can take this last quantity to be $g_{(m,i)}$ by choosing $c' = e^{-(\theta+1)}$. On the other hand, if $\lim_{n \to \infty} k_{-n}/2^n$ does not exist then we must have $k_{-n}/2^n \to \infty$ as $n \to \infty$, for otherwise the defining ratios would converge to distinct limits along different subsequences. But the ratio $(Q^{n+1})_{k-ni}/(Q^n)_{k-n0}$, for example, is a sum of positive terms including

$$\left[ \frac{e^{-(1-(1/2)n+1)}}{e^{-(1-(1/2)n)}} \right] \left[ \frac{1-(\frac{1}{2})^{n+1}}{1-(\frac{1}{2})^n} \right]^{k-n} \frac{[1-(\frac{1}{2})^{n+1}]^i}{i!} \geq c_i \left(1+\frac{1}{2^{n+1}}\right)^{k-n}, c_i > 0,$$

and this last expression tends to $\infty$ as $n \to \infty$ if $k_{-n}/2

for a unique probability measure $\lambda$ on $\mathbb{R}_2^+$ such that $\lambda(\{(\theta, \eta) : \mu_{\theta n} \in \mathcal{E}_Q\}) = 1$. Evaluating both sides on $\{\omega \mid \omega_n = i, \omega_{n+1} = j\}$, we derive the equation

$$e^{-\bar{\theta}\eta} \left\{e^{-(\bar{\theta}(1/2)^n + 1)}(\bar{\theta}(\frac{1}{2})^n + 1)^{i}/i! \right\} \left\{e^{-(\bar{\eta}2^n + 1)}(\bar{\eta}2^n + 1)^{j}/j! \right\}$$

$$= \int_0^\infty \int_0^\infty e^{-\theta\eta} \left\{e^{-(\theta(1/2)^n + 1)}(\theta(\frac{1}{2})^n + 1)^{i}/i! \right\}$$

$$\times \left\{e^{-(\eta 2^n + 1)}(\eta 2^n + 1)^{j}/j! \right\} d\lambda(\theta, \eta).$$

Multiply both sides by $u^i v^j$ ($u, v \in \mathbb{R}$), sum over $i, j \in S$, and interchange summation and integration, to obtain

$$e^{-\bar{\theta}\eta} \left\{e^{-(\bar{\theta}(1/2)^n(1 - u)} \right\} \left\{e^{-\bar{\eta}2^n + 1(1 - v)} \right\}$$

$$= \int_0^\infty \int_0^\infty e^{-\theta\eta} \left\{e^{-(\theta(1/2)^n(1 - u)} \right\} \left\{e^{-\eta 2^n + 1(1 - v)} \right\} d\lambda(\theta, \eta).$$

If we make the change of variables: $x = (1 - u)/2^n$, $y = 2^{n+1}(1 - v

convex combination $\mu = \frac{1}{2}\mu_{00} + \frac{1}{2}\mu_{11}$. Clearly $\mu \in \mathcal{G}_Q$, and to see that $\mu$ is not the measure for a Markov process it suffices to check that

$$\Pr[x_2 = 0 \mid x_0 = 0 \land x_1 = 0] \neq \Pr[x_2 = 0 \mid x_1 = 0].$$

The $\pi_n$ and $P_n$ for $\mu_{11}$ satisfy $\pi_{0,0} = e^{-4}, \pi_{1,0} = e^{-9/2}, P_{0,00} = e^{-1}Q_{00}$ and $P_{1,00} = e^{-2}Q_{00}$. Thus

$$\Pr[x_2 = 0 \mid x_0 = 0 \land x_1 = 0] = \frac{\frac{1}{2}(e^{-1}Q_{00}Q_{00}) + \frac{1}{2}(e^{-4}e^{-1}Q_{00}e^{-2}Q_{00})}{\frac{1}{2}(e^{-1}Q_{00}) + \frac{1}{2}(e^{-4}e^{-1}Q_{00})} = \frac{1 + e^{-6}}{1 + e^{-4}}Q_{00},$$

while

$$\Pr[x_2 = 0 \mid x_1 = 0] = \frac{\frac{1}{2}(e^{-1}Q_{00}) + \frac{1}{2}(e^{-9/2}e^{-2}Q_{00})}{\frac{1}{2}e^{-1} + \frac{1}{2}e^{-9/2}} = \frac{1 + e^{-11/2}}{1 + e^{-7/2}}Q_{00}.$$

Hence $\{x_n\}$ has the two-sided Markov property, but not the one-sided Markov property.

We conclude this section by mentioning without proof the deepest result to date in the theory of denumerable Markov fields on $\

Example 12-43: Tree processes. $S = \{0, 1, \ldots, N\}$ and $T$ is a countable tree (i.e., $T$ is endowed with a neighbor structure $\partial$ which defines a connected graph with no loops). Let $P$ be a strictly positive $N$-state transition matrix with regular measure $\alpha$, and assume that $P$ is $\alpha$-reversible. The random field $\{x_t\}$ on $S^T$ is called a tree process for $(\alpha, P)$ if $\mu$ is defined by the following three properties:

(i) $\Pr[x_t = i] = \alpha_i$ for all $i \in S, t \in T$;

(ii) $\Pr[x_{t_0} = i_0 \land x_{t_1} = i_1 \land \cdots \land x_{t_l} = i_l] = \alpha_{t_0} P_{t_0 i_1} \cdots P_{t_l - 1 i_l}$ whenever $\{t_0, t_1, \ldots, t_l\}$ is a finite path in the tree $T$ and $i_0, i_1, \ldots, i_l \in S$;

(iii) $\Pr[x_{t_0} = i_0 \land \cdots \land x_{t_l} = i_l \mid x_{t_r} = i_r$ for all $r \in \Lambda]$

$$= \Pr[x_{t_0} = i_0 \land \cdots \land x_{t_l} = i_l \mid x_{t_0} = i_0]$$

for any finite $\Lambda \subset T$ and path $\{t_0, \ldots, t_l\} \subset T$ which intersect only at site $t_0$, and any $i_0, \ldots, i_l \in S$.

For given $\alpha$ and $Q$, conditions (i)–(iii) determine a well-defined and unique Markov field. According to (i) and (ii) the process behaves like a reversible Markov chain along paths (reversibility ensures that cylinder probabilities are independent of the direction we travel along a path

the likelihood of 1's near $t$ (and similarly for 0's). More precisely this implies that in Theorem 12-30 $\mu^{\kappa n}(\{x_i = 1\})$ is maximized when $\kappa^n$ consists of "all 1's" on $K(n)$. Using this fact it is possible to show that in the attractive case there is phase multiplicity for the potential corresponding to $(\alpha, P)$ if and only if $(p - q)^2 - 2(p + q) + 1 \geq 0$ and $(p, q) \neq (\frac{1}{4}, \frac{1}{4})$. The $(\alpha, P)$-process is repulsive when $p + q \geq 1$, and in this case one can prove by entirely different methods that phase multiplicity occurs if and only if $p + q > \frac{3}{2}$.

Random fields on countable trees $T$ have the advantage that most physically meaningful quantities can be computed explicitly; the fact that $T$ has no loops enables one to use inductive methods. The natural setting for statistical mechanics is $T = \mathbb{Z}^d$, however, and in this case the theory is immensely more difficult. We summarize some of the leading results for the simplest Markov fields on the two-dimensional integer lattice in our last example.

**Example 12-44: Two-dimensional Ising model.** $S = \{0, 1\}, T = \mathbb{Z}^2$. $V$ is a normalized potential of the form:

$$V_{\{a\}}(\iota) = v_0 \quad V_{\{a,b\}}(\iota) = v_1$$

whenever $|a - b| = 1$ and $i_a = i_b = 1$, with $V_A(\iota) = 0$ in all other cases. $V$ is attractive if $v_1 \geq 0$, repulsive otherwise; the intuitive interpretation is the same as in the previous example. When $V$ is attractive there is phase multiplicity if and only if $v_0 + 2v_1 = 0$ and $v_1 > 2 \ln(\sqrt{2} + 1)$.

a $K$-neighbor potential if $U_A = 0$ whenever $A$ contains two sites which are not $K$-neighbors. Show that $\{x_i\}$ is $K$-Markov if and only if the canonical potential $V$ for $\{x_i\}$ is $K$-neighbor. What does this say when $K = 0$? [Hint: Define a new neighbor system.]

4. Suppose that there is a metric $d$ defined on $T$, and say that $\{x_i\}$ is $L$-Markov ($L \geq 0$) if $\mu_a^A = \mu_a^{B(a,L)}$ whenever $B(a,L) = \{t \in T: d(a,t) \leq L\} \subset A \subset T$. What property for the canonical potential $V$ is equivalent to the $L$-Markov property for $\{x_i\}$? State and prove a theorem to justify your assertion. Describe the $\sqrt{2}$-Markov fields on $\mathbb{Z}^2$.

5. Show that if $\{x_i\}$ has any neighbor potential $U$, then $\{x_i\}$ is a Markov field. Give an example of a Markov field with potential $U$, such that $U$ is not a neighbor potential. [Hint: For the first part, look carefully at the proof of Theorem 12-16.]

6. Let $T = \mathbb{Z}$. Prove that $\mathcal{G}_Q = \varnothing$ if

$$\lim_{n \to \infty} \sup_{t,k \in S} \frac{(Q^n)_{ij}(Q^n)_{jk}}{(Q^{2n})_{ik}} = 0 \quad \text{for some } j \in S.$$

[Hint: Show that this condition forces $\Pr[x_0 = j] = 0$.]

7. Give an example of a Markov process $\{x_n\}_{n \in \mathbb{Z}}$ which is not extreme in its class of Markov fields. [Hint: Use the matrix $Q$ of Example 12-41.]

8. Let $S = \{0, 1, \ldots\}$, $T =

NOTES

Chapter 3:

Stochastic processes with the martingale property were first studied by Lévy [1937]. Lévy considered, in Sections 67 to 70, partial sums of sequences $\{f_n\}$ such that

$$M[f_{n+1} \mid f_0 \wedge \cdots \wedge f_n] = 0.$$

These are a natural generalization of sums of independent random variables with mean 0. He proved theorems such as a central limit theorem suggested by comparison with sums of independent random variables. Ville [1939] recognized the importance of studying processes representing a fair game and for which system theorems should hold. He called these processes martingales. Although he did not prove any convergence theorems, he did prove the inequality given in Problem 7. From this he was able to conclude that non-negative martingales had finite lim sup with probability one. He made application of this to the study of sample paths of coin tossing. In particular, he proved one half of the law of the iterated logarithm. The basic convergence theorem, Theorem 3-12, for martingales was proved by Doob [1940]. In his book on stochastic processes, Doob [1953] introduced submartingales (called semi-martingales in that book) and made a systematic study of the system theorems and convergence theorems for these processes. The proof of Proposition 3-11 for martingales is due to Doob [1940]. The proof given here and the extension to submartingales is due to Snell [1952]. Additional applications of martingale theory to Markov chains may be found in Lamperti [1960a] and [1963a].

Chapter 4:

Markov chains with a finite number of states were introduced by Markov [1907]. Kolmogorov [1936] considered the case of a denumerable number of states. Important contributions in the foundations of Markov chains were made by Doeblin [1938]. There are a number of books devoted to the study of finite Markov chains. Among these are Fréchet [1938

literature on branching processes. References to this literature as well as an account of the theory of these processes may be found in a book of Harris [1963]. The process called the basic example in this book is often referred to as a "renewal process."

The recognition of the need for and the importance of system theorems is due to Doob. See Doob [1953], Chapter VII. The strong Markov property which holds for any denumerable Markov chain does not hold for general Markov processes where time is allowed to be continuous and the state space is the real line. For a discussion of this problem in the more general setting, see Blumenthal [1957].

A discussion of system theorems and a rather systematic use of these theorems in Markov chain theory may also be found in Chung [1960].

Chapter 5:

Kemeny and Snell [1960], Chapter III, showed that the fundamental matrix $N$ could be used to obtain moments of many descriptive quantities for finite absorbing chains. The extension of this use of $N$ to denumerable chains was made in Kemeny and Snell [1961b]. Theorem 5-10 is the analog of the Riesz Decomposition Theorem for superregular functions. A systematic discussion of results of this type which exploit the analogy between superregular functions for a Markov chain and classical superharmonic functions may be found in Feller [1956] and Doob [1959]. The proof of Proposition 5-20 is due to Dynkin and Malyutov [1961].

Proposition 5-22 is true even if we drop the hypothesis of finitely many $k$-values. This theorem is due to Chung and Erdos [1951], and a simplified proof of this result was given by Chung and Ornstein [1962].

Chapter 6:

Theorem 6-9 is due to Derman [1954]. He proved existence by showing that $\alpha_j = i\bar{N}_{ij}$ is a regular measure. His proof of uniqueness is less elementary than ours and uses the Doeblin ratio theorem applied to the chain reversed by $\alpha$. This ratio theorem proved by Doeblin [1

identifying martingale and submartingale theory with the theory of harmonic and superharmonic functions. Important contributions again exploiting connections between Brownian motion and classical potential theory were made by Kac [1951]. The next major contribution was made by Hunt [1957], [1958]. Hunt showed that one could develop a potential theory for essentially the most general Markov process. He considers continuous time and abstract state space. He showed conversely that under rather minimal requirements for a potential theory one can construct a Markov process associated with this theory. His work related to the potential theory that goes with transient processes.

Although many of Hunt’s results go over easily to the Markov chain case, even for transient chains new problems arise, and a whole new theory must be developed for the recurrent case. These extensions were made by Kemeny and Snell [1961b] for general Markov chains and by Spitzer [1962] for the important class of Markov chains which arise from sums of lattice-valued independent random variables.

The fact that the symmetric random walk in one and two dimensions is recurrent, whereas in dimension three or greater it is transient was first proved by Polya [1921]. The proof of Proposition 7-10 was supplied by Lamperti.

Chapter 8:

The notion of $h$-regular function was introduced into the study of potential theory by Brelot [1956] and the corresponding idea of a function regular in the $h$-process for chains was discussed in Feller [1956] and Doob [1959].

A discussion of equilibrium potential, equilibrium charge, and capacity as they arise in electrostatics and Newtonian potential theory may be found in the book of Kellogg [1929]. A somewhat more modern approach may be found in Brelot [1959]. In the classical theory the Green’s function which plays the role of the matrix $N$ is always symmetric. The fact that there is an interesting potential theory even for nonsymmetric operators in probability was first shown by Hunt [1957], [1958].

The results of Sections 1 and 2 of this chapter were for the most part in Doob [1959]. Those of Sections 3 and 4 are special

The notion of energy seems to be significant only in the case of reversible chains and even here it does not have the nice probabilistic interpretations that the other potential theory concepts have.

The results of Section 8 are taken from Kemeny and Snell [1961b]. The idea of developing a potential theory for supermartingales was suggested by Doob [1961] where he also indicated the proof of Proposition 8-79.

Chapter 9:

The potential theory for recurrent chains discussed in this chapter was introduced by Kemeny and Snell [1961b].

The existence of the limit in Theorem 9-4 was first proved by Doeblin [1938]. The identification of the limit was made by Chung [1950]. The present proof is from Kemeny [1962].

Theorem 9-7 was proved under a mild assumption in Kemeny and Snell [1961b]. The case $i = j$ was proved in general by a method due to Chung in Chung [1961] and Kemeny and Snell [1961c]. The general case was proved by Kemeny [1963].

The fact that all ergodic chains are normal follows from Theorem 4, Chapter 1, Section 11 of Chung [1961]. The remaining results in the first three sections are taken primarily from Kemeny and Snell [1961b].

Proposition 9-65 was first proved by Lamperti [1960b]. Results of the form of Propositions 9-67 and 9-68 may be found in Chung [1960] Chapter 1, Section 11.

The notion of strong ergodic chains introduced here is new. The matrix $Z$ was introduced in Kemeny and Snell [1960]. It was shown in this book that the matrix $Z$ for finite ergodic chains could be used to express the moments of many interesting descriptive quantities and hence played for recurrent chains a role similar to the matrix $N$ for finite absorbing chains.

All sums of independent random variables processes which form aperiodic recurrent Markov chains are normal. This was proved by Kemeny and Snell [1961

detail supplied, except that we have used a slightly different definition of boundary than that listed by Hunt. The difference is as follows. Doob introduced a metric on the state space, the one we have used if $\pi$ assigns all its weight to one point, and completed the state space in terms of this metric. A point was called a boundary point by Doob in the completed space if it was a limit point of the original states. It is possible for one of the original states to be such a limit point. To avoid this peculiarity, Hunt modified Doob's metric slightly to make such a point into a new point. Since these new points are always nonminimal points and appear to play no essential role in the theory, we have followed Doob's metric. However, we have chosen to call the boundary simply the new points added by the completion. The observation that $\pi N > 0$ is the only condition on $\pi$ that is needed appears in Orey [1964].

One can also use G. Choquet's theory of convex cones to develop Martin boundary theory. This approach has been carried out by Neveu [1964]. See also Hennequin and Tortrat [1965].

Brelot [1956] showed that the Martin boundary was ideally suited to the study of the first boundary problem, or the Dirichlet problem. His approach was to generalize the method developed by Perron and Wiener (see Kellogg [1929]) for regions in Euclidean space.

The probabilistic approach to the first boundary problem was first suggested by Kakutani [1945] and done more generally using the Martin boundary by Doob [1958]. The method presented in this book is the probabilistic approach of Kakutani and Doob.

The discussion of fine boundary limits follows that of Doob [1957], who considered these problems for superharmonic functions using Brownian motion theory.

The Martin boundary has now been worked out for several important classes of Markov chains. In particular, Doob, Snell and Williamson [1960] have worked out the boundary for general sums of independent random variables. Related results may be found in Dynkin and Malyutov [1961]. There are close connections between classical moment problems and the Martin boundary for certain

Chapter 11:
