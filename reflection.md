# Reflection

>[!note] Which issues were the easiest to fix, and which were the hardest? Why?
>The easiest issues to fix were definitely the simple style warnings, like adding blank lines or removing unused imports. They're quick, mechanical changes. The hardest was refactoring the global variable, since that required changing function definitions and modifying how data was passed through the entire program. It was much more involved than any other fix.

>[!note] Did the static analysis tools report any false positives? If so, describe one example.
> I didn't really run into any obvious false positives in this lab. All the major issues flagged by the tools, especially the security and bug warnings, seemed like legitimate problems that were good to fix.

>[!note] How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
> For a real workflow, I'd integrate these tools in two key places. First, I'd set them up as a **local pre-commit hook**. This would automatically check my code for issues before I even commit it. Second, I'd add a step to the **CI pipeline** (like a GitHub Action) to run the static analysis. This would act as a safety net to block any pull requests that introduce new issues.

>[!note] What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
>The code quality improved a lot. It's much **more readable** now with the consistent naming and the new docstrings. It also feels much **more robust** and **safer**; getting rid of the bare `except` and the dangerous `eval` function makes it less likely to crash or be exploited. Finally, removing the global state makes the code feel much cleaner and easier to maintain or add to in the future.
