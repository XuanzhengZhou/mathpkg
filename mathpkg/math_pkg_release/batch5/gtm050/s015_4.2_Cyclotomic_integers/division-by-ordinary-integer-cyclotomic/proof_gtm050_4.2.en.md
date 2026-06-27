---
role: proof
locale: en
of_concept: division-by-ordinary-integer-cyclotomic
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

**Necessity.** Suppose $h(\alpha) = a_0 \cdot g(\alpha)$ for some cyclotomic integer $g(\alpha) = c_0 + c_1\alpha + \cdots + c_{\lambda-1}\alpha^{\lambda-1}$. Then
$$h(\alpha) = a_0c_0 + a_0c_1\alpha + \cdots + a_0c_{\lambda-1}\alpha^{\lambda-1}.$$
In this representation, every coefficient of $h(\alpha)$ is a multiple of $a_0$, so all coefficients are congruent to $0$ modulo $a_0$, hence congruent to one another. However, this condition refers to a particular representation. To express it invariantly, note that if two representations differ by an integer multiple of the fundamental relation $\phi(\alpha) = 1 + \alpha + \cdots + \alpha^{\lambda-1}$, say by $c \cdot \phi(\alpha)$, then the coefficients change by adding $c$ uniformly. Therefore the differences $b_i - b_j$ for $i \neq j$ are invariant under changes of representation. Since in the representation with all coefficients divisible by $a_0$ we have $b_i \equiv b_j \equiv 0 \pmod{a_0}$ for all $i, j$, the invariant condition is $b_i \equiv b_j \pmod{a_0}$ for all $i, j$.

**Sufficiency.** Suppose all coefficients $b_0, b_1, \ldots, b_{\lambda-1}$ of $h(\alpha)$ are congruent to one another modulo $a_0$. Choose the least residue; without loss of generality, let $b_{\lambda-1}$ be minimal. Subtract $b_{\lambda-1}$ from each coefficient and use the relation $\phi(\alpha) = 0$:
$$h(\alpha) = (b_0 - b_{\lambda-1}) + (b_1 - b_{\lambda-1})\alpha + \cdots + (b_{\lambda-2} - b_{\lambda-1})\alpha^{\lambda-2} + b_{\lambda-1}\phi(\alpha).$$
Since $\phi(\alpha) = 0$, we have $h(\alpha) = (b_0 - b_{\lambda-1}) + (b_1 - b_{\lambda-1})\alpha + \cdots + (b_{\lambda-2} - b_{\lambda-1})\alpha^{\lambda-2}$. Now each coefficient $b_j - b_{\lambda-1}$ is divisible by $a_0$ because $b_j \equiv b_{\lambda-1} \pmod{a_0}$. Writing $b_j - b_{\lambda-1} = a_0 \cdot c_j$ for integers $c_j$, we obtain
$$h(\alpha) = a_0\bigl(c_0 + c_1\alpha + \cdots + c_{\lambda-2}\alpha^{\lambda-2}\bigr) = a_0 \cdot g(\alpha),$$
with $g(\alpha)$ a cyclotomic integer.
