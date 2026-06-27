---
role: proof
locale: en
of_concept: iterated-exponential-is-primitive-recursive
source_book: gtm037
source_chapter: "2"
source_section: "Elementary Recursive and Primitive Recursive Functions"
---

The function $a$ is defined by primitive recursion on its second argument:

- Base ($n = 0$): $a(m, 0) = m = U_0^1(m)$, which is a projection function and hence primitive recursive.
- Step: $a(m, n+1) = m^{a(m, n)} = \exp(m, a(m, n))$, where $\exp(x, y) = x^y$ is exponentiation.

Exponentiation is elementary (by Lemma 2.8(v)), and in particular it is primitive recursive. The step function $h(m, n, z) = m^z = \exp(U_0^3(m, n, z), U_2^3(m, n, z))$ is a composition of the primitive recursive functions $\exp$ and projections. Therefore $a$ is obtained by primitive recursion from primitive recursive functions, so $a$ is primitive recursive.
