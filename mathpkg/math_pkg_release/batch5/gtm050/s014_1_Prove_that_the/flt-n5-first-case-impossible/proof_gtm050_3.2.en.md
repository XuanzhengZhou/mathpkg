---
role: proof
locale: en
of_concept: flt-n5-first-case-impossible
source_book: gtm050
source_chapter: "3"
source_section: "3.2"
---

**Proof.** If $x$ or $y$ is divisible by 5, move the other term to the right side of $x^5 + y^5 = z^5$ to obtain $u^5 \pm v^5 = w^5$ where $u, v, w$ are pairwise relatively prime, $w$ is divisible by 10, and $u, v$ are odd (relatively prime to the even number $w$).

Following Euler's proof for $n = 3$, set $u+v = 2p$ and $u-v = 2q$. Then $u = p+q$, $v = p-q$, and expanding $(p+q)^5 \pm (p-q)^5$ yields an expression that can be rewritten as $P^2 - 5Q^2 = \text{fifth power}$ for certain integers $P, Q$ derived from $p$ and $q$.

The integer $Q$ in this expression is divisible by 5. Moreover, $P$ and $Q$ are relatively prime and have opposite parity. By Dirichlet's Lemma, these conditions imply $P + Q\sqrt{5} = (A + B\sqrt{5})^5$ for integers $A, B$.

Expanding $(A + B\sqrt{5})^5$ and examining the coefficient of $\sqrt{5}$ gives $Q = 5A^4B + 50A^2B^3 + 25B^5$. Since $Q = 10r^2$ and $5^2 \cdot 2r$ is a fifth power, one deduces $5^4 \cdot 2B = \text{fifth power}$ and $A^4 + 10A^2B^2 + 5B^4 = \text{fifth power}$.

Completing the square in the last expression gives $(A^2 + 5B^2)^2 - 5(2B^2)^2 = \text{fifth power}$. This yields a smaller positive solution to the same type of equation, and infinite descent completes the proof that no solution exists. $\square$
