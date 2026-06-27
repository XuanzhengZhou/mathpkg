---
role: proof
locale: en
of_concept: local-diffeomorphism-extension
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

Since $\phi(0) = 0$, $\phi = (d\phi)_0 + \beta$ where $\beta$ is $O(|x|^2)$ near $0$. We first show that $\beta$ can be damped out off $K$. Let $\rho: \mathbb{R}^n \to \mathbb{R}$ be a smooth function such that $\rho \equiv 1$ on a nbhd of $0$ and $\rho \equiv 0$ off $K$. Consider $\tau = (d\phi)_0 + \rho\beta$. Clearly $\tau = \phi$ on a nbhd of $0$ and $\tau = (d\phi)_0$ off $K$. We wish to choose $\rho$ so that $\tau$ will be a diffeomorphism. By Lemma 5.2 it is enough to show that $\tau$ is an immersion.

Now for $v$ in $T_x\mathbb{R}^n = \mathbb{R}^n$,
$$|(d\tau)_x(v)| \geq |(d\phi)_0(v)| - |(d(\rho\beta))_x| \cdot |v| \geq (c - |(d(\rho\beta))_x|)|v|$$
where $c = |(d\phi)_0^{-1}|^{-1}$. Thus if we choose $\rho$ so that $|d(\rho\beta)| < c$, then $\tau$ will be an immersion.

Choose $\sigma: \mathbb{R}^n \to \mathbb{R}$ such that $\sigma \equiv 1$ on a nbhd of $0$ and $\mathrm{supp}\,\sigma \subset B(1) =$ ball of radius $1$ centered at the origin. Let $\rho(x) = \sigma(rx)$ for some positive constant $r$. Then $\rho \equiv 1$ on a nbhd of $0$ and $\mathrm{supp}\,\rho \subset B(1/r)$. By choosing $r$ large enough $\mathrm{supp}\,\rho \subset K$. Let $M = \sup |d\sigma|$. Then $rM \geq |d\rho|$. Since $\beta$ is $O(|x|^2)$ and $\mathrm{supp}\,\rho \subset B(1/r)$ there exist constants $e$ and $f$ so that $|\beta(x)| \leq e|x|^2$ and $|(d\beta)_x| \leq f|x|$ on $\mathrm{supp}\,\rho$. Thus
$$|(d(\rho\beta))| \leq |d\rho| \cdot |\beta| + |\rho| \cdot |d\beta| \leq (eM + f)/r.$$
Choose $r$ large enough so that $(eM + f)/r < c$.

Next we show that given a linear map $\alpha$ with $\det \alpha > 0$ there exists a diffeomorphism $g$ so that $g = \alpha$ on a nbhd of $0$ and $g = \mathrm{id}_{\mathbb{R}^n}$ outside of $K$. If $g$ exists, then $\eta = \alpha^{-1} \cdot g \cdot \tau$ is the desired diffeomorphism where $\alpha = (d\phi)_0$. (We use the hypothesis that $\det(d\phi)_0 > 0$ here.)

Moreover, it is sufficient to show that there exists a $\delta > 0$ so that $g$ exists whenever $|\alpha - I_n| < \delta$. For we may choose a curve $c: \mathbb{R} \to \mathrm{GL}(n, \mathbb{R})$ so that $c(0) = I_n$ and $c(1) = \alpha$ using Lemma 5.4. Also, since $[0,1]$ is compact there exist points $t_0 = 0 < t_1 < \cdots < t_k = 1$ such that $|c(t_i) \cdot c(t_{i-1})^{-1} - I_n| < \delta$ for $1 \leq i \leq k$. Let $g_i$ be the diffeomorphism associated with $c(t_i) \cdot c(t_{i-1})^{-1}$, then $g = g_k \cdots g_1$ is the desired diffeomorphism.

Let $\rho: \mathbb{R}^n \to \mathbb{R}$ be a smooth function such that $\rho \equiv 1$ on a nbhd of $0$ and $\rho \equiv 0$ off $K$, then consider $g = I_n + \rho(\alpha - I_n)$. Clearly $g = \alpha$ near $0$ and $g = I_n$ off $K$. Using Lemma 5.2 again, we need only show that $g$ is an immersion to see that $g$ is a diffeomorphism. Indeed
$$|(dg)_x(v)| \geq |v| - (|(d\rho)_x| + |\rho(x)|)|\alpha - I_n| \cdot |v|.$$
Thus if we choose $\delta < 1/\sup(|d\rho| + |\rho|)$, then whenever $|\alpha - I_n| < \delta$, the associated $g$ will be an immersion.
