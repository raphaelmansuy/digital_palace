# How to use llm command

### Set the default model

```bash
llm models default stablelm-2-zephyr-1_6b-Q4_1
```

### Use a specific model

```bash
llm -m "mistral:latest"
```

```bash
llm -m stablelm-2-zephyr-1_6b-Q4_1
```

### Summarize

**Using the system prompt**

```bash
 pbpaste | llm -s "summarize this:"  -m mistral:latest | tee /dev/tty | pbcopy
 ```

## Create template

**Using a prompt**

```bash 
llm 'Summarize this: $input' --save summarize
```

**Using a system prompt**

```bash 
llm  -s 'Summarize this' --save summarize
```

**Template with parameters**

```bash
llm --system 'Summarize this text in the voice of $voice' \
  --model gpt-4 -p voice GlaDOS --save summarize
  ```

**Using the template with parameter**

```bash
llm --system 'Summarize this text in the voice of $voice' \
  --model gpt-4 -p voice GlaDOS --save summarize
  ```
## Using a template

```bash
cat text1.text | llm -t summarize
```

### Save a template

```bash
llm -m stablelm-2-zephyr-1_6b-Q4_1 -s "Format as markown:" --save markdown
```


### Useful

**Format as markdown, but don't interpret the prompt**

```bash
pbpaste | llm -s "You are a prompt engineer, with 30 years of experience, Just format the input text using the markdown format. Text to format:"  -m mistral:latest | tee /dev/tty | pbcopy
```

**Summary of Webpage**

```bash
curl -s https://www.nytimes.com/ \

  | strip-tags .story-wrapper \

  | llm -s 'summarize the news' -m stablelm2
```

**Count the number of tokens**

```bash
cat my-file.txt | ttok
```

**Searching in a code base**

```bash
symbex 'test*csv*' | \
  llm --system 'based on these tests guess what this tool does'
  ```
  