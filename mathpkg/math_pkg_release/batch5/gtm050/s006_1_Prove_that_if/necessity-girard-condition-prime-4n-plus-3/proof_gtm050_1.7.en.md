---
role: proof
locale: en
of_concept: necessity-girard-condition-prime-4n-plus-3
source_book: gtm050
source_chapter: "1"
source_section: "1.7"
---

The proof is given in Exercise 2 of Section 1.8. The key lemma: if a prime $p = 4n + 3$ divides $x^2 + y^2$, then $p$ must divide both $x$ and $y$.

Proof of the lemma: If $p \mid x^2 + y^2$, then $p \mid (x^2)^{2n+1} + (y^2)^{2n+1} = x^{4n+2} + y^{4n+2}$. Unless $p$ divides both $x$ and $y$, this number is either 1 or 2 greater than a multiple of $p$ (by Fermat's little theorem, $x^{p-1} \equiv 1 \pmod{p}$ if $p \nmid x$), and therefore not divisible by $p$. Hence $p$ must divide both $x$ and $y$.

Now let $N$ be a number and let $N = s^2 \cdot Q$ where $s^2$ is the largest square dividing $N$. If $Q$ has a prime factor $p = 4n+3$, and if $N = x^2 + y^2$, then $p \mid x^2 + y^2$, so $p \mid x$ and $p \mid y$. Then $p^2 \mid x^2 + y^2 = N$. But this contradicts that $s^2$ is the largest square dividing $N$ (unless $p^2 \mid s^2$, i.e., $p \mid s$, which would mean $p^2 \mid N$ and we could factor out another $p$). Repeating this argument shows that every prime $4n+3$ must appear with even exponent, which is precisely Girard's necessary condition.
