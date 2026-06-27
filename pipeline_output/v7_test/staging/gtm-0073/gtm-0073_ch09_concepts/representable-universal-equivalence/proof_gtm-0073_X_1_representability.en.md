---
role: proof
source_book: gtm-0073
chapter: X
section: "X.1"
proof_technique: bijection-construction
locale: en
content_hash: ""
written_against: ""
---
Suppose $(A, \alpha)$ is a representation of $T$. Let $u = \alpha_A(1_A) \in T(A)$. We claim that $(A, u)$ is a universal element of $T$. Let $(B, s)$ be an object of $\mathcal{C}_T$, i.e., $s \in T(B)$. Then $\alpha_B : \hom_{\mathcal{C}}(A, B) \to T(B)$ is a bijection, so there exists a unique $f \in \hom_{\mathcal{C}}(A, B)$ such that $\alpha_B(f) = s$. By Lemma 1.5, $\alpha_B(f) = T(f)(u) = s$, whence $f$ is a morphism $(A, u) \to (B, s)$ in $\mathcal{C}_T$. If $g$ is another such morphism, then $T(g)(u) = s = T(f)(u)$, so $\alpha_B(g) = \alpha_B(f)$, and bijectivity of $\alpha_B$ forces $f = g$. Thus $(A, u)$ is universal.

Conversely, let $(A, u)$ be a universal element. Define $\beta : h_A \to T$ by $\beta_C(f) = T(f)(u)$ for $f \in \hom_{\mathcal{C}}(A, C)$. By Lemma 1.5(ii), $\beta$ is a natural transformation. For any $s \in T(C)$, $(C, s) \in \mathcal{C}_T$, so universality gives $f \in \hom_{\mathcal{C}}(A, C)$ with $s = T(f)(u) = \beta_C(f)$, proving $\beta_C$ surjective. If $\beta_C(f_1) = \beta_C(f_2)$, then $T(f_1)(u) = T(f_2)(u)$, so both $f_1$ and $f_2$ are morphisms $(A, u) \to (C, T(f_1)(u))$ in $\mathcal{C}_T$, and universality forces $f_1 = f_2$. Thus each $\beta_C$ is bijective, so $\beta$ is a natural isomorphism and $(A, \beta)$ represents $T$.
