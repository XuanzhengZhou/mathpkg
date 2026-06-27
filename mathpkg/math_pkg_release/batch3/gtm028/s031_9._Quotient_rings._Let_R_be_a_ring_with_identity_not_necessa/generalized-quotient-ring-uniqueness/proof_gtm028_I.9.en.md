---
role: proof
locale: en
of_concept: generalized-quotient-ring-uniqueness
source_book: gtm028
source_chapter: "I"
source_section: "9. Quotient rings"
---

Let $\mathfrak{n} = \{ x \in R \mid \exists m \in M,\; xm = 0 \}$. By condition (1) for both $h$ and $f$, we have $\ker h = \ker f = \mathfrak{n}$. Since $h(R) \cong R/\mathfrak{n}$ (by the first isomorphism theorem), and similarly $f(R) \cong R/\mathfrak{n}$, there is an isomorphism $\bar{f}: h(R) \to f(R)$ defined by $\bar{f}(h(x)) = f(x)$ for $x \in R$.

Now $R_M$ is the quotient ring of $h(R)$ with respect to the regular multiplicative system $h(M)$ in $h(R)$ (since $\ker h = \mathfrak{n}$ has been factored out, making $h(M)$ regular). Similarly, $S$ is the quotient ring of $f(R)$ with respect to the regular multiplicative system $f(M)$ in $f(R)$.

The isomorphism $\bar{f}: h(R) \to f(R)$ maps the multiplicative system $h(M)$ onto $f(M)$. By the universal property of quotient rings in the regular case, $\bar{f}$ extends uniquely to an isomorphism $f': R_M \to S$ on the quotient rings. Explicitly, for any element $h(x)/h(m) \in R_M$ (with $x \in R$, $m \in M$), we set

$$
f'\left( \frac{h(x)}{h(m)} \right) = \frac{\bar{f}(h(x))}{\bar{f}(h(m))} = \frac{f(x)}{f(m)}.
$$

This is well-defined because $\bar{f}$ is an isomorphism and maps $h(M)$ onto $f(M)$. The map $f'$ is an isomorphism onto $S$ since every element of $S$ is, by condition (3) for $f$, of the form $f(x)/f(m)$, and $f(x)/f(m) = f'(h(x)/h(m))$.

Finally, for any $x \in R$, we have $(h \circ f')(x) = f'(h(x)) = f(x)/f(1) = f(x)$, where $1 \in M$ (since $M$ is non-empty and closed under multiplication, it contains the identity if $R$ has one; otherwise we interpret $f(x)/f(1)$ via the canonical identification). Thus $f = h \circ f'$.
