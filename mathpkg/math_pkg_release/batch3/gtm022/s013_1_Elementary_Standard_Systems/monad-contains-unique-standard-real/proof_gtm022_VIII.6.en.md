---
role: proof
locale: en
of_concept: monad-contains-unique-standard-real
source_book: gtm022
source_chapter: "VIII"
source_section: "6"
---

If $r, s \in \mu(a)$ and $r, s$ are standard, then $|r - s|$ is an infinitesimal standard real number. Since the only standard infinitesimal real is $0$, we have $|r - s| = 0$ and $r = s$. This proves uniqueness.

For existence: we must show there is a standard real number in $\mu(a)$. If $a$ is standard, this is trivial. Otherwise, let $u = \{x \in \mathbb{R} \mid x < a\}$. Since $a$ is finite, $u$ is bounded above in $\mathbb{R}$. Let $r = \sup u$. Then for any standard $\varepsilon > 0$, we have $r - \varepsilon < a < r + \varepsilon$, so $|a - r| < \varepsilon$, showing $a \cong r$ and $r \in \mu(a)$.

The ring properties of $R_0$ and the ideal properties of $R_1$ follow directly from the definitions: sums and products of finite numbers are finite, and the product of an infinitesimal with a finite number is infinitesimal. The isomorphism $R_0/R_1 \cong \mathbb{R}$ is given by the map sending each monad to its unique standard representative.
