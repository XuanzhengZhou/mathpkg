---
role: proof
locale: en
of_concept: inconsistency-equivalent-conditions
source_book: gtm037
source_chapter: "Chapter 8: Sentential Logic"
source_section: "2. Elements of Logic"
---
Obviously $(i) \Rightarrow (ii) \Rightarrow (iii)$. Now suppose $\Gamma \vdash \neg(\varphi \rightarrow \varphi)$ for a certain sentence $\varphi$. Let $\psi$ be any sentence. By A1,
$$\Gamma \vdash (\varphi \rightarrow \varphi) \rightarrow [\neg\psi \rightarrow (\varphi \rightarrow \varphi)];$$
from 8.10 we infer that $\Gamma \vdash \neg\psi \rightarrow (\varphi \rightarrow \varphi)$, and then 8.17 yields $\Gamma \vdash \neg(\varphi \rightarrow \varphi) \rightarrow \neg\psi$. Hence $\Gamma \vdash \neg\psi$. So by 8.16, $\Gamma \vdash \psi$: $\psi$ being any sentence, $\Gamma$ is inconsistent.
