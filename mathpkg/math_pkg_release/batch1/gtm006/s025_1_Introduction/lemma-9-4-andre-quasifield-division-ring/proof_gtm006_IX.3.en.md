---
role: proof
locale: en
of_concept: lemma-9-4-andre-quasifield-division-ring
source_book: gtm006
source_chapter: "IX"
source_section: "3"
---

The implications (ii) $\Rightarrow$ (i), (iii) $\Rightarrow$ (i), and (ii) $\Leftrightarrow$ (iii) are clear.

(iv) $\Rightarrow$ (iii): If $k^{\phi} = \varepsilon$ for all $k \in N$, then for any $x \in F^*$, $x^{\bar{\alpha}} = x^{\nu\phi}$. Since $\phi$ is trivial on $N = (F^*)^{\nu}$, we have $x^{\bar{\alpha}} = \varepsilon$ for all $x$, meaning $x^{\bar{\alpha}}$ is the identity automorphism. Thus $x \odot y = xy^1 = xy$, so multiplication in $F_{\phi}$ coincides with multiplication in $F$, and $F_{\phi} \cong F$.

(i) $\Rightarrow$ (iv): Suppose $F_{\phi}$ is a division ring. Then $F_{\phi}$ satisfies the right distributive law. For all $a, b, x \in F^*$:

$$a \odot x + b \odot x = (a + b) \odot x,$$

which, using the definition of $\odot$, becomes:

$$ax^{\bar{\alpha}_a} + bx^{\bar{\alpha}_b} = (a + b)x^{\bar{\alpha}_{a+b}},$$

where $\bar{\alpha}_a$ denotes the image of $a$ under $\alpha = \nu\phi$.

Regarding $a$ and $b$ as fixed, this is an identity in $x$. Replace $x$ by $xy$:

$$a (xy)^{\bar{\alpha}_a} + b (xy)^{\bar{\alpha}_b} = (a + b)(xy)^{\bar{\alpha}_{a+b}}.$$

Since each $\bar{\alpha}$ is a field automorphism, $(xy)^{\bar{\alpha}} = x^{\bar{\alpha}} y^{\bar{\alpha}}$, giving:

$$a x^{\bar{\alpha}_a} y^{\bar{\alpha}_a} + b x^{\bar{\alpha}_b} y^{\bar{\alpha}_b} = (a + b) x^{\bar{\alpha}_{a+b}} y^{\bar{\alpha}_{a+b}}.$$

Using the original identity, the left side equals $[(a + b)x^{\bar{\alpha}_{a+b}}]y^{\bar{\alpha}_{a+b}}$ only if $\bar{\alpha}_a = \bar{\alpha}_b = \bar{\alpha}_{a+b}$ for the $y$-exponents to match. More precisely, comparing the expressions forces $\bar{\alpha}_a = \bar{\alpha}_b$ for all $a, b \in F^*$.

In particular, taking $b = 1$, we get $\bar{\alpha}_a = \bar{\alpha}_1 = \varepsilon$ (since $1$ maps to the identity). Thus $a^{\bar{\alpha}} = a^{\varepsilon} = a$ for all $a$. This means $k^{\phi} = \varepsilon$ for all $k \in N$, which is condition (iv).
