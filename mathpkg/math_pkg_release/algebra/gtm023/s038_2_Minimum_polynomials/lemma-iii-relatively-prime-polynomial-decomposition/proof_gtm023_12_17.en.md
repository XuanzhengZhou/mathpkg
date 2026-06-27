---
role: proof
locale: en
of_concept: lemma-iii-relatively-prime-polynomial-decomposition
source_book: gtm023
source_chapter: "12"
source_section: "12.17"
---

**Proof.** For $k = 1$ set $u = t$ and $v = 0$. Then (i) holds because $g \mid g(t)$, and (ii) holds because $t + g \cdot 0 = t$.

Next consider the case $k = 2$. Since $g$ and $g'$ are relatively prime, there exist polynomials $p$ and $q$ such that

$$1 + p g' = q g.$$

The Taylor expansion gives, in view of the relation above,

$$g(t + p g) = \sum_{i=0}^{\infty} \frac{g^{(i)}}{i!} (p g)^i = g + g' p g + \cdots + \frac{g^{(n)}}{n!} (p g)^n$$

$$= g(1 + g' p) + g^2 \cdot \ell$$

$$= g^2 q + g^2 \ell = g^2(q + \ell).$$

Thus setting $u_2 = t + p g$ and $v_2$ appropriately, we obtain the result for $k = 2$ with $g(u_2) = g^2(q + \ell)$, so $g^2 \mid g(u_2)$, and $u_2 + g v_2 = t$.

Now assume the lemma holds for $k - 1$ with polynomials $u_{k-1}$ and $v_{k-1}$. Replacing $t$ by $u_{k-1}$ in the $k = 2$ relation we obtain

$$u_2(u_{k-1}) + g(u_{k-1}) v_2(u_{k-1}) = u_{k-1}. \tag{12.31}$$

By the induction hypothesis,

$$g^{k-1} \mid g(u_{k-1}),$$

hence $g \mid g(u_{k-1})$. Thus we can write

$$g(u_{k-1}) = g \cdot q$$

where $q$ is some polynomial. Now (12.31) can be written as

$$u_k + g \cdot q \cdot v_2(u_{k-1}) = u_{k-1}, \tag{12.32}$$

where we set $u_k = u_2(u_{k-1})$. By the induction hypothesis, property (ii) gives

$$u_{k-1} = t - g v_{k-1}. \tag{12.33}$$

Relations (12.32) and (12.33) imply that

$$u_k + g \cdot (q \cdot v_2(u_{k-1}) + v_{k-1}) = t.$$

Setting $v_k = q \cdot v_2(u_{k-1}) + v_{k-1}$ we obtain

$$u_k + g v_k = t,$$

which establishes (ii) for $k$.

It remains to show that $g^k$ divides $g(u_k)$. Observe that

$$g(u_k) = g(u_2(u_{k-1})) = (g \circ u_2)(u_{k-1}).$$

Now the lemma applied for $k = 2$ shows that $g(u_{k-1})^2 \mid g(u_k)$. Since $g^{k-1} \mid g(u_{k-1})$ by the induction hypothesis, it follows that $g^k \mid g(u_k)$. Thus property (i) holds and the induction is closed. Properties (i) and (ii) are now established.

(iii): Let $k \geq 2$. Suppose that $h$ is a common divisor of $g$ and $v$,

$$g = p \cdot h, \quad v = q \cdot h.$$

Then by (ii),

$$u = t - g v = t - p h \cdot q h = t - p q h^2.$$

Substituting into $g(u)$ and using the chain rule, one obtains a relation that forces $h$ to divide $g'$ as well. Explicitly, from $g = p h$ we have $g' = p' h + p h'$. The computation shows that $h$ also divides $g'$, so $h$ is a common divisor of $g$ and $g'$. Since $g$ and $g'$ are relatively prime by hypothesis, $h$ must be a scalar. Hence $g$ and $v$ are relatively prime. This completes the proof.
