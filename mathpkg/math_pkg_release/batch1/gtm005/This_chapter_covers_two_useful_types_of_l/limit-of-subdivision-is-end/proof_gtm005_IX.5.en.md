---
role: proof
locale: en
of_concept: limit-of-subdivision-is-end
source_book: gtm005
source_chapter: "IX"
source_section: "5"
---

For $S: C^{\mathrm{op}} \times C \to X$, the end $\int_c S(c, c)$ can be computed as a limit over the subdivision (twisted arrow) category $C^{\S}$.

Objects of $C^{\S}$ are arrows $f: a \to b$ in $C$. A morphism from $f: a \to b$ to $f': a' \to b'$ is a pair $(h: a' \to a, k: b \to b')$ with $k \circ f \circ h = f'$. Define $\tilde{S}: C^{\S} \to X$ by $\tilde{S}(f: a \to b) = S(a, b)$.

A wedge $\tau: x \xrightarrow{\bullet} S$ assigns to each $c$ a component $\tau_c: x \to S(c, c)$. For each arrow $f: a \to b$, we get a map $x \to S(a, b)$ by composing $\tau_a$ with $S(1, f)$ or $\tau_b$ with $S(f, 1)$. The dinaturality condition equates these, giving a cone over $\tilde{S}$. The universal end corresponds to the limit of $\tilde{S}$.
