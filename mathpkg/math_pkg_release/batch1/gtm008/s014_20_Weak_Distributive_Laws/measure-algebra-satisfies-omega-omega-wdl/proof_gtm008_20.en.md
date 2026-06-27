---
role: proof
locale: en
of_concept: measure-algebra-satisfies-omega-omega-wdl
source_book: gtm008
source_chapter: "20"
source_section: "20. Weak Distributive Laws"
---

Let $\{b_{n,k} \mid n, k < \omega\} \subseteq B$. For each $n < \omega$, define
$$
a_n = \sum_{k < \omega} b_{nk}, \qquad a = \prod_{n < \omega} a_n.
$$

For each $f \in \omega^\omega$, define
$$
c_f = \prod_{n < \omega} \sum_{k \leq f(n)} b_{nk}.
$$

Clearly $c_f \leq a_n$ for every $n$, so $c_f \leq a$ for all $f$, and therefore
$$
\sum_{f \in \omega^\omega} c_f \leq a.
$$

To prove the reverse inequality, suppose $d = a \cdot \left(-\sum_{f} c_f\right) \neq 0$. Since $m$ is strictly positive, $m(d) > 0$. Set $\varepsilon = m(d) / 2 > 0$.

For each $n < \omega$, since $m$ is a $\sigma$-measure,
$$
\lim_{l \to \infty} m\!\left(\sum_{k \leq l} b_{nk}\right) = m(a_n),
$$
and thus by $\sigma$-additivity,
$$
\lim_{l \to \infty} m\!\left(a_n - \sum_{k \leq l} b_{nk}\right) = 0.
$$

Hence for each $n$ there exists $f(n) \in \omega$ such that
$$
m\!\left(a_n - \sum_{k \leq f(n)} b_{nk}\right) < \frac{\varepsilon}{2^{n+1}}.
$$

This defines a function $f \in \omega^\omega$. For each $n$, set
$$
c_{f,n} = \sum_{k \leq f(n)} b_{nk}.
$$

Then $c_f = \prod_{n < \omega} c_{f,n}$. Now
$$
a - c_f = a \cdot (-c_f) = a \cdot \left(-\prod_{n} c_{f,n}\right)
= a \cdot \sum_{n} (-c_{f,n})
= \sum_{n} \left( (-c_{f,n}) \cdot \prod_{m} a_m \right)
\leq \sum_{n} (a_n - c_{f,n}),
$$
where the last inequality uses that $(-c_{f,n}) \cdot \prod_m a_m \leq (-c_{f,n}) \cdot a_n = a_n - c_{f,n}$.

Therefore,
$$
m(a - c_f) \leq \sum_{n < \omega} m(a_n - c_{f,n})
= \sum_{n < \omega} m\!\left(a_n - \sum_{k \leq f(n)} b_{nk}\right)
< \sum_{n < \omega} \frac{\varepsilon}{2^{n+1}}
= \varepsilon.
$$

Since $d \leq a$ and $d \leq -\sum_f c_f \leq -c_f$, we have $d \leq a \cdot (-c_f) = a - c_f$, so
$$
m(d) \leq m(a - c_f) < \varepsilon = \frac{m(d)}{2},
$$
a contradiction. Hence $d = 0$, which means $a \leq \sum_f c_f$, establishing
$$
a = \sum_{f \in \omega^\omega} c_f,
$$
i.e., the $(\omega, \omega)$-WDL holds.
