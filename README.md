# Getting Started

## 1. Create Your Own Repository

This repository is provided as a GitHub template:

https://github.com/StatisticsExeter/mthm503_intro

Select:

```text
Use this template
```

and create your own repository from it.

Choose a sensible repository name such as:

```text
mthm503_intro_yourusername
```

or

```text
mthm503_python_practice
```

You should now have your own copy of the repository under your GitHub account.

---

## 2. Clone Your Repository

Clone your repository (not the template repository).

For example:

```bash
git clone https://github.com/YOUR_USERNAME/mthm503_intro_yourusername.git
```

Move into the repository:

```bash
cd mthm503_intro_yourusername
```

---

## 3. Create the Conda Environment

Create the Python environment described in `environment.yml`.

```bash
conda env create -f environment.yml
```

This only needs to be done once.

---

## 4. Activate the Environment

Activate the environment:

```bash
conda activate pyintro
```

---

## 5. Check the Available Commands

Run:

```bash
./run help
```

This displays all available commands.

---

# Week 1

To work on the Week 1 exercises:

```bash
./run week1
```

This will:

1. Run the Week 1 tests.
2. Display any failures.
3. Run code-quality checks if all tests pass.

If everything passes, you should see:

```text
✓ All tests passed
✓ No linting issues found
✓ Week 1 complete
✓ Ready to commit and push
```

---

# Week 2

To work on the Week 2 exercises:

```bash
./run week2
```

---

# 
