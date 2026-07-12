# 📚 LangChain Tools

This repository contains simple examples demonstrating how to use **Tools** in LangChain. Each example focuses on integrating an external utility with a language model to extend its capabilities.

## Wikipedia Tool

The **Wikipedia Tool** allows applications to retrieve factual information from Wikipedia. It uses LangChain's `WikipediaAPIWrapper` to search for and summarize information about people, places, events, organizations, and other topics.

### What this example demonstrates

* Initializing the `WikipediaAPIWrapper`
* Wrapping it as a LangChain `Tool`
* Invoking the tool with a user query
* Retrieving and displaying information from Wikipedia

### Technologies Used

* Python
* LangChain
* LangChain Community
* OpenAI
* Wikipedia API

### Sample Query

```python
query = "Who is Ada Lovelace?"
result = wikipedia_tool.invoke(query)

print(result)
```

### Example Output

```
Ada Lovelace was an English mathematician and writer, chiefly known for her work on Charles Babbage's proposed mechanical general-purpose computer, the Analytical Engine...
```


