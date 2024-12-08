To get started, set your OPENAI_API_KEY environment variable.
Mit Poershell z.B. So: 
$env:OPENAI_API_KEY="Ihr_API_Schlüssel"
nachgucken mit:
echo $env:OPENAI_API_KEY


Einen Blick in prompts.txt und promptfooconfig.yaml werfen. Insbesondere welche CSV genutzt wird!

To get the right prepared dataformat from features_labeled_4llm_step3. The Script: .\transform_to_llm_prompt.py can be used.
Promptfoos expactation ist the following Columns: lessoften,moreoften,rootcause_bynezha,__expected

Then run:

```
promptfoo eval
```

Afterwards, you can view the results by running `promptfoo view`
