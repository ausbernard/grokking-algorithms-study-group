# 📘 Week 00 — Syllabus & Study Group Overview

![Study Group](https://img.shields.io/badge/Study%20Group-Grokking%20Algorithms-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)
![Made With](https://img.shields.io/badge/Made%20With-Markdown-lightgrey)


Welcome to the **Grokking Algorithms Study Group** — a collaborative, engineer-focused journey through Aditya Bhargava’s Grokking Algorithms. The group was devised within [Brilliant Black Minds](https://karat.com/brilliant-black-minds/).

## *LEARNERS WANTED.*

*Anyone who is interested in learning is welcome to join, consistency is encouraged.*

**We will move together through the book chapter-by-chapter.**

*Until we have finished the book.*

**Goal:** By the end of the program, every member will have a small portfolio of algorithms implementations on GitHub.


## Schedule & Pace

**📅 Start date**: *tbd*

**📅 End date**: *tbd* 

**Weekly release schedule**: Every Sunday night the next week’s lesson plan will be uploaded to GitHub.

**Weekly meeting time**: *tbd*

**Meeting length**: 60-90 minutes

**Meeting format**: Zoom

## 📚 Chapters & Timeline
We are covering the book from start to finish:
| Week  | Chapter(s) | Topic                                    |
| ----  | ---------- | ---------------------------------------- |
| 00    | —          | Syllabus / Setup                         |
| 01    | 1          | Introduction to Algorithms               |
| 02    | 2          | Selection Sort                           |
| 03    | 3          | Recursion                                |
| 04    | 4          | Quicksort                                |
| 05    | 5          | Hash Tables                              |
| 06    | 6          | Breadth-first Search                     |
| 07    | 7          | Trees                                    |
| 08    | 8          | Balanced Trees                           |
| 09    | 9          | Dijkstra’s Algorithm (from Chapter 10)   |
| 10    | 10         | Greedy Algorithms                        |
| 11    | 11         | Dynamic Programming                      |
| 12    | 12         | K-Nearest Neighbors                      |
| 13    | —          | “Where to go next” & capstone discussion |
 

## 📕 Required Materials

- [*Grokking Algorithms* by Aditya Bhargava](https://www.amazon.com/Grokking-Algorithms-Second-Aditya-Bhargava/dp/1633438538/ref=sr_1_1?adgrpid=1345802804315310&dib=eyJ2IjoiMSJ9.OszIb92nF6C6wDw_2J3jHv6LOeuO2_jPAZoClXEevBLDAudxZJIPXAIY6Y0Wu3kaaBw7GfZBIp2d0A6DmRGQEl5L3oLNl6ryJNzrLW9sS--UrjUsD75PI2uTO9Hdhi_tUJrLClGOaT4ohNlS2A--S4znJEASEGSACy_pCRu7G3lWiHZ46apTup8VpCNUvo9g0_UH7j4vGKmXa38D14_E7aNKK5KNNKF7VULU04nX-nw.ewy_UbqV1xyRXceacWJ0rall3GKf1AqgyBeD9MCsI_Q&dib_tag=se&hvadid=84112914703875&hvbmt=bp&hvdev=c&hvlocphy=79496&hvnetw=o&hvqmt=p&hvtargid=kwd-84113038179711%3Aloc-190&hydadcr=16378_13421694&keywords=grokking+algorithms&mcid=46e290681c8e3593bcd3fa0341610468&msclkid=5ae7de7ff3451955d6e0b762d3e0ee4c&qid=1763516585&sr=8-1)
  
  >Grokking Algorithms is a visual, example-driven introduction to algorithms. 
  >It’s intentionally friendly, beginner-safe, and perfect for mixed-experience groups.

- [GitHub account](https://github.com/) (ability to clone, fork, push, and pull)
- Local dev environment ([Python](https://www.python.org/downloads/)/JS/etc.)
- [LeetCode account](https://leetcode.com/accounts/signup/) (optional but recommended)

> **Tip**: If you're new, Python is the simplest choice and easiest for algorithm practice.

### Optional Nice to Haves:
<details>
<summary>Click to expand</summary>

- [VS Code](https://code.visualstudio.com/download) (with Python/JS plugins)
- Quokka.js or a REPL environment for quick testing
- [Jupyter Notebook](https://jupyter.org/install) (Python folks)
- A notebook for sketching diagrams
- A tool like [Excalidraw](https://excalidraw.com/) (for tree/BFS sketches)
</details>


## Roles & Expectations

**Members**:
- Read the chapter before the meeting
- Complete the book exercises
- Upload solutions to your GitHub
- Attempt stretch problems (optionals)
- Attend weekly meetings consistently
- If you haven’t completed the reading or the exercises for the week, please listen in rather than ask questions. You're always welcome to catch up and re-join fully next wek.

**Coordinator (Sarah)**:
- Meeting dates are set and we have a valid link for video meetings in Discord (channel)
- Help field any `issues` in the repo

**Facilitator (Austin)**:
- Review high-level structure
- Keep weekly agenda
- Every Sunday night the next week’s lesson plan will be uploaded to GitHub.
- Assign Problems
- Run breakout sessions 
- Help field any `issues` in the repo


## 📝 Weekly Workflow

1. **Read** the assigned chapter
2. **Solve** book exercises
3. **Complete** stretch/interview-level problems
4. **Commit** solutions to GitHub under the proper week folder
    ```
    a. fork the repository
    b. everyone keeps their own folder under problems/ to avoid merge conflicts.
    
    format suggestion:
    ---
    week-01-introduction/
       problems/
        solutions/
          yourname/
            problem-01.py
            problem-02.py
    ---
    ```
    ```bash
    # If you fork this repo, remember to “Sync fork” each week before adding new solutions.
    git remote add upstream https://github.com/ausbernard/grokking-algorithms-study-group.git
    git fetch upstream
    git merge upstream/main
    ```
5. **Meet** weekly to discuss & pair-program
6. **Reflect** by writing 3 takeaways in your `README.md`

## 🧑‍💻 Coding Expectations
You may use **any programming language**, but Python examples will be provided most often.

Your code doesn’t need to be perfect — the goal is clarity and learning.

**Format suggestion:**
```
week-01-introduction/
  problems/
    yourname/
      problem-01.py
      problem-02.py
```

## 📝 Weekly Meeting Structure (60–90 minutes)
```
1. Warm-Up Discussion (5–10 min)

   - Quick round: “Biggest insight from this week’s reading”

2. Review Key Concepts (10–15 min)

   - Facilitator explains main ideas
   - Reference code examples

3. GitHub Walkthrough (10–15 min)

   - Volunteers share solutions (share the problem, time and space complexities, and solution)

4. Group Exercise (20 min)
    - Solve a fresh problem together on a shared pad
    - Discuss pitfalls

5. Breakout Interviews (10–20 min)
    - 1 partner interviews, 1 codes
    - Swap
    - Debrief

6. Plan Next Week (5 min)
    - Assign readings
    - Assign problems
    - Optional advanced challenge
```

## Code of Conduct
```
We assume good intent.
We help each other learn.
No put-downs, no discouragement.
We are all here to improve.
```

## 🧭 Goals for Week 00

Before Week 01, please:

✔️ Fork this repo (from `main` branch)

✔️ Read the README's.

✔️ Browse the folder structure

✔️ Set up your coding language environment

✔️ Join the discussion channel (Discord/Slack/etc.)

✔️ Make sure you can run simple scripts (Python/JS/etc.)

## 💬 Questions / Contributions

**If you spot an problems or have any questions leave an `issue` at the top of the repo.**



## 🚀 Let’s get started

This is a relaxed but focused group.
Show up, try the problems, ask questions — and enjoy the process.

Welcome to **Week 00** !
