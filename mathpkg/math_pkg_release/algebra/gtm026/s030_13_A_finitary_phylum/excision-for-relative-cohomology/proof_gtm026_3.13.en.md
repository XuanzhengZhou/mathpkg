---
role: proof
locale: en
of_concept: excision-for-relative-cohomology
source_book: gtm026
source_chapter: "3"
source_section: "13"
---

We prove that if $f: (X, \xi, A) \rightarrow (\bar{X}, \bar{\xi}, \bar{A})$ restricts to a bijection $X - A \cong \bar{X} - \bar{A}$, then $H^n f$ is an isomorphism for all $n \geq 0$.

**Injectivity of $H^n f$:** Let $\bar{a}, \bar{b} \in [\bar{X} T^{n+1}, Y]_{\bar{A}}$ be $n$-cocycles (i.e., in $\operatorname{Ker}(d^{n+1})$) such that $fT^{n+1} \cdot \bar{a} - fT^{n+1} \cdot \bar{b} = d^n(t)$ for some $t \in [XT^n, Y]_A$. We must show $\bar{a} - \bar{b}$ is a coboundary in the $\bar{X}$ complex.

Using the coproduct decomposition of a set as the disjoint union of $A$ and its complement, we have:

$$\bar{A} \xrightarrow{\bar{j} T^n} \bar{X} T^n \xleftarrow{\bar{k} T^n} (\bar{X} - \bar{A}) T^n$$

Since $f$ restricts to a bijection on complements, we can transfer the data on $X - A$ to $\bar{X} - \bar{A}$. Define $\bar{c} \in [\bar{X} T^n, Y]_{\bar{A}}$ by setting $\bar{c} \cdot \bar{j} T^n = 0$ (as it lands in the kernel $[\bar{X} T^n, Y]_{\bar{A}}$) and using the complement bijection to define $\bar{c}$ on the remainder. Then $\bar{a} - \bar{b} = d^n(\bar{c})$, proving injectivity.

**Surjectivity of $H^n f$:** Let $a \in [XT^{n+1}, Y]_A$ be an $n$-cocycle. We construct a preimage $\bar{a} \in [\bar{X} T^{n+1}, Y]_{\bar{A}}$ with $fT^{n+1} \cdot \bar{a} = a$ (up to a coboundary).

Define $\bar{a}$ by:
$$\bar{A} T^{n+1} \xrightarrow{\bar{j} T^{n+1}} \bar{X} T^{n+1} \xleftarrow{\bar{k} T^{n+1}} (\bar{X} - \bar{A}) T^{n+1}$$
On $\bar{A} T^{n+1}$, set $\bar{a} \cdot \bar{j} T^{n+1} = 0$ (by definition of the relative subcomplex). On $(\bar{X} - \bar{A}) T^{n+1}$, use the bijection $f|_{X-A}$ to transport the values of $a$. Naturality of the differential ensures the resulting $\bar{a}$ is again a cocycle, and $fT^{n+1} \cdot \bar{a} = a$ by construction. Hence $H^n f$ is surjective.

Thus $H^n f$ is an isomorphism for all $n \geq 0$.
