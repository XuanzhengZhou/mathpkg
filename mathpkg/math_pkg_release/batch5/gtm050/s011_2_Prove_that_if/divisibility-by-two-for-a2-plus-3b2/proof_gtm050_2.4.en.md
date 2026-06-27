---
role: proof
locale: en
of_concept: divisibility-by-two-for-a2-plus-3b2
source_book: gtm050
source_chapter: "2"
source_section: "2.4"
---

Suppose $a^2+3b^2$ is even. Consider the parities of $a$ and $b$. If $a$ and $b$ are both odd, then $a^2 \equiv 1 \pmod{4}$ and $3b^2 \equiv 3 \pmod{4}$, so $a^2+3b^2 \equiv 0 \pmod{4}$. If $a$ and $b$ are both even, then $a=2a'$, $b=2b'$, so $a^2+3b^2 = 4(a'^2+3b'^2)$.

If one of $a,b$ is even and the other odd, one checks that $a^2+3b^2$ is odd. Hence if $a^2+3b^2$ is even, then $a$ and $b$ have the same parity, which implies $a^2+3b^2$ is divisible by 4. Moreover, after factoring out 4, the quotient $(a/2)^2+3(b/2)^2$ is again of the form $c^2+3d^2$ with $c=a/2$, $d=b/2$ (if $a,b$ are both even), or via a more detailed analysis requiring $a \equiv b \pmod{2}$ in the mixed case. In all cases, the quotient by 4 retains the required form.
