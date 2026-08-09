from flask import Flask, render_template, jsonify, request
import requests
import json
from datetime import datetime

app = Flask(__name__)

# GitHub username
GITHUB_USERNAME = "Allallahlou"

# Projects data (fallback)
PROJECTS = [
    {
        "name": "Cooking Website",
        "repo": "cooking_website",
        "description": "موقع طبخ تفاعلي يحتوي على وصفات متنوعة مع تصميم عصري وجذاب",
        "language": "CSS",
        "icon": "fa-utensils",
        "gradient": "linear-gradient(135deg, #6366f1, #ec4899)"
    },
    {
        "name": "Appyallavamos",
        "repo": "appyallavamos",
        "description": "تطبيق Python متكامل مع ميزات متقدمة وواجهة مستخدم سهلة الاستخدام",
        "language": "Python",
        "icon": "fa-python",
        "gradient": "linear-gradient(135deg, #3776ab, #ffd43b)"
    },
    {
        "name": "Perfume Store",
        "repo": "PerfumeStore",
        "description": "متجر عطور إلكتروني مع سلة تسوق ونظام دفع تفاعلي",
        "language": "JavaScript",
        "icon": "fa-shopping-bag",
        "gradient": "linear-gradient(135deg, #f0db4f, #323330)"
    },
    {
        "name": "Snake App",
        "repo": "SnakeApp",
        "description": "لعبة الثعبان الكلاسيكية مبرمجة بلغة C++ مع رسوميات متقدمة",
        "language": "C++",
        "icon": "fa-gamepad",
        "gradient": "linear-gradient(135deg, #00599c, #004482)"
    },
    {
        "name": "Soudor Full Site",
        "repo": "soudor_full_site",
        "description": "موقع ويب كامل بتصميم احترافي ومتجاوب مع جميع الأجهزة",
        "language": "HTML",
        "icon": "fa-globe",
        "gradient": "linear-gradient(135deg, #e34c26, #f06529)"
    },
    {
        "name": "Color Screen",
        "repo": "Color_Screen",
        "description": "تطبيق Flutter لإنشاء شاشات ملونة مع ميزات تخصيص متقدمة",
        "language": "Dart",
        "icon": "fa-mobile-alt",
        "gradient": "linear-gradient(135deg, #00b4d8, #0077b6)"
    },
    {
        "name": "Tic Tac Toe Kotlin",
        "repo": "TicTacToeKotlin",
        "description": "لعبة إكس أو تفاعلية مبرمجة بلغة Kotlin لتطبيقات Android",
        "language": "Kotlin",
        "icon": "fa-times",
        "gradient": "linear-gradient(135deg, #7f52ff, #e2445c)"
    },
    {
        "name": "Calculatris App",
        "repo": "CalculatrisApp",
        "description": "آلة حاسبة علمية متقدمة بتصميم عصري لمستخدمي Android",
        "language": "Kotlin",
        "icon": "fa-calculator",
        "gradient": "linear-gradient(135deg, #7f52ff, #0095d5)"
    },
    {
        "name": "Probable Train",
        "repo": "probable-train",
        "description": "محاكاة نظام قطارات متقدمة بلغة C++ مع خوارزميات ذكية",
        "language": "C++",
        "icon": "fa-train",
        "gradient": "linear-gradient(135deg, #00599c, #00b4d8)"
    },
    {
        "name": "Happy Farm",
        "repo": "happy_farm",
        "description": "لعبة مزرعة سعيدة تفاعلية مع رسوميات جذابة وميكانيكية متقدمة",
        "language": "C++",
        "icon": "fa-tractor",
        "gradient": "linear-gradient(135deg, #22c55e, #16a34a)"
    }
]

SKILLS = [
    {"name": "Flutter", "icon": "fa-flutter", "level": 95},
    {"name": "Dart", "icon": "fa-code", "level": 90},
    {"name": "Python", "icon": "fa-python", "level": 85},
    {"name": "JavaScript", "icon": "fa-js", "level": 80},
    {"name": "HTML5", "icon": "fa-html5", "level": 90},
    {"name": "CSS3", "icon": "fa-css3-alt", "level": 85},
    {"name": "C++", "icon": "fa-copyright", "level": 75},
    {"name": "Kotlin", "icon": "fa-android", "level": 80},
    {"name": "Git", "icon": "fa-git-alt", "level": 85},
    {"name": "GitHub", "icon": "fa-github", "level": 90}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/projects')
def get_projects():
    try:
        # Try to fetch from GitHub API
        response = requests.get(
            f'https://api.github.com/users/{GITHUB_USERNAME}/repos',
            timeout=10
        )
        if response.status_code == 200:
            repos = response.json()
            projects = []
            for repo in repos:
                projects.append({
                    "name": repo['name'].replace('_', ' ').replace('-', ' ').title(),
                    "repo": repo['name'],
                    "description": repo['description'] or PROJECTS.get(repo['name'], {}).get('description', ''),
                    "language": repo['language'] or 'Unknown',
                    "stars": repo['stargazers_count'],
                    "forks": repo['forks_count'],
                    "updated": repo['updated_at'],
                    "url": repo['html_url']
                })
            return jsonify({"success": True, "projects": projects})
    except Exception as e:
        pass

    # Fallback to static data
    return jsonify({"success": True, "projects": PROJECTS})

@app.route('/api/skills')
def get_skills():
    return jsonify({"success": True, "skills": SKILLS})

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name', '')
    email = data.get('email', '')
    message = data.get('message', '')

    # Here you would typically send an email or save to database
    # For now, just return success
    return jsonify({
        "success": True,
        "message": "تم إرسال رسالتك بنجاح! سأتواصل معك قريباً."
    })

@app.route('/api/github-stats')
def github_stats():
    try:
        response = requests.get(
            f'https://api.github.com/users/{GITHUB_USERNAME}',
            timeout=10
        )
        if response.status_code == 200:
            user = response.json()
            return jsonify({
                "success": True,
                "stats": {
                    "repos": user['public_repos'],
                    "followers": user['followers'],
                    "following": user['following']
                }
            })
    except:
        pass

    return jsonify({
        "success": True,
        "stats": {
            "repos": 10,
            "followers": 0,
            "following": 1
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)