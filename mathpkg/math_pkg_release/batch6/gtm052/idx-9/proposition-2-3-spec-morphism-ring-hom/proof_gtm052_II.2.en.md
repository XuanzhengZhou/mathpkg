---
role: proof
locale: en
of_concept: proposition-2-3-spec-morphism-ring-hom
source_book: gtm052
source_chapter: "II"
source_section: "2"
---

(a) This follows from Proposition 2.2(a).

(b) Given a homomorphism $\varphi: A \to B$, define $f: \text{Spec } B \to \text{Spec } A$ by $f(\mathfrak{p}) = \varphi^{-1}(\mathfrak{p})$ for any $\mathfrak{p} \in \text{Spec } B$. If $\mathfrak{a}$ is an ideal of $A$, then $f^{-1}(V(\mathfrak{a})) = V(\varphi(\mathfrak{a}))$, so $f$ is continuous.

For each $\mathfrak{p} \in \text{Spec } B$, we define a local homomorphism of local rings $f^\#_\mathfrak{p}: \mathcal{O}_{\text{Spec } A, f(\mathfrak{p})} \to \mathcal{O}_{\text{Spec } B, \mathfrak{p}}$. Using Proposition 2.2(a), these stalks are $A_{\varphi^{-1}(\mathfrak{p})}$ and $B_\mathfrak{p}$. The ring homomorphism $\varphi$ induces a natural homomorphism $A_{\varphi^{-1}(\mathfrak{p})} \to B_\mathfrak{p}$ by the universal property of localization, which is a local homomorphism. These stalk maps glue to give a sheaf morphism $f^\#: \mathcal{O}_{\text{Spec } A} \to f_*\mathcal{O}_{\text{Spec } B}$.

(c) Let $(f, f^\#): (\text{Spec } B, \mathcal{O}_{\text{Spec } B}) \to (\text{Spec } A, \mathcal{O}_{\text{Spec } A})$ be a morphism of locally ringed spaces. Taking global sections gives a ring homomorphism $\varphi = \Gamma(f^\#): A = \Gamma(\text{Spec } A, \mathcal{O}_{\text{Spec } A}) \to \Gamma(\text{Spec } B, \mathcal{O}_{\text{Spec } B}) = B$, using Proposition 2.2(c).

For any $\mathfrak{p} \in \text{Spec } B$, consider the stalk map $f^\#_\mathfrak{p}: A_{f(\mathfrak{p})} \to B_\mathfrak{p}$. By the definition of a locally ringed space morphism, this is a local homomorphism. Tracing through the definition shows that $f(\mathfrak{p}) = \varphi^{-1}(\mathfrak{p})$. Since $f^\#$ is a local homomorphism, it follows that $\varphi^{-1}(\mathfrak{p}) = f(\mathfrak{p})$, which shows that $f$ coincides with the map $\text{Spec } B \to \text{Spec } A$ induced by $\varphi$. Then $f^\#$ is also induced by $\varphi$, so the morphism $(f, f^\#)$ comes from the ring homomorphism $\varphi$.

Note: Statement (c) would be false if we did not require that the induced maps on stalks be local homomorphisms (see Caution 2.3.0).
