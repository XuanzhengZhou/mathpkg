---
role: proof
locale: en
of_concept: fermat-euler-theorem
source_book: gtm077
source_chapter: "I"
source_section: "2"
---
# Proof of Theorem 9 (Fermat's Theorem)

Let $a$ be an integer relatively prime to $n$. Consider the $arphi(n)$ integers

$$x_1, x_2, \ldots, x_{arphi(n)}$$

that form a reduced residue system modulo $n$ (i.e., they represent all residue classes coprime to $n$). Multiplying each by $a$, the products

$$a x_1, a x_2, \ldots, a x_{arphi(n)}$$

also form a reduced residue system modulo $n$, since $a$ is coprime to $n$ and multiplication by a unit permutes the residue classes. Therefore

$$\prod_{i=1}^{arphi(n)} x_i quiv \prod_{i=1}^{arphi(n)} (a x_i) quiv a^{arphi(n)} \prod_{i=1}^{arphi(n)} x_i \pmod{n}.$$

Since each $x_i$ is relatively prime to $n$, the product $\prod x_i$ is also relatively prime to $n$. Cancelling this common factor (permissible since it is coprime to $n$) yields

$$a^{arphi(n)} quiv 1 \pmod{n}.$$

In particular, if $n = p$ is a prime, then $arphi(p) = p - 1$, so

$$a^{p-1} quiv 1 \pmod{p}$$

for all $a$ not divisible by $p$. Multiplying both sides by $a$ gives the equivalent form

$$a^p quiv a \pmod{p},$$

which holds for all integers $a$ (the congruence is trivially true when $p \mid a$). This theorem forms the basis for the theory of higher congruences and is the starting point for the investigation of the multiplicative structure of residue class rings.

The deeper significance of this proof becomes fully apparent in Chapter II, where the general group concept reveals that the reduced residue classes modulo $n$ form a multiplicative group of order $arphi(n)$, and the theorem follows immediately from Lagrange's theorem on the order of elements in a finite group.

