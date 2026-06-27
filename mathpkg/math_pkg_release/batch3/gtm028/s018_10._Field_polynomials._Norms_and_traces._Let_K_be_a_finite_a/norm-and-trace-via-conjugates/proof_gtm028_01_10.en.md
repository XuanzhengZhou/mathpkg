---
role: proof
locale: en
of_concept: norm-and-trace-via-conjugates
source_book: gtm028
source_chapter: "I"
source_section: "10"
---
Since $K = k(x)$, Theorem 20 tells us that the minimal polynomial $f(X)$ coincides with the field polynomial of $x$ over $k$. Write the field polynomial as
$$f(X) = X^n + a_1 X^{n-1} + \cdots + a_n.$$

From the matrix definition, the field polynomial is $\det(XE - A)$ where $A$ is the matrix of multiplication by $x$. Expanding this determinant gives:
$$\det(XE - A) = X^n - \operatorname{tr}(A) X^{n-1} + \cdots + (-1)^n \det(A).$$

Comparing coefficients, we obtain
$$a_1 = -T(x), \qquad a_n = (-1)^n N(x).$$

On the other hand, factoring $f(X)$ in a normal extension $K'$ gives
$$f(X) = \prod_{i=1}^{n} (X - x_i) = X^n - \left(\sum x_i\right) X^{n-1} + \cdots + (-1)^n \prod x_i.$$

Hence $\sum x_i = -a_1 = T(x)$ and $\prod x_i = (-1)^n a_n = N(x)$.

For the inseparable case, if $x$ has only $n_0$ distinct conjugates, then each conjugate appears with multiplicity $p^e$ in the factorization of $f(X)$, where $p^e = [k(x):k]_i$. The formulas with the distinct conjugates follow immediately.
