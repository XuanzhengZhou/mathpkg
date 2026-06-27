---
role: proof
locale: en
of_concept: projective-injective-restriction-to-subgroup
source_book: gtm004
source_chapter: "VI"
source_section: "1"
---

# Proof of Corollary 1.4: Restriction of Projective/Injective Modules to Subgroups

Let $U \leq G$ be a subgroup. The inclusion $i: U \hookrightarrow G$ induces a ring homomorphism $\mathbb{Z}i: \mathbb{Z}U \to \mathbb{Z}G$, which by (IV.12.3) gives rise to the restriction-of-scalars functor

$$U: \mathbb{M}_{\mathbb{Z}G} \longrightarrow \mathbb{M}_{\mathbb{Z}U},$$

where a $G$-module $M$ is regarded as a $U$-module via the inclusion. By standard extension-of-scalars (IV.12.4), this functor has both a left adjoint and a right adjoint:

- **Left adjoint** (induction): $F = \mathbb{Z}G \otimes_{\mathbb{Z}U} - : \mathbb{M}_{\mathbb{Z}U} \to \mathbb{M}_{\mathbb{Z}G}$,
- **Right adjoint** (coinduction): $G = \operatorname{Hom}_{\mathbb{Z}U}(\mathbb{Z}G, -) : \mathbb{M}_{\mathbb{Z}U} \to \mathbb{M}_{\mathbb{Z}G}$.

Now recall Lemma 1.3: the restriction functor $U$ is exact. Equivalently, $\mathbb{Z}G$ is flat as a $\mathbb{Z}U$-module (which follows because $\mathbb{Z}G$ is a free $\mathbb{Z}U$-module with basis a set of coset representatives of $U$ in $G$).

By Theorem IV.12.5:
- A functor that has an **exact right adjoint** preserves projective objects. Here, the left adjoint $F = \mathbb{Z}G \otimes_{\mathbb{Z}U} -$ is right exact, and it is in fact exact because $\mathbb{Z}G$ is free (hence flat) over $\mathbb{Z}U$. Thus $F$ is exact, and it is left adjoint to $U$. Hence $U$ preserves injectives (a functor with an exact left adjoint preserves injectives).
- Similarly, the right adjoint $G = \operatorname{Hom}_{\mathbb{Z}U}(\mathbb{Z}G, -)$ is exact because $\mathbb{Z}G$ is $\mathbb{Z}U$-projective. Since $G$ is right adjoint to $U$ and is exact, $U$ preserves projectives.

Therefore, if $P$ is a projective $G$-module, then $UP$ is a projective $U$-module. If $I$ is an injective $G$-module, then $UI$ is an injective $U$-module.

**Alternative direct proof (Exercise 1.5):** Since $\mathbb{Z}G$ is a free $\mathbb{Z}U$-module (with basis the cosets $U \backslash G$), any free $G$-module restricts to a free $U$-module. A projective $G$-module is a direct summand of a free $G$-module, hence restricts to a direct summand of a free $U$-module, i.e. a projective $U$-module. The injective case follows by a dual argument using the fact that $\mathbb{Z}G$ is also $\mathbb{Z}U$-free, hence the coinduction functor preserves injectives.
