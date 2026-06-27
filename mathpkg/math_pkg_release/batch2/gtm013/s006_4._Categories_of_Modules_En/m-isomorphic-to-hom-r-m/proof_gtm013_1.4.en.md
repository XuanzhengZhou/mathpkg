---
role: proof
locale: en
of_concept: m-isomorphic-to-hom-r-m
source_book: gtm013
source_chapter: "1"
source_section: "4"
---

Define $\rho: M \to \operatorname{Hom}_R(R, M)$ by $\rho(x)(r) = rx$ for $x \in M, r \in R$. For each $x \in M$, the map $\rho(x): R \to M$ is an $R$-homomorphism because $\rho(x)(rs) = (rs)x = r(sx) = r\rho(x)(s)$.

$\rho$ is $R$-linear: for $x, y \in M, s \in R$,
$\rho(x+y)(r) = r(x+y) = rx + ry = \rho(x)(r) + \rho(y)(r)$,
$\rho(sx)(r) = r(sx) = (rs)x = \rho(x)(rs) = (s\rho(x))(r)$,
where the last equality uses the left $R$-module structure on $\operatorname{Hom}_R(R, M)$ from (4.4.1): $(sf)(r) = f(rs)$.

$\rho$ is injective: if $\rho(x) = 0$, then $\rho(x)(1) = 1x = x = 0$.

$\rho$ is surjective: given $f \in \operatorname{Hom}_R(R, M)$, let $x = f(1) \in M$. Then for any $r \in R$, $\rho(x)(r) = rx = rf(1) = f(r)$, so $\rho(x) = f$.
