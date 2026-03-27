> **How to use this activity**
>
> This activity supports practical application of the concepts in your lesson.
> 
> 1. Download this activity as a docx file
> 2. Work through the activity step by step. Keep your answers concise and focused
> 3. Return to your lesson when you are done.
>
> {% if page.meta.what_to_do %}**What to do:** {{ page.meta.what_to_do }}{% endif %}
>
> {% if page.meta.expected_output %}**Expected output:** {{ page.meta.expected_output }}{% endif %}
>
> {% if page.meta.approximate_time %}**Approximate time:** {{ page.meta.approximate_time }}{% endif %}
>
> **Used in**
> {% for item in page.meta.used_in %}
> - {{ item }}
> {% endfor %}
>
> **Before you start**
>
> You will typically need:
>
> - Outputs from earlier activities (if applicable)
> - Notes from your current lesson

{% set docx_name = page.file.src_path.split('/')[-1].replace('.md', '.docx') %}
<div class="download-btn-wrapper" markdown="0">
<a class="md-button download-doc-btn" href="../../downloads/{{ docx_name }}" download>
⬇ Download as .docx
</a>
</div>
