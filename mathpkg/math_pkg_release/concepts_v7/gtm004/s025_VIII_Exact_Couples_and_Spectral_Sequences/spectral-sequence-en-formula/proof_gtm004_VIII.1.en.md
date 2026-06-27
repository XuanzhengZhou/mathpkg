---
role: proof
locale: en
of_concept: spectral-sequence-en-formula
source_book: gtm004
source_chapter: "VIII"
source_section: "1. Exact Couples and Spectral Sequences"
---

# Proof of the Formula for Terms of a Spectral Sequence (Theorem 1.2)

Let $EC = \{D, E, \alpha, \beta, \gamma\}$ be an exact couple in an abelian category $\mathfrak{A}$, with exact triangle

$$\begin{CD}
D @>\alpha>> D \\
@A\gamma AA @VV\beta V \\
E
\end{CD}$$

Let $E = \{(E_n, d_n)\}_{n \geq 0}$ be the spectral sequence obtained by iterating the derived couple construction. Recall that $E_0 = E$, $d_0 = \beta\gamma$, and the $n$-th derived couple is $EC^{(n)} = \{D_n, E_n, \alpha_n, \beta_n, \gamma_n\}$ with $D_n = \alpha^n D$.

**Theorem 1.2.** For each $n \geq 0$,

$$E_n = \gamma^{-1}(\alpha^n D) / \beta(\alpha^{-n}(0)),$$

and the differential $d_n : E_n \to E_n$ is induced by $\beta\alpha^{-n}\gamma$.

Here the notation means:
- $\gamma^{-1}(\alpha^n D) = \{z \in E : \gamma(z) \in \alpha^n D\}$,
- $\alpha^{-n}(0) = \{x \in D : \alpha^n x = 0\}$,
- $\beta(\alpha^{-n}(0)) = \{\beta x : x \in D, \; \alpha^n x = 0\} \subseteq \gamma^{-1}(\alpha^n D)$,
and $\beta\alpha^{-n}\gamma$ denotes the map sending $z \in \gamma^{-1}(\alpha^n D)$ to $\beta x$, where $x \in D$ is such that $\gamma(z) = \alpha^n x$.

**Proof.** We proceed by induction on $n$.

**Base case $n = 0$.** By convention $\alpha^0 = \operatorname{id}_D$, so $\gamma^{-1}(\alpha^0 D) = \gamma^{-1}(D) = E$ (since $\gamma$ maps into $D$). Also $\alpha^0(0) = 0$, so $\beta(\alpha^0(0)) = \beta(0) = 0$. Thus the formula gives $E / 0 = E = E_0$, and $d_0 = \beta \alpha^0 \gamma = \beta \gamma$, which agrees with the definition.

**Inductive step.** Assume the formula holds for $n$. We compute $E_{n+1} = H(E_n, d_n)$ using the derived couple construction applied to $EC^{(n)} = \{D_n, E_n, \alpha_n, \beta_n, \gamma_n\}$.

By the induction hypothesis, an element of $E_n$ is represented by some $z \in \gamma^{-1}(\alpha^n D)$, i.e., $\gamma(z) = \alpha^n x$ for some $x \in D$. Two such elements $z_1, z_2$ represent the same class in $E_n$ if and only if $z_1 - z_2 \in \beta(\alpha^{-n}(0))$, i.e., $z_1 - z_2 = \beta w$ with $\alpha^n w = 0$.

The differential $d_n$ is induced by $\beta\alpha^{-n}\gamma$: for $z \in \gamma^{-1}(\alpha^n D)$ with $\gamma(z) = \alpha^n x$, we have $d_n[z] = [\beta x]$, where the bracket denotes the class in $E_n$.

Now $E_{n+1} = \ker d_n / \operatorname{im} d_n$. A class $[z] \in E_n$ lies in $\ker d_n$ precisely when $d_n[z] = 0$, i.e., $[\beta x] = 0$ in $E_n$. By the induction hypothesis, this means $\beta x \in \beta(\alpha^{-n}(0))$, so $\beta x = \beta w$ for some $w \in D$ with $\alpha^n w = 0$. Equivalently, $x - w \in \ker \beta = \operatorname{im} \alpha = \alpha D$, and since $\alpha^n w = 0$, the condition translates to the existence of $u \in D$ with $\gamma(z) = \alpha^{n+1} u$. Thus $z \in \gamma^{-1}(\alpha^{n+1} D)$.

Hence $\ker d_n$ consists of those classes $[z]$ where $z \in \gamma^{-1}(\alpha^{n+1} D)$.

Now consider $\operatorname{im} d_n$. A class in $\operatorname{im} d_n$ is represented by $z = \beta x$ where $\gamma(\beta x) \in \alpha^n D$ (so that $\beta x \in \gamma^{-1}(\alpha^n D)$) and there exists a pre-image, say $y \in \gamma^{-1}(\alpha^n D)$ with $\gamma(y) = \alpha^n v$, such that $d_n[y] = [\beta v] = [z] = [\beta x]$. This means $\beta x - \beta v \in \beta(\alpha^{-n}(0))$, i.e., $x - v \in \alpha^{-n}(0) + \ker \beta$.

More systematically, the elements of $\operatorname{im} d_n$ in $E_n$ are those of the form $[\beta x]$ where $x \in D$ satisfies $\gamma(\beta x) \in \alpha^n D$ (automatically true since $\gamma\beta = 0 \in \alpha^n D$) and there exists $y$ with $\gamma(y) = \alpha^n x$ such that $d_n[y] = [\beta x]$. This condition simply means that $\beta x \in \operatorname{im} d_n$ if and only if there exists $y \in \gamma^{-1}(\alpha^n D)$ with $d_n[y] = [\beta x]$. Since we can always take $y$ with $\gamma(y) = \alpha^n x$ (this is the definition of representing the element), we need to check: when is $[\beta x]$ representable as $d_n[y]$ for some $y$ whose image under $\gamma$ lands in $\alpha^n D$?

Actually, a cleaner argument: the subset $\beta(\alpha^{-n-1}(0))$ is contained in $\gamma^{-1}(\alpha^{n+1} D)$, because if $x \in \alpha^{-n-1}(0)$, then $\alpha^{n+1} x = 0$, so $0 = \gamma(\beta x) \in \alpha^{n+1} D$ trivially, hence $\beta x \in \gamma^{-1}(\alpha^{n+1} D)$.

We claim that the denominator in the quotient description advances from $\beta(\alpha^{-n}(0))$ to $\beta(\alpha^{-n-1}(0))$. Indeed, elements of $\operatorname{im} d_n$ are precisely those classes $[z] \in E_n$ where $z \in \beta(\alpha^{-n-1}(0))$ modulo $\beta(\alpha^{-n}(0))$.

To verify: if $z \in \beta(\alpha^{-n-1}(0))$, write $z = \beta x$ with $\alpha^{n+1} x = 0$. Then $\gamma(z) = 0 \in \alpha^n D$, so $z \in \gamma^{-1}(\alpha^n D)$ and $[z]$ is a class in $E_n$. We must show $[z] = d_n[y]$ for some $y$. Note that $\alpha(\alpha^n x) = 0$, so $\alpha^n x \in \ker \alpha = \operatorname{im} \gamma$. Choose $y \in E$ with $\gamma(y) = \alpha^n x$. Then $y \in \gamma^{-1}(\alpha^n D)$, and $d_n[y] = [\beta x] = [z]$.

Conversely, if $d_n[y] \in \operatorname{im} d_n$, write $\gamma(y) = \alpha^n v$ for some $v \in D$. Then $d_n[y] = [\beta v]$. Now we must have $[\beta v] \in \ker d_n$, i.e., $\beta v \in \gamma^{-1}(\alpha^{n+1} D)$, which means $0 = \gamma\beta v \in \alpha^{n+1} D$ (always true), so actually the additional condition is that $\gamma(\beta v) = \alpha^{n+1} w$ for some $w$, but $\gamma\beta v = 0$, so $w = 0$ works. So $\beta v$ needs $\alpha^{n+1} v = 0$ for the boundary to be in $\beta(\alpha^{-n-1}(0))$.

Wait—let me restructure this more carefully.

The formula for $E_{n+1}$ as the homology of $(E_n, d_n)$ is:

$$E_{n+1} = \frac{\{z \in \gamma^{-1}(\alpha^n D) : \beta\alpha^{-n}\gamma(z) \in \beta(\alpha^{-n}(0)) \text{ in } E_n\}}{\beta(\alpha^{-n}(0)) + \operatorname{im}(\beta\alpha^{-n}\gamma)}.$$

The condition $\beta\alpha^{-n}\gamma(z) \in \beta(\alpha^{-n}(0))$ in $E_n$ means that, writing $\gamma(z) = \alpha^n x$, we have $\beta x = \beta w$ for some $w$ with $\alpha^n w = 0$. Thus $x - w \in \ker \beta = \operatorname{im} \alpha$, so $x = w + \alpha u$. Then $\gamma(z) = \alpha^n(w + \alpha u) = \alpha^n w + \alpha^{n+1} u = \alpha^{n+1} u$, since $\alpha^n w = 0$. Therefore $z \in \gamma^{-1}(\alpha^{n+1} D)$. This establishes $\ker d_n \cong \gamma^{-1}(\alpha^{n+1} D) / \beta(\alpha^{-n}(0))$ (modulo the existing denominator).

Similarly, one checks that the image of $d_n$ corresponds precisely to those classes coming from $\beta(\alpha^{-n-1}(0))$ modulo $\beta(\alpha^{-n}(0))$.

Passing to the quotient, we obtain

$$E_{n+1} = \frac{\gamma^{-1}(\alpha^{n+1} D) / \beta(\alpha^{-n}(0))}{\beta(\alpha^{-n-1}(0)) / \beta(\alpha^{-n}(0))} \cong \frac{\gamma^{-1}(\alpha^{n+1} D)}{\beta(\alpha^{-n-1}(0))},$$

which is the formula for index $n+1$. The description of $d_{n+1}$ as induced by $\beta\alpha^{-n-1}\gamma$ follows from the construction of the derived couple applied to $EC^{(n+1)}$: writing $\gamma(z) = \alpha^{n+1} x$ for $z \in \gamma^{-1}(\alpha^{n+1} D)$, the $(n+1)$-st differential sends $[z]$ to $[\beta x]$.

**Consequences.** Formula (1.5) gives the exact sequence

$$\alpha^n D \xrightarrow{\alpha_n} \alpha^n D \xrightarrow{\beta_n} E_n \xrightarrow{\gamma_n} \alpha^n D \xrightarrow{\alpha_n} \alpha^n D,$$

where $\alpha_n = \alpha|_{\alpha^n D}$, $\beta_n$ is induced by $\beta\alpha^{-n}$, and $\gamma_n$ is induced by $\gamma$. This yields the short exact sequence

$$0 \to \operatorname{coker} \alpha_n \xrightarrow{\bar{\beta}_n} E_n \xrightarrow{\bar{\gamma}_n} \ker \alpha_n \to 0,$$

with $\operatorname{coker} \alpha_n = \alpha^n D / \alpha^{n+1} D$ and $\ker \alpha_n = \alpha^n D \cap \alpha^{-1}(0)$. $\square$
