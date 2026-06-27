---
role: proof
locale: en
of_concept: normal-form-for-elliptic-hyperbolic-umbilics
source_book: gtm014
source_chapter: "VII"
source_section: "5. Umbilics"
---

We derive the normal form for the hyperbolic case; the elliptic case is similar with appropriate modifications. 

By choosing suitable coordinates, we may assume $f$ has the form $f(x_1, \ldots, x_n) = (h_1(x), h_2(x), x_3, \ldots, x_n)$. Since $x_0$ is an $S_2$ singularity, the 1-jet of $f$ vanishes in the first two coordinate directions, so $h_1, h_2$ have no linear terms in $x_1, x_2$. The transversality condition $j^1 f \pitchfork S_2$ implies that the quadratic parts of $h_1, h_2$ in $x_1, x_2$ are nondegenerate.

Using the Malgrange Preparation Theorem, we can write
$$x_1^2 = f^*\alpha_1 + f^*\beta_1 x_1 + f^*\gamma_1 x_2$$
$$x_2^2 = f^*\alpha_2 + f^*\beta_2 x_1 + f^*\gamma_2 x_2$$
where $\alpha_i, \beta_i, \gamma_i$ are smooth functions of $y$. By appropriate coordinate changes (replacing $x_1$ by $x_1 + f^*\beta_1/2$ and $x_2$ by $x_2 + f^*\gamma_2/2$), we can assume $\beta_1 = \gamma_2 = 0$. Setting $\gamma = -\gamma_1$ and $\beta = -\beta_2$ yields
$$f^*\alpha_1 = x_1^2 + f^*\gamma x_2$$
$$f^*\alpha_2 = x_2^2 + f^*\beta x_1.$$

Comparing quadratic terms and using the hyperbolicity condition, we obtain that $\alpha_1(y_1, y_2, 0, \ldots, 0) = y_1 + \cdots$ and $\alpha_2(y_1, y_2, 0, \ldots, 0) = y_2 + \cdots$, where the dots indicate higher order terms. The maps $(y_1, \ldots, y_n) \mapsto (\alpha_1(y), \alpha_2(y), y_3, \ldots, y_n)$ are legitimate coordinate changes by the inverse function theorem. After these coordinate changes, we obtain the canonical form.
