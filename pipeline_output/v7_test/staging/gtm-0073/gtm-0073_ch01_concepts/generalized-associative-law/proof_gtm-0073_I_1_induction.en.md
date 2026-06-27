---
role: proof
locale: en
content_hash: ""
written_against: ""
source: gtm-0073
section: "I.1"
---

# Proof of Theorem 1.6

We use induction on $n$ to show that every meaningful product of
$a_1, \ldots, a_n$ equals the standard $n$ product $\prod_{i=1}^{n} a_i$.

For $n = 1, 2$ the statement is trivially true. Assume $n > 2$ and the statement
holds for all $k < n$. By definition of a meaningful product,
\[
(a_1 \cdots a_n) = (a_1 \cdots a_m)(a_{m+1} \cdots a_n)
\]
for some $m$ with $1 \leq m < n$. Applying the induction hypothesis to both
factors we obtain
\[
(a_1 \cdots a_m) = \prod_{i=1}^{m} a_i, \qquad
(a_{m+1} \cdots a_n) = \prod_{i=1}^{n-m} a_{m+i}.
\]
If $m = n-1$, then
\[
(a_1 \cdots a_n) = \left( \prod_{i=1}^{n-1} a_i \right) a_n
                   = \prod_{i=1}^{n} a_i
\]
by definition of the standard $n$ product.

If $m < n-1$, apply the induction hypothesis and ordinary associativity:
\begin{align*}
(a_1 \cdots a_n)
&= \left( \prod_{i=1}^{m} a_i \right)
   \left( \prod_{i=1}^{n-m} a_{m+i} \right) \\
&= \left( \prod_{i=1}^{m} a_i \right)
   \left( \left( \prod_{i=1}^{n-m-1} a_{m+i} \right) a_n \right) \\
&= \left( \left( \prod_{i=1}^{m} a_i \right)
            \left( \prod_{i=1}^{n-m-1} a_{m+i} \right) \right) a_n \\
&= \left( \prod_{i=1}^{n-1} a_i \right) a_n
 = \prod_{i=1}^{n} a_i.
\end{align*}
Thus every meaningful product equals the standard $n$ product.
