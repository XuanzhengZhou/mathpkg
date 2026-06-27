---
role: proof
locale: en
of_concept: iwasawa-artin-hasse-formula
source_book: gtm059
source_chapter: "9"
source_section: "1. Statement of the Reciprocity Laws"
---

The proof occupies the remainder of the chapter. The key idea is to use the logarithmic derivative $D_n$ to relate the multiplicative and additive structures. For the formal multiplicative group over $\mathbb{Q}_p$, the logarithm is $\log(1+X)$ and one computes

$$
\log N_{n+1}(u_i) \equiv z \pmod{p^{n+1}}
$$

where $z \equiv 0 \pmod{p^{n+1}}$ since $p \mid 2$. Hence

$$
-T_n(\log u_i) = \log N_{n+1}(u_i) \equiv N_{n+1}(u_i) - 1 \pmod{p^{n+1}}.
$$

Since $K$ is unramified over $\mathbb{Q}_p$, we have $n = p$, and the corollary follows. For the general case, the proof uses the Lubin-Tate formal group $A_f(\pi)$ and the operator $D_n$ defined via the derivative of the power series representing elements. The compatibility of the bracket symbol with norms yields the general formula $(x, \alpha)_n = [x, \alpha]_n |u_n|$.
