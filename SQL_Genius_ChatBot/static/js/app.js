class SQLGenius {
    constructor() {
        this.messages = document.getElementById('messages');
        this.userInput = document.getElementById('user-input');
        this.sendButton = document.getElementById('send-btn');
        this.themeToggle = document.getElementById('theme-toggle');
        
        this.setupEventListeners();
        this.loadTheme();
    }

    setupEventListeners() {
        this.sendButton.addEventListener('click', () => this.handleUserInput());
        this.userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.handleUserInput();
            }
        });
        this.themeToggle.addEventListener('click', () => this.toggleTheme());
    }

    loadTheme() {
        const isDark = localStorage.getItem('darkMode') !== 'false';
        document.body.classList.toggle('light-mode', !isDark);
        this.themeToggle.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    }

    toggleTheme() {
        const isDark = document.body.classList.toggle('light-mode');
        localStorage.setItem('darkMode', (!isDark).toString());
        this.themeToggle.innerHTML = isDark ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
    }

    async handleUserInput() {
        const userMessage = this.userInput.value.trim();
        if (!userMessage) return;

        // Add user message
        this.addMessage(userMessage, 'user');
        this.userInput.value = '';

        // Show typing indicator
        const botMessageContainer = this.addMessage('Generating...', 'bot');
        
        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: userMessage
                })
            });

            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'API request failed');
            }
            
            const formattedResponse = this.formatResponse(data.response);
            botMessageContainer.innerHTML = formattedResponse;
            
            // Initialize syntax highlighting
            botMessageContainer.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightElement(block);
            });

            // Add copy buttons
            botMessageContainer.querySelectorAll('.code-block').forEach((block) => {
                const copyButton = document.createElement('button');
                copyButton.className = 'copy-button';
                copyButton.innerHTML = '<i class="fas fa-copy"></i> Copy';
                copyButton.addEventListener('click', () => this.copyCode(block));
                block.appendChild(copyButton);
            });
        } catch (error) {
            botMessageContainer.textContent = 'Sorry, I encountered an error. Please try again.';
            console.error('Error:', error);
        }

        this.messages.scrollTop = this.messages.scrollHeight;
    }

    addMessage(content, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        messageDiv.textContent = content;
        this.messages.appendChild(messageDiv);
        return messageDiv;
    }

    formatResponse(response) {
        // First, separate code blocks to prevent markdown processing inside them
        const segments = response.split(/(```sql[\s\S]*?```)/);
        let formattedResponse = '';

        segments.forEach((segment, index) => {
            if (index % 2 === 0) {
                // This is regular text/markdown content
                let processed = segment
                    .replace(/^# (.*$)/gm, '<h1>$1</h1>')
                    .replace(/^## (.*$)/gm, '<h2>$1</h2>')
                    .replace(/^### (.*$)/gm, '<h3>$1</h3>')
                    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
                    .replace(/\*(.*?)\*/g, '<em>$1</em>')
                    // Process lists
                    .replace(/^- (.+)$/gm, '<li>$1</li>')
                    .replace(/(<li>.*<\/li>(\n|$))+/g, match => `<ul>${match}</ul>`)
                    // Process paragraphs
                    .replace(/^(?!<[uh]|<li).+$/gm, match => `<p>${match}</p>`);
                
                formattedResponse += `<div class="markdown-content">${processed}</div>`;
            } else {
                // This is a code block
                const code = segment.replace(/```sql\n?|\n?```/g, '').trim();
                formattedResponse += `
                    <div class="code-block">
                        <pre><code class="sql">${this.escapeHtml(code)}</code></pre>
                    </div>
                `;
            }
        });

        return formattedResponse;
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    async copyCode(codeBlock) {
        const code = codeBlock.querySelector('code').textContent;
        await navigator.clipboard.writeText(code);
        
        const copyButton = codeBlock.querySelector('.copy-button');
        const originalText = copyButton.innerHTML;
        copyButton.innerHTML = '<i class="fas fa-check"></i> Copied!';
        setTimeout(() => {
            copyButton.innerHTML = originalText;
        }, 2000);
    }
}

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    window.sqlGenius = new SQLGenius();
});
