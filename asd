# Why I Chose Rust for AI-Assisted Software Development

**Engineering Journal — Initial Thoughts**

## Background

As I've continued exploring software development with AI coding agents, I've become increasingly interested in what makes a programming language suitable for AI-assisted engineering.

AI can generate code in nearly any popular language. However, generating code is only one part of software engineering. The more important questions are whether that code is correct, secure, maintainable, efficient, and capable of evolving over time.

This is what led me to explore Rust.

## Why Rust?

One of my primary interests in Rust is its compiler and the guarantees provided by its type system, ownership model, and borrowing rules.

Unlike languages where certain mistakes may not be discovered until runtime, Rust can identify many categories of problems during compilation.

I believe this creates an interesting advantage when using AI to write software.

Rather than trusting an AI model to consistently generate correct code, I can use Rust's compiler and development tools as part of an automated verification process.

This doesn't guarantee that the application is correct, but it introduces an additional layer of engineering discipline.

## Where AI Skills Fit In

My interest extends beyond Rust itself.

I want to explore how reusable AI Skills, coding standards, structured instructions, and automated quality checks can improve the consistency of AI-generated software.

My working hypothesis is that combining Rust with well-designed Skills and automated verification can produce software that is more reliable and maintainable, while reducing certain types of engineering mistakes.

I also want to understand the tradeoffs, including development time, AI token usage, complexity, and performance.

## Why Not Just Python?

Python offers significant benefits, particularly its simplicity, rapid development capabilities, and extensive ecosystem.

However, I want to investigate whether Rust provides additional advantages when the majority of implementation work is performed by AI.

If AI can handle much of the initial coding complexity, does Rust's steeper learning curve become less significant? And do its compile-time checks make the overall AI development process more dependable?

These are questions I intend to explore rather than conclusions I've already reached.

## What I Want to Document

Throughout this journey, I plan to record:

- What I learn about Rust and its ecosystem.
- My experience using AI to develop real applications.
- How Skills influence AI-generated code.
- Mistakes caught by Rust's compiler.
- Situations where Rust makes development harder.
- Comparisons with Python and other languages.
- Experiments, performance observations, and lessons learned.
- How my opinions change as I gain experience.

## Initial Perspective

I am not attempting to establish that Rust is universally better than other programming languages.

Instead, I want to understand whether Rust provides a stronger foundation for the type of AI-assisted engineering I want to pursue.

**My starting belief is that AI can accelerate implementation, while Rust's compiler and a well-designed engineering workflow can help enforce quality.**

The purpose of this documentation is to test that belief through experience and evidence.
