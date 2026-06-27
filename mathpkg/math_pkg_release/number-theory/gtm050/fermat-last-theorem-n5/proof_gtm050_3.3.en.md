---
role: proof
locale: en
of_concept: fermat-last-theorem-n5
source_book: gtm050
source_chapter: "3"
source_section: "3.3"
---

The proof splits into two cases depending on whether the term divisible by 5 is also even (first case) or not (second case).

**First case:** Suppose $w$ is divisible by 10. Then $u^5 + v^5 = w^5$ with $u,v$ odd. Set $u+v = 2p$, $u-v = 2q$. Then $u^5+v^5 = 2p(p^4+10p^2q^2+5q^4)$. By analyzing the factors and using infinite descent, one derives a contradiction.

**Second case:** The even term and the term divisible by 5 are distinct. The proof follows Euler's pattern for $n=3$, using the arithmetic of the ring $\mathbb{Z}[\sqrt{5}]$. After reducing to $p^2 - 5q^2$ being a fifth power, one invokes the lemma that under suitable conditions, $p + q\sqrt{5} = (a + b\sqrt{5})^5$. This leads to an infinite descent argument, completing the proof. (The full 1825 joint paper by Dirichlet and Legendre contained the complete argument; Edwards provides a detailed exposition.)
