---
role: proof
locale: en
of_concept: theorem-2-9-jet-multiple-transversality
source_book: gtm033
source_chapter: "3"
source_section: "2. Transversality"
---

# Proof of Theorem 2.9: Jet Transversality to Multiple Submanifolds

**Theorem 2.9.** Let $A_0, \ldots, A_q$ be $C^\infty$ submanifolds of $J^r(M,N)$. If $1 \leqslant r < s \leqslant \infty$ then the set

$$\{f \in C^s(M,N) : j^r f \pitchfork A_k, \; k = 0, \ldots, q\}$$

is residual in $C^s_S(M,N)$.

*Proof.* By the Jet Transversality Theorem (Theorem 2.8), for each individual submanifold $A_k \subset J^r(M,N)$, the set

$$S_k = \{f \in C^s(M,N) : j^r f \pitchfork A_k\}$$

is residual in $C^s_S(M,N)$.

The intersection of finitely many residual sets is residual (a fundamental property of Baire spaces: the countable intersection of residual sets is residual):

$$\bigcap_{k=0}^{q} S_k = \{f \in C^s(M,N) : j^r f \pitchfork A_k, \; k = 0, \ldots, q\}$$

is residual in $C^s_S(M,N)$.

**Application.** As an illustration, consider the question of density of immersions in $C^2_S(M,N)$. Let $A_k \subset J^1(M,N)$ be the set of $1$-jets of rank $k$. Let $m = \dim M$, $n = \dim N$. Then $A_0, \ldots, A_{m-1}$ form a $C^\infty$ submanifold family (the sets of jets of submaximal rank). A map $f: M \to N$ is an immersion if and only if the image of $j^1 f$ misses $A_0 \cup \cdots \cup A_{m-1}$.

The set of $f \in C^2(M,N)$ such that $j^1 f$ is transverse to $A_0, \ldots, A_{m-1}$ is dense in $C^2_S(M,N)$. If, for $i = 0, \ldots, m-1$,

$$\dim A_i + \dim M < \dim J^1(M,N),$$

such transversality implies that $j^1 f$ misses $A_i$, hence $f$ is an immersion. Computing dimensions (assuming $m \leqslant n$):

$$\dim A_i \leqslant \dim A_{m-1} = 2m + mn - 1,$$
$$\dim J^1(M,N) = mn + m + n.$$

The inequality $\dim A_i + m < \dim J^1(M,N)$ becomes

$$(2m + mn - 1) + m < mn + m + n$$
$$\iff 3m - 1 < m + n$$
$$\iff 2m < n + 1$$
$$\iff n \geqslant 2m,$$

exactly the dimension condition for density of immersions.

QED
