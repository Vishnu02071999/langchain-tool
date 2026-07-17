# 📚 LangChain Tools

This repository contains simple examples demonstrating how to use **Tools** in LangChain. Each example focuses on integrating an external utility with a language model to extend its capabilities.

---

## 📖 Wikipedia Tool

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

---

## 🌦️ Weather Tool

The **Weather Tool** demonstrates how to create a custom LangChain tool using the `@tool` decorator. It fetches the current weather for a specified city by making a request to the free **wttr.in** weather service.

### What this example demonstrates

* Creating a custom tool using the `@tool` decorator
* Accepting user input as a tool argument
* Fetching weather data from an external REST API
* Invoking the tool using `.invoke()`

### Technologies Used

* Python
* LangChain Core
* Requests
* wttr.in Weather Service

### Sample Query

```python
city = "Bangalore"
result = weather_tool.invoke(city)

print(result)
```

### Example Output

```
Bangalore: 🌦️ +24°C
```

---

## 📧 Email Validation Tool

The **Email Validation Tool** demonstrates how to build a custom LangChain tool that validates whether an email address is correctly formatted. It leverages the `email-validator` library to check the syntax of an email and returns a clear validation message.

### What this example demonstrates

* Creating a custom tool using the `@tool` decorator
* Validating email addresses using the `email-validator` library
* Handling invalid email formats with exceptions
* Invoking the tool using `.invoke()`

### Technologies Used

* Python
* LangChain Core
* email-validator

### Sample Query

```python
email = "john.doe@example.com"
result = validate_email_tool.invoke(email)

print(result)
```

### Example Output

```
✅ 'john.doe@example.com' is a valid email address.
```

For an invalid email:

```
❌ Invalid email address: An email address must have an @-sign.
```

---

## 🕒 Current Date & Time Tool

The **Current Date & Time Tool** demonstrates how to build a simple custom LangChain tool that returns the system's current date and time. It uses Python's built-in `datetime` module and exposes the functionality through LangChain's `@tool` decorator.

### What this example demonstrates

* Creating a custom tool using the `@tool` decorator
* Retrieving the current system date and time
* Formatting the output in a human-readable format
* Invoking the tool using `.invoke()`

### Technologies Used

* Python
* LangChain Core
* datetime

### Sample Query

```python
result = current_datetime_tool.invoke({})

print(result)
```

### Example Output

```
Monday, 14 July 2026 | 10:45:32 AM
```
---

## 🌐 Web Search Tool

The **Web Search Tool** demonstrates how to integrate web search capabilities into LangChain using the `DuckDuckGoSearchRun` tool. It allows applications to search the web for the latest information and retrieve relevant results without requiring an API key.

Unlike the Wikipedia Tool, which searches only Wikipedia articles, the Web Search Tool can retrieve information from across the web, making it useful for answering questions about recent events, trends, technologies, and other topics that require up-to-date information.

### What this example demonstrates

* Integrating DuckDuckGo Search with LangChain
* Creating a custom tool using the `@tool` decorator
* Accepting user queries as input
* Retrieving real-time information from the web
* Invoking the tool using `.invoke()`

### Technologies Used

* Python
* LangChain Core
* LangChain Community
* DuckDuckGo Search

### Sample Query

```python
query = "Latest advancements in Artificial Intelligence"

result = web_search_tool.invoke(query)

print(result)
```

### Example Output

```
Recent advancements in Artificial Intelligence include improvements in multimodal models, AI agents, reasoning models, robotics, and generative AI applications across healthcare, finance, education, and software development.
```

