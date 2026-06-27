---
role: proof
locale: en
of_concept: monic-epic-via-exact-sequences
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof.** The proof is trivial from the definitions.

(1) The sequence $0 \to M \xrightarrow{f} N \xrightarrow{n} \text{Coker}\, f \to 0$ is exact at:
- $M$: $f$ is monic iff $\text{Ker}\, f = 0$, i.e., the image of $0 \to M$ is $\text{Ker}\, f$.
- $N$: $\text{Im}\, f = \text{Ker}\, n$ by definition of the cokernel (the natural epimorphism $N \to N/\text{Im}\, f$ has kernel $\text{Im}\, f$).
- $\text{Coker}\, f$: $n$ is epic by definition, so $\text{Im}\, n = \text{Coker}\, f = \text{Ker}(\text{Coker}\, f \to 0)$.

(2) The sequence $0 \to \text{Ker}\, f \xrightarrow{i} M \xrightarrow{f} N \to 0$ is exact at:
- $\text{Ker}\, f$: $i$ is monic (inclusion), so the image of $0 \to \text{Ker}\, f$ is $\text{Ker}\, i = 0$.
- $M$: $\text{Im}\, i = \text{Ker}\, f$, which is exactness at $M$.
- $N$: $f$ is epic iff $\text{Im}\, f = N = \text{Ker}(N \to 0)$.

Both proofs are immediate from the definitions of kernel, cokernel, monomorphism, and epimorphism. $\square$
