---
role: proof
locale: en
of_concept: alternative-implies-inverse-property
source_book: gtm006
source_chapter: "6"
source_section: "7. The Skornyakov-San Soucie Theorem"
---

**Proof of Theorem 6.17.** By definition of $k$, we have $k(w, x, y, y) = 0$ for all $w, x, y$ in an alternative division ring (since $[wx, y, y] = [x, y, y] = [w, y, y] = 0$ by the right alternative law). Hence by Lemma (19), $k(w, x, y, z) = 0$ whenever any two arguments are equal. Thus,
$$0 = k(z, x, y, z) = [zx, y, z] - [x, y, z]z - x[z, y, z].$$

By the alternating property of the associator (Lemma 18), $[z, y, z] = -[z, y, z] = 0$ in an alternative division ring. We then have $[zx, y, z] = [x, y, z] z$.

Now let $a'$ be the inverse of $a$ (so $aa' = 1$). Then
$$0 = [1, a, b] = [aa', a, b] = [a', a, b] a,$$
where the last equality uses $[zx, y, z] = [x, y, z] z$ with $z = a$, $x = a'$, $y = a$.

Since $a \neq 0$, this means $[a', a, b] = 0$. Moreover, by Lemma (18),
$$[a', a, b] = -[b, a, a']$$
so we have $[b, a, a'] = 0$ and hence $(ba)a' = b(aa') = b \cdot 1 = b$.

This establishes the right inverse property: $(ba)a^{-1} = b$. A symmetric argument (using the alternating property and the fact that alternative rings are also left alternative) gives the left inverse property $a^{-1}(ab) = b$. Thus $D$ has the inverse property. $\square$
