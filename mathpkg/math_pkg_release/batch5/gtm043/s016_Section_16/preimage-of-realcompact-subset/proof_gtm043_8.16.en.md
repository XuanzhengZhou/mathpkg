---
role: proof
locale: en
of_concept: preimage-of-realcompact-subset
source_book: gtm043
source_chapter: "8"
source_section: "16"
---

Let $$F$$ be a realcompact set in $$Y$$, and let $$S = \tau^{\leftarrow}[F]$$. Because $$X$$ is realcompact, the identity map $$\sigma$$ on $$S$$ has a continuous extension to a mapping $$\sigma^{\circ}: vS \to X$$. Also, $$\tau|_S$$ has a continuous extension $$(\tau|_S)^{\circ}: vS \to F$$. Since $$S$$ is dense in $$vS$$, both these extensions are determined by their values on $$S$$.

Now, $$\tau|_S = \tau \circ \sigma$$, and therefore $$(\tau|_S)^{\circ} = (\tau \circ \sigma)^{\circ} = \tau \circ \sigma^{\circ}$$. But by Lemma 6.11,

$$\sigma^{\circ}[vS - S] \subset X - S,$$

so that

$$(\tau \circ \sigma^{\circ})[vS - S] \subset Y - F,$$

whereas

$$(\tau|_S)^{\circ}[vS - S] \subset F.$$

Therefore, $$vS - S = \emptyset$$, i.e., $$S = vS$$, so $$S$$ is realcompact.
