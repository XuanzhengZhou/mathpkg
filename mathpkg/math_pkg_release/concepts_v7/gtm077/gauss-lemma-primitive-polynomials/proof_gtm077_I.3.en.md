---
role: proof
locale: en
of_concept: gauss-lemma-primitive-polynomials
source_book: gtm077
source_chapter: "I"
source_section: "3"
---
# Proof of Gauss's Lemma on Primitive Polynomials (Theorem 13a)

Recall that an integral polynomial is called **primitive** if its coefficients are relatively prime, i.e., if for every prime $p$ the polynomial is not identically zero modulo $p$.

**Theorem 13a (Gauss's Lemma).** The product of two primitive polynomials is again a primitive polynomial.

*Proof.* Let $f(x)$ and $g(x)$ be primitive integral polynomials. Suppose, for contradiction, that their product $h(x) = f(x) g(x)$ is not primitive. Then there exists a prime $p$ such that all coefficients of $h(x)$ are divisible by $p$, i.e.,

$$h(x) = f(x) g(x) quiv 0 \pmod{p}.$$

By Theorem 13 (the preliminary result that if a product of two polynomials is $quiv 0 \pmod{p}$, then at least one factor is $quiv 0 \pmod{p}$), this implies either

$$f(x) quiv 0 \pmod{p} \qquad 	ext{or} \qquad g(x) quiv 0 \pmod{p}.$$

But this contradicts the assumption that $f(x)$ and $g(x)$ are primitive—for a primitive polynomial, by definition, no prime divides all its coefficients simultaneously. Therefore our supposition was false, and $h(x)$ must be primitive. $\square$

Gauss's Lemma is a cornerstone of the theory of polynomials over the integers and over factorial rings. It ensures that primitivity is preserved under multiplication, a fact that plays a crucial role in proving the irreducibility of polynomials over $\mathbb{Q}$ via reduction to $\mathbb{Z}$.

