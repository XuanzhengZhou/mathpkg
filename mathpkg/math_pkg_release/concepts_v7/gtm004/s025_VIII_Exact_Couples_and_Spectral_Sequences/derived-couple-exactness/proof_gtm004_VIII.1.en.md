---
role: proof
locale: en
of_concept: derived-couple-exactness
source_book: gtm004
source_chapter: "VIII"
source_section: "1. Exact Couples and Spectral Sequences"
---

# Proof of Derived Couple Exactness (Theorem 1.1)

Let $\mathfrak{A}$ be an abelian category and let $EC = \{D, E, \alpha, \beta, \gamma\}$ be an exact couple in $\mathfrak{A}$. Thus we have an exact triangle

$$\begin{CD}
D @>\alpha>> D \\
@A\gamma AA @VV\beta V \\
E
\end{CD}$$

with $\operatorname{im} \alpha = \ker \beta$, $\operatorname{im} \beta = \ker \gamma$, $\operatorname{im} \gamma = \ker \alpha$, and consequently $\beta\alpha = 0$, $\gamma\beta = 0$, $\alpha\gamma = 0$.

Set $d_0 = \beta\gamma : E \to E$. Then $d_0^2 = \beta\gamma\beta\gamma = 0$, so $(E, d_0)$ is a differential object. Define the **derived couple** $EC' = \{D_1, E_1, \alpha_1, \beta_1, \gamma_1\}$ by:

- $D_1 = \alpha D = \operatorname{im} \alpha = \ker \beta$;
- $E_1 = H(E, d_0) = \ker d_0 / \operatorname{im} d_0$;
- $\alpha_1 = \alpha|_{D_1} : D_1 \to D_1$ (note that $\alpha(D_1) = \alpha^2 D \subseteq \alpha D = D_1$);
- $\beta_1(\alpha x) = [\beta x]$, where $[z]$ denotes the homology class of the cycle $z \in \ker d_0$;
- $\gamma_1[z] = \gamma(z)$.

The maps $\beta_1$ and $\gamma_1$ are well-defined:

- For $\beta_1$: $\beta x$ is a cycle because $d_0(\beta x) = \beta\gamma\beta x = 0$. If $\alpha x = 0$, then $x \in \ker \alpha = \operatorname{im} \gamma$, so $x = \gamma y$ for some $y \in E$. Then $\beta x = \beta\gamma y = d_0 y$, which is a boundary, so $[\beta x] = 0$. Hence $[\beta x]$ depends only on $\alpha x$.
- For $\gamma_1$: If $[z] \in E_1$, then $d_0 z = \beta\gamma z = 0$, so $\gamma z \in \ker \beta = D_1$. If $z = d_0 y = \beta\gamma y$ is a boundary, then $\gamma z = \gamma\beta\gamma y = 0$. Hence $\gamma(z)$ depends only on $[z]$.

We must now prove that the derived couple $EC'$ is exact.

### 1. Exactness at $D_1$ (top left): $\ker \alpha_1 = \operatorname{im} \gamma_1$

First, $\alpha_1 \gamma_1[z] = \alpha\gamma(z) = 0$, so $\operatorname{im} \gamma_1 \subseteq \ker \alpha_1$.

Conversely, let $x \in D_1 = \alpha D$ satisfy $\alpha_1 x = \alpha x = 0$. Then $x \in \ker \alpha = \operatorname{im} \gamma$, so $x = \gamma y$ for some $y \in E$. Since $x \in D_1 = \ker \beta$, we have $\beta x = \beta\gamma y = d_0 y = 0$, so $y$ is a cycle of $(E, d_0)$. Hence $x = \gamma y = \gamma_1[y] \in \operatorname{im} \gamma_1$.

### 2. Exactness at $D_1$ (domain of $\beta_1$): $\ker \beta_1 = \operatorname{im} \alpha_1$

First, $\beta_1(\alpha_1(\alpha x)) = \beta_1(\alpha(\alpha x)) = [\beta(\alpha x)] = [0] = 0$, so $\operatorname{im} \alpha_1 \subseteq \ker \beta_1$.

Conversely, let $\alpha x \in D_1$ satisfy $\beta_1(\alpha x) = [\beta x] = 0$. Then $\beta x$ is a boundary, so $\beta x = d_0 y = \beta\gamma y$ for some $y \in E$. Hence $\beta(x - \gamma y) = 0$, so $x - \gamma y \in \ker \beta = \operatorname{im} \alpha$. Write $x - \gamma y = \alpha w$ for some $w \in D$. Then

$$\alpha x = \alpha(x - \gamma y) + \alpha\gamma y = \alpha^2 w + 0 = \alpha_1(\alpha w) \in \operatorname{im} \alpha_1.$$

### 3. Exactness at $E_1$: $\ker \gamma_1 = \operatorname{im} \beta_1$

First, $\gamma_1(\beta_1(\alpha x)) = \gamma_1([\beta x]) = \gamma\beta x = 0$, so $\operatorname{im} \beta_1 \subseteq \ker \gamma_1$.

Conversely, let $[z] \in E_1$ satisfy $\gamma_1[z] = \gamma z = 0$. Then $z \in \ker \gamma = \operatorname{im} \beta$, so $z = \beta x$ for some $x \in D$. Then

$$[z] = [\beta x] = \beta_1(\alpha x) \in \operatorname{im} \beta_1,$$

where we note that $\beta x$ is indeed a cycle (since $d_0(\beta x) = \beta\gamma\beta x = 0$) and $\alpha x \in D_1$. This completes the proof that the derived couple is exact.
