---
role: proof
locale: en
of_concept: irreducibility-of-xpe-minus-a
source_book: gtm028
source_chapter: "II"
source_section: "5. Separable and inseparable algebraic extension"
---

**Proof (first method, using derivatives).** The theorem is trivial if $e = 0$, for in that case $X^{p^e} - a = X - a$ and the condition $\sqrt[p]{a} \notin k$ is irrelevant. We now proceed by induction with respect to $e$.

Let $\varphi(X)$ be a monic irreducible factor of $X^{p^e} - a$ in $k[X]$ and let $[\varphi(X)]^h$ be the highest power of $\varphi(X)$ which divides $X^{p^e} - a$:

$$X^{p^e} - a = [\varphi(X)]^h \psi(X), \quad (\varphi(X), \psi(X)) = 1.$$

Taking derivatives of both sides and dividing by $[\varphi(X)]^{h-1}$, we obtain the identity

$$h\varphi'(X)\psi(X) + \varphi(X)\psi'(X) = 0,$$

and hence $\psi(X)$ divides the product $\varphi(X)\psi'(X)$. Since $\psi(X)$ and $\varphi(X)$ are relatively prime, we must have $\psi'(X) = 0$, for in the contrary case $\psi'(X)$ would be a non-zero polynomial of smaller degree than $\psi(X)$, and $\psi(X)$ could not divide $\psi'(X)$. We must therefore have simultaneously: $h\varphi'(X) = 0$ and $\psi'(X) = 0$.

The condition $\psi'(X) = 0$ implies that $\psi(X) \in k[X^p]$, i.e., $\psi(X) = [\psi_1(X)]^p$ for some $\psi_1(X) \in k[X]$. If $\psi(X)$ were non-constant, this would contradict the fact that $\psi$ is relatively prime to $\varphi$ (since $X^{p^e} - a$ would have a repeated factor). Therefore $\psi(X)$ is a constant, and since both $X^{p^e} - a$ and $\varphi(X)$ are monic, we have $h\varphi'(X) = 0$ with $h \neq 0$, whence $\varphi'(X) = 0$.

Thus $\varphi(X) \in k[X^p]$, so $\varphi(X) = \varphi_1(X^p)$ for some $\varphi_1(X) \in k[X]$. Then $X^{p^e} - a = [\varphi_1(X^p)]^h$. Substituting $Y = X^p$, we get $Y^{p^{e-1}} - a = [\varphi_1(Y)]^h$. By the induction hypothesis (or the case $e=0$ when $e=1$), $Y^{p^{e-1}} - a$ is irreducible, so $h = 1$ and $\varphi_1(Y)$ differs from $Y^{p^{e-1}} - a$ by a constant factor. Since both are monic, $\varphi_1(Y) = Y^{p^{e-1}} - a$, whence $\varphi(X) = X^{p^e} - a$. Thus $X^{p^e} - a$ is irreducible.

**Proof (second method, using extension fields).** There exists an algebraic extension $k'$ of $k$ such that $\varphi(X)$ has a root $\alpha$ in $k'$ (Theorem 3', §2). We have $a = \alpha^{p^e}$ and hence $X^{p^e} - a = (X - \alpha)^{p^e}$. It is now easy to see that $X^{p^e} - a$ is necessarily a power of $\varphi(X)$. For assume this is not the case, and let $\psi(X)$ be an irreducible factor of $X^{p^e} - a$ such that $(\varphi(X), \psi(X)) = 1$. Then we have an identity of the form $A(X)\varphi(X) + B(X)\psi(X) = 1$, where $A(X), B(X) \in k[X]$. Since $\psi(X)$ divides $(X - \alpha)^{p^e}$ in $k'[X]$, $\alpha$ is a root of $\psi(X)$, and hence the substitution $X \to \alpha$ in the above identity leads to a contradiction ($0 = 1$).

Since therefore $\varphi(X)$ is necessarily a power of $X - \alpha$, it follows that $X^{p^e} - a = [\varphi(X)]^{p^\rho}$, $\rho \geq 0$, and the fact that $\sqrt[p]{a} \notin k$ yields at once $\rho = 0$. Hence $X^{p^e} - a = \varphi(X)$, so $X^{p^e} - a$ is irreducible.
