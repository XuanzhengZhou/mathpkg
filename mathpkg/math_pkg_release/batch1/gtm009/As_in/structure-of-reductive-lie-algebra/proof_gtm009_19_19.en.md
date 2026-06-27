---
role: proof
locale: en
of_concept: structure-of-reductive-lie-algebra
source_book: gtm009
source_chapter: "19"
source_section: "19.1"
---

**Proof.** If $L$ is abelian, the statement is trivial ($[LL] = 0$, $Z(L) = L$). Assume $L$ is reductive but not abelian. Then $L' = L/Z(L)$ is semisimple, and $\operatorname{ad} L \cong \operatorname{ad} L'$ acts completely reducibly on $L$ by Theorem 6.3. Hence we can write $L = M \oplus Z(L)$ where $M$ is an ideal of $L$ complementary to the center. In particular, $[LL] = [MM] \subset M$. But the canonical projection $L \to L'$ maps $[LL]$ onto $L'$, which forces $\dim [LL] \geq \dim L' = \dim L - \dim Z(L)$. Since $[LL] \subset M$ and $\dim M = \dim L - \dim Z(L)$, we obtain $[LL] = M$. Therefore $L = [LL] \oplus Z(L)$. Moreover, $[LL] \cong L/Z(L) = L'$ is semisimple. $\square$
