---
role: proof
locale: en
of_concept: prime-cyclotomic-integer-characterization
source_book: gtm050
source_chapter: "4"
source_section: "4.3"
---
The proof proceeds in several steps:

1. If $Nh(\alpha)$ is prime, then $h(\alpha)$ divides $p = Nh(\alpha)$. The same argument as for ordinary integers shows $h(\alpha)$ is prime.

2. Conversely, if $h(\alpha)$ is prime with $Nh(\alpha) = p$, then $h(\alpha) \mid p$. The conjugates $h(\alpha^j)$ also divide $p$. Let $k$ be an integer such that $h(\alpha) \mid (\alpha - k)$. Then $k^\lambda \equiv 1 \pmod{p}$ and $k \not\equiv 1 \pmod{p}$ unless $p = \lambda$.

3. From $k^\lambda \equiv 1 \pmod{p}$ and Fermat's Little Theorem $k^{p-1} \equiv 1 \pmod{p}$, we get $\lambda \mid (p-1)$ (or $p = \lambda$). Hence $p \equiv 0$ or $1 \pmod{\lambda}$.

4. The congruence condition: since $\alpha \equiv k \pmod{h(\alpha)}$, we have $f(\alpha) \equiv f(k) \pmod{h(\alpha)}$. Then $f(\alpha) \equiv g(\alpha) \pmod{h(\alpha)} \iff f(k) \equiv g(k) \pmod{p}$.

5. Corollary: $\alpha-1$ is prime because $N(\alpha-1) = \lambda$ is prime.

6. Corollary: If $Nh_1(\alpha) = p = Nh_2(\alpha)$ is prime, then $h_2(\alpha)$ is a unit times a conjugate of $h_1(\alpha)$.
