---
role: proof
locale: en
of_concept: hom-functors-left-exact
source_book: gtm013
source_chapter: "1"
source_section: "§16. The Hom Functors and Exactness—Projectivity and Injectivity"
---

We prove the contravariant case. Let $0 \to K \xrightarrow{f} M \xrightarrow{g} N \to 0$ be exact. If $\gamma \in Hom_R(N, U)$ and $0 = g^*(\gamma) = \gamma g$, then $\gamma = 0$ because $g$ is epic. Thus $g^*$ is monic. Since the Hom functors are additive we have $f^* g^* = (gf)^* = 0^* = 0$, so $Im(g^*) \subseteq Ker(f^*)$. If $\beta \in Ker(f^*)$, then $\beta f = f^*(\beta) = 0$, so $Ker(\beta) \supseteq Im(f) = Ker(g)$. By the Factor Theorem, $\beta$ factors through $g$. Therefore $\beta = \gamma g = g^*(\gamma) \in Im(g^*)$, proving $Im(g^*) = Ker(f^*)$. The covariant case follows similarly or by considering opposite rings.
