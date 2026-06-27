---
role: proof
locale: en
of_concept: genus-theory-intro
source_book: gtm077
source_chapter: "VII"
source_section: "§44"
---
# Proof of Theorem 134

**Theorem 134.** Let $d$ be the product of two distinct primes $q_1 \equiv q_2 \equiv 3 \pmod{4}$. Then in $k(\sqrt{d})$ the norm of the fundamental unit equals $+1$, and consequently $h_0 = 2h$. Moreover, each of the primes $q_1, q_2$ is the norm of some integer in $k(\sqrt{d})$.

*Proof.* By Theorem 132, the basis number of the strict class group belonging to 2 is $e_0(2) = t - 1$, where $t$ denotes the number of distinct primes dividing the discriminant $d$. For $d = q_1 q_2$ with $q_1 \equiv q_2 \equiv 3 \pmod{4}$, we have $t = 2$, so $e_0(2) = 1$. This means there are exactly $2^{t-1} = 2$ classes in $k$ whose square is the strict principal class.

Since in each case (a) $d < -4$, (b) $d > 0$ and norm of fundamental unit is $-1$, (c) $d > 0$ and norm of fundamental unit is $+1$, the proof of Theorem 132 showed that exactly $t-1$ classes $Q_1, \ldots, Q_t$ are independent. Applying this to our field with $t = 2$, there is exactly one nontrivial relation between $Q_1$ and $Q_2$.

Now, the ideal $(1 + \varepsilon)$ is equal to its conjugate but is not equal to any rational principal ideal. For if $1 + \varepsilon = r_1 \varepsilon^k$ held with rational $r_1$, then

$$\varepsilon = \frac{1 + \varepsilon}{1 + \varepsilon'} = \varepsilon^{2k}, \quad \varepsilon^{2k-1} = 1,$$

which is impossible since $\varepsilon$ is a fundamental unit. Consequently, $(1 + \varepsilon)$ has a decomposition

$$(1 + \varepsilon) = \text{rational ideal} \times q_1^{b_1} \cdots q_t^{b_t},$$

where at least one of the exponents $b_i$ is odd. Thus in $k(\sqrt{q_1 q_2})$ there holds a relation

$$q_1^{a_1} q_2^{a_2} \approx 1 \tag{115}$$

where $a_1$ and $a_2$ are not both even. If both were odd, then $q_1 q_2 = \sqrt{q_1 q_2} \approx 1$, implying there exists a unit $\eta$ such that $N(\eta\sqrt{q_1 q_2}) > 0$, i.e., $N(\eta) = -1$, which is impossible in this case. Hence one exponent equals 1 and the other equals 0 in (115).

This shows that exactly one of $q_1, q_2$ is a principal ideal (in the strict sense), so precisely one of the two primes is the norm of an integer $(x + y\sqrt{q_1 q_2})/2$. Consequently $h_0 = 2h$, and the norm of the fundamental unit must be $+1$ (otherwise $h_0 = h$ would hold). $\square$
