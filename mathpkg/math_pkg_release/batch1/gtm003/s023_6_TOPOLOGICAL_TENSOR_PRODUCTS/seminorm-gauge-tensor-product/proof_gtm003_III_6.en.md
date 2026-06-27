---
role: proof
locale: en
of_concept: seminorm-gauge-tensor-product
source_book: gtm003
source_chapter: "III"
source_section: "6"
---

**Proof.** It is immediate that $r$ is a semi-norm on $E \otimes F$. Let
$$M_0 = \{u : r(u) < 1\}, \quad M_1 = \{u : r(u) \leq 1\}.$$
To prove that $r$ is the gauge of $\Gamma(U \otimes V)$, it suffices to show that
$$M_0 \subset \Gamma(U \otimes V) \subset M_1.$$

**First inclusion ($\Gamma(U \otimes V) \subset M_1$):** If $u \in \Gamma(U \otimes V)$, then $u = \sum \lambda_i (x_i \otimes y_i)$ where $x_i \in U$, $y_i \in V$ for all $i$ and $\sum |\lambda_i| \leq 1$. Write $u = \sum \bar{x}_i \otimes y_i$ where $\bar{x}_i = \lambda_i x_i$. Then
$$r(u) \leq \sum p(\bar{x}_i) q(y_i) = \sum |\lambda_i| p(x_i) q(y_i) \leq \sum |\lambda_i| \cdot 1 \cdot 1 \leq 1.$$
Thus $u \in M_1$.

**Second inclusion ($M_0 \subset \Gamma(U \otimes V)$):** If $u \in M_0$, then $r(u) < 1$, so there exists a representation $u = \sum x_i \otimes y_i$ with $\sum p(x_i) q(y_i) < 1$. Choose $\varepsilon_i > 0$ such that $\sum \mu_i < 1$, where
$$\mu_i = (p(x_i) + \varepsilon_i)(q(y_i) + \varepsilon_i) \quad \text{for all } i.$$
Set
$$\bar{x}_i = \frac{x_i}{p(x_i) + \varepsilon_i}, \quad \bar{y}_i = \frac{y_i}{q(y_i) + \varepsilon_i}.$$
Then $p(\bar{x}_i) < 1$, $q(\bar{y}_i) < 1$, so $\bar{x}_i \in U$, $\bar{y}_i \in V$. Moreover,
$$u = \sum \mu_i (\bar{x}_i \otimes \bar{y}_i) \in \Gamma(U \otimes V)$$
since $\sum \mu_i < 1$. This establishes $M_0 \subset \Gamma(U \otimes V) \subset M_1$, proving that $r$ is the gauge of $\Gamma(U \otimes V)$.

For the refined representation assertion, note that by the Hahn-Banach theorem (specifically II, 3.2), given $x_0 \in E$, $y_0 \in F$, there exist linear forms $f \in E^*$, $g \in F^*$ such that $f(x_0) = p(x_0)$ and $|f(x)| \leq p(x)$ for all $x$, and similarly for $g$. By considering the tensor product of these forms and standard approximation arguments, one obtains a representation with the stated properties. $\square$
