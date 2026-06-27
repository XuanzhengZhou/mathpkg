---
role: proof
locale: en
of_concept: theorem-krull-domain-1
source_book: gtm029
source_chapter: "VI"
source_section: "13"
---

(a) The intersection $\bigcap_{w \in (G)} R_w$ is the polynomial ring $K[X]$, by definition of the $a(X)$-adic valuations. Now, if a polynomial $P(X) = a_0 + a_1X + \cdots + a_nX^n$ ($a_i \in K$) satisfies the inequality $v'(P) \geq 0$ for every $v'$ in $(F')$, then we have min $(v(a_i)) \geq 0$ for all $v$ in $(F)$, i.e., $v(a_i) \geq 0$ for every $v$ and every $i$, and this is equivalent to saying that $a_i \in R$ for every $i$. This proves (a).

(b) Suppose that $(F)$ is the family of essential valuations of the Krull domain $R$. We have to show that the set $(F') \cup (G)$ satisfies conditions $(E_1), (E_2), (E_3), (E_4)$ with respect to the ring $R[X]$. Condition $(E_1)$ is trivial. Condition $(E_2)$ has been proved in (a). As for $(E_3)$, given a polynomial $P(X) = a_0 + a_1X + \cdots + a_nX^n$ there is only a finite number of $a(X)$-adic valuations $w$ in $(G)$ for which $w(P) > 0$, since $P$ has only a finite number of irreducible factors (in $K[X]$); on the other hand, if $a_i$ is a non-zero coefficient of $P(X)$, the valuations $v'$ in $(F')$ for which $v'(P) > 0$ are among those for which $v(a_i) > 0$, by definition of $v'$, and these latter valuations are finite in number according to $(E_3)$ as applied to $R$. It remains

this prime ideal $\mathfrak{p}$ is obviously the extension to $R_v[X]$ of the center $\mathfrak{p}(v')$ of $v'$ in $R[X]$. Thus, the valuation ring we are investigating, is, by the transitivity of quotient ring formations (Vol. I, Ch. IV, § 11, p. 231) equal to the quotient ring $(R[X])_{\mathfrak{p}(v')}$. The proof of (b) is now complete.

(c) We use the characterization of UFD’s by Theorem 27. For $v'$ in $(F')$, we take an element $a_v$ in $R$ such that $v(a_v) = 1$ and $u(a_v) = 0$ for every $u \neq v$ in $(F)$. If we consider $a_v$ as a constant polynomial in $R[X]$, we have $v'(a_v) = 1$, $u'(a_v) = 0$ for every $u' \neq v'$ in $(F')$, and $w(a_v) = 0$ for every $w$ in $(G)$, since $a_v$ is a constant polynomial. For the $a(X)$-adic valuation $w$ in $(G)$, we take for $a_w$ a constant multiple of $a(X)$, all the coefficients of which are in $R$ and are relatively prime; we then have $w(a_w) = 1$, $u(a_w) = 0$ for every $u \neq w$ in $(G)$, and $v'(a_w) = 0$ for every $v'$ in $(F')$ since the coefficients of $a_w$ are relatively prime and cannot have strictly positive orders for $v$. Thus also (c) is proved.

REMARK. Observe that (c) has already been proved (Vol. I, Ch. I, § 17, Theorem 10) by elementary methods.
