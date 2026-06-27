#!/usr/bin/env python3
"""Extract missing concepts from GTM011 - Principles, Formulas, and unnamed theorems."""
import os, re
from pathlib import Path

SECTION_DIR = "/home/a123/文档/mathpkg/pipeline_output/stitched_sections/(GTM011)Functions of One Complex Variable I"
OUTPUT_DIR = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch2/gtm011"
TODAY = "2026-06-27"

# Manually specify missing concepts that don't follow "X.Y ConceptType." pattern
MISSING_CONCEPTS = {
    "schwarz-reflection-principle": {
        "source_file": "s032_1.1_Schwarz_Reflection_Principle.md",
        "type": "theorem",
        "num": "1.1",
        "title_en": "1.1 Schwarz Reflection Principle",
        "domain": "analysis",
        "subdomain": "complex-analysis",
        "chapter": "Analytic Continuation and Riemann Surfaces",
        "section": "1. Schwarz Reflection Principle",
        "statement": """Let $G$ be a region such that $G = G^*$ (symmetric with respect to the real axis). If $f: G_+ \\cup G_0 \\to \\mathbb{C}$ is a continuous function which is analytic on $G_+$ and if $f(x)$ is real for $x$ in $G_0$, then there is an analytic function $g: G \\to \\mathbb{C}$ such that $g(z) = f(z)$ for $z$ in $G_+ \\cup G_0$.""",
        "proof": """For $z$ in $G_-$ define $g(z) = \\overline{f(\\bar{z})}$ and for $z$ in $G_+ \\cup G_0$ let $g(z) = f(z)$. It is easy to see that $g: G \\to \\mathbb{C}$ is continuous; it must be shown that $g$ is analytic."""
    },
    "jensens-formula": {
        "source_file": "s043_1._Jensens_Formula.md",
        "type": "theorem",
        "num": "1.2",
        "title_en": "1.2 Jensen's Formula",
        "domain": "analysis",
        "subdomain": "complex-analysis",
        "chapter": "Entire Functions",
        "section": "1. Jensen's Formula",
        "statement": """Let $f$ be analytic in an open set containing $\\bar{B}(0; r)$ and suppose that $a_1, \\ldots, a_n$ are the zeros of $f$ in $B(0; r)$ repeated according to multiplicity. If $f(0) \\neq 0$ then

$$\\log |f(0)| = -\\sum_{k=1}^{n} \\log \\left( \\frac{r}{|a_k|} \\right) + \\frac{1}{2\\pi} \\int_{0}^{2\\pi} \\log |f(re^{i\\theta})| d\\theta.$$""",
        "proof": """If $|b| < 1$ then the map $(z-b)(1-\\bar{b}z)^{-1}$ takes the disk $B(0; 1)$ onto itself and maps the boundary onto itself. Hence

$$\\frac{r^2(z-a_k)}{r^2 - \\bar{a}_k z}$$

maps $B(0; r)$ onto itself and takes the boundary to the boundary. Therefore

$$F(z) = f(z) \\prod_{k=1}^{n} \\frac{r^2 - \\bar{a}_k z}{r(z-a_k)}$$

is analytic in an open set containing $\\bar{B}(0; r)$, has no zeros in $B(0; r)$, and $|F(z)| = |f(z)|$ for $|z| = r$. So (1.1) applies to $F$ to give

$$\\log |F(0)| = \\frac{1}{2\\pi} \\int_{0}^{2\\pi} \\log |f(re^{i\\theta})| d\\theta.$$

However $F(0) = f(0) \\prod_{k=1}^{n} \\left( -\\frac{r}{a_k} \\right)$ so that Jensen's Formula results."""
    },
    "poisson-jensen-formula": {
        "source_file": "s043_1._Jensens_Formula.md",
        "type": "theorem",
        "num": "1.3",
        "title_en": "1.3 Poisson-Jensen Formula",
        "domain": "analysis",
        "subdomain": "complex-analysis",
        "chapter": "Entire Functions",
        "section": "1. Jensen's Formula",
        "statement": """Let $f$ be analytic in a region which contains $\\bar{B}(0; r)$ and let $a_1, \\ldots, a_n$ be the zeros of $f$ in $B(0; r)$ counted according to multiplicity. If $f(z) \\neq 0$ then

$$\\log |f(z)| = -\\sum_{k=1}^{n} \\log \\left| \\frac{r^2 - \\bar{a}_k z}{r(z - a_k)} \\right| + \\frac{1}{2\\pi} \\int_{0}^{2\\pi} \\operatorname{Re} \\left( \\frac{re^{i\\theta} + z}{re^{i\\theta} - z} \\right) \\log |f(re^{i\\theta})| d\\theta$$

for $|z| < r$, $z \\neq a_k$.""",
        "proof": """The Poisson-Jensen Formula is derived using the same methods as Jensen's Formula but replacing the Mean Value Property with Corollary X.2.9."""
    },
    "orientation-principle": {
        "source_file": "s007_3.16_Proposition.md",
        "type": "theorem",
        "num": "3.21",
        "title_en": "3.21 Orientation Principle",
        "domain": "analysis",
        "subdomain": "complex-analysis",
        "chapter": "Elementary Properties and Examples of Analytic Functions",
        "section": "3. Analytic functions as mappings, Möbius transformations",
        "statement": """Let $\\Gamma_1$ and $\\Gamma_2$ be two circles in $\\mathbb{C}_{\\infty}$ and let $T$ be a Möbius transformation such that $T(\\Gamma_1) = \\Gamma_2$. Let $(z_1, z_2, z_3)$ be an orientation for $\\Gamma_1$. Then $T$ takes the right side and the left side of $\\Gamma_1$ onto the right side and left side of $\\Gamma_2$ with respect to the orientation $(Tz_1, Tz_2, Tz_3)$.""",
        "proof": "(The proof is left as an exercise.)"
    },
    "cauchy-estimate": {
        "source_file": "s008_1.12_Definition.md",
        "type": "corollary",
        "num": "2.14",
        "title_en": "2.14 Cauchy's Estimate",
        "domain": "analysis",
        "subdomain": "complex-analysis",
        "chapter": "Complex Integration",
        "section": "2. Power series representation of analytic functions",
        "statement": """Let $f$ be analytic in $B(a; R)$ and suppose $|f(z)| \\leq M$ for all $z$ in $B(a; R)$. Then

$$|f^{(n)}(a)| \\leq \\frac{n!M}{R^n}.$$""",
        "proof": """Since Corollary 2.13 applies with $r < R$, Proposition 1.17 implies that

$$|f^{(n)}(a)| \\leq \\left( \\frac{n!}{2\\pi} \\right) \\frac{M}{r^{n+1}} \\cdot 2\\pi r = \\frac{n!M}{r^n}$$

Since $r < R$ is arbitrary, the result follows by letting $r \\rightarrow R-$. """
    },
    "liouvilles-theorem": {
        "source_file": "s009_3.2_Definition.md",
        "type": "theorem",
        "num": "3.4",
        "title_en": "3.4 Liouville's Theorem",
        "domain": "analysis",
        "subdomain": "complex-analysis",
        "chapter": "Elementary Properties and Examples of Analytic Functions",
        "section": "3. Zeros of an analytic function",
        "statement": """If $f$ is a bounded entire function then $f$ is constant.""",
        "proof": """Suppose $|f(z)| \\leq M$ for all $z$ in $\\mathbb{C}$. We will show that $f'(z) = 0$ for all $z$ in $\\mathbb{C}$. To do this use Cauchy's Estimate (Corollary 2.14). Since $f$ is analytic in any disk $B(z; R)$ we have that $|f'(z)| \\leq M/R$. Since $R$ was arbitrary, it follows that $f'(z) = 0$ for each $z$ in $\\mathbb{C}$."""
    },
    "maximum-modulus-theorem": {
        "source_file": "s009_3.2_Definition.md",
        "type": "theorem",
        "num": "3.11",
        "title_en": "3.11 Maximum Modulus Theorem",
        "domain": "analysis",
        "subdomain": "complex-analysis",
        "chapter": "Elementary Properties and Examples of Analytic Functions",
        "section": "3. Zeros of an analytic function",
        "statement": """If $f$ is analytic on an open connected set $G$ and $|f|$ attains its maximum value at some point $a$ in $G$, then $f$ is constant.""",
        "proof": """(See Chapter VI for a detailed proof and consequences.)"""
    },
    "abel-theorem": {
        "source_file": "s005_2.21_Corollary.md",
        "type": "theorem",
        "num": "3.4",
        "title_en": "3.4 Theorem (Conformal Mapping - Angle Preservation)",
        "domain": "analysis",
        "subdomain": "complex-analysis",
        "chapter": "Elementary Properties and Examples of Analytic Functions",
        "section": "3. Analytic functions as mappings",
        "statement": """If $f: G \\to \\mathbb{C}$ is analytic then $f$ is conformal (angle-preserving) at each point $z_0$ in $G$ where $f'(z_0) \\neq 0$.""",
        "proof": """Given any two paths $\\gamma_1$ and $\\gamma_2$ through $z_0$, $f$ maps these paths onto two paths through $\\omega_0 = f(z_0)$ and, when $f'(z_0) \\neq 0$, the angles between the curves are preserved both in magnitude and direction."""
    },
}

def write_concept_files(slug, info):
    concept_dir = os.path.join(OUTPUT_DIR, slug)
    os.makedirs(concept_dir, exist_ok=True)

    # concept.yaml
    yaml_content = f"""id: {slug}
title_en: "{info['title_en']}"
title_zh: ""
type: {info['type']}
domain: {info['domain']}
subdomain: {info['subdomain']}
difficulty: {"basic" if info['type'] in ('definition',) else "intermediate"}
tags: []
depends_on:
  required: []
  recommended: []
  suggested: []
source_books:
  - book_id: "gtm011"
    author: "John B. Conway"
    title: "Functions of One Complex Variable I"
    chapter: "{info['chapter']}"
    section: "{info['section']}"
    pages: ""
    role_in_book: ""
content_hash: ""
extraction_date: "{TODAY}"
extraction_agent: "v8-full-extract"
"""
    with open(os.path.join(concept_dir, 'concept.yaml'), 'w') as f:
        f.write(yaml_content)

    # theorem.tex
    with open(os.path.join(concept_dir, 'theorem.tex'), 'w') as f:
        f.write(info['statement'])

    # introduce.en.md
    intro = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

{info['title_en']} from Conway's "Functions of One Complex Variable I."
{info['statement'][:250].strip()}...
"""
    with open(os.path.join(concept_dir, 'introduce.en.md'), 'w') as f:
        f.write(intro)

    # proof file for non-definition types
    if info['type'] in ('theorem', 'proposition', 'corollary', 'lemma'):
        ch_sec = info['section'].replace('. ', '_').replace('.', '_').replace(' ', '_')
        proof_fn = f"proof_gtm011_{ch_sec}.en.md"
        proof_yaml = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: gtm011
source_chapter: "{info['chapter']}"
source_section: "{info['section']}"
---

{info['proof']}
"""
        with open(os.path.join(concept_dir, proof_fn), 'w') as f:
            f.write(proof_yaml)

    print(f"  Created: {slug}")

def main():
    for slug, info in MISSING_CONCEPTS.items():
        write_concept_files(slug, info)

    print(f"\nExtracted {len(MISSING_CONCEPTS)} additional concepts")

if __name__ == '__main__':
    main()
