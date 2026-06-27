---
role: proof
locale: en
of_concept: lemma-11-10
source_book: gtm040
source_chapter: "11"
source_section: "10"
---

**Proof:** It suffices to consider the function $B^E_j$ where $E$ is a finite set. If $E \

Proof: By Proposition 11-9, the functions $B^{E_k}(x, \cdot)h$ converge pointwise to $h(x)$. Thus by dominated convergence their integrals against any Borel measure on $*S$ converge to the integral of $h$. That is, the functions converge to $h$ weakly. Thus $h$ is in the weak closure of the set $\{B^{E_k}(x, \cdot)h\}$, is certainly in the weak closure of the convex hull of the set, and must therefore be in the strong closure of the convex hull of the set. (See Dunford and Schwartz [1958], p. 422, Corollary 14.)

Proposition 11-12: The set of $T$-continuous functions is exactly the uniform closure of the set of elementary continuous functions.

Proof: Every $T$-continuous function is contained in the uniform closure according to Lemma 11-11, since $B^{E_k}(x, j)$ vanishes unless $j$ is in $E_k$. Conversely, every elementary continuous function is $T$-continuous by Lemma 11-10, and the uniform limit of $T$-continuous functions is $T$-continuous, since $T$ has norm no greater than one.

5. Normal chains and convergence to the boundary

As an application of the machinery of Section 4, we can prove the second convergence theorem—that each row of $P^n$ converges weak-star to the harmonic measure $\beta$ in a suitable class of normal chains. This result was suggested in the discussion in Section 1, and it was pointed out that the key to the proof should be a certain interchange of limits. In fact, this interchange has already taken place and is concealed in the proof of Lemma 11-11.

We begin with a particularly sharp form of the convergence theorem.

Theorem 11-13: If $P$ is normal, if $i$ is any state in $S$, and if $h$ is $T$-continuous, then

$$\lim_n (P^n h)_i = \int_*S h(x)d\beta(x).$$

Conversely, if this equation holds for

it contains only those sets $\{E_k\}$ with $k \geq k_0$. Since $h$ is $T$-continuous, we can apply Lemma 11-11 to the truncated sequence to obtain a convex combination of the functions $B^{E_k}(x, \cdot)h$ which is uniformly within $\epsilon$ of $h$. If, say,

$$\|\sum c_j B^{E_j}h - h\| < \epsilon,$$

then also

$$\left| P_i^n \left( \sum c_j B^{E_j}h - h \right) \right| < \epsilon$$

since $P^n = 1$ and $P^n \geq 0$. Consequently,

$$\left| \int h(x) d\beta(x) - (P^n h)_i \right| \leq \left| \int h(x) d\beta(x) - \sum c_j \lambda^{E_j}h \right|$$

$$+ \left| \sum c_j \left( \lambda^{E_j} - P_i^n B^{E_j} \right) h \right|$$

$$+ \left| P_i^n \left( \sum c_j B^{E_j}h - h \right) \right|$$

$$< 2\epsilon + \left| \sum c_j \left( \lambda^{E_j} - P_i^n B^{E_j} \right) h \right|.$$

The sum on the right is a finite sum and in each summand only finitely many entries of $\lambda^{E_j} - P_i^n B^{E_j}$ can be non-zero. Since $P_i^n B^{E_j} \rightarrow \lambda^{E_j}$ pointwise, we conclude that the sum on the right side is less than $\epsilon$ for $n$ sufficiently large.

The converse follows by applying the assumption to columns of $B^E$ for two-point sets $E$.

The convergence theorem is as follows.
