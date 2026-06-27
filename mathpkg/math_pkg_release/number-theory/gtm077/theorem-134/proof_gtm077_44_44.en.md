---
role: proof
locale: en
of_concept: theorem-134
source_book: gtm077
source_chapter: "VII"
source_section: "Summary and the System of Ideal Classes"
---
# Proof of Theorem 134

**Theorem 134.** Let $d$ be the product of two distinct primes $q_1 \equiv q_2 \equiv 3 \pmod{4}$. Then in $k(\sqrt{d})$ the norm of the fundamental unit equals $+1$, and consequently $h_0 = 2h$. Moreover, each of the primes $q_1, q_2$ is the norm of some integer in $k(\sqrt{d})$.

*Proof.* By Theorem 132, the basis number of the strict class group belonging to 2 is $e_0(2) = t - 1$, where $t$ denotes the number of distinct primes dividing the discriminant $d$. For $d = q_1 q_2$ with $q_1 \equiv q_2 \equiv 3 \pmod{4}$, we have $t = 2$, so $e_0(2) = 1$. This means there are exactly $2^{t-1} = 2$ classes in $k$ whose square is the strict principal class.

Applying the proof of Theorem 132 to this field with $t = 2$, there is exactly one nontrivial relation between the ambiguous classes $Q_1$ and $Q_2$ corresponding to $q_1$ and $q_2$ respectively.

The ideal $(1 + \varepsilon)$ is equal to its conjugate but is not equal to any rational principal ideal. For if $1 + \varepsilon = r_1 \varepsilon^k$ held with rational $r_1$, then

$$\varepsilon = \frac{1 + \varepsilon}{1 + \varepsilon'} = \varepsilon^{2k}, \quad \varepsilon^{2k-1} = 1,$$

which is impossible since $\varepsilon$ is a fundamental unit. Consequently, $(1 + \varepsilon)$ has a decomposition

$$(1 + \varepsilon) = \text{rational ideal} \times q_1^{b_1} \cdots q_t^{b_t},$$

where at least one of the exponents $b_i$ is odd. Thus in $k(\sqrt{q_1 q_2})$ there holds a relation

$$q_1^{a_1} q_2^{a_2} \approx 1 \tag{115}$$

where $a_1$ and $a_2$ are not both even. If both were odd, then $q_1 q_2 = \sqrt{q_1 q_2} \approx 1$, implying there exists a unit $\eta$ such that $N(\eta\sqrt{q_1 q_2}) > 0$, i.e., $N(\eta) = -1$, which is impossible in this case. Hence one exponent equals 1 and the other equals 0 in (115).

This shows that exactly one of $q_1, q_2$ is a principal ideal (in the strict sense), so precisely one of the two primes is represented by the norm form $x^2 - q_1 q_2 y^2$. Consequently $h_0 = 2h$, and the norm of the fundamental unit must be $+1$ (otherwise $h_0 = h$ would hold). $\square$
