---
role: proof
locale: en
of_concept: splitting-field-is-finite-normal-extension
source_book: gtm028
source_chapter: "II"
source_section: "6. Splitting fields and normal extensions"
---

Let $K$ be a splitting field, over $k$, of a polynomial $f(X)$ in $k[X]$ and let $\varphi(X)$ be any irreducible polynomial in $k[X]$ which has a root $\alpha$ in $K$. We fix a splitting field $K'$ of $\varphi(X)$ over $K$. Let $\beta$ be any root of $\varphi(X)$ in $K'$. Since $\varphi(X)$ is irreducible over $k$, we have a $k$-isomorphism $\tau$ between $k(\alpha)$ and $k(\beta)$ which sends $\alpha$ into $\beta$. This isomorphism leaves $f(X)$ invariant (since the coefficients of $f$ are in $k$), and on the other hand the fields $K$ and $K(\beta)$ are splitting fields of $f(X)$ respectively over $k(\alpha)$ and $k(\beta)$ (since $k(\alpha) \subset K$, $k(\beta) \subset K(\beta)$ and $K = k(x_1, x_2, \cdots, x_n)$). Hence, by Theorem 12, the isomorphism $\tau$ of $k(\alpha)$ onto $k(\beta)$ can be extended to an isomorphism $\rho$ of $K$ onto $K(\beta)$. We are dealing here with an isomorphism $\rho$ of $K$ into a field containing $K$, namely into $K'$. Since $\rho$ is also a $k$-isomorphism and since the polynomial $f(X)$, whose coefficients are in $k$, factors completely in $K[X]$ into linear factors, it follows that $\rho$ must transform onto itself the set of roots of $f(X)$ in $K$. Since the roots of $f(X)$ in $K$ generate $K$ over $k$, it follows that $\rho$ is an automorphism of $K$. Since $\alpha \in K$ and $\alpha\rho = \beta$, we have $\beta \in K$. We have thus shown that every root $\beta$ of $\varphi(X)$ lies in $K$, so $\varphi(X)$ factors completely in $K[X]$. Therefore $K$ is normal over $k$.
