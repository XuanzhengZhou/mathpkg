---
role: proof
locale: en
of_concept: theorem-1-1
source_book: gtm059
source_chapter: "6"
source_section: "6"
---

*Proof.* The second condition is a special case of K.4. As to the first:

$$\varphi_0(u_k) = \varphi_1(u_k) - \zeta^k.$$

An associated power series of $1 - \zeta^k$ is $f(X) = 1 - X^k$, and

$$f'(X) = \frac{-k X^{k-1}}{1 - X^k}.$$

Then

$$D f / f(X) = -k(1+X) \sum_{i=0}^{\infty} X^{ki} = -k \sum_{i=0}^{\infty} (1 - \zeta^{ki}) \equiv -k \pmod{p}.$$

Hence

$$D^{-1}(D f / f)(0) \equiv -k \pmod{p}$$

as desired.
