---
role: proof
locale: en
of_concept: dedekind-sum-transformation-evenness
source_book: gtm041
source_chapter: "3"
source_section: "3.7"
---
Taking $k = c$ in Theorem 3.8(b) we find

$$12ac\left\{s(a, c) - \frac{a + d}{12c}\right\} \equiv a^2 + 1 - a(a + d) \equiv -bc \pmod{\theta c},$$

where $\theta = (3, c)$. The same theorem with $k = c_1 = c/q$ gives, after multiplication by $q$,

$$12ac\left\{s(a, c_1) - \frac{a + d}{12c_1}\right\} \equiv qa^2 + q - qa(a + d) \equiv -qbc \pmod{\theta_1c},$$

where $\theta_1 = (3, c_1)$. Note that $\theta_1 \mid \theta$, so both congruences hold modulo $\theta_1c$.

Subtracting the congruences and multiplying by $r = 12$, we find

$$12acr\delta \equiv r(q - 1)bc \pmod{\theta_1c}.$$

But $r(q - 1)bc = 24bc \equiv 0 \pmod{\theta_1c}$, so this gives

$$12acr\delta \equiv 0 \pmod{\theta_1c}.$$

Now $(a, c) = 1$ since $ad - bc = 1$, and $12c\delta$ is an integer, so we can cancel $a$ to obtain

$$12cr\delta \equiv 0 \pmod{\theta_1c}.$$

Next, one shows that $12cr\delta \equiv 0 \pmod{3c}$ by treating the case $q > 3$ and the case $q = 3$ separately. For $q > 3$, $\theta = \theta_1$ so the previous congruence suffices. For $q = 3$, a separate computation using Theorem 3.8(b) and $r = 12$ shows $12rac\delta \equiv 0 \pmod{9}$, and since $3 \nmid a$, cancellation yields $12rc\delta \equiv 0 \pmod{9}$.

The final step proves $12cr\delta \equiv 0 \pmod{24c}$, which implies $12\delta$ is even. This is established by treating the cases $c$ odd and $c$ even separately.

For $c$ odd, apply Theorem 3.9 (formula (40)) with $k = c$ and $k = c_1$, subtract, multiply by $r = 12$, and use $4cr \equiv 0 \pmod{8}$ to get $12cr\delta \equiv 0 \pmod{8}$. Combined with the modulo-3 result, this gives $12cr\delta \equiv 0 \pmod{24c}$.

For $c$ even, write $c = 2^{\lambda}\gamma$ with $\gamma$ odd. Using Theorem 3.10 with $h = a$ and $k = c$, we obtain a congruence modulo $2^{\lambda+3}$. The same reasoning with $c_1$ and after subtraction yields $12car\delta \equiv 0 \pmod{2^{\lambda+3}}$. Canceling the odd $a$ gives $12cr\delta \equiv 0 \pmod{2^{\lambda+3}}$, which with the modulo-3 congruence yields $12cr\delta \equiv 0 \pmod{24c}$.

Thus $12\delta$ is an even integer. For $a < 0$, write $\delta = \delta(a)$ and observe that $\delta(a+tc) - \delta(a) = t(q-1)/12$, so $12\delta(a+tc) - 12\delta(a) = 2t$ is even. Choosing $t$ so that $a' = a + tc \geq 1$ guarantees $12\delta(a')$ is even by the argument above, hence $12\delta(a)$ is also even.
