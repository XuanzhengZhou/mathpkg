---
role: proof
locale: en
of_concept: decomposition-in-kummer-extensions
source_book: gtm077
source_chapter: "V"
source_section: "39"
---
# Proof of Theorem 117-118: Decomposition in Kummer Extensions

**Theorem 117.** For a prime ideal $\mathfrak{p}$ of $k$ in the Kummer extension $K = k(\sqrt[l]{\mu})$, exactly one of the following holds:
1. $\mathfrak{p}$ remains prime in $K$ (inert),
2. $\mathfrak{p} = \mathfrak{P}^l$ for a prime ideal $\mathfrak{P}$ of $K$ (totally ramified),
3. $\mathfrak{p} = \mathfrak{P}_1 \cdots \mathfrak{P}_l$ with distinct $\mathfrak{P}_i$ (totally split).

**Theorem 118 (Decomposition Criterion).** Let the exponent $a$ be defined by $\mathfrak{p}^a \parallel \mu$ (i.e., the exact power of $\mathfrak{p}$ dividing $\mu$). Then:
- If $l \nmid a$, then $\mathfrak{p}$ is totally ramified in $K$ (case 2 of Theorem 117).
- If $l \mid a$, then, after replacing $\mu$ by $\mu^* = \mu \beta^{-a}$ (which generates the same field) so that $a = 0$:
  - If $\mathfrak{p} \nmid l$ and $\mu \equiv \xi^l \pmod{\mathfrak{p}}$ is solvable in $k$, then $\mathfrak{p}$ splits completely (case 3);
  - If $\mathfrak{p} \nmid l$ and $\mu \equiv \xi^l \pmod{\mathfrak{p}}$ is not solvable, then $\mathfrak{p}$ remains prime (case 1).

*Proof of Theorem 117.* As shown in the separate proof of Theorem 117, let $\mathfrak{P} \mid \mathfrak{p}$ in $K$. The relative norm gives $\prod_{m=0}^{l-1} s^m \mathfrak{P} = \mathfrak{p}^{f_1}$. If $\mathfrak{P} = s^m \mathfrak{P}$ for some $m \not\equiv 0 \pmod{l}$, then all conjugates coincide and $\mathfrak{p} = \mathfrak{P}^l$. If all conjugates are distinct, then $\mathfrak{p}$ is the product of these $l$ distinct primes or remains prime itself.

*Proof of Theorem 118.*
**I. $l \nmid a$.** We may assume $a = 1$ by replacing $\mu$ with $\mu^* = \mu^x \beta^{ly}$ where $\beta$ is divisible by $\mathfrak{p}$ but not by $\mathfrak{p}^2$, and $x, y$ are integers with $xa + yl = 1$. Then $\mathfrak{p} \parallel \mu^*$ while $\sqrt[l]{\mu^*}$ generates the same field.

Define $\mathfrak{P} = (\mathfrak{p}, \sqrt[l]{\mu})$. Computing its $l$th power:

$$\mathfrak{P}^l = (\mathfrak{p}^l, \mathfrak{p}^{l-1}\sqrt[l]{\mu}, \ldots, \mathfrak{p}(\sqrt[l]{\mu})^{l-1}, \mu) = (\mathfrak{p}^l, \mu) = \mathfrak{p},$$

where the last equality uses that $\mathfrak{p} \parallel \mu$ (so $(\mathfrak{p}^l, \mu) = \mathfrak{p}$). By Theorem 108, $\mathfrak{P}$ is a prime ideal and $\mathfrak{p} = \mathfrak{P}^l$.

**II. $l \mid a$.** Replace $\mu$ by $\mu^* = \mu \beta^{-a}$ where $\beta$ is such that $\mathfrak{p} \parallel \beta$. Then $\mathfrak{p} \nmid \mu^*$ (exponent $a = 0$) and $K = k(\sqrt[l]{\mu^*})$.

*II(a).* $\mathfrak{p} \nmid l$ and $\mu \equiv \xi^l \pmod{\mathfrak{p}}$ solvable. Then

$$\mu - \xi^l = \prod_{m=0}^{l-1} (\sqrt[l]{\mu} - \zeta^m \xi).$$

Since $\mathfrak{p}$ divides the left side, it must divide one of the factors on the right, say $\mathfrak{P} \mid (\sqrt[l]{\mu} - \xi)$. But the factors are conjugates under the Galois group. If $\mathfrak{p}$ divided two distinct factors, their difference would also be divisible by $\mathfrak{p}$, implying $\mathfrak{p} \mid (1 - \zeta)$, contradicting $\mathfrak{p} \nmid l$. Hence the $l$ factors are divisible by $l$ distinct conjugate prime ideals in $K$, giving total splitting.

*II(b).* $\mathfrak{p} \nmid l$ and $\mu \equiv \xi^l \pmod{\mathfrak{p}}$ unsolvable. Then $\mathfrak{p}$ cannot split (otherwise $\mu$ would be an $l$th power modulo a factor) and cannot ramify (since $\mathfrak{p} \nmid \mu$ and the relative discriminant criterion). Hence $\mathfrak{p}$ remains prime. $\square$
