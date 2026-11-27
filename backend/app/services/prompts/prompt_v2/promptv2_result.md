# Git Version Control for Game Development: A Beginner’s Guide

This guide outlines a semi-industry standard workflow for using Git to manage game projects safely, focusing on branch management and pull requests to prevent code instability.

### Executive Summary

- **Main Branch:** Reserved exclusively for the latest stable, release-ready version of the game.
- **Dev Branch:** Acts as the integration hub for new features and ongoing work.
- **Feature Branches:** Temporary branches created from `Dev` to isolate specific tasks (scripts, assets, bug fixes).
- **Pull Requests (PRs):** A safe, controlled mechanism to request merging changes from one branch to another.
- **Conflict Resolution:** PRs allow you to check for code conflicts before merging, ensuring stability.
- **Reversion:** If a merge breaks the `Dev` branch, you can perform a "revert" PR to undo the changes.
- **Workflow:** Work on `Feature` -> Merge to `Dev` -> Verify -> Merge to `Main`.

---

### Key Concepts & Processes

#### Branching Strategy

- **Main:** The "Gold" version. Never develop directly on this branch.
- **Dev:** The "Work-in-Progress" version. Contains the most recent stable build plus new features.
- **Feature Branch:** Always branched off `Dev`. This keeps the `Dev` branch clean while you experiment.

#### The Pull Request (PR) Workflow

1.  **Creation:** Once a feature is committed locally, push the branch to the remote repository.
2.  **Requesting:** Open a PR to merge the `Feature` branch into `Dev`.
3.  **Review:** Use the PR interface to invite team members to review code (optional for solo devs).
4.  **Merging:** If there are no conflicts, confirm the merge. The feature is now part of `Dev`.
5.  **Reverting:** If a merge causes bugs, use the "Revert" button on the PR to automatically generate an undo request.

---

### Glossary

| Term               | Simple Definition                        | Why it Matters                                               |
| :----------------- | :--------------------------------------- | :----------------------------------------------------------- |
| **Main Branch**    | The primary, stable version of the game. | Ensures users always have a working build.                   |
| **Dev Branch**     | A staging area for new features.         | Keeps experimental code separate from the stable build.      |
| **Feature Branch** | A sandbox for specific tasks.            | Prevents broken code from affecting the rest of the project. |
| **Pull Request**   | A formal request to merge code.          | Provides a safe, reviewable way to integrate changes.        |
| **Merge**          | Combining two branches.                  | Updates the project with new, tested code.                   |
| **Revert**         | Undoing a previous merge.                | Acts as a safety net if a new feature breaks the game.       |

---

### Key Takeaways

1.  **Never develop on Main.** Keep it pristine for stable releases.
2.  **Always branch off Dev.** Your `Feature` branches should reflect the latest state of `Dev`.
3.  **Use descriptive titles.** When committing and creating PRs, clearly label what you changed.
4.  **Push to remote.** Local commits are not backed up until you push your branch to the remote repository.
5.  **Test before merging.** Ensure your `Feature` branch works before requesting a merge into `Dev`.
6.  **Use Revert for accidents.** Don't panic if a merge breaks `Dev`; the revert feature is a built-in safety tool.

---

### Conclusion

Safe version control in game development relies on isolating work into specific branches and using pull requests as a gatekeeper. By maintaining a strict hierarchy—`Feature` to `Dev`, and `Dev` to `Main`—you ensure that your project remains stable even during active development.

### Common Misconceptions

- **Misconception:** You can safely work directly on the `Main` branch if you are a solo developer. **Correction:** You should still use `Dev` and `Feature` branches to maintain a history of stable versions and prevent accidental breakage.
- **Misconception:** Pushing a local branch automatically merges it. **Correction:** Pushing only uploads the branch; you must still create and confirm a Pull Request to merge the code.

### Unexplained Concepts / Gaps

- **Merge Conflicts:** The transcript mentions "conflicts" but does not provide a step-by-step guide on how to manually resolve them when code overlaps.
- **Advanced Git:** Command-line Git usage, rebasing, and stashing are not covered.

---

### 7-Day Study Plan (15–30 Mins Daily)

- **Day 1:** Set up your repository on GitHub Desktop with `Main` and `Dev` branches.
- **Day 2:** Practice creating a `Feature` branch off `Dev` and making a dummy script change.
- **Day 3:** Commit your changes to the `Feature` branch and push it to the remote repository.
- **Day 4:** Create a Pull Request from your `Feature` branch to `Dev` and merge it.
- **Day 5:** Practice the "Revert" process by undoing a merge on the `Dev` branch.
- **Day 6:** Review the branch history to see how the commits appear in the logs.
- **Day 7:** Simulate a full cycle: Create a feature, merge to `Dev`, and then merge `Dev` to `Main`.
