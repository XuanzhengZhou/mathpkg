---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.1"
proof_technique: diagram-chase
locale: en
content_hash: ""
written_against: ""
---
(i) Suppose $\alpha$ and $\gamma$ are monomorphisms. To show $\beta$ is a monomorphism, assume $\beta(b) = 0$ for $b \in B$. Then $\gamma g(b) = g'\beta(b) = 0$. Since $\gamma$ is mono, $g(b) = 0$, so $b \in \operatorname{Ker} g = \operatorname{Im} f$. Write $b = f(a)$ for $a \in A$. Then $f'\alpha(a) = \beta f(a) = \beta(b) = 0$. Since $f'$ is mono and $\alpha$ is mono, $a = 0$, so $b = f(0) = 0$. Hence $\beta$ is mono.

(ii) Suppose $\alpha$ and $\gamma$ are epimorphisms. Let $b' \in B'$. Then $g'(b') \in C'$. Since $\gamma$ is epi, $g'(b') = \gamma(c)$ for some $c \in C$. Since $g$ is epi, $c = g(b)$ for some $b \in B$. Then $g'\beta(b) = \gamma g(b) = \gamma(c) = g'(b')$, so $g'(\beta(b) - b') = 0$. Thus $\beta(b) - b' \in \operatorname{Ker} g' = \operatorname{Im} f'$, say $\beta(b) - b' = f'(a')$ for $a' \in A'$. Since $\alpha$ is epi, $a' = \alpha(a)$ for some $a \in A$. Consider $b - f(a) \in B$: $\beta(b - f(a)) = \beta(b) - \beta f(a) = \beta(b) - f'\alpha(a) = \beta(b) - f'(a') = b'$. Hence $\beta$ is epi.

(iii) is an immediate consequence of (i) and (ii).
