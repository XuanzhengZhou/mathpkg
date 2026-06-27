---
role: proof
locale: en
of_concept: dedekind-multiplier-parity
source_book: gtm041
source_chapter: "3"
source_section: "3.9"
---

The proof proceeds in several steps, establishing congruences modulo increasing powers of $2$ and $3$, and finally combining them to get the result modulo $24c$.

**Step 1: A congruence modulo $\theta c$.** Taking $k = c$ in Theorem 3.8(b), we obtain
$$12ac\left\{s(a,c) - \frac{a+d}{12c}\right\} \equiv a^2 + 1 - a(a+d) \equiv -bc \pmod{\theta c},$$
where $\theta = (3, c)$. Applying the same theorem with $k = c_1 = c/q$ and multiplying by $q$:
$$12ac\left\{s(a,c_1) - \frac{a+d}{12c_1}\right\} \equiv qa^2 + q - qa(a+d) \equiv -qbc \pmod{\theta_1 c},$$
where $\theta_1 = (3, c_1)$. Since $\theta_1 \mid \theta$, both congruences hold modulo $\theta_1 c$. Subtracting and multiplying by $r = 12$:
$$12acr\delta \equiv r(q-1)bc \pmod{\theta_1 c}.$$
But $r(q-1)bc = 24bc \equiv 0 \pmod{\theta_1 c}$, so
$$12acr\delta \equiv 0 \pmod{\theta_1 c}.$$
Since $(a,c) = 1$ and $12c\delta$ is an integer, we can cancel $a$ to get
$$12cr\delta \equiv 0 \pmod{\theta_1 c}.$$

**Step 2: Congruence modulo $3c$.** We show $12cr\delta \equiv 0 \pmod{3c}$. If $q > 3$, then $\theta = \theta_1$ and the result follows from Step 1. If $q = 3$, then $3 \mid c$ and $\theta = 3$, $\theta_1 = 1$. Using Theorem 3.8(b) modulo $9$ and the fact that $r = 12$, one verifies directly that
$$12rac\delta \equiv 0 \pmod{9}.$$
Since $3 \nmid a$, cancel $a$ to obtain $12rc\delta \equiv 0 \pmod{9}$, which together with Step 1 gives $12cr\delta \equiv 0 \pmod{3c}$.

**Step 3: Congruence modulo $24c$.** To prove $12cr\delta \equiv 0 \pmod{24c}$, we treat two cases.

*Case 1: $c$ odd.* Apply Theorem 3.9 (congruence mod $8$) with $k = c$ and $k = c_1$. Subtracting the resulting congruences, multiplying by $r$, and using $4cr \equiv 0 \pmod{8}$, we obtain $12cr\delta \equiv 0 \pmod{8}$. Combining with Step 2 gives the result modulo $24c$.

*Case 2: $c$ even.* Write $c = 2^{\lambda}\gamma$ with $\gamma$ odd. Apply Theorem 3.10 with $k = c$ and $k = c_1$. Subtracting, multiplying by $r$, and using $4cr \equiv 0 \pmod{2^{\lambda+3}}$, we get
$$12car\delta \equiv 0 \pmod{2^{\lambda+3}}.$$
Since $a$ is odd, cancel $a$ to obtain $12cr\delta \equiv 0 \pmod{2^{\lambda+3}}$. With Step 2, this yields $12cr\delta \equiv 0 \pmod{3 \cdot 2^{\lambda}\gamma} = 0 \pmod{3c}$, and together they imply $12cr\delta \equiv 0 \pmod{24c}$.

Since $12cr\delta$ is divisible by $24c$, it follows that $r\delta = 12\delta$ is even. The case $a < 0$ is reduced to $a \geq 1$ by adding an integer multiple of $c$ to $a$, which changes $\delta$ by an even integer and does not affect the parity conclusion. $\square$
