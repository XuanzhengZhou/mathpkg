---
role: proof
locale: en
of_concept: division-ring-rip-characterization
source_book: gtm006
source_chapter: "V"
source_section: "6"
---

(i) Suppose $\mathcal{P}$ is $((0,0), [0])$-transitive. Equation (2) determines $n$ for given $m, b, x$ and Eq. (3) then determines $u$. If, for a given $x$ and $b$, $k$ is the particular value of $n$ when $m = 1$, then $ku = x$ and $kb = b + x$. Thus if $k, b, x, u$ satisfy $kb = b + x$, $ku = x$, and if $nb = m(b + x)$ for any $m$, then $nu = mx$. In the special case $b = -1$, the conditions $k = 1 - x$, $ku = x$, and $n = m(1 - x)$ imply $n = mk$, so $(mk)u = nu = mx = m(ku)$. Since $\mathcal{O}$ is $(0,0), [0]$-transitive, as $x$ and $b$ vary, $k$ will vary over all possible values in $R$. Hence, for any $m, k$, if $u$ satisfies $k = 1 - ku$, we have

$$(mk)u = m(ku).$$

Let $v = 1 + u$ so that $kv = 1$. Then

$$(mk)v = (mk)(1 + u) = mk + mk(u) \quad \text{(by the left distributive law)}$$
$$= mk + m(ku) \quad \text{(by the derived identity)}$$
$$= m(k(1 + u))$$
$$= m(kv) = m \quad \text{since } kv = 1.$$

But $k$ was defined by $[1, x]^{*b} = [k, x]$, and as $b$ varies over $R^*$, $k$ takes all possible values in $R^*$. Therefore $R$ has RIP.

(ii) Suppose $R$ has RIP. For any $b \in R^*$, define $\phi_b$ by:

$$(x, y) \rightarrow ((b^{-1} + x^{-1})^{-1}, (yx^{-1})(b^{-1} + x^{-1})^{-1}) \quad \text{for } x \neq 0,$$

and extend appropriately to all points. Suppose

$$(m + kb^{-1})(b^{-1} + x^{-1})^{-1} + (yx^{-1})(b^{-1} + x^{-1})^{-1} = k.$$

Then multiplying both sides by $(b^{-1} + x^{-1})$ and using the right distributive law, RIP, and Lemma 6.10 giving $(b^{-1} + x^{-1})^{-1}(b^{-1} + x^{-1}) = 1$, we obtain

$$(m + kb^{-1}) + yx^{-1} = k(b^{-1} + x^{-1}).$$

By associativity of addition and the left distributive law, this simplifies to

$$m + kb^{-1} + yx^{-1} = kb^{-1} + kx^{-1}.$$

Since $(R, +)$ is an abelian group, cancel $kb^{-1}$:

$$m + yx^{-1} = kx^{-1}.$$

Multiplying both sides on the right by $x$ and using the right distributive law, RIP, and Lemma 6.10 yields $mx + y = k$ as required. Thus $\phi_b$ preserves incidence, defining the required $((0,0), [0])$-elation.
