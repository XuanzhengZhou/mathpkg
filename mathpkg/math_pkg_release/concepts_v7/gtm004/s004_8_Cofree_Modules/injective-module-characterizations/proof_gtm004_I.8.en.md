---
role: proof
locale: en
of_concept: injective-module-characterizations
source_book: gtm004
source_chapter: "I. Modules"
source_section: "8. Cofree Modules"
---

# Proof of Theorem 8.4: Equivalent Characterizations of Injective Modules

The proof is dual to the proof of Theorem 4.7 (the projective module characterizations). We indicate the dual correspondences.

**(1) $\Rightarrow$ (2).** Suppose $I$ is injective and $A \xrightarrow{\mu} B \xrightarrow{\varepsilon} C$ is exact. The induced sequence

$$0 \rightarrow \operatorname{Hom}_{\Lambda}(C, I) \xrightarrow{\varepsilon^*} \operatorname{Hom}_{\Lambda}(B, I) \xrightarrow{\mu^*} \operatorname{Hom}_{\Lambda}(A, I) \rightarrow 0$$

is dual to the projective case. Exactness at $\operatorname{Hom}_{\Lambda}(C, I)$ follows from $\varepsilon$ being an epimorphism. Exactness at $\operatorname{Hom}_{\Lambda}(B, I)$ and $\operatorname{Hom}_{\Lambda}(A, I)$ uses the injectivity of $I$: given $\varphi \in \ker \mu^*$, i.e. $\varphi \mu = 0$, we have $\varphi$ factoring through $\operatorname{coker} \mu \cong C$ (since $\varepsilon$ is the cokernel of $\mu$), so $\varphi = \varepsilon^*(\psi)$ for some $\psi$. Surjectivity of $\mu^*$ is the essential use of injectivity: any $\alpha : A \rightarrow I$ extends along $\mu$ by definition of injectivity.

**(2) $\Rightarrow$ (3).** Take the exact sequence $0 \rightarrow I \xrightarrow{\mu} B \rightarrow B/I \rightarrow 0$. By (2), $\mu^* : \operatorname{Hom}_{\Lambda}(B, I) \rightarrow \operatorname{Hom}_{\Lambda}(I, I)$ is surjective, so there exists $\beta : B \rightarrow I$ with $\mu^*(\beta) = 1_I$, i.e. $\beta \mu = 1_I$.

**(3) $\Rightarrow$ (4).** If $\mu : I \rightarrow B$ is a monomorphism with retraction $\beta : B \rightarrow I$, $\beta \mu = 1_I$, then $B \cong I \oplus \ker \beta$. Thus $I$ is a direct summand of $B$.

**(4) $\Rightarrow$ (5).** We must embed $I$ into a cofree module. This is dual to Lemma 4.6: For any $\Lambda$-module $I$, there exists an epimorphism from a direct product of copies of $\Lambda^* = \operatorname{Hom}_{\mathbb{Z}}(\Lambda, \mathbb{Q}/\mathbb{Z})$ onto an appropriate module. Dually, we embed $I$ into a direct product of copies of $\Lambda^*$. Specifically, take the canonical map

$$I \rightarrow \prod_{\varphi \in \operatorname{Hom}_{\Lambda}(I, \Lambda^*)} \Lambda^*, \quad x \mapsto (\varphi(x))_{\varphi}.$$

This is a monomorphism (since for any $0 \neq x \in I$ there exists $\varphi$ with $\varphi(x) \neq 0$, via the abelian group embedding into $\mathbb{Q}/\mathbb{Z}$ and Proposition 8.1). By (4), $I$ is then a direct summand in this cofree module.

**(5) $\Rightarrow$ (1).** Cofree modules are direct products of $\Lambda^* = \operatorname{Hom}_{\mathbb{Z}}(\Lambda, \mathbb{Q}/\mathbb{Z})$, which is injective by Theorem 8.2 (since $\mathbb{Q}/\mathbb{Z}$ is divisible). Direct products of injective modules are injective (Proposition 6.3), and direct summands of injective modules are injective. Hence $I$ is injective.

**Step (3) $\Rightarrow$ (4) detail.** This requires the dual of Lemma 4.6. Given a monomorphism $\mu : I \rightarrow B$ with retraction $\beta$ ($\beta \mu = 1_I$), we have the split exact sequence

$$0 \rightarrow I \xrightarrow{\mu} B \xrightarrow{1_B - \mu \beta} \ker \beta \rightarrow 0.$$

Thus $B = I \oplus \ker \beta$, and $I$ is a direct summand of $B$. $\square$
