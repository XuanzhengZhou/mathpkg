---
role: proof
locale: en
of_concept: semisimple-int-l-conjugacy
source_book: gtm009
source_chapter: "16"
source_section: "16.5"
---

The proof proceeds in several steps, building on the results of Sections 15-16.

Let $H$ and $H'$ be two Cartan subalgebras of the semisimple Lie algebra $L$. By Theorem 15.3, each CSA is a minimal Engel subalgebra, so $H = L_0(\operatorname{ad} x)$ for some regular element $x \in L$, and similarly $H' = L_0(\operatorname{ad} x')$.

First, embed $H$ and $H'$ into Borel subalgebras. Let $B$ be a Borel subalgebra containing $H$, and $B'$ a Borel subalgebra containing $H'$. By the conjugacy of Borel subalgebras (Theorem 16.4), there exists $\sigma \in \mathcal{E}(L) \subset \operatorname{Int} L$ such that $\sigma(B') = B$.

Now $H$ and $\sigma(H')$ are both Cartan subalgebras of $B$. By Theorem 16.2 (conjugacy of Cartan subalgebras in a solvable Lie algebra), applied to the solvable algebra $B$, there exists $\tau \in \mathcal{E}(B) \subset \mathcal{E}(L; B) \subset \mathcal{E}(L)$ such that $\tau(\sigma(H')) = H$.

Therefore $\tau \sigma \in \mathcal{E}(L) \subset \operatorname{Int} L$ sends $H'$ to $H$.

To identify Cartan subalgebras with maximal toral subalgebras in the semisimple case: a maximal toral subalgebra $T$ of $L$ is abelian (hence nilpotent), and $N_L(T) = T$ because any $[x, T] \subset T$ with $x$ ad-nilpotent would contradict maximality of $T$. Thus $T$ is a CSA. Conversely, a CSA $H$ of a semisimple Lie algebra consists entirely of ad-semisimple elements (by the abstract Jordan decomposition and the fact that the Killing form is nondegenerate on $H$), making $H$ a toral subalgebra, necessarily maximal since any CSA is self-normalizing.
