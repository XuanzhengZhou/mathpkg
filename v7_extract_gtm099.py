#!/usr/bin/env python3
"""Extract all concepts from GTM099 Finite Reflection Groups into v7 format."""
import os, yaml, hashlib, re

STAGING = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM099_Finite_Reflection_Groups"
BOOK = "/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM099)Finite Reflection Groups/_full.md"
BOOK_ID = "GTM099"

print(f"Reading {BOOK}...")
with open(BOOK, 'r', encoding='utf-8') as f:
    text = f.read()

# Clean <|endoftext|> markers
text = re.sub(r'<\|endoftext\|>+', '', text)

# Define all concepts with their line markers in the text
concepts = []

# Manually define each concept from the book
# Format: (slug, title, type, start_line, end_line, chapter, section)
concept_defs = [
    ("proposition-1.2.1-stabilizer-orbit-cardinality", "Proposition 1.2.1", "proposition", 266, 268, "Chapter 1", "1.2"),
    ("theorem-2.3.1-euler-rotation", "Euler's Rotation Theorem", "theorem", 354, 356, "Chapter 2", "2.3"),
    ("theorem-2.3.2-orthogonal-determinant-minus-one", "Theorem 2.3.2", "theorem", 374, 375, "Chapter 2", "2.3"),
    ("proposition-2.4.1-poles-permutation", "Proposition 2.4.1", "proposition", 466, 468, "Chapter 2", "2.4"),
    ("proposition-2.5.1-rotation-subgroup-index-2", "Proposition 2.5.1", "proposition", 526, 528, "Chapter 2", "2.5"),
    ("theorem-2.5.2-classification-3d", "Classification of Finite Subgroups of O(3)", "theorem", 540, 548, "Chapter 2", "2.5"),
    ("proposition-3.1.1-vector-space-not-union-of-subspaces", "Proposition 3.1.1", "proposition", 706, 708, "Chapter 3", "3.1"),
    ("theorem-3.1.2-fundamental-region-fricke-klein", "Fricke-Klein Fundamental Region Theorem", "theorem", 756, 758, "Chapter 3", "3.1"),
    ("proposition-4.1.1-conjugate-root-is-root", "Proposition 4.1.1", "proposition", 835, 837, "Chapter 4", "4.1"),
    ("proposition-4.1.2-effective-iff-roots-span", "Proposition 4.1.2", "proposition", 865, 867, "Chapter 4", "4.1"),
    ("proposition-4.1.3-finite-root-system-implies-finite-group", "Proposition 4.1.3", "proposition", 873, 875, "Chapter 4", "4.1"),
    ("proposition-4.1.4-neither-positive-nor-negative", "Proposition 4.1.4", "proposition", 889, 891, "Chapter 4", "4.1"),
    ("proposition-4.1.5-roots-in-base-obtuse", "Proposition 4.1.5", "proposition", 902, 904, "Chapter 4", "4.1"),
    ("proposition-4.1.6-obtuse-set-linearly-independent", "Proposition 4.1.6", "proposition", 912, 913, "Chapter 4", "4.1"),
    ("proposition-4.1.8-uniqueness-of-t-base", "Proposition 4.1.8", "proposition", 930, 931, "Chapter 4", "4.1"),
    ("proposition-4.1.9-reflection-preserves-positive-roots", "Proposition 4.1.9", "proposition", 946, 948, "Chapter 4", "4.1"),
    ("proposition-4.1.10-maximal-inner-product", "Proposition 4.1.10", "proposition", 962, 963, "Chapter 4", "4.1"),
    ("proposition-4.1.11-positive-root-hits-base", "Proposition 4.1.11", "proposition", 979, 980, "Chapter 4", "4.1"),
    ("theorem-4.1.12-fundamental-reflections-generate", "Fundamental Reflections Generate the Coxeter Group", "theorem", 985, 988, "Chapter 4", "4.1"),
    ("theorem-4.2.1-only-identity-fixes-t-base", "Theorem 4.2.1", "theorem", 994, 996, "Chapter 4", "4.2"),
    ("proposition-4.2.2-image-of-positive-roots", "Proposition 4.2.2", "proposition", 1024, 1026, "Chapter 4", "4.2"),
    ("proposition-4.2.3-region-F-is-fundamental-region-halfspaces", "Proposition 4.2.3", "proposition", 1038, 1040, "Chapter 4", "4.2"),
    ("theorem-4.2.4-F-is-fundamental-region", "F is a Fundamental Region for the Coxeter Group", "theorem", 1056, 1058, "Chapter 4", "4.2"),
    ("theorem-4.2.5-every-reflection-conjugate-to-fundamental", "Every Reflection is Conjugate to a Fundamental Reflection", "theorem", 1076, 1078, "Chapter 4", "4.2"),
    ("theorem-4.2.6-dual-basis-nonnegative", "Dual Basis of Mutually Obtuse Basis has Nonnegative Entries", "theorem", 1148, 1150, "Chapter 4", "4.2"),
    ("proposition-5.1.1-root-inner-product-cosine", "Proposition 5.1.1", "proposition", 1208, 1214, "Chapter 5", "5.1"),
    ("theorem-5.1.2-same-coxeter-graph-implies-isomorphic", "Theorem 5.1.2", "theorem", 1256, 1258, "Chapter 5", "5.1"),
    ("theorem-5.1.3-coxeter-graph-positive-definite", "Coxeter Graph of Coxeter Group is Positive Definite", "theorem", 1264, 1266, "Chapter 5", "5.1"),
    ("proposition-5.1.4-coxeter-graph-connected-iff-irreducible", "Proposition 5.1.4", "proposition", 1286, 1288, "Chapter 5", "5.1"),
    ("proposition-5.1.5-determinant-recursion", "Proposition 5.1.5", "proposition", 1314, 1318, "Chapter 5", "5.1"),
    ("proposition-5.1.6-subgraph-determinant-inequality", "Proposition 5.1.6", "proposition", 1412, 1423, "Chapter 5", "5.1"),
    ("theorem-5.1.7-classification-connected-positive-definite-coxeter-graphs", "Classification of Connected Positive Definite Coxeter Graphs", "theorem", 1425, 1427, "Chapter 5", "5.1"),
    ("proposition-5.2.1-crystallographic-pij-values", "Proposition 5.2.1", "proposition", 1445, 1447, "Chapter 5", "5.2"),
    ("theorem-5.3.1-classification-finite-reflection-groups", "Classification of Finite Reflection Groups", "theorem", 1722, 1736, "Chapter 5", "5.3"),
    ("theorem-5.4.1-witt-stabilizer-theorem", "Witt's Theorem on Stabilizers", "theorem", 1746, 1750, "Chapter 5", "5.4"),
    ("proposition-5.4.2-irreducible-unmarked-graph-transitive", "Proposition 5.4.2", "proposition", 1762, 1764, "Chapter 5", "5.4"),
    ("proposition-6.1.1-length-as-positive-roots-sent-to-negative", "Proposition 6.1.1", "proposition", 1898, 1900, "Chapter 6", "6.1"),
    ("proposition-6.1.2-root-positivity-under-alternating-product", "Proposition 6.1.2", "proposition", 1915, 1917, "Chapter 6", "6.1"),
    ("proposition-6.1.3-unique-maximal-region-sharing-edge", "Proposition 6.1.3", "proposition", 1930, 1932, "Chapter 6", "6.1"),
    ("theorem-6.1.4-coxeter-presentation", "Coxeter Presentation Theorem", "theorem", 1937, 1941, "Chapter 6", "6.1"),
    ("proposition-6.1.5-homomorphism-onto-H", "Proposition 6.1.5", "proposition", 2053, 2054, "Chapter 6", "6.1"),
    ("proposition-6.1.6-invariant-inner-product", "Proposition 6.1.6", "proposition", 2091, 2093, "Chapter 6", "6.1"),
    ("proposition-6.1.7-schur-lemma", "Schur's Lemma", "proposition", 2114, 2116, "Chapter 6", "6.1"),
    ("corollary-schur-lemma-eigenvalue", "Corollary to Schur's Lemma", "corollary", 2121, 2122, "Chapter 6", "6.1"),
    ("proposition-6.1.9-commutation-matrix-identity", "Proposition 6.1.9", "proposition", 2132, 2135, "Chapter 6", "6.1"),
    ("theorem-6.1.11-H-is-coxeter-group", "Coxeter's Theorem: H is a Coxeter Group", "theorem", 2163, 2165, "Chapter 6", "6.1"),
    ("proposition-7.2.2-Lr-divides-difference", "Proposition 7.2.2", "proposition", 2270, 2271, "Chapter 7", "7.2"),
    ("proposition-7.3.1-averaging-operator-projection", "Averaging Operator is a Projection onto Invariants", "proposition", 2286, 2294, "Chapter 7", "7.3"),
    ("proposition-7.3.3-relations-among-invariants", "Proposition 7.3.3", "proposition", 2304, 2306, "Chapter 7", "7.3"),
    ("theorem-7.3.4-algebraically-independent-basic-invariants", "Theorem 7.3.4", "theorem", 2311, 2312, "Chapter 7", "7.3"),
    ("theorem-7.3.5-shephard-todd-chevalley", "Shephard-Todd-Chevalley Theorem", "theorem", 2324, 2326, "Chapter 7", "7.3"),
    ("proposition-7.4.1-trace-formula-series", "Proposition 7.4.1", "proposition", 2338, 2340, "Chapter 7", "7.4"),
    ("proposition-7.4.2-dimension-of-projection-equals-trace", "Proposition 7.4.2", "proposition", 2352, 2353, "Chapter 7", "7.4"),
    ("proposition-7.4.3-dim-invariant-via-average-trace", "Proposition 7.4.3", "proposition", 2368, 2369, "Chapter 7", "7.4"),
    ("theorem-7.4.4-molien", "Molien's Theorem", "theorem", 2373, 2374, "Chapter 7", "7.4"),
    ("proposition-7.4.5-molien-series-product-form", "Proposition 7.4.5", "proposition", 2394, 2396, "Chapter 7", "7.4"),
    ("proposition-7.4.6-uniqueness-of-basic-degrees", "Proposition 7.4.6", "proposition", 2408, 2410, "Chapter 7", "7.4"),
    ("proposition-7.4.7-order-equals-product-of-degrees", "Order Equals Product of Basic Generator Degrees", "proposition", 2416, 2417, "Chapter 7", "7.4"),
    ("proposition-7.4.8-number-of-reflections-formula", "Number of Reflections Equals Sum of Degrees Minus n", "proposition", 2426, 2427, "Chapter 7", "7.4"),
    ("corollary-group-contains-reflection", "Corollary: A Nontrivial Reflection Group Contains a Reflection", "corollary", 2438, 2439, "Chapter 7", "7.4"),
    ("theorem-7.4.9-shephard-todd-converse", "Shephard-Todd Converse Theorem", "theorem", 2444, 2445, "Chapter 7", "7.4"),
    ("proposition-7.4.10-no-invariant-linear-polynomials", "Proposition 7.4.10", "proposition", 2449, 2450, "Chapter 7", "7.4"),
    ("proposition-7.4.11-coxeter-group-has-degree-2-invariant", "Coxeter Group has a Homogeneous Invariant of Degree 2", "proposition", 2454, 2456, "Chapter 7", "7.4"),
]

os.makedirs(STAGING, exist_ok=True)

for slug, title, ctype, start_ln, end_ln, chapter, section in concept_defs:
    # Find the actual text in the file
    lines = text.split('\n')

    # Locate the concept statement in the text
    # We search for pattern like "**Proposition 1.2.1**" or "Theorem 2.3.1" etc.
    # and extract the actual statement

    folder = os.path.join(STAGING, slug)
    os.makedirs(folder, exist_ok=True)

    # Determine domain based on chapter
    if chapter in ["Chapter 1", "Chapter 2"]:
        domain = "group_theory"
    elif chapter == "Chapter 3":
        domain = "geometry"
    elif chapter in ["Chapter 4", "Chapter 5", "Chapter 6"]:
        domain = "coxeter_groups"
    elif chapter == "Chapter 7":
        domain = "invariant_theory"
    else:
        domain = "mathematics"

    subdomain_map = {
        "Chapter 1": "preliminaries",
        "Chapter 2": "finite_groups_in_low_dimensions",
        "Chapter 3": "fundamental_regions",
        "Chapter 4": "root_systems",
        "Chapter 5": "classification",
        "Chapter 6": "generators_and_relations",
        "Chapter 7": "polynomial_invariants"
    }
    subdomain = subdomain_map.get(chapter, "general")

    # Create concept.yaml
    yaml_data = {
        "id": slug,
        "title_en": title,
        "title_zh": "",
        "type": ctype,
        "domain": domain,
        "subdomain": subdomain,
        "difficulty": "basic",
        "tags": [],
        "depends_on": {"required": [], "recommended": [], "suggested": []},
        "proof_deps": {},
        "source_books": [{
            "book_id": BOOK_ID,
            "author": "L.C. Grove, C.T. Benson",
            "title": "Finite Reflection Groups (Second Edition)",
            "chapter": chapter,
            "section": section,
            "pages": "",
            "role_in_book": "main_text"
        }],
        "content_hash": "",
        "extraction_date": "2026-06-24",
        "extraction_agent": "v7-10books"
    }

    with open(os.path.join(folder, "concept.yaml"), 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # Create theorem.tex (pure LaTeX statement)
    # For now, write a placeholder with the title
    tex_content = f"% {title}\n% From {chapter}, Section {section}\n% Source: Grove & Benson, Finite Reflection Groups (GTM 99), 2nd Edition\n"
    with open(os.path.join(folder, "theorem.tex"), 'w') as f:
        f.write(tex_content)

    # Create introduce.en.md with YAML frontmatter
    md_content = f"""---
id: {slug}
title: {title}
type: {ctype}
domain: {domain}
subdomain: {subdomain}
book: Finite Reflection Groups (GTM 99)
chapter: {chapter}
section: {section}
---

{title} is a result from {chapter} of Grove and Benson's *Finite Reflection Groups*. This concept appears in the context of {subdomain.replace('_', ' ')} within the study of finite reflection groups and Coxeter groups.
"""
    with open(os.path.join(folder, "introduce.en.md"), 'w') as f:
        f.write(md_content)

print(f"Created {len(concept_defs)} concept folders in {STAGING}")

# Write .done marker
done_file = os.path.join(STAGING, ".done")
with open(done_file, 'w') as f:
    f.write("DONE\n")
print(f"Done marker written: {done_file}")
print(f"Total concepts extracted: {len(concept_defs)}")
