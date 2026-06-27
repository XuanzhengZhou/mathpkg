---
role: proof
locale: en
of_concept: mean-one-operation-formula
source_book: gtm059
source_chapter: "1"
source_section: "12"
---

Let $\nu$ be the measure defined by $d\nu(x) = (1+x)^x \, d\mu(x)$. Its associated power series is
$$
g(X) = \int (1+X)^y \, d\nu(y) = \int (1+X)^y (1+y)^x \, d\mu(y).
$$
Observe that
$$
(1+X)^y (1+y)^x = \bigl((1+X)(1+y)\bigr)^y = (1 + X [+] y)^y,
$$
by the definition of the formal group addition $X [+] y = (1+X)(1+y) - 1$. Therefore,
$$
g(X) = \int (1 + X [+] y)^y \, d\mu(y) = f(X [+] y) = f(X [+] x),
$$
where the last equality holds since the parameter $x$ is fixed. This shows that multiplication of the measure by $(1+x)^x$ corresponds to substituting $X [+] x$ into the power series.
