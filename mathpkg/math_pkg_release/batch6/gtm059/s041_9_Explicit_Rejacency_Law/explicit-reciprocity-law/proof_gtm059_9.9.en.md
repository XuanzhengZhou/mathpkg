---
role: proof
locale: en
of_concept: explicit-reciprocity-law
source_book: gtm059
source_chapter: "9"
source_section: "9"
---

We may again suppose $m = n + 1$. We have (as in the proof of Theorem 2.2 of Chapter 9)

$$N_{k+1,k}(-x_{k+1}) = -x_k.$$

The formula to be proved amounts to

$$\frac{1}{Y(x_{k+1})} = T_{k+1,k} \left( \frac{1}{Y(x_{k+1})} \right).$$

We have $n_x = f(x_{k+1})$ and since $f(X) = x(X)$, we have

$$f(X) = f(X)f'(X) = x(X).$$

We put $X = x_{k+1}$ and see that the formula amounts to

$$T_{k+1,k} \left( \frac{n_x}{Y(x_{k+1})} \right) = 1.$$

We replace $n_x$ by $f(x_{k+1})$, and the relation of elementary algebra yields

$$T_{k+1,k} \left( \frac{f(x_{k+1})}{f(X)} \right) = 1 \quad \text{if } f = q,$$
$$= 0 \quad \text{if } f < q.$$

This proves what we wanted.

The proof is general when $n_x = n$ follows exactly the same pattern, but we end up with only the second congruence. We give the details.

By the Weierstrass theorem, we may factor in $n_x$

$$X - x_k = g(X)h(X)$$

where

$$g(X) = b_0 + \cdots + b_{k+1}X' + X^n,$$
$$b_0 \equiv 0 \pmod{v_x},$$
$$h(X) = c_1 X + \cdots + c_{k+1} \text{ is a unit power series},$$

where

$$T_{k+1,k} = g(X)(h(X))_k.$$

Proceeding as before, we again replace $x_i$ by $f(x_{i+1})$. From the factorization we have

$$c_i \equiv 1 \pmod{n}.$$

Hence

$$h(x_{i+1})^{-1} \equiv 1 \pmod{n}.$$

From the orthogonality relation, we obtain a combination of 1 from the trace of one item.
