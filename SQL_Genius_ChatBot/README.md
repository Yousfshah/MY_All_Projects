# **SQLGenius - Advanced Database Query Assistant**

A professional SQL query assistant that helps generate optimized database queries through natural language interaction. Built with modern web technologies and featuring a sleek, responsive design.

<div style="text-align: center;">
    <img src="project_banner.jpg" alt="Project Banner" style="width: 100%; height:400px; border-radius: 10px;"/>
</div>

## Features

- Natural language to SQL query conversion
- Syntax highlighted SQL code
- Dark/Light theme support
- Copy-to-clipboard functionality
- Mobile responsive design
- Markdown-formatted explanations

## **Setup**

### 1. Clone the repository:
```bash
git clone https://github.com/Yousfshah/SQL_Genius_ChatBot.git
```

### 2. Install dependencies:
```bash
conda install --file runtime.txt
pip install -r requirements.txt
```

### 3. Create a .env file in the root directory:
   
- [Access openrouter API Key](https://openrouter.ai/qwen/qwen2.5-vl-72b-instruct:free/api)
```bash
OPENROUTER_API_KEY="your_openrouter_api_key"
```
- Note: Don't Use Quotes for the API Key

### 4. Run python file
```bash
python app.py
```

## **Security Note**

The API key is stored in .env which is listed in .gitignore to prevent it from being tracked by Git. Make sure to never commit your API keys to version control.

## **Feel Free to Reach out**

<div class="contact-info">
  <h3 class="section-title">
    <strong>Author:</strong>
    <a href="https://www.linkedin.com/in/yousuf-shah-7ba9492b4/" target="_blank">Yousuf Shah</a>
  </h3>
  <table>
    <tr>
      <td>
        <a href="https://www.linkedin.com/in/yousuf-shah-7ba9492b4/" target="_blank">
          <img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn" />
        </a>
      </td>
      <td>
        <a href="https://yousfshah.github.io/Portfolio_Website/" target="_blank">
          <img src="https://img.shields.io/badge/Portfolio_Website-Website-blue?style=for-the-badge&logo=link" alt="Portfolio Website" />
        </a>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/Yousfshah" target="_blank">
          <img src="https://img.shields.io/badge/GitHub-Profile-green?style=for-the-badge&logo=github" alt="GitHub" />
        </a>
      </td>
      <td>
        <a href="https://www.kaggle.com/yousufshah" target="_blank">
          <img src="https://img.shields.io/badge/Kaggle-Profile-orange?style=for-the-badge&logo=kaggle" alt="Kaggle" />
        </a>
      </td>
    </tr>
  </table>
</div>
