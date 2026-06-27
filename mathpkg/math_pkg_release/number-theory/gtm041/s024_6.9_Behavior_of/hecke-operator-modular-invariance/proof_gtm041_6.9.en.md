---
role: proof
locale: en
of_concept: hecke-operator-modular-invariance
source_book: gtm041
source_chapter: "6"
source_section: "6.9"
---

We use the representation in (21) to write

$$(T_n f)(\tau) = \frac{1}{n} \sum_{A_1} a_1^k f(A_1 \tau)$$

where $A_1 = \begin{pmatrix} a_1 & b_1 \\ 0 & d_1 \end{pmatrix}$ and $A_1$ runs through a complete set of nonequivalent elements in $\Gamma(n)$. Replacing $\tau$ by $V \tau$ we find

$$(T_n f)(V \tau) = \frac{1}{n} \sum_{A_1} a_1^k f(A_1 V \tau).$$

By Theorems 6.7 and 6.9, there exist matrices

$$A_2 = \begin{pmatrix} a_2 & b_2 \\ 0 & d_2 \end{pmatrix}$$

in $\Gamma(n)$ and an element $V_1 \in \Gamma$ such that

$$A_1 V = V_1 A_2.$$

Moreover, as $A_1$ runs through a complete set of nonequivalent elements of $\Gamma(n)$, so does $A_2$. Also, $V_1$ has the form

$$V_1 = \begin{pmatrix} \alpha_1 & \beta_1 \\ \gamma_1 & \delta_1 \end{pmatrix}.$$

Since $f \in M_k$ we have

$$f(A_1 V \tau) = f(V_1 A_2 \tau) = (\gamma_1 A_2 \tau + \delta_1)^{-k} f(A_2 \tau).$$

Now we compute

$$(\gamma \tau + \delta)^{-k} (T_n f)(V \tau) = \frac{1}{n} \sum_{A_1} a_1^k (\gamma \tau + \delta)^{-k} f(A_1 V \tau).$$

Using the relation $A_1 V = V_1 A_2$ we obtain

$$(\gamma \tau + \delta)^{-k} f(A_1 V \tau) = (\gamma \tau + \delta)^{-k} (\gamma_1 A_2 \tau + \delta_1)^{-k} f(A_2 \tau).$$

A computation shows that

$$a_1 (\gamma \tau + \delta) = a_2 (\gamma_1 A_2 \tau + \delta_1),$$

hence

$$a_1^k (\gamma \tau + \delta)^{-k} = a_2^k (\gamma_1 A_2 \tau + \delta_1)^{-k}.$$

Therefore

$$(\gamma \tau + \delta)^{-k} (T_n f)(V \tau) = \frac{1}{n} \sum_{A_2} a_2^k f(A_2 \tau) = (T_n f)(\tau),$$

which proves (24).
