
# Today I Learned: Building an AI Chat TUI with Textual

**Source:** [Anatomy of a Textual User Interface](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/) 

## Key Takeaways

### 1. **Inline Dependency Management**
- Textual supports Python 3.12+ and uses a comment-based dependency syntax (`# /// script`) to declare requirements like `llm` and `textual`. Tools like `uv` can auto-setup environments using this format ([PEP 0723](https://peps.python.org/pep-0723/)).

### 2. **Widget Design with Markdown**
- The TUI uses `Prompt` and `Response` widgets, both subclassing `Markdown` to display user inputs and AI responses. This leverages Textual's built-in support for Markdown formatting and styling.
- Example code:
  ```python
  class Prompt(Markdown):
      pass

  class Response(Markdown):
      BORDER_TITLE = "Mother"
  ```

### 3. **App Structure and Styling**
- The `MotherApp` class defines the UI layout using Textual's CSS-like styling (TCSS):
  - `AUTO_FOCUS = "Input"` ensures the input field is active on startup.
  - Custom styles for `Prompt` (primary color background) and `Response` (green border) create a retro terminal aesthetic.
  ```python
  CSS = """
  Prompt { background: $primary 10%; margin-right: 8; }
  Response { border: wide $success; margin-left: 8; }
  """
  ```

### 4. **Event Handling and Async Workflows**
- **Input Handling**: The `on_input` method triggers when the user submits text. It clears the input, mounts new `Prompt` and `Response` widgets, and anchors the response to the bottom of a scrollable `VerticalScroll` container.
- **Concurrency**: The `@work(thread=True)` decorator runs the LLM interaction in a background thread to avoid blocking the UI. Responses stream incrementally using `response.update()`.
  ```python
  @on(Input.Submitted)
  async def on_input(self, event: Input.Submitted) -> None:
      await chat_view.mount(Prompt(event.value))
      await chat_view.mount(response := Response())
      self.send_prompt(event.value, response)
  ```

### 5. **Layout and Responsiveness**
- The `compose` method structures the UI with a `Header`, scrollable chat area (`VerticalScroll`), input field, and `Footer`. The layout adjusts dynamically to terminal resizing.
  ```python
  def compose(self) -> ComposeResult:
      yield Header()
      with VerticalScroll(id="chat-view"):
          yield Response("INTERFACE 2037 READY FOR INQUIRY")
          yield Input(placeholder="How can I help you?")
      yield Footer()
  ```

---

## Why This Matters
- **Declarative UI Design**: Textual abstracts low-terminal complexities, allowing developers to focus on layout and interactivity.
- **Modern TUIs**: Features like threading, CSS styling, and Markdown support make terminal apps as rich as web interfaces.

---

**Try It Yourself**  
Run the script with `uv` after setting your OpenAI API key. For the full code, see the [original post](https://textual.textualize.io/blog/2024/09/15/anatomy-of-a-textual-user-interface/).
