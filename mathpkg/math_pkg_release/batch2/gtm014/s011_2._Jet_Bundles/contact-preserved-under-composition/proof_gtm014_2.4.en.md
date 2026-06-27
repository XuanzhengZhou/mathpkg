---
role: proof
locale: en
of_concept: contact-preserved-under-composition
source_book: gtm014
source_chapter: "2"
source_section: "2. Jet Bundles"
---

(1) We proceed by induction on $k$. For $k = 1$, $f \sim_1 g$ at $p$ means $(df)_p = (dg)_p$. By the chain rule, $d(h \circ f)_p = dh_{f(p)} \circ (df)_p = dh_{g(p)} \circ (dg)_p = d(h \circ g)_p$, since $f(p) = g(p) = q$. Hence $h \circ f \sim_1 h \circ g$ at $p$.

Assume the statement holds for $k - 1$. Suppose $f \sim_k g$ at $p$. This means $(df) \sim_{k-1} (dg)$ at every point of $T_p X$. Consider the differentials of the composites:

$$d(h \circ f) = dh \circ (df), \quad d(h \circ g) = dh \circ (dg).$$

Since $dh: TY \to TZ$ is a smooth map and $(df) \sim_{k-1} (dg)$ at every point of $T_p X$, the induction hypothesis applied to the maps $(df), (dg): TX \to TY$ and $dh: TY \to TZ$ yields $dh \circ (df) \sim_{k-1} dh \circ (dg)$ at every point of $T_p X$. Therefore $d(h \circ f) \sim_{k-1} d(h \circ g)$ at every point of $T_p X$, which means $h \circ f \sim_k h \circ g$ at $p$.

(2) Similarly by induction. For $k = 1$, $(df)_p = (dg)_p$ implies $(df)_p \circ (d\phi)_{\phi^{-1}(p)} = (dg)_p \circ (d\phi)_{\phi^{-1}(p)}$, so $d(f \circ \phi)_{\phi^{-1}(p)} = d(g \circ \phi)_{\phi^{-1}(p)}$.

Assume true for $k - 1$. If $f \sim_k g$ at $p$, then $(df) \sim_{k-1} (dg)$ on $T_p X$. The map $d\phi: TW \to TX$ is a diffeomorphism (since $\phi$ is a diffeomorphism). By the induction hypothesis with the diffeomorphism $d\phi$, we have $(df) \circ d\phi \sim_{k-1} (dg) \circ d\phi$ on $T_{\phi^{-1}(p)} W$. Hence $d(f \circ \phi) \sim_{k-1} d(g \circ \phi)$ on $T_{\phi^{-1}(p)} W$, giving $f \circ \phi \sim_k g \circ \phi$ at $\phi^{-1}(p)$.
