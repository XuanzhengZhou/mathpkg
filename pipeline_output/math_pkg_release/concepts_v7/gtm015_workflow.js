export const meta = {
  name: 'v7-extract-gtm015',
  description: 'GTM015: 18 sections → concept extraction',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

var SECTIONS = ["/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s001_1_Topological_algebraic_structures.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s002_4_Subgroups_and_quotient_grou.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s003_5_Uniformity_in_topological_groups.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s004_11_Real_and_complex_topological_vector_spaces.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s005_20_Topologically_supplementary_subspaces.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s006_21_Hyperplanes_and_linear_forms.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s007_22_Closed_hyperplanes_and_con.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s008_35_Compact_convex_sets_in_a_TVS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s009_36_Extremal_points_of_a_convex_set.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s00_preface.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s010_37_Seminorms_and_local_convexity.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s011_40_Continuous_linear_mappings_of_normed_spaces.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s012_41_Hilbert_spaces.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s013_42_Duality_in_Hilbert_spaces.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s014_45_The_bidual_of_a_normed_space.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s015_51_Resolvent_and_spectrum.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s016_58_Preliminaries.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM015)Lectures.in.functional.analysis.and.operator.theory,.Berberian.S.K..(GTM,.Springer,.1974)(ISBN.0387900802)(600dpi)(T)(358s)_MCf_/s017_68_Von_Neumann_algebras.md"]
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm015'
var BOOK_SLUG = 'gtm015'

phase('Extract')
log(BOOK_SLUG + ': ' + SECTIONS.length + ' sections')

var results = await pipeline(SECTIONS, function(prev, sp) {
  return async function() {
    var sn = sp.split('/').pop().replace('.md','')
    var dd = STAGING + '/' + sn
    
    var prompt = '=== V7 CONCEPT EXTRACTOR (Per-Section) ===\n\n' +
      'READ: ' + sp + '\n\n' +
      'Extract EVERY theorem, definition, lemma, proposition, corollary, axiom.\n' +
      'For EACH concept, write 3 files in: ' + dd + '/{SLUG}/\n\n' +
      '1. concept.yaml: id,title_en,title_zh:"",type,domain,subdomain,difficulty,tags,depends_on,source_books,content_hash:"",extraction_date:"2026-06-25",extraction_agent:"v7-test"\n' +
      '2. theorem.tex: PURE LaTeX STATEMENT only. NO proof.\n' +
      '3. introduce.en.md: YAML frontmatter(role:introduce,locale:en,content_hash:"",written_against:"") + 2-4 English sentences.\n\n' +
      'CRITICAL: slug = semantic-english-lowercase-hyphen (kummers-theorem NOT ' + key.lower() + '-thm-3-2). ' +
      'source_books = array of OBJECTS. theorem.tex = ZERO natural language.\n\n' +
      'Write .done: echo DONE > ' + dd + '/.done\n' +
      'Write .fail if stuck: echo FAIL > ' + dd + '/.fail'
    
    try { await agent(prompt, { label: sn.substring(0,40), phase: 'Extract' }) } catch(e) {}
    
    // Count on disk
    var cnt = 0
    try {
      var cr = await agent(
        'python3 -c "import os; d=\'' + dd + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]) if os.path.exists(d) else 0)"',
        { label: 'cnt-'+sn.substring(0,25), phase: 'Extract' }
      )
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}
    
    return { section: sn.substring(0,50), concepts: cnt }
  }
})

var valid = results.filter(function(r) { return r !== null })
var total = valid.reduce(function(s, r) { return s + (r.concepts || 0) }, 0)
log(BOOK_SLUG + ': ' + total + ' concepts from ' + valid.length + '/' + SECTIONS.length + ' sections')
return { book: BOOK_SLUG, sections: SECTIONS.length, sections_done: valid.length, concepts: total }
