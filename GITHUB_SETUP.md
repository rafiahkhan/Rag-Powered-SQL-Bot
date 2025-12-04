# 🚀 GitHub Upload Guide

This guide will help you upload your RAG-Chatbot-Over-SQL-Database project to GitHub.

## Prerequisites

- Git installed on your system
- GitHub account
- Project ready to upload

## Step-by-Step Instructions

### 1. Initialize Git Repository (if not already done)

Open terminal in your project directory and run:

```bash
cd /home/rafia-khan/S7/deep/RAG-Chatbot-Over-SQL-Database

# Initialize git repository
git init
```

### 2. Check What Will Be Uploaded

Before committing, check what files will be included:

```bash
# See all files (including ignored ones)
git status

# See only files that will be committed
git status --short
```

**Important:** Make sure your `.env` file is NOT listed (it should be ignored by `.gitignore`)

### 3. Create .env.example File (Optional but Recommended)

Create a template file for environment variables that others can copy:

```bash
# Create .env.example file
cat > .env.example << EOF
GROQ_API_KEY=your_groq_api_key_here
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=yourdatabasename
EOF
```

This file will be committed and shows users what environment variables they need.

### 4. Add All Files to Git

```bash
# Add all files (respecting .gitignore)
git add .

# Or add files selectively:
# git add README.md
# git add app.py
# git add requirements.txt
# git add chains/
# git add config/
# git add frontend/
# git add utils/
# git add .gitignore
```

### 5. Make Your First Commit

```bash
git commit -m "Initial commit: RAG-Chatbot-Over-SQL-Database

- Natural language to SQL query conversion
- MySQL database integration
- Streamlit-based chat interface
- Powered by LangChain and Groq LLaMA 3.3-70B
- Read-only query execution for security"
```

### 6. Create Repository on GitHub

1. Go to [GitHub.com](https://github.com) and log in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in the repository details:
   - **Repository name:** `RAG-Chatbot-Over-SQL-Database`
   - **Description:** `Chat with Your MySQL Database Using Natural Language - Powered by LangChain, Groq LLaMA 3.3-70B, and Streamlit`
   - **Visibility:** Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (you already have these)
5. Click **"Create repository"**

### 7. Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Copy the repository URL and run:

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/RAG-Chatbot-Over-SQL-Database.git

# Or if using SSH:
# git remote add origin git@github.com:YOUR_USERNAME/RAG-Chatbot-Over-SQL-Database.git

# Verify remote was added
git remote -v
```

### 8. Push to GitHub

```bash
# Push to GitHub (first time)
git push -u origin main

# If your default branch is 'master' instead of 'main':
# git branch -M main
# git push -u origin main
```

### 9. Verify Upload

1. Go to your GitHub repository page
2. Refresh the page
3. You should see all your files uploaded
4. Verify that:
   - ✅ README.md is displayed with proper formatting
   - ✅ .env file is NOT visible (it's ignored)
   - ✅ All code files are present
   - ✅ Requirements.txt is present

### 10. Update README Repository Links

After uploading, update the repository URL in README.md:

1. Find this line in README.md (around line 223):
   ```markdown
   git clone https://github.com/yourusername/RAG-Chatbot-Over-SQL-Database.git
   ```
2. Replace `yourusername` with your actual GitHub username
3. Commit and push the change:
   ```bash
   git add README.md
   git commit -m "Update repository URL in README"
   git push
   ```

## Additional Steps

### Add Repository Topics/Tags

On your GitHub repository page:
1. Click the gear icon ⚙️ next to "About"
2. Add topics: `python`, `streamlit`, `langchain`, `llm`, `rag`, `sql`, `mysql`, `chatbot`, `nlp`, `groq`
3. Add description if needed
4. Click "Save changes"

### Add Demo Video to GitHub

#### Option 1: Upload Video to GitHub Releases

1. Go to your repository
2. Click "Releases" → "Create a new release"
3. Upload your `Demo.mp4` file
4. Update README with the release link

#### Option 2: Use GitHub's Video Hosting

GitHub supports `.mp4` files directly in repositories, but they should be reasonable size (< 50MB recommended). For larger videos:
- Upload to YouTube and embed
- Use other video hosting services
- Use GitHub Releases

#### Option 3: Keep Video in Repository

If the video is small enough (< 25MB recommended):
1. Keep `Demo.mp4` in the repository
2. Reference it in README (already done)
3. GitHub will display it automatically

### Create LICENSE File (Optional)

If you want to add a license:

```bash
# Create MIT License (most common for open source)
# Or visit choosealicense.com for options
```

### Enable GitHub Pages (Optional)

If you want to create a project website:

1. Go to repository Settings
2. Navigate to Pages
3. Select source branch (usually `main`)
4. Save

## Common Issues & Solutions

### Issue: "fatal: remote origin already exists"

**Solution:**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/RAG-Chatbot-Over-SQL-Database.git
```

### Issue: Large file warning (Demo.mp4)

**Solution:**
If your video is too large:
1. Compress the video
2. Or use external hosting (YouTube, etc.)
3. Or use Git LFS for large files:
   ```bash
   git lfs install
   git lfs track "*.mp4"
   git add .gitattributes
   ```

### Issue: ".env file was accidentally committed"

**Solution:**
```bash
# Remove from git but keep locally
git rm --cached .env

# Commit the removal
git commit -m "Remove .env file from repository"

# Push changes
git push
```

Then add `.env` to `.gitignore` (already done) and ensure it's not tracked.

### Issue: Authentication failed

**Solution:**
- Use GitHub Personal Access Token instead of password
- Or set up SSH keys
- Or use GitHub Desktop application

## Future Updates

To update your repository with new changes:

```bash
# Check status
git status

# Add changed files
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push
```

## Repository Checklist

Before uploading, ensure:

- [x] `.gitignore` file is present and comprehensive
- [x] `.env` file is in `.gitignore`
- [x] `README.md` is complete and well-formatted
- [x] `requirements.txt` is up to date
- [x] All code files are included
- [x] No sensitive information in code files
- [x] Demo video is handled appropriately
- [x] Repository description is clear
- [x] Topics/tags are added

## Need Help?

- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com
- GitHub Desktop (GUI alternative): https://desktop.github.com

---

**Happy Coding! 🎉**

