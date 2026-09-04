# Model Tank

**Version:** v0.1  
**Date:** 2026-09-03

Model Tank is an experimental local desktop assistant.

For now, Tank lives on a local computer and serves as a sandbox for learning how AI assistants and agents work. The long-term goal is to make Tank useful for everyday tasks such as reminders, schedules, messages, and lightweight desktop assistance.

Eventually, I would like to move Tank onto a Raspberry Pi so it can become a small physical assistant that sits on my desk.

## Core Design Goal

Tank should remain useful even with **$0 in AI API usage**.

Its core functionality should be local and free to operate wherever practical. Cloud AI should be an optional enhancement rather than a requirement.

## Project Goals

- Learn how AI assistants and agents work
- Build Tank one capability at a time
- Keep core functionality local and free
- Use cloud AI only where it adds meaningful value
- Design the software so it can eventually move to a Raspberry Pi
- Keep the project modular and portable

## Roadmap

### v0 — Computer Prototype

Tank currently lives on my computer.

Planned capabilities:

- Run as a local Python application
- Accept user input
- Store simple local memory
- Read and work with local files
- Provide reminders
- Display schedule information
- Connect to calendar and email services
- Use desktop notifications
- Perform useful tasks without requiring AI
- Optionally use an AI model for more complex reasoning or summarization

### v1 — Raspberry Pi Desktop Assistant

Once the software becomes useful and stable, Tank can move to a Raspberry Pi.

Possible additions:

- Run continuously on a Raspberry Pi
- Small desktop display
- Speaker or audio notifications
- Physical buttons or status indicators
- Optional microphone and voice interaction
- Desktop enclosure

## AI Philosophy

AI is a tool inside Tank, not Tank itself.

Whenever possible:

```text
simple task
→ local Python logic

complex language/reasoning task
→ optional AI model