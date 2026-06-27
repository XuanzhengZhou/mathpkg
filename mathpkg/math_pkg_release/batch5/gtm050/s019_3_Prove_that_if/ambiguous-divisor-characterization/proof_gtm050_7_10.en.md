---
role: proof
locale: en
of_concept: ambiguous-divisor-characterization
source_book: gtm050
source_chapter: "7"
source_section: "7.10"
---

The proof proceeds in two directions.

($\Leftarrow$) If a divisor $A$ divides $4D$ (when $D \equiv 2$ or $3 \pmod 4$) or divides $D$ (when $D \equiv 1 \pmod 4$), then all its prime factors are ramified primes (and possibly 2, which ramifies when $D \equiv 2$ or $3 \pmod 4$). By the theorem that ramified primes generate ambiguous classes, any divisor composed solely of such factors lies in an ambiguous class. Hence any divisor equivalent to $A$ is ambiguous.

($\Rightarrow$) Conversely, suppose $A$ is ambiguous, i.e., $A \sim \bar{A}$. By the structure theorem for ambiguous divisor classes, $A$ is equivalent to a divisor of the form $(p_1,*)(p_2,*)\cdots(p_k,*)$ where each $p_i$ is a ramified prime (or $-1$ when $D > 0$). Every such divisor divides $4D$ (or $D$ in the case $D \equiv 1 \pmod 4$). Thus $A$ is equivalent to a divisor of $4D$ or $D$.

Therefore, to count inequivalent ambiguous divisors, it suffices to count inequivalent divisors of $4D$ or $D$.
