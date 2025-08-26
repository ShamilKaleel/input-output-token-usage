# Torken Usage

A simple DSPy implementation for tracking token usage with Google's Gemini model.

## Overview

This project demonstrates how to use DSPy with Gemini model to track token consumption for language model calls. It implements a simple question-answering program that makes multiple LM calls and reports token usage statistics.

## Setup

1. **Install dependencies using uv:**
   ```bash
   uv sync
   ```

2. **Configure environment variables:**
   Create a `.env` file with your Gemini API credentials:
   ```
   GEMINI_API_KEY=your_api_key_here
   GEMINI_MODEL=gemini-2.0-flash
   ```

## Usage

Run the program:
```bash
uv run python main.py
```

## Example Output

```
Output: Prediction(
    reasoning='The answer is a straightforward factual question...',
    score='Correct'
)
Token Usage: {
    'gemini/gemini-2.0-flash': {
        'completion_tokens': 51,
        'prompt_tokens': 231,
        'total_tokens': 282,
        'completion_tokens_details': None,
        'prompt_tokens_details': {
            'audio_tokens': None,
            'cached_tokens': None,
            'text_tokens': 231,
            'image_tokens': None
        }
    }
}
```

## Requirements

- Python >= 3.12
- DSPy AI
- python-dotenv
- Valid Gemini API key

## Features

- Token usage tracking with `track_usage=True`
- Chain-of-thought reasoning
- Multiple LM call orchestration
- Detailed token consumption breakdown