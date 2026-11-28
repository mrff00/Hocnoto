# Git

Version Control for Game Development: A Beginner’s Guide
**Overview:** This guide outlines
a professional, safe workflow for using Git in game development by utilizing a structured branching strategy to maintain project stability.

###

Executive Summary

- **Main Branch:** Reserved exclusively for the latest stable, release-ready version of the game.

- **Dev Branch:** Acts as a sandbox for integrating new features into the working project before they reach the main branch.
- **Feature Branches:** Temporary branches created specifically for individual tasks (bugs, scripts, assets) to ensure isolated development.
- **Workflow
  :** Always base new feature branches off the **Dev** branch, not the **Main** branch.
- **Pull Requests (PRs
  ):** Serve as a gatekeeper mechanism to request and review merges between branches safely.
- **Conflict Resolution:** PR
  s provide a visual indicator if your changes conflict with the base branch files.
- **Safety Measures:** Features can be easily
  reverted if they break the project by creating a "revert" pull request.

---

### Key Concepts & Processes

#### Branching Strategy

- **Main:** The "Gold Standard" of your project. If the game is at
  version 0.1, Main is exactly that.
- **Dev:** The integration hub. It contains the current stable
  version plus all successfully tested, in-progress features.
- **Feature Branches:** These allow you to work on code
  or assets in isolation. You create these locally from **Dev**, complete your work, commit changes, and then push them to
  the remote repository.

#### The Pull Request (PR) Lifecycle

1.  **Creation:** Once a feature branch is pushed to the
    remote repo, create a PR to merge that feature into **Dev**.
2.  **Review:** Use PRs to request
    peer review via email notifications if working on a team.
3.  **Validation:** The system checks for code conflicts.
    If clear, you merge the PR.
4.  **Deployment:** Once **Dev** is stable and contains all
    desired features, a final PR merges **Dev** into **Main** to update the official project version.
5.  **Re
    version:** If a merge introduces bugs to **Dev**, you can use the "Revert" function in the PR history
    to automatically generate a pull request that rolls back those changes.

---

### Glossary

| Term | Definition | Why
it Matters |
| :--- | :--- | :--- |
| **Main Branch** | The primary stable version of the game.
| Ensures users/players always have a working build. |
| **Dev Branch** | The testing ground for new features. | Prev
ents broken code from reaching the stable version. |
| **Feature Branch** | A unique branch for a single task. | Keeps experimental work
separate from working code. |
| **Pull Request** | A formal request to merge one branch into another. | Provides
a safe, controlled way to review changes before finalizing. |
| **Conflict** | A state where two branches modified
the same file. | Prevents accidental overwriting of teammate work. |

---

### Key Takeaways

1
. Never develop directly on **Main** or **Dev**. 2. **Dev** is for the working build +
new features; **Main** is for the stable release. 3. Always base new features on the **Dev** branch.

4. **Pull Requests** are your primary tool for safe merging and conflict checking.
5. Use the "Revert"
   feature in PRs to quickly recover from accidental bugs.
6. The remote repository must be updated (pushed) before you
   can initiate a Pull Request.

### Conclusion

Safe game development version control relies on isolation. By keeping your "Stable" (
Main) and "Working" (Dev) code separate, and performing all granular work on temporary "Feature" branches, you
minimize the risk of losing progress or corrupting your game builds.

### Common Misconceptions

- **Misconception:** You should
  merge feature branches directly into **Main**.
  - **Correction:** Feature branches should be merged into **Dev**
    first to ensure stability before upgrading the official release.
- **Misconception:** Git will automatically stop you from breaking
  your code.
  - **Correction:** Git identifies \*conflicts\* between files, but logical errors (broken scripts
    ) must be managed by the developer via careful merging and the use of the "Revert" tool.

### Un

explained Concepts / Gaps

- Handling complex merge conflicts manually (Not covered in transcript).
- Detailed Git
  ignore configuration for game engines (Not covered in transcript).
- Advanced CLI (Command Line Interface) usage (Not covered in
  transcript).

### 7-Day Study Plan (15–30 Mins Daily)

- **Day 1:** Set
  up your repository with Main and Dev branches; practice switching between them.
  dummy" feature branch from Dev and perform a local commit.
- **Day 3:** Push your local feature branch to the remote
  repository.
- **Day 4:** Initiate a Pull Request from your feature branch to Dev and review the interface
  .
- **Day 5:** Practice the merge process and verify the changes appear in Dev.
- **Day
  6:** Practice the "Revert" process on a test script to understand how to undo a merge.
- **Day
  7:** Review the entire loop: Feature -> Dev -> (Merge) -> Revert (if needed).

## PROPS TO: https://www.youtube.com/watch?v=ZvXMn9aPyZI / @TooLoo on Youtube
